# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class InboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(..., alias="profileUuid")
    tag: str
    type: str
    network: str | None = None
    security: str | None = None
    port: float | None = None
    raw_inbound: Any | None = Field(None, alias="rawInbound")


class ConfigProfileNodesDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(..., alias="countryCode")


class ConfigProfilesDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    config: Any
    inbounds: list[InboundsDto]
    nodes: list[ConfigProfileNodesDto]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class GetAllConfigProfilesResponseDto(BaseModel):
    total: float
    config_profiles: list[ConfigProfilesDto] = Field(..., alias="configProfiles")


class GetAllInboundsResponseInboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(..., alias="profileUuid")
    tag: str
    type: str
    network: str | None = None
    security: str | None = None
    port: float | None = None
    raw_inbound: Any | None = Field(None, alias="rawInbound")
    active_squads: list[UUID] = Field(..., alias="activeSquads")


class GetAllInboundsResponseDto(BaseModel):
    total: float
    inbounds: list[GetAllInboundsResponseInboundsDto]


class GetInboundsByProfileUuidResponseDto(GetAllInboundsResponseDto):
    """Alias of GetAllInboundsResponseDto (envelope unwrapped)."""


class GetConfigProfileByUuidResponseDto(ConfigProfilesDto):
    """Alias of ConfigProfilesDto (envelope unwrapped)."""


class GetComputedConfigProfileByUuidResponseDto(ConfigProfilesDto):
    """Alias of ConfigProfilesDto (envelope unwrapped)."""


class CreateConfigProfileRequestDto(BaseModel):
    name: str
    config: dict[str, Any]


class CreateConfigProfileResponseDto(ConfigProfilesDto):
    """Alias of ConfigProfilesDto (envelope unwrapped)."""


class UpdateConfigProfileRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    config: dict[str, Any] | None = None


class UpdateConfigProfileResponseDto(ConfigProfilesDto):
    """Alias of ConfigProfilesDto (envelope unwrapped)."""


class ReorderConfigProfileItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderConfigProfilesRequestDto(BaseModel):
    items: list[ReorderConfigProfileItem]


class ReorderConfigProfilesResponseDto(GetAllConfigProfilesResponseDto):
    """Alias of GetAllConfigProfilesResponseDto (envelope unwrapped)."""
