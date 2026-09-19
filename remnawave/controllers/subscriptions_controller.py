from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetAllSubscriptionsResponseDto,
    GetConnectionKeysByUuidResponseDto,
    GetRawSubscriptionByShortUuidResponseDto,
    GetSubpageConfigByShortUuidRequestBodyDto,
    GetSubpageConfigByShortUuidResponseDto,
    GetSubscriptionByIdResponseDto,
    GetSubscriptionByShortUUIDResponseDto,
    GetSubscriptionByUsernameResponseDto,
)
from remnawave.rapid import BaseController, get


class SubscriptionsController(BaseController):
    """Protected subscription endpoints."""

    @get("/subscriptions", response_class=GetAllSubscriptionsResponseDto)
    async def get_all_subscriptions(
        self,
        start: Annotated[
            int, Query(default=0, ge=0, description="Index to start pagination from")
        ] = 0,
        size: Annotated[
            int, Query(default=25, ge=1, description="Number of users per page")
        ] = 25,
    ) -> GetAllSubscriptionsResponseDto:
        """Get all subscriptions"""

    @get("/subscriptions/by-id/{userId}", response_class=GetSubscriptionByIdResponseDto)
    async def get_subscription_by_id(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> GetSubscriptionByIdResponseDto:
        """Get subscription by user ID"""

    @get(
        "/subscriptions/by-short-uuid/{shortUuid}",
        response_class=GetSubscriptionByShortUUIDResponseDto,
    )
    async def get_subscription_by_short_uuid(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the subscription")
        ],
    ) -> GetSubscriptionByShortUUIDResponseDto:
        """Get subscription by short UUID"""

    @get(
        "/subscriptions/by-username/{username}",
        response_class=GetSubscriptionByUsernameResponseDto,
    )
    async def get_subscription_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> GetSubscriptionByUsernameResponseDto:
        """Get subscription by username"""

    @get(
        "/subscriptions/by-short-uuid/{shortUuid}/raw",
        response_class=GetRawSubscriptionByShortUuidResponseDto,
    )
    async def get_raw_subscription(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the user")
        ],
        with_disabled_hosts: Annotated[
            bool,
            Query(
                default=False,
                alias="withDisabledHosts",
                description="Include disabled hosts",
            ),
        ] = False,
    ) -> GetRawSubscriptionByShortUuidResponseDto:
        """Get raw subscription (hosts, user, headers)"""

    @get(
        "/subscriptions/connection-keys/{userId}",
        response_class=GetConnectionKeysByUuidResponseDto,
    )
    async def get_connection_keys_by_user_id(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> GetConnectionKeysByUuidResponseDto:
        """Get connection keys (base64) by user ID"""

    @get(
        "/subscriptions/subpage-config/{shortUuid}",
        response_class=GetSubpageConfigByShortUuidResponseDto,
    )
    async def get_subpage_config(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the subscription")
        ],
        body: Annotated[GetSubpageConfigByShortUuidRequestBodyDto, PydanticBody()],
    ) -> GetSubpageConfigByShortUuidResponseDto:
        """Get subscription page config by short UUID"""
