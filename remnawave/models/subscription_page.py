# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class ConfigsDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    config: Any | None = None


class GetSubscriptionPageConfigsResponseDto(BaseModel):
    total: float
    configs: list[ConfigsDto]


class GetSubscriptionPageConfigResponseDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    config: Any


class UpdateSubscriptionPageConfigRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    config: Any | None = None


class UpdateSubpageConfigResponseDto(GetSubscriptionPageConfigResponseDto):
    """Alias of GetSubscriptionPageConfigResponseDto (envelope unwrapped)."""


class CreateSubscriptionPageConfigRequestDto(BaseModel):
    name: str


class CreateSubpageConfigResponseDto(ConfigsDto):
    """Alias of ConfigsDto (envelope unwrapped)."""


class ReorderSubscriptionPageConfigItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderSubscriptionPageConfigsRequestDto(BaseModel):
    items: list[ReorderSubscriptionPageConfigItem]


class ReorderSubscriptionPageConfigsResponseDto(GetSubscriptionPageConfigsResponseDto):
    """Alias of GetSubscriptionPageConfigsResponseDto (envelope unwrapped)."""


class CloneSubscriptionPageConfigRequestDto(BaseModel):
    clone_from_uuid: UUID = Field(..., serialization_alias="cloneFromUuid")


class CloneSubscriptionPageConfigResponseDto(GetSubscriptionPageConfigResponseDto):
    """Alias of GetSubscriptionPageConfigResponseDto (envelope unwrapped)."""
