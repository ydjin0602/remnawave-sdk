# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field


class UserDto(BaseModel):
    username: str


class NodePluginNodeDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(..., alias="countryCode")


class ActionReportDto(BaseModel):
    blocked: bool
    ip: str
    block_duration: float = Field(..., alias="blockDuration")
    will_unblock_at: datetime = Field(..., alias="willUnblockAt")
    user_id: str = Field(..., alias="userId")
    processed_at: datetime = Field(..., alias="processedAt")


class XrayReportDto(BaseModel):
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


class ReportDto(BaseModel):
    action_report: ActionReportDto = Field(..., alias="actionReport")
    xray_report: XrayReportDto = Field(..., alias="xrayReport")


class NodePluginRecordsDto(BaseModel):
    id: int
    user_id: int = Field(..., alias="userId")
    node_id: int = Field(..., alias="nodeId")
    user: UserDto
    node: NodePluginNodeDto
    report: ReportDto
    created_at: datetime = Field(..., alias="createdAt")


class GetTorrentBlockerReportsResponseDto(BaseModel):
    records: list[NodePluginRecordsDto]
    total: float


class NodePluginStatsDto(BaseModel):
    distinct_nodes: float = Field(..., alias="distinctNodes")
    distinct_users: float = Field(..., alias="distinctUsers")
    total_reports: float = Field(..., alias="totalReports")
    reports_last24_hours: float = Field(..., alias="reportsLast24Hours")


class NodePluginTopUsersDto(BaseModel):
    user_id: int = Field(..., alias="userId")
    color: str
    username: str
    total: float


class NodePluginTopNodesDto(BaseModel):
    uuid: UUID
    country_code: str = Field(..., alias="countryCode")
    color: str
    name: str
    total: float


class GetTorrentBlockerReportsStatsResponseDto(BaseModel):
    stats: NodePluginStatsDto
    top_users: list[NodePluginTopUsersDto] = Field(..., alias="topUsers")
    top_nodes: list[NodePluginTopNodesDto] = Field(..., alias="topNodes")


class NodePluginsDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    plugin_config: Any | None = Field(None, alias="pluginConfig")


class GetNodePluginsResponseDto(BaseModel):
    total: float
    node_plugins: list[NodePluginsDto] = Field(..., alias="nodePlugins")


class GetNodePluginResponseDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    plugin_config: Any = Field(..., alias="pluginConfig")


class UpdateNodePluginRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    plugin_config: Any | None = Field(None, serialization_alias="pluginConfig")


class UpdateNodePluginResponseDto(GetNodePluginResponseDto):
    """Alias of GetNodePluginResponseDto (envelope unwrapped)."""


class CreateNodePluginRequestDto(BaseModel):
    name: str


class CreateNodePluginResponseDto(NodePluginsDto):
    """Alias of NodePluginsDto (envelope unwrapped)."""


class ReorderNodePluginItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderNodePluginsRequestDto(BaseModel):
    items: list[ReorderNodePluginItem]


class ReorderNodePluginsResponseDto(GetNodePluginsResponseDto):
    """Alias of GetNodePluginsResponseDto (envelope unwrapped)."""


class CloneNodePluginRequestDto(BaseModel):
    clone_from_uuid: UUID = Field(..., serialization_alias="cloneFromUuid")


class CloneNodePluginResponseDto(GetNodePluginResponseDto):
    """Alias of GetNodePluginResponseDto (envelope unwrapped)."""


class BlockIpItemDto(BaseModel):
    ip: str
    timeout: float


class BlockIpsCommandDto(BaseModel):
    command: Literal["blockIps"]
    ips: list[BlockIpItemDto]


class UnblockIpsCommandDto(BaseModel):
    command: Literal["unblockIps"]
    ips: list[str]


class RecreateTablesCommandDto(BaseModel):
    command: Literal["recreateTables"]


class NodePluginTargetAllNodesDto(BaseModel):
    target: Literal["allNodes"]


class NodePluginTargetSpecificNodesDto(BaseModel):
    target: Literal["specificNodes"]
    node_uuids: list[UUID] = Field(..., serialization_alias="nodeUuids")


class PluginExecutorRequestDto(BaseModel):
    command: BlockIpsCommandDto | UnblockIpsCommandDto | RecreateTablesCommandDto
    target_nodes: NodePluginTargetAllNodesDto | NodePluginTargetSpecificNodesDto = (
        Field(..., serialization_alias="targetNodes")
    )
