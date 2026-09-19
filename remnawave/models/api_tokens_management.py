# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class CreateApiTokenRequestDto(BaseModel):
    name: str
    expires_in_days: float = Field(..., serialization_alias="expiresInDays")
    scopes: list[str] | None = None


class CreateApiTokenResponseDto(BaseModel):
    uuid: UUID
    name: str
    expire_at: datetime = Field(..., alias="expireAt")
    scopes: list[str]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    token: str


class EndpointsDto(BaseModel):
    key: str
    kind: Literal["read", "write"]
    method: str
    path: str
    description: str


class ResourcesDto(BaseModel):
    resource: str
    resource_scopes: list[str] = Field(..., alias="resourceScopes")
    endpoints: list[EndpointsDto]


class GetApiTokenScopesResponseDto(BaseModel):
    wildcard: str
    resources: list[ResourcesDto]


class TokensDto(BaseModel):
    uuid: UUID
    name: str
    expire_at: datetime = Field(..., alias="expireAt")
    scopes: list[str]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class FindAllApiTokensResponseDto(BaseModel):
    tokens: list[TokensDto]
