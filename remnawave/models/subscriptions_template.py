# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import TemplateType


class TemplateTemplatesDto(BaseModel):
    uuid: UUID
    view_position: int = Field(..., alias="viewPosition")
    name: str
    template_type: TemplateType = Field(..., alias="templateType")
    template_json: Any | None = Field(None, alias="templateJson")
    encoded_template_yaml: str | None = Field(None, alias="encodedTemplateYaml")


class GetTemplatesResponseDto(BaseModel):
    total: float
    templates: list[TemplateTemplatesDto]


class GetTemplateResponseDto(TemplateTemplatesDto):
    """Alias of TemplateTemplatesDto (envelope unwrapped)."""


class UpdateTemplateRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    template_json: dict[str, Any] | None = Field(
        None, serialization_alias="templateJson"
    )
    encoded_template_yaml: str | None = Field(
        None, serialization_alias="encodedTemplateYaml"
    )


class UpdateTemplateResponseDto(TemplateTemplatesDto):
    """Alias of TemplateTemplatesDto (envelope unwrapped)."""


class CreateSubscriptionTemplateRequestDto(BaseModel):
    name: str
    template_type: TemplateType = Field(..., serialization_alias="templateType")


class CreateSubscriptionTemplateResponseDto(TemplateTemplatesDto):
    """Alias of TemplateTemplatesDto (envelope unwrapped)."""


class ReorderTemplateItem(BaseModel):
    view_position: int = Field(..., alias="viewPosition")
    uuid: UUID


class ReorderSubscriptionTemplatesRequestDto(BaseModel):
    items: list[ReorderTemplateItem]


class ReorderSubscriptionTemplatesResponseDto(GetTemplatesResponseDto):
    """Alias of GetTemplatesResponseDto (envelope unwrapped)."""
