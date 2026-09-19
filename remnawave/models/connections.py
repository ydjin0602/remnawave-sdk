# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class ConnectionsByUserResponseDto(BaseModel):
    job_id: str = Field(..., alias="jobId")


class ProgressDto(BaseModel):
    total: float
    completed: float
    percent: float


class IpsDto(BaseModel):
    ip: str
    last_seen: datetime = Field(..., alias="lastSeen")


class ConnectionsNodesDto(BaseModel):
    node_uuid: UUID = Field(..., alias="nodeUuid")
    node_name: str = Field(..., alias="nodeName")
    country_code: str = Field(..., alias="countryCode")
    ips: list[IpsDto]


class ResultDto(BaseModel):
    success: bool
    user_id: int = Field(..., alias="userId")
    nodes: list[ConnectionsNodesDto]


class ConnectionsByUserResultResponseDto(BaseModel):
    is_completed: bool = Field(..., alias="isCompleted")
    is_failed: bool = Field(..., alias="isFailed")
    progress: ProgressDto
    result: ResultDto | None = None


class DropByUserIds(BaseModel):
    by: Literal["userIds"]
    user_ids: list[int] = Field(..., serialization_alias="userIds")


class DropByIpAddresses(BaseModel):
    by: Literal["ipAddresses"]
    ip_addresses: list[str] = Field(..., serialization_alias="ipAddresses")


class TargetAllNodesDto(BaseModel):
    target: Literal["allNodes"]


class TargetSpecificNodesDto(BaseModel):
    target: Literal["specificNodes"]
    node_uuids: list[UUID] = Field(..., serialization_alias="nodeUuids")


class DropConnectionsRequestDto(BaseModel):
    drop_by: DropByUserIds | DropByIpAddresses = Field(
        ..., serialization_alias="dropBy"
    )
    target_nodes: TargetAllNodesDto | TargetSpecificNodesDto = Field(
        ..., serialization_alias="targetNodes"
    )


class ConnectionsByNodeResponseDto(ConnectionsByUserResponseDto):
    """Alias of ConnectionsByUserResponseDto (envelope unwrapped)."""


class ConnectionsUsersDto(BaseModel):
    user_id: int = Field(..., alias="userId")
    ips: list[IpsDto]


class ConnectionsByNodeResultResponseResultDto(BaseModel):
    success: bool
    node_uuid: UUID = Field(..., alias="nodeUuid")
    users: list[ConnectionsUsersDto]


class ConnectionsByNodeResultResponseDto(BaseModel):
    is_completed: bool = Field(..., alias="isCompleted")
    is_failed: bool = Field(..., alias="isFailed")
    result: ConnectionsByNodeResultResponseResultDto | None = None


class RemnawaveNodeConnectionsStreamMessageDto(BaseModel):
    v: Literal["1"]
    node_id: str = Field(..., alias="nodeId")
    ts: datetime
    users: str
