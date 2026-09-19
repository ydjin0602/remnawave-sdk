# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime

from pydantic import BaseModel, Field


class GetPasskeyRegistrationOptionsResponseDto(BaseModel):
    pass


class VerifyPasskeyRegistrationResponseDto(BaseModel):
    verified: bool


class PasskeysDto(BaseModel):
    id: str
    name: str
    created_at: datetime = Field(..., alias="createdAt")
    last_used_at: datetime = Field(..., alias="lastUsedAt")


class GetAllPasskeysResponseDto(BaseModel):
    passkeys: list[PasskeysDto]


class DeletePasskeyRequestDto(BaseModel):
    id: str


class UpdatePasskeyRequestDto(BaseModel):
    id: str
    name: str


class UpdatePasskeyResponseDto(GetAllPasskeysResponseDto):
    """Alias of GetAllPasskeysResponseDto (envelope unwrapped)."""
