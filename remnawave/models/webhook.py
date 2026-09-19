# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import NodeUsageType, TrafficLimitStrategy, UserStatus


class WebhookActiveInternalSquadsDto(BaseModel):
    uuid: UUID
    name: str


class WebhookUserTrafficDto(BaseModel):
    used_traffic_bytes: float = Field(..., alias="usedTrafficBytes")
    lifetime_used_traffic_bytes: float = Field(..., alias="lifetimeUsedTrafficBytes")
    online_at: datetime | None = Field(None, alias="onlineAt")
    first_connected_at: datetime | None = Field(None, alias="firstConnectedAt")
    last_connected_node_uuid: UUID | None = Field(None, alias="lastConnectedNodeUuid")


class WebhookUserDto(BaseModel):
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
    active_internal_squads: list[WebhookActiveInternalSquadsDto] = Field(
        ..., alias="activeInternalSquads"
    )
    user_traffic: WebhookUserTrafficDto = Field(..., alias="userTraffic")


class WebhookUserMetaDto(BaseModel):
    not_connected_after_hours: float | None = Field(
        None, alias="notConnectedAfterHours"
    )
    expiration: float | None = None


class WebhookUserEventsDto(BaseModel):
    scope: Literal["user"]
    event: Literal[
        "user.created",
        "user.modified",
        "user.deleted",
        "user.revoked",
        "user.disabled",
        "user.enabled",
        "user.limited",
        "user.expired",
        "user.traffic_reset",
        "user.first_connected",
        "user.bandwidth_usage_threshold_reached",
        "user.not_connected",
        "user.expiration",
    ]
    timestamp: datetime
    data: WebhookUserDto
    meta: WebhookUserMetaDto | None = None


class HwidUserDeviceDto(BaseModel):
    hwid: str
    user_id: int = Field(..., alias="userId")
    platform: str | None = None
    os_version: str | None = Field(None, alias="osVersion")
    device_model: str | None = Field(None, alias="deviceModel")
    user_agent: str | None = Field(None, alias="userAgent")
    request_ip: str | None = Field(None, alias="requestIp")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class WebhookUserHwidDeviceDto(BaseModel):
    user: WebhookUserDto
    hwid_user_device: HwidUserDeviceDto = Field(..., alias="hwidUserDevice")


class WebhookUserHwidDevicesEventsDto(BaseModel):
    scope: Literal["user_hwid_devices"]
    event: Literal["user_hwid_devices.added", "user_hwid_devices.deleted"]
    timestamp: datetime
    data: WebhookUserHwidDeviceDto


class WebhookIpsDto(BaseModel):
    ip: str
    status: NodeUsageType


class WebhookActiveInboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(..., alias="profileUuid")
    tag: str
    type: str
    network: str | None = None
    security: str | None = None
    port: float | None = None
    raw_inbound: Any | None = Field(None, alias="rawInbound")


class WebhookNodeConfigProfileDto(BaseModel):
    active_config_profile_uuid: UUID | None = Field(
        None, alias="activeConfigProfileUuid"
    )
    active_inbounds: list[WebhookActiveInboundsDto] = Field(..., alias="activeInbounds")


class WebhookProviderDto(BaseModel):
    uuid: UUID
    name: str
    favicon_link: str | None = Field(None, alias="faviconLink")
    login_url: str | None = Field(None, alias="loginUrl")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class NodeSystemInfoDto(BaseModel):
    arch: str
    cpus: int
    cpu_model: str = Field(..., alias="cpuModel")
    memory_total: float = Field(..., alias="memoryTotal")
    hostname: str
    platform: str
    release: str
    type: str
    version: str
    network_interfaces: list[str] = Field(..., alias="networkInterfaces")


class WebhookInterfaceDto(BaseModel):
    interface: str
    rx_bytes_per_sec: float = Field(..., alias="rxBytesPerSec")
    tx_bytes_per_sec: float = Field(..., alias="txBytesPerSec")
    rx_total: float = Field(..., alias="rxTotal")
    tx_total: float = Field(..., alias="txTotal")


class NodeSystemStatsDto(BaseModel):
    memory_free: float = Field(..., alias="memoryFree")
    memory_used: float = Field(..., alias="memoryUsed")
    uptime: float
    load_avg: list[float] = Field(..., alias="loadAvg")
    interface: WebhookInterfaceDto | None = None


class NodeSystemDto(BaseModel):
    info: NodeSystemInfoDto
    stats: NodeSystemStatsDto


class NodeVersionsDto(BaseModel):
    xray: str
    node: str


class WebhookNodeDto(BaseModel):
    uuid: UUID
    id: int
    name: str
    address: str
    port: int | None = None
    proxy_url: str | None = Field(None, alias="proxyUrl")
    is_connected: bool = Field(..., alias="isConnected")
    is_disabled: bool = Field(..., alias="isDisabled")
    is_connecting: bool = Field(..., alias="isConnecting")
    last_status_change: datetime | None = Field(None, alias="lastStatusChange")
    last_status_message: str | None = Field(None, alias="lastStatusMessage")
    is_traffic_tracking_active: bool = Field(..., alias="isTrafficTrackingActive")
    traffic_reset_day: int | None = Field(None, alias="trafficResetDay")
    traffic_limit_bytes: float | None = Field(None, alias="trafficLimitBytes")
    traffic_used_bytes: float | None = Field(None, alias="trafficUsedBytes")
    notify_percent: int | None = Field(None, alias="notifyPercent")
    view_position: int = Field(..., alias="viewPosition")
    country_code: str = Field(..., alias="countryCode")
    consumption_multiplier: float = Field(..., alias="consumptionMultiplier")
    node_consumption_multiplier: float = Field(..., alias="nodeConsumptionMultiplier")
    tags: list[str]
    ips: list[WebhookIpsDto]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    config_profile: WebhookNodeConfigProfileDto = Field(..., alias="configProfile")
    provider_uuid: UUID | None = Field(None, alias="providerUuid")
    provider: WebhookProviderDto | None = None
    active_plugin_uuid: UUID | None = Field(None, alias="activePluginUuid")
    system: NodeSystemDto | None = None
    versions: NodeVersionsDto | None = None
    xray_uptime: float = Field(..., alias="xrayUptime")
    users_online: float = Field(..., alias="usersOnline")
    note: str | None = None


class WebhookNodeEventsDto(BaseModel):
    scope: Literal["node"]
    event: Literal[
        "node.created",
        "node.modified",
        "node.disabled",
        "node.enabled",
        "node.deleted",
        "node.connection_lost",
        "node.connection_restored",
        "node.traffic_notify",
    ]
    timestamp: datetime
    data: WebhookNodeDto


class LoginAttemptDto(BaseModel):
    username: str
    ip: str
    user_agent: str = Field(..., alias="userAgent")
    description: str | None = None
    password: str | None = None


class SubpageConfigDto(BaseModel):
    action: Literal["CREATED", "UPDATED", "DELETED"]
    uuid: UUID


class ApiTokenDto(BaseModel):
    name: str
    uuid: UUID
    expire_at: datetime = Field(..., alias="expireAt")
    scopes: list[str]


class WebhookServiceDataDto(BaseModel):
    login_attempt: LoginAttemptDto | None = Field(None, alias="loginAttempt")
    panel_version: str | None = Field(None, alias="panelVersion")
    subpage_config: SubpageConfigDto | None = Field(None, alias="subpageConfig")
    api_token: ApiTokenDto | None = Field(None, alias="apiToken")


class WebhookServiceEventsDto(BaseModel):
    scope: Literal["service"]
    event: Literal[
        "service.panel_started",
        "service.login_attempt_failed",
        "service.login_attempt_success",
        "service.subpage_config_changed",
        "service.api_token_created",
        "service.api_token_deleted",
    ]
    timestamp: datetime
    data: WebhookServiceDataDto


class WebhookErrorsDataDto(BaseModel):
    description: str


class WebhookErrorsEventsDto(BaseModel):
    scope: Literal["errors"]
    event: Literal["errors.bandwidth_usage_threshold_reached_max_notifications"]
    timestamp: datetime
    data: WebhookErrorsDataDto


class WebhookCrmDataDto(BaseModel):
    provider_name: str = Field(..., alias="providerName")
    node_name: str = Field(..., alias="nodeName")
    next_billing_at: datetime = Field(..., alias="nextBillingAt")
    login_url: str = Field(..., alias="loginUrl")


class WebhookCrmEventsDto(BaseModel):
    scope: Literal["crm"]
    event: Literal[
        "crm.infra_billing_node_payment_in_7_days",
        "crm.infra_billing_node_payment_in_48hrs",
        "crm.infra_billing_node_payment_in_24hrs",
        "crm.infra_billing_node_payment_due_today",
        "crm.infra_billing_node_payment_overdue_24hrs",
        "crm.infra_billing_node_payment_overdue_48hrs",
        "crm.infra_billing_node_payment_overdue_7_days",
    ]
    timestamp: datetime
    data: WebhookCrmDataDto


class WebhookActionReportDto(BaseModel):
    blocked: bool
    ip: str
    block_duration: float = Field(..., alias="blockDuration")
    will_unblock_at: datetime = Field(..., alias="willUnblockAt")
    user_id: str = Field(..., alias="userId")
    processed_at: datetime = Field(..., alias="processedAt")


class WebhookXrayReportDto(BaseModel):
    email: str | None = None
    level: float | None = None
    protocol: str | None = None
    network: str
    source: str | None = None
    destination: str
    route_target: str | None = Field(None, alias="routeTarget")
    original_target: str | None = Field(None, alias="originalTarget")
    inbound_tag: str | None = Field(None, alias="inboundTag")
    inbound_name: str | None = Field(None, alias="inboundName")
    inbound_local: str | None = Field(None, alias="inboundLocal")
    outbound_tag: str | None = Field(None, alias="outboundTag")
    ts: float


class WebhookReportDto(BaseModel):
    action_report: WebhookActionReportDto = Field(..., alias="actionReport")
    xray_report: WebhookXrayReportDto = Field(..., alias="xrayReport")


class WebhookTorrentBlockerReportDto(BaseModel):
    node: WebhookNodeDto
    user: WebhookUserDto
    report: WebhookReportDto


class WebhookTorrentBlockerEventsDto(BaseModel):
    scope: Literal["torrent_blocker"]
    event: Literal["torrent_blocker.report"]
    timestamp: datetime
    data: WebhookTorrentBlockerReportDto
