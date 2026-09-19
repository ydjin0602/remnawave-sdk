# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any

from pydantic import BaseModel


class SnippetsDto(BaseModel):
    name: str
    snippet: Any


class GetSnippetsResponseDto(BaseModel):
    total: float
    snippets: list[SnippetsDto]


class SyncSnippetRequestDto(BaseModel):
    name: str


class DeleteSnippetRequestDto(BaseModel):
    name: str


class CreateSnippetRequestDto(BaseModel):
    name: str
    snippet: list[dict[str, Any]]


class CreateSnippetResponseDto(GetSnippetsResponseDto):
    """Alias of GetSnippetsResponseDto (envelope unwrapped)."""


class UpdateSnippetRequestDto(BaseModel):
    name: str
    snippet: list[dict[str, Any]]


class UpdateSnippetResponseDto(GetSnippetsResponseDto):
    """Alias of GetSnippetsResponseDto (envelope unwrapped)."""
