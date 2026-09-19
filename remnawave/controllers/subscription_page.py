from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CloneSubscriptionPageConfigRequestDto,
    CloneSubscriptionPageConfigResponseDto,
    CreateSubpageConfigResponseDto,
    CreateSubscriptionPageConfigRequestDto,
    GetSubscriptionPageConfigResponseDto,
    GetSubscriptionPageConfigsResponseDto,
    ReorderSubscriptionPageConfigsRequestDto,
    ReorderSubscriptionPageConfigsResponseDto,
    UpdateSubpageConfigResponseDto,
    UpdateSubscriptionPageConfigRequestDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class SubscriptionPageConfigController(BaseController):
    @get(
        "/subscription-page-configs",
        response_class=GetSubscriptionPageConfigsResponseDto,
    )
    async def get_all_configs(self) -> GetSubscriptionPageConfigsResponseDto:
        """Get all subscription page configs"""

    @post("/subscription-page-configs", response_class=CreateSubpageConfigResponseDto)
    async def create_config(
        self,
        body: Annotated[CreateSubscriptionPageConfigRequestDto, PydanticBody()],
    ) -> CreateSubpageConfigResponseDto:
        """Create a new subscription page config"""

    @patch("/subscription-page-configs", response_class=UpdateSubpageConfigResponseDto)
    async def update_config(
        self,
        body: Annotated[UpdateSubscriptionPageConfigRequestDto, PydanticBody()],
    ) -> UpdateSubpageConfigResponseDto:
        """Update subscription page config"""

    @post(
        "/subscription-page-configs/actions/clone",
        response_class=CloneSubscriptionPageConfigResponseDto,
    )
    async def clone_subscription_page_config(
        self,
        body: Annotated[CloneSubscriptionPageConfigRequestDto, PydanticBody()],
    ) -> CloneSubscriptionPageConfigResponseDto:
        """Clone subscription page config"""

    @post(
        "/subscription-page-configs/actions/reorder",
        response_class=ReorderSubscriptionPageConfigsResponseDto,
    )
    async def reorder_subscription_page_configs(
        self,
        body: Annotated[ReorderSubscriptionPageConfigsRequestDto, PydanticBody()],
    ) -> ReorderSubscriptionPageConfigsResponseDto:
        """Reorder subscription page configs"""

    @get(
        "/subscription-page-configs/{uuid}",
        response_class=GetSubscriptionPageConfigResponseDto,
    )
    async def get_config_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config")],
    ) -> GetSubscriptionPageConfigResponseDto:
        """Get config by UUID"""

    @delete("/subscription-page-configs/{uuid}", response_class=None)
    async def delete_config(
        self,
        uuid: Annotated[str, Path(description="UUID of the config")],
    ) -> None:
        """Delete config by UUID"""
