# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import TemplateType


class InfoDto(BaseModel):
    members_count: int = Field(..., alias="membersCount")


class TemplatesDto(BaseModel):
    template_uuid: UUID = Field(..., alias="templateUuid")
    template_type: TemplateType = Field(..., alias="templateType")


class SubscriptionSettingsDto(BaseModel):
    serve_json_at_base_subscription: bool | None = Field(
        None, alias="serveJsonAtBaseSubscription"
    )
    is_show_custom_remarks: bool | None = Field(None, alias="isShowCustomRemarks")
    randomize_hosts: bool | None = Field(None, alias="randomizeHosts")


class HostOverridesDto(BaseModel):
    server_description: str | None = Field(None, alias="serverDescription")
    vless_route_id: int | None = Field(None, alias="vlessRouteId")


class HwidSettingsDto(BaseModel):
    enabled: bool
    fallback_device_limit: float = Field(..., alias="fallbackDeviceLimit")
    max_devices_announce: str | None = Field(None, alias="maxDevicesAnnounce")


class CustomRemarksDto(BaseModel):
    expired_users: list[str] = Field(..., alias="expiredUsers")
    limited_users: list[str] = Field(..., alias="limitedUsers")
    disabled_users: list[str] = Field(..., alias="disabledUsers")
    empty_hosts: list[str] = Field(..., alias="emptyHosts")
    hwid_max_devices_exceeded: list[str] = Field(..., alias="HWIDMaxDevicesExceeded")
    hwid_not_supported: list[str] = Field(..., alias="HWIDNotSupported")


class ExternalSquadsDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    info: InfoDto
    templates: list[TemplatesDto]
    subscription_settings: SubscriptionSettingsDto | None = Field(
        None, alias="subscriptionSettings"
    )
    host_overrides: HostOverridesDto | None = Field(None, alias="hostOverrides")
    response_headers_add: dict[str, Any] = Field(..., alias="responseHeadersAdd")
    response_headers_remove: list[str] = Field(..., alias="responseHeadersRemove")
    hwid_settings: HwidSettingsDto | None = Field(None, alias="hwidSettings")
    custom_remarks: CustomRemarksDto | None = Field(None, alias="customRemarks")
    subpage_config_uuid: UUID | None = Field(None, alias="subpageConfigUuid")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class GetExternalSquadsResponseDto(BaseModel):
    total: float
    external_squads: list[ExternalSquadsDto] = Field(..., alias="externalSquads")


class GetExternalSquadByUuidResponseDto(ExternalSquadsDto):
    """Alias of ExternalSquadsDto (envelope unwrapped)."""


class CreateExternalSquadRequestDto(BaseModel):
    name: str


class CreateExternalSquadResponseDto(ExternalSquadsDto):
    """Alias of ExternalSquadsDto (envelope unwrapped)."""


class UpdateExternalSquadRequestTemplatesDto(BaseModel):
    template_uuid: UUID = Field(..., alias="templateUuid")
    template_type: TemplateType = Field(..., alias="templateType")


class UpdateExternalSquadRequestSubscriptionSettingsDto(BaseModel):
    serve_json_at_base_subscription: bool | None = Field(
        None, alias="serveJsonAtBaseSubscription"
    )
    is_show_custom_remarks: bool | None = Field(None, alias="isShowCustomRemarks")
    randomize_hosts: bool | None = Field(None, alias="randomizeHosts")


class UpdateExternalSquadRequestHostOverridesDto(BaseModel):
    server_description: str | None = Field(None, alias="serverDescription")
    vless_route_id: int | None = Field(None, alias="vlessRouteId")


class UpdateExternalSquadRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    templates: list[UpdateExternalSquadRequestTemplatesDto] | None = None
    subscription_settings: UpdateExternalSquadRequestSubscriptionSettingsDto | None = (
        Field(None, serialization_alias="subscriptionSettings")
    )
    host_overrides: UpdateExternalSquadRequestHostOverridesDto | None = Field(
        None, serialization_alias="hostOverrides"
    )
    response_headers_add: dict[str, Any] | None = Field(
        None, serialization_alias="responseHeadersAdd"
    )
    response_headers_remove: list[str] | None = Field(
        None, serialization_alias="responseHeadersRemove"
    )
    hwid_settings: HwidSettingsDto | None = Field(
        None, serialization_alias="hwidSettings"
    )
    custom_remarks: CustomRemarksDto | None = Field(
        None, serialization_alias="customRemarks"
    )
    subpage_config_uuid: UUID | None = Field(
        None, serialization_alias="subpageConfigUuid"
    )


class UpdateExternalSquadResponseDto(ExternalSquadsDto):
    """Alias of ExternalSquadsDto (envelope unwrapped)."""


class ItemsDto(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderExternalSquadsRequestDto(BaseModel):
    items: list[ItemsDto]


class ReorderExternalSquadsResponseDto(GetExternalSquadsResponseDto):
    """Alias of GetExternalSquadsResponseDto (envelope unwrapped)."""
