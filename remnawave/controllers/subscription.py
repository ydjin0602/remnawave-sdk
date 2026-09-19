from typing import Annotated

from rapid_api_client import Path

from remnawave.enums import ClientType
from remnawave.models import GetSubscriptionInfoResponseDto
from remnawave.rapid import BaseController, get


class SubscriptionController(BaseController):
    """Public (unauthenticated) subscription endpoints."""

    @get("/sub/{shortUuid}", response_class=str)
    async def get_subscription(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the user")
        ],
    ) -> str:
        """Get base subscription content"""

    @get("/sub/{shortUuid}/info", response_class=GetSubscriptionInfoResponseDto)
    async def get_subscription_info_by_short_uuid(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the user")
        ],
    ) -> GetSubscriptionInfoResponseDto:
        """Get subscription info (JSON)"""

    @get("/sub/{shortUuid}/{clientType}", response_class=str)
    async def get_subscription_by_client_type(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the user")
        ],
        client_type: Annotated[
            ClientType, Path(alias="clientType", description="Client type")
        ],
    ) -> str:
        """Get subscription content for a specific client type"""
