# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import TemplateType, TrafficLimitStrategy, UserStatus
from remnawave.utils.happ_crypt import create_happ_crypto_link


class SubUserDto(BaseModel):
    short_uuid: str = Field(..., alias="shortUuid")
    days_left: int = Field(..., alias="daysLeft")
    traffic_used: str = Field(..., alias="trafficUsed")
    traffic_limit: str = Field(..., alias="trafficLimit")
    lifetime_traffic_used: str = Field(..., alias="lifetimeTrafficUsed")
    traffic_used_bytes: str = Field(..., alias="trafficUsedBytes")
    traffic_limit_bytes: str = Field(..., alias="trafficLimitBytes")
    lifetime_traffic_used_bytes: str = Field(..., alias="lifetimeTrafficUsedBytes")
    username: str
    expires_at: datetime = Field(..., alias="expiresAt")
    is_active: bool = Field(..., alias="isActive")
    user_status: UserStatus = Field(..., alias="userStatus")
    traffic_limit_strategy: TrafficLimitStrategy = Field(
        ..., alias="trafficLimitStrategy"
    )


class GetSubscriptionInfoResponseDto(BaseModel):
    is_found: bool = Field(..., alias="isFound")
    user: SubUserDto
    links: list[str]
    ss_conf_links: dict[str, Any] = Field(..., alias="ssConfLinks")
    subscription_url: str = Field(..., alias="subscriptionUrl")


class GetAllSubscriptionsResponseDto(BaseModel):
    subscriptions: list[GetSubscriptionInfoResponseDto]
    total: float


class GetSubscriptionByUsernameResponseDto(GetSubscriptionInfoResponseDto):
    """Alias of GetSubscriptionInfoResponseDto (envelope unwrapped)."""


class GetSubscriptionByShortUUIDResponseDto(GetSubscriptionInfoResponseDto):
    """Alias of GetSubscriptionInfoResponseDto (envelope unwrapped)."""


class GetSubscriptionByIdResponseDto(GetSubscriptionInfoResponseDto):
    """Alias of GetSubscriptionInfoResponseDto (envelope unwrapped)."""


class ActiveInternalSquadsDto(BaseModel):
    uuid: UUID
    name: str


class UserTrafficDto(BaseModel):
    used_traffic_bytes: float = Field(..., alias="usedTrafficBytes")
    lifetime_used_traffic_bytes: float = Field(..., alias="lifetimeUsedTrafficBytes")
    online_at: datetime | None = Field(None, alias="onlineAt")
    first_connected_at: datetime | None = Field(None, alias="firstConnectedAt")
    last_connected_node_uuid: UUID | None = Field(None, alias="lastConnectedNodeUuid")


class GetRawSubscriptionByShortUuidResponseUserDto(BaseModel):
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
    active_internal_squads: list[ActiveInternalSquadsDto] = Field(
        ..., alias="activeInternalSquads"
    )
    user_traffic: UserTrafficDto = Field(..., alias="userTraffic")


class HwidCheckupDto(BaseModel):
    subscription_allowed: bool = Field(..., alias="subscriptionAllowed")
    max_device_reached: bool = Field(..., alias="maxDeviceReached")
    hwid_not_supported: bool = Field(..., alias="hwidNotSupported")
    limit_bypassed: bool = Field(..., alias="limitBypassed")


class ConvertedUserInfoDto(BaseModel):
    days_left: int = Field(..., alias="daysLeft")
    traffic_limit: str = Field(..., alias="trafficLimit")
    traffic_used: str = Field(..., alias="trafficUsed")
    lifetime_traffic_used: str = Field(..., alias="lifetimeTrafficUsed")
    hwid_checkup: HwidCheckupDto | None = Field(None, alias="hwidCheckup")


class ProtocolOptionsDto(BaseModel):
    encryption: str
    id: str
    flow: Literal["", "xtls-rprx-vision", "xtls-rprx-vision-udp443"]


class GetRawSubscriptionByShortUuidResponseProtocolOptionsDto(BaseModel):
    password: str


class GetRawSubscriptionByShortUuidResponseProtocolOptionsDto2(BaseModel):
    method: str
    password: str
    uot: bool
    uot_version: int = Field(..., alias="uotVersion")


class GetRawSubscriptionByShortUuidResponseProtocolOptionsDto3(BaseModel):
    version: int


class HeaderDto(BaseModel):
    type: Literal["none"]


class RequestDto(BaseModel):
    version: str | None = None
    method: str | None = None
    path: list[str] | None = None
    headers: dict[str, Any] | None = None


class ResponseDto(BaseModel):
    version: str | None = None
    status: str | None = None
    reason: str | None = None
    headers: dict[str, Any] | None = None


class GetRawSubscriptionByShortUuidResponseHeaderDto(BaseModel):
    type: Literal["http"]
    request: RequestDto | None = None
    response: ResponseDto | None = None


class TransportOptionsDto(BaseModel):
    header: HeaderDto | GetRawSubscriptionByShortUuidResponseHeaderDto | None = None


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto(BaseModel):
    path: str | None = None
    host: str | None = None
    mode: Literal["auto", "packet-up", "stream-up", "stream-one"]
    extra: dict[str, Any] | None = None


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto2(BaseModel):
    path: str | None = None
    host: str | None = None
    headers: dict[str, Any] | None = None
    heartbeat_period: float | None = Field(None, alias="heartbeatPeriod")


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto3(BaseModel):
    path: str | None = None
    host: str | None = None
    headers: dict[str, Any] | None = None


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto4(BaseModel):
    authority: str | None = None
    service_name: str | None = Field(None, alias="serviceName")
    multi_mode: bool = Field(..., alias="multiMode")


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto5(BaseModel):
    client_mtu: int = Field(..., alias="clientMtu")
    client_tti: int = Field(..., alias="clientTti")
    congestion: bool


class GetRawSubscriptionByShortUuidResponseTransportOptionsDto6(BaseModel):
    version: int
    auth: str


class SecurityOptionsDto(BaseModel):
    pinned_peer_cert_sha256: str | None = Field(None, alias="pinnedPeerCertSha256")
    verify_peer_cert_by_name: str | None = Field(None, alias="verifyPeerCertByName")
    alpn: str | None = None
    enable_session_resumption: bool = Field(..., alias="enableSessionResumption")
    fingerprint: str | None = None
    server_name: str | None = Field(None, alias="serverName")
    ech_config_list: str | None = Field(None, alias="echConfigList")
    ech_force_query: str | None = Field(None, alias="echForceQuery")
    ech_sockopt: Any | None = Field(None, alias="echSockopt")
    cipher_suites: str | None = Field(None, alias="cipherSuites")


class GetRawSubscriptionByShortUuidResponseSecurityOptionsDto(BaseModel):
    fingerprint: str
    public_key: str = Field(..., alias="publicKey")
    short_id: str | None = Field(None, alias="shortId")
    server_name: str = Field(..., alias="serverName")
    spider_x: str | None = Field(None, alias="spiderX")
    mldsa65_verify: str | None = Field(None, alias="mldsa65Verify")


class StreamOverridesDto(BaseModel):
    final_mask: Any | None = Field(None, alias="finalMask")
    sockopt: Any | None = None


class ClientOverridesDto(BaseModel):
    shuffle_host: bool = Field(..., alias="shuffleHost")
    mihomo_x25519: bool = Field(..., alias="mihomoX25519")
    mihomo_ip_version: str | None = Field(None, alias="mihomoIpVersion")
    server_description: str | None = Field(None, alias="serverDescription")
    xray_json_template: Any | None = Field(None, alias="xrayJsonTemplate")


class MetadataDto(BaseModel):
    uuid: UUID
    tags: list[str]
    exclude_from_subscription_types: list[TemplateType] = Field(
        ..., alias="excludeFromSubscriptionTypes"
    )
    inbound_tag: str = Field(..., alias="inboundTag")
    config_profile_uuid: UUID | None = Field(None, alias="configProfileUuid")
    config_profile_inbound_uuid: UUID | None = Field(
        None, alias="configProfileInboundUuid"
    )
    is_disabled: bool = Field(..., alias="isDisabled")
    is_hidden: bool = Field(..., alias="isHidden")
    view_position: int = Field(..., alias="viewPosition")
    remark: str
    vless_route_id: int | None = Field(None, alias="vlessRouteId")
    raw_inbound: Any | None = Field(None, alias="rawInbound")


class ResolvedProxyConfigsDto(BaseModel):
    final_remark: str = Field(..., alias="finalRemark")
    address: str
    port: int
    protocol: Literal["vless", "trojan", "shadowsocks", "hysteria"]
    protocol_options: (
        ProtocolOptionsDto
        | GetRawSubscriptionByShortUuidResponseProtocolOptionsDto
        | GetRawSubscriptionByShortUuidResponseProtocolOptionsDto2
        | GetRawSubscriptionByShortUuidResponseProtocolOptionsDto3
    ) = Field(..., alias="protocolOptions")
    transport: Literal["tcp", "xhttp", "ws", "httpupgrade", "grpc", "kcp", "hysteria"]
    transport_options: (
        TransportOptionsDto
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto2
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto3
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto4
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto5
        | GetRawSubscriptionByShortUuidResponseTransportOptionsDto6
    ) = Field(..., alias="transportOptions")
    security: Literal["tls", "reality", "none"]
    security_options: (
        SecurityOptionsDto
        | GetRawSubscriptionByShortUuidResponseSecurityOptionsDto
        | None
    ) = Field(None, alias="securityOptions")
    stream_overrides: StreamOverridesDto = Field(..., alias="streamOverrides")
    mux: Any | None = None
    client_overrides: ClientOverridesDto = Field(..., alias="clientOverrides")
    metadata: MetadataDto


class GetRawSubscriptionByShortUuidResponseDto(BaseModel):
    user: GetRawSubscriptionByShortUuidResponseUserDto
    converted_user_info: ConvertedUserInfoDto = Field(..., alias="convertedUserInfo")
    headers: dict[str, Any]
    resolved_proxy_configs: list[ResolvedProxyConfigsDto] = Field(
        ..., alias="resolvedProxyConfigs"
    )


class GetSubpageConfigByShortUuidRequestBodyDto(BaseModel):
    request_headers: dict[str, Any] = Field(..., serialization_alias="requestHeaders")


class GetSubpageConfigByShortUuidResponseDto(BaseModel):
    subpage_config_uuid: UUID | None = Field(None, alias="subpageConfigUuid")
    webpage_allowed: bool = Field(..., alias="webpageAllowed")


class GetConnectionKeysByUuidResponseDto(BaseModel):
    enabled_keys: list[str] = Field(..., alias="enabledKeys")
    hidden_keys: list[str] = Field(..., alias="hiddenKeys")
    disabled_keys: list[str] = Field(..., alias="disabledKeys")


class HappCrypto(BaseModel):
    """HAPP crypto link (generated client-side)"""

    crypto_link: str = Field(alias="cryptoLink")


def _attach_happ(cls):
    @property
    def happ(self) -> HappCrypto:
        """Generate HAPP link on the fly"""
        crypto_link = create_happ_crypto_link(self.subscription_url)
        return HappCrypto(cryptoLink=crypto_link)

    cls.happ = happ
    return cls


for _cls in (
    GetSubscriptionInfoResponseDto,
    GetAllSubscriptionsResponseDto,
    GetSubscriptionByUsernameResponseDto,
    GetSubscriptionByShortUUIDResponseDto,
    GetSubscriptionByIdResponseDto,
):
    _attach_happ(_cls)
