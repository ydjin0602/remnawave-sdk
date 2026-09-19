# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class NodesDto(BaseModel):
    uuid: UUID
    total_bytes: float = Field(..., alias="totalBytes")


class DaysDto(BaseModel):
    date: str
    nodes: list[NodesDto]


class GetInternalSquadUserUsageResponseDto(BaseModel):
    days: list[DaysDto]


class GetNodeUsageRequestDto(BaseModel):
    nodes_uuids: list[UUID] = Field(..., serialization_alias="nodesUuids")


class UsersDto(BaseModel):
    id: int
    total_bytes: float = Field(..., alias="totalBytes")


class GetNodeUsageResponseNodesDto(BaseModel):
    uuid: UUID
    users: list[UsersDto]


class GetNodeUsageResponseDto(BaseModel):
    nodes: list[GetNodeUsageResponseNodesDto]


class TopUsersDto(BaseModel):
    color: str
    username: str
    total: float


class GetStatsNodeUsersUsageResponseDto(BaseModel):
    categories: list[str]
    sparkline_data: list[float] = Field(..., alias="sparklineData")
    top_users: list[TopUsersDto] = Field(..., alias="topUsers")


class GetStatsNodesUsersUsageRequestDto(BaseModel):
    nodes_uuids: list[UUID] = Field(..., serialization_alias="nodesUuids")


class GetStatsNodesUsersUsageResponseDto(GetStatsNodeUsersUsageResponseDto):
    """Alias of GetStatsNodeUsersUsageResponseDto (envelope unwrapped)."""


class TopNodesDto(BaseModel):
    uuid: UUID
    color: str
    name: str
    country_code: str = Field(..., alias="countryCode")
    total: float


class SeriesDto(BaseModel):
    uuid: UUID
    name: str
    color: str
    country_code: str = Field(..., alias="countryCode")
    total: float
    data: list[float]


class GetStatsUserUsageResponseDto(BaseModel):
    categories: list[str]
    sparkline_data: list[float] = Field(..., alias="sparklineData")
    top_nodes: list[TopNodesDto] = Field(..., alias="topNodes")
    series: list[SeriesDto]


class GetStatsNodesUsageResponseDto(GetStatsUserUsageResponseDto):
    """Alias of GetStatsUserUsageResponseDto (envelope unwrapped)."""


class RemnawaveUserUsageStreamMessageDto(BaseModel):
    v: Literal["1"]
    node_id: str = Field(..., alias="nodeId")
    ts: datetime
    records: str
