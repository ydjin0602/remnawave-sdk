# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import (
    EncryptionMethod,
    ResponseRuleConditionOperator,
    ResponseRuleOperator,
    ResponseType,
)


class SubscriptionSettingsCustomRemarksDto(BaseModel):
    expired_users: list[str] = Field(..., alias="expiredUsers")
    limited_users: list[str] = Field(..., alias="limitedUsers")
    disabled_users: list[str] = Field(..., alias="disabledUsers")
    empty_hosts: list[str] = Field(..., alias="emptyHosts")
    hwid_max_devices_exceeded: list[str] = Field(..., alias="HWIDMaxDevicesExceeded")
    hwid_not_supported: list[str] = Field(..., alias="HWIDNotSupported")


class SettingsDto(BaseModel):
    disable_subscription_access_by_path: bool | None = Field(
        None, alias="disableSubscriptionAccessByPath"
    )


class ConditionsDto(BaseModel):
    header_name: str = Field(..., alias="headerName")
    operator: ResponseRuleConditionOperator
    value: str
    case_sensitive: bool = Field(..., alias="caseSensitive")


class HeadersDto(BaseModel):
    key: str
    value: str


class EncryptionDto(BaseModel):
    method: EncryptionMethod
    key: str


class ResponseModificationsDto(BaseModel):
    headers: list[HeadersDto] | None = None
    apply_headers_to_end: bool | None = Field(None, alias="applyHeadersToEnd")
    subscription_template: str | None = Field(None, alias="subscriptionTemplate")
    ignore_host_xray_json_template: bool | None = Field(
        None, alias="ignoreHostXrayJsonTemplate"
    )
    ignore_serve_json_at_base_subscription: bool | None = Field(
        None, alias="ignoreServeJsonAtBaseSubscription"
    )
    additional_extended_clients_regex: list[str] | None = Field(
        None, alias="additionalExtendedClientsRegex"
    )
    disable_hwid_check: bool | None = Field(None, alias="disableHwidCheck")
    encryption: EncryptionDto | None = None
    exclude_hosts_by_tags: list[str] | None = Field(None, alias="excludeHostsByTags")


class RulesDto(BaseModel):
    name: str
    description: str | None = None
    enabled: bool
    operator: ResponseRuleOperator
    conditions: list[ConditionsDto]
    response_type: ResponseType = Field(..., alias="responseType")
    response_modifications: ResponseModificationsDto | None = Field(
        None, alias="responseModifications"
    )


class ResponseRulesDto(BaseModel):
    version: Literal["1"]
    settings: SettingsDto | None = None
    rules: list[RulesDto]


class SubscriptionSettingsHwidSettingsDto(BaseModel):
    enabled: bool
    fallback_device_limit: float = Field(..., alias="fallbackDeviceLimit")
    max_devices_announce: str | None = Field(None, alias="maxDevicesAnnounce")


class GetSubscriptionSettingsResponseDto(BaseModel):
    uuid: UUID
    serve_json_at_base_subscription: bool = Field(
        ..., alias="serveJsonAtBaseSubscription"
    )
    is_show_custom_remarks: bool = Field(..., alias="isShowCustomRemarks")
    custom_remarks: SubscriptionSettingsCustomRemarksDto = Field(
        ..., alias="customRemarks"
    )
    custom_response_headers: dict[str, Any] | None = Field(
        None, alias="customResponseHeaders"
    )
    randomize_hosts: bool = Field(..., alias="randomizeHosts")
    response_rules: ResponseRulesDto | None = Field(None, alias="responseRules")
    hwid_settings: SubscriptionSettingsHwidSettingsDto | None = Field(
        None, alias="hwidSettings"
    )
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class UpdateSubscriptionSettingsRequestResponseRulesDto(BaseModel):
    version: Literal["1"]
    settings: SettingsDto | None = None
    rules: list[RulesDto]


class UpdateSubscriptionSettingsRequestHwidSettingsDto(BaseModel):
    enabled: bool
    fallback_device_limit: float = Field(..., alias="fallbackDeviceLimit")
    max_devices_announce: str | None = Field(None, alias="maxDevicesAnnounce")


class UpdateSubscriptionSettingsRequestDto(BaseModel):
    uuid: UUID
    serve_json_at_base_subscription: bool | None = Field(
        None, serialization_alias="serveJsonAtBaseSubscription"
    )
    is_show_custom_remarks: bool | None = Field(
        None, serialization_alias="isShowCustomRemarks"
    )
    custom_remarks: SubscriptionSettingsCustomRemarksDto | None = Field(
        None, serialization_alias="customRemarks"
    )
    custom_response_headers: dict[str, Any] | None = Field(
        None, serialization_alias="customResponseHeaders"
    )
    randomize_hosts: bool | None = Field(None, serialization_alias="randomizeHosts")
    response_rules: UpdateSubscriptionSettingsRequestResponseRulesDto | None = Field(
        None, serialization_alias="responseRules"
    )
    hwid_settings: UpdateSubscriptionSettingsRequestHwidSettingsDto | None = Field(
        None, serialization_alias="hwidSettings"
    )


class UpdateSubscriptionSettingsResponseDto(GetSubscriptionSettingsResponseDto):
    """Alias of GetSubscriptionSettingsResponseDto (envelope unwrapped)."""
