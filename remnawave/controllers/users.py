from typing import Annotated, Any

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateUserRequestDto,
    ExtendUserRequestDto,
    GetAllTagsResponseDto,
    GetAllUsersResponseDto,
    GetUserAccessibleNodesResponseDto,
    GetUsersStreamResponseDto,
    GetUserSubscriptionRequestHistoryResponseDto,
    ResolveUserRequestBodyDto,
    ResolveUserResponseDto,
    RevokeUserRequestDto,
    UpdateUserRequestDto,
    UserResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class UsersController(BaseController):
    @post("/users", response_class=UserResponseDto)
    async def create_user(
        self,
        body: Annotated[CreateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Create a new user"""

    @patch("/users", response_class=UserResponseDto)
    async def update_user(
        self,
        body: Annotated[UpdateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Update a user by ID or username"""

    @get("/users", response_class=GetAllUsersResponseDto)
    async def get_all_users(
        self,
        start: Annotated[
            int | None,
            Query(default=0, description="Offset for pagination"),
        ] = 0,
        size: Annotated[
            int | None,
            Query(default=25, ge=1, le=1000, description="Page size for pagination"),
        ] = 25,
        filters: Annotated[
            list[dict[str, Any]] | None,
            Query(
                default=None,
                description="Table filters, e.g. [{'id': 'username', 'value': 'test'}] (JSON-encoded)",
            ),
        ] = None,
        filter_modes: Annotated[
            dict[str, str] | None,
            Query(
                default=None,
                alias="filterModes",
                description="Per-column filter modes, e.g. {'username': 'icontains'}",
            ),
        ] = None,
        global_filter_mode: Annotated[
            str | None,
            Query(
                default=None,
                alias="globalFilterMode",
                description="Global filter mode",
            ),
        ] = None,
        sorting: Annotated[
            list[dict[str, Any]] | None,
            Query(
                default=None,
                description="Sorting, e.g. [{'id': 'createdAt', 'desc': True}] (JSON-encoded)",
            ),
        ] = None,
    ) -> GetAllUsersResponseDto:
        """Get all users (paginated, filterable, sortable)"""

    @get("/users/stream", response_class=GetUsersStreamResponseDto)
    async def get_users_stream(
        self,
        size: Annotated[
            int | None,
            Query(
                default=250,
                ge=1,
                le=1000,
                description="Page size (max 1000, default 250)",
            ),
        ] = 250,
        cursor: Annotated[
            str | None,
            Query(
                default=None,
                description="Cursor from the previous response (nextCursor). Omit on the first request",
            ),
        ] = None,
        status: Annotated[
            str | None, Query(default=None, description="Filter by user status")
        ] = None,
        traffic_limit_strategy: Annotated[
            str | None,
            Query(
                default=None,
                alias="trafficLimitStrategy",
                description="Filter by traffic limit strategy",
            ),
        ] = None,
        telegram_id: Annotated[
            str | None,
            Query(
                default=None, alias="telegramId", description="Filter by Telegram ID"
            ),
        ] = None,
        email: Annotated[
            str | None, Query(default=None, description="Filter by email")
        ] = None,
        tag: Annotated[
            str | None, Query(default=None, description="Filter by tag")
        ] = None,
        external_squad_uuid: Annotated[
            str | None,
            Query(
                default=None,
                alias="externalSquadUuid",
                description="Filter by external squad UUID",
            ),
        ] = None,
    ) -> GetUsersStreamResponseDto:
        """Stream all users page by page (keyset pagination)"""

    @get("/users/tags", response_class=GetAllTagsResponseDto)
    async def get_users_tags(self) -> GetAllTagsResponseDto:
        """Get all user tags"""

    @get("/users/{userId}", response_class=UserResponseDto)
    async def get_user_by_id(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> UserResponseDto:
        """Get user by ID"""

    @get("/users/by-short-uuid/{shortUuid}", response_class=UserResponseDto)
    async def get_user_by_short_uuid(
        self,
        short_uuid: Annotated[
            str, Path(alias="shortUuid", description="Short UUID of the user")
        ],
    ) -> UserResponseDto:
        """Get user by short UUID"""

    @get("/users/by-username/{username}", response_class=UserResponseDto)
    async def get_user_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> UserResponseDto:
        """Get user by username"""

    @get(
        "/users/{userId}/accessible-nodes",
        response_class=GetUserAccessibleNodesResponseDto,
    )
    async def get_user_accessible_nodes(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> GetUserAccessibleNodesResponseDto:
        """Get nodes accessible to the user"""

    @get(
        "/users/{userId}/subscription-request-history",
        response_class=GetUserSubscriptionRequestHistoryResponseDto,
    )
    async def get_user_subscription_request_history(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> GetUserSubscriptionRequestHistoryResponseDto:
        """Get user subscription request history"""

    @post("/users/resolve", response_class=ResolveUserResponseDto)
    async def resolve_user(
        self,
        body: Annotated[ResolveUserRequestBodyDto, PydanticBody()],
    ) -> ResolveUserResponseDto:
        """Resolve a user by ID, short UUID or username"""

    @delete("/users/{userId}", response_class=None)
    async def delete_user(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> None:
        """Delete a user"""

    @post("/users/{userId}/actions/disable", response_class=UserResponseDto)
    async def disable_user(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> UserResponseDto:
        """Disable a user"""

    @post("/users/{userId}/actions/enable", response_class=UserResponseDto)
    async def enable_user(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> UserResponseDto:
        """Enable a user"""

    @post("/users/{userId}/actions/extend", response_class=UserResponseDto)
    async def extend_user_expiration_date(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
        body: Annotated[ExtendUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Extend user expiration date by N days"""

    @post("/users/{userId}/actions/reset-traffic", response_class=UserResponseDto)
    async def reset_user_traffic(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> UserResponseDto:
        """Reset user traffic"""

    @post("/users/{userId}/actions/revoke", response_class=UserResponseDto)
    async def revoke_user_subscription(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
        body: Annotated[RevokeUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Revoke user subscription"""
