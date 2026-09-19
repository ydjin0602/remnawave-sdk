import random
from uuid import UUID

import pytest

from remnawave.exceptions import ApiError
from remnawave.models import (
    CreateHostRequestDto,
    GetAllHostsResponseDto,
    GetAllHostTagsResponseDto,
    HostResponseDto,
    InboundDto,
    ReorderHostItem,
    ReorderHostRequestDto,
    ReorderHostResponseDto,
    UpdateHostRequestDto,
)
from tests.utils import generate_random_string


def _inbound_ref(panel) -> InboundDto:
    return InboundDto(
        config_profile_uuid=UUID(panel["config_profile_uuid"]),
        config_profile_inbound_uuid=UUID(panel["inbound_uuid"]),
    )


def _random_host_request(panel, **overrides) -> CreateHostRequestDto:
    kwargs: dict = dict(  # noqa: C408
        inbound=_inbound_ref(panel),
        remark=generate_random_string(),
        address=f"10.{random.randint(0, 254)}.{random.randint(0, 254)}.{random.randint(1, 254)}",
        port=random.randint(5000, 8000),
    )
    kwargs.update(overrides)
    return CreateHostRequestDto(**kwargs)


class TestHostsBasic:
    @pytest.mark.asyncio
    async def test_get_all_hosts(self, remnawave):
        hosts = await remnawave.hosts.get_all_hosts()
        assert isinstance(hosts, GetAllHostsResponseDto)
        assert isinstance(hosts.root, list)

    @pytest.mark.asyncio
    async def test_get_hosts_tags(self, remnawave):
        tags = await remnawave.hosts.get_hosts_tags()
        assert isinstance(tags, GetAllHostTagsResponseDto)
        assert hasattr(tags, "tags")


class TestHostsCRUD:
    @pytest.fixture
    async def test_host(self, remnawave, panel):
        create_host = await remnawave.hosts.create_host(
            _random_host_request(panel, tags=["TEST"])
        )
        yield create_host
        try:
            await remnawave.hosts.delete_host(uuid=str(create_host.uuid))
        except Exception:  # noqa: BLE001, S110 - teardown best effort
            pass

    @pytest.mark.asyncio
    async def test_create_host(self, remnawave, panel):
        request = _random_host_request(
            panel,
            is_hidden=False,
            server_description="Test Server",
            vless_route_id=1234,
            shuffle_host=False,
            mihomo_x25519=False,
            tags=["TEST"],
        )
        create_host = await remnawave.hosts.create_host(request)

        assert isinstance(create_host, HostResponseDto)
        assert (
            str(create_host.inbound.config_profile_inbound_uuid)
            == panel["inbound_uuid"]
        )
        assert create_host.address == request.address
        assert create_host.port == request.port
        assert create_host.remark == request.remark
        assert create_host.tags == ["TEST"]

        await remnawave.hosts.delete_host(uuid=str(create_host.uuid))

    @pytest.mark.asyncio
    async def test_get_one_host(self, remnawave, test_host):
        host = await remnawave.hosts.get_one_host(uuid=str(test_host.uuid))
        assert isinstance(host, HostResponseDto)
        assert host.uuid == test_host.uuid
        assert host.remark == test_host.remark

    @pytest.mark.asyncio
    async def test_update_host(self, remnawave, test_host):
        updated_host = await remnawave.hosts.update_host(
            UpdateHostRequestDto(
                uuid=test_host.uuid,
                server_description="Updated Host",
                is_disabled=False,
            )
        )
        assert isinstance(updated_host, HostResponseDto)
        assert updated_host.server_description == "Updated Host"
        assert updated_host.is_disabled is False

    @pytest.mark.asyncio
    async def test_delete_host(self, remnawave, panel):
        create_host = await remnawave.hosts.create_host(_random_host_request(panel))
        string_uuid = str(create_host.uuid)

        # v3: delete returns 204 no content
        assert await remnawave.hosts.delete_host(uuid=string_uuid) is None

        with pytest.raises(ApiError):
            await remnawave.hosts.get_one_host(uuid=string_uuid)


class TestHostsOrdering:
    @pytest.mark.asyncio
    async def test_reorder_hosts(self, remnawave, panel):
        first = await remnawave.hosts.create_host(_random_host_request(panel))
        second = await remnawave.hosts.create_host(_random_host_request(panel))
        try:
            reorder_request = ReorderHostRequestDto(
                hosts=[
                    ReorderHostItem(view_position=1, uuid=first.uuid),
                    ReorderHostItem(view_position=0, uuid=second.uuid),
                ]
            )
            response = await remnawave.hosts.reorder_hosts(body=reorder_request)
            assert isinstance(response, ReorderHostResponseDto)
        finally:
            await remnawave.hosts.delete_host(uuid=str(first.uuid))
            await remnawave.hosts.delete_host(uuid=str(second.uuid))
