# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class InternalSquadInfoDto(BaseModel):
    members_count: int = Field(..., alias="membersCount")
    inbounds_count: int = Field(..., alias="inboundsCount")


class InternalSquadInboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(..., alias="profileUuid")
    tag: str
    type: str
    network: str | None = None
    security: str | None = None
    port: float | None = None
    raw_inbound: Any | None = Field(None, alias="rawInbound")


class InternalSquadsDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    info: InternalSquadInfoDto
    inbounds: list[InternalSquadInboundsDto]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class GetAllInternalSquadsResponseDto(BaseModel):
    total: float
    internal_squads: list[InternalSquadsDto] = Field(..., alias="internalSquads")


class GetInternalSquadByUuidResponseDto(InternalSquadsDto):
    """Alias of InternalSquadsDto (envelope unwrapped)."""


class CreateInternalSquadRequestDto(BaseModel):
    name: str
    inbounds: list[UUID]


class CreateInternalSquadResponseDto(InternalSquadsDto):
    """Alias of InternalSquadsDto (envelope unwrapped)."""


class AccessibleNodesDto(BaseModel):
    uuid: UUID
    node_name: str = Field(..., alias="nodeName")
    country_code: str = Field(..., alias="countryCode")
    config_profile_uuid: UUID = Field(..., alias="configProfileUuid")
    config_profile_name: str = Field(..., alias="configProfileName")
    active_inbounds: list[str] = Field(..., alias="activeInbounds")


class GetInternalSquadAccessibleNodesResponseDto(BaseModel):
    squad_uuid: UUID = Field(..., alias="squadUuid")
    accessible_nodes: list[AccessibleNodesDto] = Field(..., alias="accessibleNodes")


class InternalSquadUsersDto(BaseModel):
    id: int
    total_bytes: float = Field(..., alias="totalBytes")


class GetInternalSquadUsageResponseDto(BaseModel):
    squad_uuid: UUID = Field(..., alias="squadUuid")
    users: list[InternalSquadUsersDto]
    next_cursor: str | None = Field(None, alias="nextCursor")
    has_more: bool = Field(..., alias="hasMore")


class UpdateInternalSquadRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    inbounds: list[UUID] | None = None


class UpdateInternalSquadResponseDto(InternalSquadsDto):
    """Alias of InternalSquadsDto (envelope unwrapped)."""


class ReorderInternalSquadItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderInternalSquadsRequestDto(BaseModel):
    items: list[ReorderInternalSquadItem]


class ReorderInternalSquadsResponseDto(GetAllInternalSquadsResponseDto):
    """Alias of GetAllInternalSquadsResponseDto (envelope unwrapped)."""


class AddManyUsersToInternalSquadRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")


class DeleteManyUsersFromInternalSquadRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")
