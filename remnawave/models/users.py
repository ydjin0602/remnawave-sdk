# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from remnawave.enums import TrafficLimitStrategy, UserStatus
from remnawave.utils.happ_crypt import create_happ_crypto_link


class CreateUserRequestDto(BaseModel):
    username: str
    status: UserStatus | None = None
    short_uuid: str | None = Field(None, serialization_alias="shortUuid")
    trojan_password: str | None = Field(None, serialization_alias="trojanPassword")
    vless_uuid: UUID | None = Field(None, serialization_alias="vlessUuid")
    ss_password: str | None = Field(None, serialization_alias="ssPassword")
    traffic_limit_bytes: float | None = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    traffic_limit_strategy: TrafficLimitStrategy | None = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    expire_at: datetime = Field(..., serialization_alias="expireAt")
    created_at: datetime | None = Field(None, serialization_alias="createdAt")
    last_traffic_reset_at: datetime | None = Field(
        None, serialization_alias="lastTrafficResetAt"
    )
    description: str | None = None
    tag: str | None = None
    telegram_id: int | None = Field(None, serialization_alias="telegramId")
    email: EmailStr | None = None
    hwid_device_limit: int | None = Field(None, serialization_alias="hwidDeviceLimit")
    active_internal_squads: list[UUID] | None = Field(
        None, serialization_alias="activeInternalSquads"
    )
    external_squad_uuid: UUID | None = Field(
        None, serialization_alias="externalSquadUuid"
    )


class ActiveInternalSquadDto(BaseModel):
    uuid: UUID
    name: str


class UserUserTrafficDto(BaseModel):
    used_traffic_bytes: float = Field(..., alias="usedTrafficBytes")
    lifetime_used_traffic_bytes: float = Field(..., alias="lifetimeUsedTrafficBytes")
    online_at: datetime | None = Field(None, alias="onlineAt")
    first_connected_at: datetime | None = Field(None, alias="firstConnectedAt")
    last_connected_node_uuid: UUID | None = Field(None, alias="lastConnectedNodeUuid")


class UserResponseDto(BaseModel):
    id: int
    short_uuid: str = Field(..., alias="shortUuid")
    username: str
    status: UserStatus
    traffic_limit_bytes: float = Field(..., alias="trafficLimitBytes")
    traffic_limit_strategy: TrafficLimitStrategy = Field(
        ..., alias="trafficLimitStrategy"
    )
    expire_at: datetime = Field(..., alias="expireAt")
    telegram_id: int | None = Field(None, alias="telegramId")
    email: str | None = None
    description: str | None = None
    tag: str | None = None
    hwid_device_limit: int | None = Field(None, alias="hwidDeviceLimit")
    external_squad_uuid: UUID | None = Field(None, alias="externalSquadUuid")
    trojan_password: str = Field(..., alias="trojanPassword")
    vless_uuid: UUID = Field(..., alias="vlessUuid")
    ss_password: str = Field(..., alias="ssPassword")
    last_triggered_threshold: int = Field(..., alias="lastTriggeredThreshold")
    sub_revoked_at: datetime | None = Field(None, alias="subRevokedAt")
    last_traffic_reset_at: datetime | None = Field(None, alias="lastTrafficResetAt")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    subscription_url: str = Field(..., alias="subscriptionUrl")
    active_internal_squads: list[ActiveInternalSquadDto] = Field(
        ..., alias="activeInternalSquads"
    )
    user_traffic: UserUserTrafficDto = Field(..., alias="userTraffic")


class UpdateUserRequestDto(BaseModel):
    username: str | None = None
    id: int | None = None
    status: Literal["ACTIVE", "DISABLED"] | None = None
    traffic_limit_bytes: float | None = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    traffic_limit_strategy: TrafficLimitStrategy | None = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    expire_at: datetime | None = Field(None, serialization_alias="expireAt")
    description: str | None = None
    tag: str | None = None
    telegram_id: int | None = Field(None, serialization_alias="telegramId")
    email: EmailStr | None = None
    hwid_device_limit: int | None = Field(None, serialization_alias="hwidDeviceLimit")
    active_internal_squads: list[UUID] | None = Field(
        None, serialization_alias="activeInternalSquads"
    )
    external_squad_uuid: UUID | None = Field(
        None, serialization_alias="externalSquadUuid"
    )


class GetAllUsersResponseDto(BaseModel):
    users: list[UserResponseDto]
    total: float


class GetUsersStreamResponseDto(BaseModel):
    users: list[UserResponseDto]
    next_cursor: str | None = Field(None, alias="nextCursor")
    has_more: bool = Field(..., alias="hasMore")


class GetAllTagsResponseDto(BaseModel):
    tags: list[str]


class ActiveSquadsDto(BaseModel):
    squad_name: str = Field(..., alias="squadName")
    active_inbounds: list[str] = Field(..., alias="activeInbounds")


class ActiveNodesDto(BaseModel):
    uuid: UUID
    node_name: str = Field(..., alias="nodeName")
    country_code: str = Field(..., alias="countryCode")
    config_profile_uuid: UUID = Field(..., alias="configProfileUuid")
    config_profile_name: str = Field(..., alias="configProfileName")
    active_squads: list[ActiveSquadsDto] = Field(..., alias="activeSquads")


class GetUserAccessibleNodesResponseDto(BaseModel):
    user_id: int = Field(..., alias="userId")
    active_nodes: list[ActiveNodesDto] = Field(..., alias="activeNodes")


class UserRecordsDto(BaseModel):
    id: int
    user_id: int = Field(..., alias="userId")
    request_at: datetime = Field(..., alias="requestAt")
    srr_response_type: str = Field(..., alias="srrResponseType")
    request_ip: str | None = Field(None, alias="requestIp")
    user_agent: str | None = Field(None, alias="userAgent")
    srr_rule_name: str | None = Field(None, alias="srrRuleName")


class GetUserSubscriptionRequestHistoryResponseDto(BaseModel):
    total: float
    records: list[UserRecordsDto]


class RevokeUserRequestDto(BaseModel):
    revoke_only_passwords: bool | None = Field(
        None, serialization_alias="revokeOnlyPasswords"
    )
    short_uuid: str | None = Field(None, serialization_alias="shortUuid")


class ExtendUserRequestDto(BaseModel):
    days: int


class ResolveUserRequestBodyDto(BaseModel):
    id: int | None = None
    short_uuid: str | None = Field(None, serialization_alias="shortUuid")
    username: str | None = None


class ResolveUserResponseDto(BaseModel):
    id: int
    username: str
    short_uuid: str = Field(..., alias="shortUuid")


class UserHappCrypto(BaseModel):
    """HAPP crypto link (generated client-side)"""

    crypto_link: str = Field(alias="cryptoLink")


def _attach_happ(cls):
    """Attach happ helpers to a response model with subscription_url."""

    @property
    def happ(self) -> UserHappCrypto:
        """Generate Happ Crypto Link"""
        crypto_link = create_happ_crypto_link(self.subscription_url)
        return UserHappCrypto(cryptoLink=crypto_link)

    def happ_with_version(self, version: Literal["v3", "v4"] = "v4") -> UserHappCrypto:
        crypto_link = create_happ_crypto_link(
            content=self.subscription_url, method=version
        )
        return UserHappCrypto(cryptoLink=crypto_link)

    cls.happ = happ
    cls.happ_with_version = happ_with_version
    return cls


_attach_happ(UserResponseDto)


# Backward-compat accessors for user traffic fields
def _attach_traffic_props(cls):
    @property
    def used_traffic_bytes(self) -> float:
        return self.user_traffic.used_traffic_bytes

    @property
    def lifetime_used_traffic_bytes(self) -> float:
        return self.user_traffic.lifetime_used_traffic_bytes

    @property
    def online_at(self):
        return self.user_traffic.online_at

    @property
    def first_connected_at(self):
        return self.user_traffic.first_connected_at

    @property
    def last_connected_node_uuid(self):
        return self.user_traffic.last_connected_node_uuid

    cls.used_traffic_bytes = used_traffic_bytes
    cls.lifetime_used_traffic_bytes = lifetime_used_traffic_bytes
    cls.online_at = online_at
    cls.first_connected_at = first_connected_at
    cls.last_connected_node_uuid = last_connected_node_uuid
    return cls


_attach_traffic_props(UserResponseDto)
