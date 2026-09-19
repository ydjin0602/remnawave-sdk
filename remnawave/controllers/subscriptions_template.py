from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateSubscriptionTemplateRequestDto,
    CreateSubscriptionTemplateResponseDto,
    GetTemplateResponseDto,
    GetTemplatesResponseDto,
    ReorderSubscriptionTemplatesRequestDto,
    ReorderSubscriptionTemplatesResponseDto,
    UpdateTemplateRequestDto,
    UpdateTemplateResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class SubscriptionsTemplateController(BaseController):
    @get("/subscription-templates", response_class=GetTemplatesResponseDto)
    async def get_all_templates(self) -> GetTemplatesResponseDto:
        """Get all subscription templates"""

    @post(
        "/subscription-templates", response_class=CreateSubscriptionTemplateResponseDto
    )
    async def create_template(
        self,
        body: Annotated[CreateSubscriptionTemplateRequestDto, PydanticBody()],
    ) -> CreateSubscriptionTemplateResponseDto:
        """Create a new subscription template"""

    @patch("/subscription-templates", response_class=UpdateTemplateResponseDto)
    async def update_template(
        self,
        body: Annotated[UpdateTemplateRequestDto, PydanticBody()],
    ) -> UpdateTemplateResponseDto:
        """Update subscription template"""

    @post(
        "/subscription-templates/actions/reorder",
        response_class=ReorderSubscriptionTemplatesResponseDto,
    )
    async def reorder_subscription_templates(
        self,
        body: Annotated[ReorderSubscriptionTemplatesRequestDto, PydanticBody()],
    ) -> ReorderSubscriptionTemplatesResponseDto:
        """Reorder subscription templates"""

    @get("/subscription-templates/{uuid}", response_class=GetTemplateResponseDto)
    async def get_template_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the template")],
    ) -> GetTemplateResponseDto:
        """Get template by UUID"""

    @delete("/subscription-templates/{uuid}", response_class=None)
    async def delete_template(
        self,
        uuid: Annotated[str, Path(description="UUID of the template")],
    ) -> None:
        """Delete template by UUID"""
