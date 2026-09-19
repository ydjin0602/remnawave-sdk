import os
import secrets
import string
import sys
import time
from datetime import UTC

import httpx
import pytest
from dotenv import load_dotenv

from remnawave import RemnawaveSDK

load_dotenv()

# ---- Manual override (run tests against your own panel) ----
# If both REMNAWAVE_BASE_URL and REMNAWAVE_TOKEN are set, the testcontainers
# stack is skipped entirely.
REMNAWAVE_BASE_URL = os.getenv("REMNAWAVE_BASE_URL")
REMNAWAVE_TOKEN = os.getenv("REMNAWAVE_TOKEN")

# Container images (override with env if needed)
PANEL_IMAGE = os.getenv("REMNAWAVE_TEST_PANEL_IMAGE", "remnawave/backend:3.2.3")
POSTGRES_IMAGE = os.getenv("REMNAWAVE_TEST_POSTGRES_IMAGE", "postgres:18.4")
VALKEY_IMAGE = os.getenv("REMNAWAVE_TEST_VALKEY_IMAGE", "valkey/valkey:9-alpine")
NODE_IMAGE = os.getenv("REMNAWAVE_TEST_NODE_IMAGE", "remnawave/node:3.2.2")
WITH_NODE = os.getenv("REMNAWAVE_TEST_WITH_NODE", "1") == "1"

ADMIN_USERNAME = "testadmin"
# Panel password policy: >= 24 chars, upper + lower + digit
ADMIN_PASSWORD = "PytestPanel0Aa7Zz9Kk5Qq3Ww"
STARTUP_TIMEOUT = float(os.getenv("REMNAWAVE_TEST_STARTUP_TIMEOUT", "300"))


def _docker_available() -> bool:
    try:
        import docker

        docker.from_env().ping()
        return True
    except Exception:  # noqa: BLE001 - docker availability probe
        return False


def _rand_hex(n: int) -> str:
    return "".join(secrets.choice(string.hexdigits.lower()[:16]) for _ in range(n))


PANEL_HEADERS = {
    "X-Forwarded-Proto": "https",
    "X-Forwarded-For": "127.0.0.1",
}


@pytest.fixture(scope="session")
def panel():
    """Session-scoped test panel.

    Boots postgres + valkey + remnawave/backend via testcontainers, waits for
    health, registers the first admin and creates a wildcard API token.

    Returns a dict with connection info and pre-fetched fixtures
    (config profile uuid, inbound uuid, user for hwid tests, etc.).
    Yields the plain env values instead when REMNAWAVE_BASE_URL/REMNAWAVE_TOKEN
    are provided.
    """
    if REMNAWAVE_BASE_URL and REMNAWAVE_TOKEN:
        info = {
            "base_url": REMNAWAVE_BASE_URL,
            "token": REMNAWAVE_TOKEN,
            "admin_username": os.getenv("REMNAWAVE_ADMIN_USERNAME", ""),
            "admin_password": os.getenv("REMNAWAVE_ADMIN_PASSWORD", ""),
        }
        yield _bootstrap_refs(info)
        return

    if not _docker_available():
        pytest.skip(
            "No panel credentials (REMNAWAVE_BASE_URL/REMNAWAVE_TOKEN) and "
            "Docker is not available for the testcontainers stack"
        )

    from testcontainers.core.container import DockerContainer
    from testcontainers.core.network import Network

    net = Network()
    net.create()
    try:
        pg = (
            DockerContainer(POSTGRES_IMAGE)
            .with_network(net)
            .with_network_aliases("remnawave-db")
            .with_env("POSTGRES_USER", "postgres")
            .with_env("POSTGRES_PASSWORD", "postgres")
            .with_env("POSTGRES_DB", "postgres")
            .with_env("TZ", "UTC")
        )
        pg.start()
        _wait_container_cmd(pg, ["pg_isready", "-U", "postgres"], "postgres")

        valkey = (
            DockerContainer(VALKEY_IMAGE)
            .with_network(net)
            .with_network_aliases("remnawave-redis")
        )
        valkey.start()
        _wait_container_cmd(valkey, ["valkey-cli", "ping"], "valkey")

        panel_container = (
            DockerContainer(PANEL_IMAGE)
            .with_network(net)
            .with_network_aliases("remnawave-panel")
            .with_env("APP_PORT", "3000")
            .with_env("METRICS_PORT", "3001")
            .with_env("API_INSTANCES", "1")
            .with_env(
                "DATABASE_URL",
                "postgresql://postgres:postgres@remnawave-db:5432/postgres",
            )
            .with_env("REDIS_HOST", "remnawave-redis")
            .with_env("REDIS_PORT", "6379")
            .with_env("APP_SECRET", _rand_hex(64))
            .with_env("PANEL_DOMAIN", "panel.localhost")
            .with_env("FRONT_END_DOMAIN", "*")
            .with_env("SUB_PUBLIC_DOMAIN", "panel.localhost/api/sub")
            .with_env("METRICS_USER", "admin")
            .with_env("METRICS_PASS", "admin")
            .with_env("IS_TELEGRAM_NOTIFICATIONS_ENABLED", "false")
            .with_env("WEBHOOK_ENABLED", "false")
        )
        panel_container.with_exposed_ports(3000, 3001)
        panel_container.start()

        node_container = None
        try:
            base_url, health_url = _wait_for_panel(panel_container)
            info = {
                "base_url": base_url,
                "health_url": health_url,
                "admin_username": ADMIN_USERNAME,
                "admin_password": ADMIN_PASSWORD,
            }
            _bootstrap_admin(info)
            refs = _bootstrap_refs(info)
            if WITH_NODE and "node_secret_key" in refs:
                node_container = _start_node_container(net, refs)
                _wait_node_connected(refs)
            yield refs
        finally:
            if os.getenv("REMNAWAVE_TEST_KEEP_STACK"):
                print(
                    "[conftest] stack kept: api="
                    + str(info.get("base_url"))
                    + " panel_id="
                    + str(panel_container._container.short_id),
                    file=sys.stderr,
                )
            else:
                if node_container is not None:
                    node_container.stop()
                panel_container.stop()
                valkey.stop()
                pg.stop()
    finally:
        if not os.getenv("REMNAWAVE_TEST_KEEP_STACK"):
            net.remove()


def _wait_container_cmd(
    container, cmd: list[str], name: str, timeout: float = 120
) -> None:
    """Wait until `cmd` inside the container exits successfully."""
    deadline = time.monotonic() + timeout
    last = None
    while time.monotonic() < deadline:
        try:
            result = container.exec(cmd)
            if result.exit_code == 0:
                return
            last = f"exit {result.exit_code}"
        except Exception as e:  # noqa: BLE001
            last = str(e)
        time.sleep(1)
    raise RuntimeError(f"{name} not ready in {timeout}s (last: {last})")


def _wait_for_panel(container) -> tuple[str, str]:
    """Poll the metrics /health endpoint until the panel is up."""
    host = container.get_container_host_ip()
    api_port = container.get_exposed_port(3000)
    metrics_port = container.get_exposed_port(3001)
    base_url = f"http://{host}:{api_port}"
    health_url = f"http://{host}:{metrics_port}/health"

    deadline = time.monotonic() + STARTUP_TIMEOUT
    last_err = None
    with httpx.Client(timeout=5) as client:
        while time.monotonic() < deadline:
            try:
                resp = client.get(health_url)
                if resp.status_code == 200:
                    return base_url, health_url
                last_err = f"HTTP {resp.status_code}"
            except Exception as e:  # noqa: BLE001
                last_err = str(e)
            time.sleep(2)
    raise RuntimeError(
        f"Panel did not become healthy in {STARTUP_TIMEOUT}s (last error: {last_err})"
    )


def _bootstrap_admin(info: dict) -> None:
    """Register the first admin and exchange it for a wildcard API token."""
    with httpx.Client(
        timeout=30, base_url=info["base_url"], headers=PANEL_HEADERS
    ) as client:
        reg = client.post(
            "/api/auth/register",
            json={
                "username": info["admin_username"],
                "password": info["admin_password"],
            },
        )
        if reg.status_code == 403:
            # First admin already exists (reused stack) - login instead
            reg = client.post(
                "/api/auth/login",
                json={
                    "username": info["admin_username"],
                    "password": info["admin_password"],
                },
            )
        reg.raise_for_status()
        jwt = reg.json()["response"]["accessToken"]

        tok = client.post(
            "/api/tokens",
            # Admin JWT is only accepted with the browser client-type header
            headers={
                "Authorization": f"Bearer {jwt}",
                "x-remnawave-client-type": "browser",
            },
            json={
                "name": "pytest",
                "expiresInDays": 7,
                "scopes": ["*"],
            },
        )
        tok.raise_for_status()
        info["token"] = tok.json()["response"]["token"]


async def _prefetch_refs(sdk: RemnawaveSDK, info: dict) -> None:
    profiles = await sdk.config_profiles.get_config_profiles()
    if profiles.config_profiles:
        profile = profiles.config_profiles[0]
        info["config_profile_uuid"] = str(profile.uuid)
        inbounds = await sdk.config_profiles.get_inbounds_by_profile_uuid(
            str(profile.uuid)
        )
        if inbounds.inbounds:
            info["inbound_uuid"] = str(inbounds.inbounds[0].uuid)

    users = await sdk.users.get_all_users(size=1)
    if not users.users:
        # Empty panel (fresh testcontainers stack): seed a reference user
        from datetime import datetime, timedelta

        from remnawave.models import CreateUserRequestDto

        await sdk.users.create_user(
            CreateUserRequestDto(
                username="refuser",
                expire_at=datetime.now(UTC) + timedelta(days=365),
            )
        )
        users = await sdk.users.get_all_users(size=1)
    if users.users:
        user = users.users[0]
        info["user_uuid"] = str(user.uuid) if hasattr(user, "uuid") else str(user.id)
        info["user_id"] = user.id
        info["short_uuid"] = user.short_uuid
        info["user_username"] = user.username

    nodes = await sdk.nodes.get_all_nodes()
    if not nodes.root:
        # Seed a reference node backed by a real remnawave/node container:
        # the address is the docker-network alias the node container will use.
        from remnawave.models import CreateNodeRequestDto

        key = await sdk.keygen.generate_key()
        created = await sdk.nodes.create_node(
            CreateNodeRequestDto(
                name="refnode",
                address="remnawave-test-node",
                port=2222,
                config_profile={
                    "activeConfigProfileUuid": info["config_profile_uuid"],
                    "activeInbounds": [info["inbound_uuid"]],
                },
                ips=[{"ip": "127.0.0.1", "status": "INBOUND"}],
            )
        )
        info["node_secret_key"] = key.secret_key
        info["node_uuid"] = str(created.uuid)
    else:
        info["node_uuid"] = str(nodes.root[0].uuid)


def _start_node_container(net, refs: dict):
    """Boot remnawave/node connected to the panel stack."""
    from testcontainers.core.container import DockerContainer

    node = (
        DockerContainer(NODE_IMAGE)
        .with_network(net)
        .with_network_aliases("remnawave-test-node")
        .with_env("NODE_PORT", "2222")
        .with_env("SECRET_KEY", refs["node_secret_key"])
    )
    node.start()
    return node


def _wait_node_connected(refs: dict, timeout: float = 120) -> None:
    """Poll the panel until the test node reports is_connected."""
    import asyncio

    async def _poll() -> bool:
        sdk = RemnawaveSDK(base_url=refs["base_url"], token=refs["token"])
        try:
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                node = await sdk.nodes.get_node(uuid=refs["node_uuid"])
                if node.is_connected:
                    return True
                await asyncio.sleep(2)
            return False
        finally:
            await sdk._client.aclose()

    if not asyncio.run(_poll()):
        raise RuntimeError(
            f"remnawave/node did not connect within {timeout}s "
            f"(uuid={refs.get('node_uuid')})"
        )


def _bootstrap_refs(info: dict) -> dict:
    """Prefetch references used by tests (config profile, inbound, user)."""
    import asyncio

    async def _main() -> None:
        sdk = RemnawaveSDK(
            base_url=info["base_url"], token=info["token"], custom_headers=PANEL_HEADERS
        )
        try:
            await _prefetch_refs(sdk, info)
        finally:
            await sdk._client.aclose()

    asyncio.run(_main())
    return info


@pytest.fixture
async def remnawave(panel) -> RemnawaveSDK:
    assert panel["token"]
    assert panel["base_url"]

    # Panel enforces reverse-proxy headers (ProxyCheckMiddleware);
    # the SDK auto-injects them for http base urls.
    sdk = RemnawaveSDK(
        base_url=panel["base_url"],
        token=panel["token"],
    )

    assert sdk.api_tokens_management is not None
    assert sdk.auth
    assert sdk.bandwidthstats is not None
    assert sdk.connections is not None
    assert sdk.hosts is not None
    assert sdk.hosts_bulk_actions is not None
    assert sdk.keygen is not None
    assert sdk.nodes is not None
    assert sdk.subscription is not None
    assert sdk.subscriptions_settings is not None
    assert sdk.subscriptions_template is not None
    assert sdk.system is not None
    assert sdk.users is not None
    assert sdk.users_bulk_actions is not None
    assert sdk.subscription_page_config is not None
    assert sdk.hwid is not None
    assert sdk.node_plugins is not None
    assert sdk.metadata is not None
    yield sdk
    await sdk._client.aclose()
