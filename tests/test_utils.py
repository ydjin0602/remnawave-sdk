import hashlib
import hmac
import json

from remnawave import RemnawaveSDK
from remnawave.controllers.webhooks import WebhookHeadersDto

# v3 webhook payload: {scope, event, timestamp, data}
VALID_BODY = {
    "scope": "user",
    "event": "user.modified",
    "timestamp": "2026-07-08T23:53:41.617Z",
    "data": {
        "id": 42,
        "shortUuid": "3P9nwj_cqo--naNE",
        "username": "399365366",
        "status": "ACTIVE",
        "trafficLimitBytes": 0,
        "trafficLimitStrategy": "NO_RESET",
        "expireAt": "2026-08-08T23:53:32.000Z",
        "telegramId": None,
        "email": None,
        "description": None,
        "tag": None,
        "hwidDeviceLimit": None,
        "externalSquadUuid": None,
        "trojanPassword": "Z0T-_G9mco40uAd7TgKLQbvtPHauuH",
        "vlessUuid": "7b44e483-82c5-4445-806e-fb1e8e58985a",
        "ssPassword": "mM_wZgb7QhDajEkcC3LLqp2_3Wk6CQPR",
        "lastTriggeredThreshold": 0,
        "subRevokedAt": None,
        "lastTrafficResetAt": None,
        "createdAt": "2026-07-08T21:03:44.463Z",
        "updatedAt": "2026-07-08T23:53:41.611Z",
        "subscriptionUrl": "https://sub.example.com/sub/3P9nwj_cqo--naNE",
        "activeInternalSquads": [],
        "userTraffic": {
            "usedTrafficBytes": 0,
            "lifetimeUsedTrafficBytes": 0,
            "onlineAt": None,
            "firstConnectedAt": None,
            "lastConnectedNodeUuid": None,
        },
    },
}

WEBHOOK_SECRET = (
    "0cfbd6e60f79f80eb5065ce715f2398a2bb342e62dfce3f6f66083b05abd9ef8"
    "05ed88b7c6ed9564d50e32a42192d5eaa9971d4c072927bbffa52e364a067817"
)

VALID_SIGNATURE = hmac.new(
    WEBHOOK_SECRET.encode(),
    json.dumps(VALID_BODY, separators=(",", ":")).encode(),
    hashlib.sha256,
).hexdigest()


def _make_sdk() -> RemnawaveSDK:
    return RemnawaveSDK(base_url="https://example.com", token="test-token")


def test_webhook_utility_valid():
    sdk = _make_sdk()
    is_valid = sdk.webhook_utility.validate_webhook(
        body=VALID_BODY,
        signature=VALID_SIGNATURE,
        webhook_secret=WEBHOOK_SECRET,
    )
    assert is_valid is True, "Webhook validation failed with valid data"


def test_webhook_utility_invalid():
    sdk = _make_sdk()
    is_valid = sdk.webhook_utility.validate_webhook(
        body=VALID_BODY,
        signature="invalidsignature",
        webhook_secret=WEBHOOK_SECRET,
    )
    assert is_valid is False


def test_parse_webhook_typed():
    sdk = _make_sdk()
    headers = WebhookHeadersDto(signature=VALID_SIGNATURE, timestamp="123")
    event = sdk.webhook_utility.parse_webhook(
        body=VALID_BODY, headers=headers, webhook_secret=WEBHOOK_SECRET
    )
    assert event is not None
    assert event.scope == "user"
    assert event.event == "user.modified"
    assert event.data.username == "399365366"


def test_parse_webhook_bad_signature():
    sdk = _make_sdk()
    headers = WebhookHeadersDto(signature="bad", timestamp="123")
    event = sdk.webhook_utility.parse_webhook(
        body=VALID_BODY, headers=headers, webhook_secret=WEBHOOK_SECRET
    )
    assert event is None


def test_parse_webhook_unknown_scope():
    sdk = _make_sdk()
    headers = WebhookHeadersDto(signature=VALID_SIGNATURE, timestamp="123")
    body = dict(VALID_BODY)
    body["scope"] = "unknown"
    event = sdk.webhook_utility.parse_webhook(
        body=body,
        headers=headers,
        webhook_secret=WEBHOOK_SECRET,
        validate=False,
    )
    assert event is None


def test_event_type_helpers():
    from remnawave.controllers.webhooks import WebhookUtility

    assert WebhookUtility.is_user_event("user.created")
    assert WebhookUtility.is_node_event("node.connection_lost")
    assert WebhookUtility.is_crm_event("crm.infra_billing_node_payment_due_today")
    assert not WebhookUtility.is_user_event("node.created")
