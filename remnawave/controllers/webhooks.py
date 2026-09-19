import hashlib
import hmac
import json

from pydantic import BaseModel

from remnawave.models.webhook import (
    WebhookCrmEventsDto,
    WebhookErrorsEventsDto,
    WebhookNodeEventsDto,
    WebhookServiceEventsDto,
    WebhookTorrentBlockerEventsDto,
    WebhookUserDto,
    WebhookUserEventsDto,
    WebhookUserHwidDeviceDto,
    WebhookUserHwidDevicesEventsDto,
)


class WebhookHeadersDto:
    """Helper class for webhook headers"""

    def __init__(self, signature: str, timestamp: str):
        self.signature = signature
        self.timestamp = timestamp

    @classmethod
    def from_headers(cls, headers: dict[str, str]) -> "WebhookHeadersDto":
        """
        Create WebhookHeadersDto from headers dictionary.
        Handles case-insensitive header names.
        """
        signature = None
        timestamp = None

        for key, value in headers.items():
            lower_key = key.lower()
            if lower_key == "x-remnawave-signature":
                signature = value
            elif lower_key == "x-remnawave-timestamp":
                timestamp = value

        if not signature or not timestamp:
            raise ValueError("Missing required webhook headers")

        return cls(signature=signature, timestamp=timestamp)


EventDto = (
    WebhookUserEventsDto
    | WebhookUserHwidDevicesEventsDto
    | WebhookNodeEventsDto
    | WebhookServiceEventsDto
    | WebhookCrmEventsDto
    | WebhookErrorsEventsDto
    | WebhookTorrentBlockerEventsDto
)

_EVENT_MODELS: dict[str, tuple[str, type[BaseModel]]] = {
    "user": ("user", WebhookUserEventsDto),
    "user_hwid_devices": ("user_hwid_devices", WebhookUserHwidDevicesEventsDto),
    "node": ("node", WebhookNodeEventsDto),
    "service": ("service", WebhookServiceEventsDto),
    "crm": ("crm", WebhookCrmEventsDto),
    "errors": ("errors", WebhookErrorsEventsDto),
    "torrent_blocker": ("torrent_blocker", WebhookTorrentBlockerEventsDto),
}


class WebhookUtility:
    @staticmethod
    def validate_webhook(
        body: str | dict,
        signature: str,
        webhook_secret: str,
    ) -> bool:
        """
        Validates the webhook's authenticity using HMAC SHA-256.

        :param body: The webhook request body (either a JSON string or a parsed dictionary).
        :param signature: The signature received from the server.
        :param webhook_secret: The secret key used to compute the HMAC.
        :return: True if the signature matches, otherwise False.
        """
        if isinstance(body, str):
            original_body = body
        else:
            original_body = json.dumps(body, separators=(",", ":"))

        key = webhook_secret.encode("utf-8")
        hmac_new = hmac.new(key, original_body.encode("utf-8"), hashlib.sha256)
        expected_signature = hmac_new.hexdigest()
        return hmac.compare_digest(expected_signature, signature)

    @staticmethod
    def validate_webhook_with_headers(
        body: str | dict,
        headers: dict[str, str] | WebhookHeadersDto,
        webhook_secret: str,
    ) -> bool:
        """
        Validates the webhook's authenticity using HMAC SHA-256 and webhook headers.

        :param body: The webhook request body (either a JSON string or a parsed dictionary).
        :param headers: Dictionary with headers or WebhookHeadersDto object.
        :param webhook_secret: The secret key used to compute the HMAC.
        :return: True if the signature matches, otherwise False.
        """
        if not isinstance(headers, WebhookHeadersDto):
            headers = WebhookHeadersDto.from_headers(headers)

        return WebhookUtility.validate_webhook(
            body=body, signature=headers.signature, webhook_secret=webhook_secret
        )

    @staticmethod
    def parse_webhook(
        body: str | dict,
        headers: dict[str, str] | WebhookHeadersDto,
        webhook_secret: str,
        validate: bool = True,
    ) -> EventDto | None:
        """
        Parses and optionally validates the webhook payload.

        Returns the scope-specific typed event DTO
        (WebhookUserEventsDto, WebhookNodeEventsDto, ...) or None if validation fails.

        :param body: The webhook request body.
        :param headers: Dictionary with headers or WebhookHeadersDto object.
        :param webhook_secret: The secret key used to compute the HMAC.
        :param validate: Whether to validate the webhook signature (default: True).
        """
        if validate and not WebhookUtility.validate_webhook_with_headers(
            body, headers, webhook_secret
        ):
            return None

        if isinstance(body, str):
            body = json.loads(body)

        scope = body.get("scope") if isinstance(body, dict) else None
        model = _EVENT_MODELS.get(scope)
        if model is None:
            return None
        try:
            return model[1].model_validate(body)  # type: ignore[return-value]
        except Exception:  # noqa: BLE001 - best-effort typed parse
            return None

    # ---- scope checks ----

    @staticmethod
    def is_user_event(event: str) -> bool:
        """Check if event is a user event."""
        return event.startswith("user.")

    @staticmethod
    def is_user_hwid_devices_event(event: str) -> bool:
        """Check if event is a user HWID devices event."""
        return event.startswith("user_hwid_devices.")

    @staticmethod
    def is_node_event(event: str) -> bool:
        """Check if event is a node event."""
        return event.startswith("node.")

    @staticmethod
    def is_infra_billing_event(event: str) -> bool:
        """Check if event is an infra billing event."""
        return event.startswith("crm.infra_billing")

    @staticmethod
    def is_crm_event(event: str) -> bool:
        """Check if event is a CRM event."""
        return event.startswith("crm.")

    @staticmethod
    def is_service_event(event: str) -> bool:
        """Check if event is a service event."""
        return event.startswith("service.")

    @staticmethod
    def is_errors_event(event: str) -> bool:
        """Check if event is an errors event."""
        return event.startswith("errors.")

    # ---- typed accessors ----

    @staticmethod
    def get_typed_data(payload: EventDto) -> dict | object:
        """
        Get typed data from a parsed webhook event DTO.
        """
        return payload.data

    @staticmethod
    def extract_user_hwid_event_data(
        payload: WebhookUserHwidDevicesEventsDto,
    ) -> tuple[WebhookUserDto, WebhookUserHwidDeviceDto] | None:
        """
        Extract user and HWID device from a user_hwid_devices event.

        :param payload: Parsed WebhookUserHwidDevicesEventsDto.
        :return: Tuple of (WebhookUserDto, WebhookUserHwidDeviceDto) or None.
        """
        data = payload.data
        user = getattr(data, "user", None)
        device = getattr(data, "hwid_user_device", None) or getattr(
            data, "hwidUserDevice", None
        )
        if user is None or device is None:
            return None
        return (user, device)
