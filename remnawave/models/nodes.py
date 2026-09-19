# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field, RootModel

from remnawave.enums import NodeUsageType


class GetAllNodesTagsResponseDto(BaseModel):
    tags: list[str]


class ConfigProfileDto(BaseModel):
    active_config_profile_uuid: UUID = Field(..., alias="activeConfigProfileUuid")
    active_inbounds: list[UUID] = Field(..., alias="activeInbounds")


class NodeIpsDto(BaseModel):
    ip: str
    status: NodeUsageType


class CreateNodeRequestDto(BaseModel):
    name: str
    address: str
    port: int | None = None
    proxy_url: str | None = Field(None, serialization_alias="proxyUrl")
    is_traffic_tracking_active: bool | None = Field(
        None, serialization_alias="isTrafficTrackingActive"
    )
    traffic_limit_bytes: float | None = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    notify_percent: int | None = Field(None, serialization_alias="notifyPercent")
    traffic_reset_day: int | None = Field(None, serialization_alias="trafficResetDay")
    country_code: str | None = Field(None, serialization_alias="countryCode")
    consumption_multiplier: float | None = Field(
        None, serialization_alias="consumptionMultiplier"
    )
    node_consumption_multiplier: float | None = Field(
        None, serialization_alias="nodeConsumptionMultiplier"
    )
    config_profile: ConfigProfileDto = Field(..., serialization_alias="configProfile")
    provider_uuid: UUID | None = Field(None, serialization_alias="providerUuid")
    tags: list[str] | None = None
    active_plugin_uuid: UUID | None = Field(
        None, serialization_alias="activePluginUuid"
    )
    note: str | None = None
    ips: list[NodeIpsDto] | None = None


class ActiveInboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(..., alias="profileUuid")
    tag: str
    type: str
    network: str | None = None
    security: str | None = None
    port: float | None = None
    raw_inbound: Any | None = Field(None, alias="rawInbound")


class NodeResponseConfigProfileDto(BaseModel):
    active_config_profile_uuid: UUID | None = Field(
        None, alias="activeConfigProfileUuid"
    )
    active_inbounds: list[ActiveInboundsDto] = Field(..., alias="activeInbounds")


class NodeProviderDto(BaseModel):
    uuid: UUID
    name: str
    favicon_link: str | None = Field(None, alias="faviconLink")
    login_url: str | None = Field(None, alias="loginUrl")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class NodeInfoDto(BaseModel):
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


class InterfaceDto(BaseModel):
    interface: str
    rx_bytes_per_sec: float = Field(..., alias="rxBytesPerSec")
    tx_bytes_per_sec: float = Field(..., alias="txBytesPerSec")
    rx_total: float = Field(..., alias="rxTotal")
    tx_total: float = Field(..., alias="txTotal")


class NodeStatsDto(BaseModel):
    memory_free: float = Field(..., alias="memoryFree")
    memory_used: float = Field(..., alias="memoryUsed")
    uptime: float
    load_avg: list[float] = Field(..., alias="loadAvg")
    interface: InterfaceDto | None = None


class SystemDto(BaseModel):
    info: NodeInfoDto
    stats: NodeStatsDto


class VersionsDto(BaseModel):
    xray: str
    node: str


class NodeResponseDto(BaseModel):
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
    ips: list[NodeIpsDto]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    config_profile: NodeResponseConfigProfileDto = Field(..., alias="configProfile")
    provider_uuid: UUID | None = Field(None, alias="providerUuid")
    provider: NodeProviderDto | None = None
    active_plugin_uuid: UUID | None = Field(None, alias="activePluginUuid")
    system: SystemDto | None = None
    versions: VersionsDto | None = None
    xray_uptime: float = Field(..., alias="xrayUptime")
    users_online: float = Field(..., alias="usersOnline")
    note: str | None = None


class GetAllNodesResponseDto(RootModel):
    root: list[NodeResponseDto]


class UpdateNodeRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    address: str | None = None
    port: float | None = None
    proxy_url: str | None = Field(None, serialization_alias="proxyUrl")
    is_traffic_tracking_active: bool | None = Field(
        None, serialization_alias="isTrafficTrackingActive"
    )
    traffic_limit_bytes: float | None = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    notify_percent: float | None = Field(None, serialization_alias="notifyPercent")
    traffic_reset_day: float | None = Field(None, serialization_alias="trafficResetDay")
    country_code: str | None = Field(None, serialization_alias="countryCode")
    consumption_multiplier: float | None = Field(
        None, serialization_alias="consumptionMultiplier"
    )
    node_consumption_multiplier: float | None = Field(
        None, serialization_alias="nodeConsumptionMultiplier"
    )
    config_profile: ConfigProfileDto | None = Field(
        None, serialization_alias="configProfile"
    )
    provider_uuid: UUID | None = Field(None, serialization_alias="providerUuid")
    tags: list[str] | None = None
    active_plugin_uuid: UUID | None = Field(
        None, serialization_alias="activePluginUuid"
    )
    note: str | None = None
    ips: list[NodeIpsDto] | None = None


class RestartNodeRequestDto(BaseModel):
    force_restart: bool = Field(..., serialization_alias="forceRestart")


class RestartAllNodesRequestDto(BaseModel):
    force_restart: bool = Field(..., serialization_alias="forceRestart")


class ReorderNodeItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderNodesRequestDto(BaseModel):
    nodes: list[ReorderNodeItem]


class ReorderNodeResponseDto(RootModel):
    root: list[NodeResponseDto]


class ProfileModificationRequestConfigProfileDto(BaseModel):
    active_config_profile_uuid: UUID = Field(..., alias="activeConfigProfileUuid")
    active_inbounds: list[UUID] = Field(..., alias="activeInbounds")


class ProfileModificationRequestDto(BaseModel):
    uuids: list[UUID]
    config_profile: ProfileModificationRequestConfigProfileDto = Field(
        ..., serialization_alias="configProfile"
    )


class BulkNodesActionsRequestDto(BaseModel):
    uuids: list[UUID]
    action: Literal["ENABLE", "DISABLE", "RESTART", "RESET_TRAFFIC"]


class NodeFieldsDto(BaseModel):
    country_code: str | None = Field(None, alias="countryCode")
    consumption_multiplier: float | None = Field(None, alias="consumptionMultiplier")
    node_consumption_multiplier: float | None = Field(
        None, alias="nodeConsumptionMultiplier"
    )
    provider_uuid: UUID | None = Field(None, alias="providerUuid")
    tags: list[str] | None = None
    active_plugin_uuid: UUID | None = Field(None, alias="activePluginUuid")
    note: str | None = None


class BulkNodesUpdateRequestDto(BaseModel):
    uuids: list[UUID]
    fields: NodeFieldsDto
