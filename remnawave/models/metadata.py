# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any

from pydantic import BaseModel


class GetUserMetadataResponseDto(BaseModel):
    metadata: dict[str, Any]


class UpsertUserMetadataRequestBodyDto(BaseModel):
    metadata: dict[str, Any]


class UpsertUserMetadataResponseDto(GetUserMetadataResponseDto):
    """Alias of GetUserMetadataResponseDto (envelope unwrapped)."""


class GetNodeMetadataResponseDto(GetUserMetadataResponseDto):
    """Alias of GetUserMetadataResponseDto (envelope unwrapped)."""


class UpsertNodeMetadataRequestBodyDto(BaseModel):
    metadata: dict[str, Any]


class UpsertNodeMetadataResponseDto(GetUserMetadataResponseDto):
    """Alias of GetUserMetadataResponseDto (envelope unwrapped)."""
