from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetInternalSquadUsageResponseDto,
    GetInternalSquadUserUsageResponseDto,
    GetNodeUsageRequestDto,
    GetNodeUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodesUsersUsageRequestDto,
    GetStatsNodesUsersUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,
)
from remnawave.rapid import BaseController, get, post


class BandWidthStatsController(BaseController):
    @get("/bandwidth-stats/nodes", response_class=GetStatsNodesUsageResponseDto)
    async def get_nodes_usage(
        self,
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        top_nodes_limit: Annotated[
            int,
            Query(default=20, alias="topNodesLimit", description="Limit of top nodes"),
        ] = 20,
    ) -> GetStatsNodesUsageResponseDto:
        """Get nodes usage stats for a period"""

    @post("/bandwidth-stats/nodes/usage", response_class=GetNodeUsageResponseDto)
    async def get_node_usage(
        self,
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        body: Annotated[GetNodeUsageRequestDto, PydanticBody()],
        min_total_bytes: Annotated[
            int,
            Query(
                default=0,
                alias="minTotalBytes",
                description="Min total bytes threshold",
            ),
        ] = 0,
    ) -> GetNodeUsageResponseDto:
        """Get usage for specific nodes"""

    @get(
        "/bandwidth-stats/nodes/{uuid}/users",
        response_class=GetStatsNodeUsersUsageResponseDto,
    )
    async def get_stats_node_users_usage(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        top_users_limit: Annotated[
            int,
            Query(default=100, alias="topUsersLimit", description="Limit of top users"),
        ] = 100,
    ) -> GetStatsNodeUsersUsageResponseDto:
        """Get users usage stats for a node"""

    @post(
        "/bandwidth-stats/nodes/users",
        response_class=GetStatsNodesUsersUsageResponseDto,
    )
    async def get_stats_nodes_users_usage(
        self,
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        body: Annotated[GetStatsNodesUsersUsageRequestDto, PydanticBody()],
        top_users_limit: Annotated[
            int,
            Query(default=100, alias="topUsersLimit", description="Limit of top users"),
        ] = 100,
    ) -> GetStatsNodesUsersUsageResponseDto:
        """Get users usage stats for specific nodes"""

    @get("/bandwidth-stats/users/{userId}", response_class=GetStatsUserUsageResponseDto)
    async def get_stats_user_usage(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        top_nodes_limit: Annotated[
            int,
            Query(default=20, alias="topNodesLimit", description="Limit of top nodes"),
        ] = 20,
    ) -> GetStatsUserUsageResponseDto:
        """Get user usage stats by nodes"""

    @get(
        "/bandwidth-stats/internal-squads/{uuid}/usage",
        response_class=GetInternalSquadUsageResponseDto,
    )
    async def get_internal_squad_usage(
        self,
        uuid: Annotated[str, Path(description="Internal squad UUID")],
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        min_total_bytes: Annotated[
            int,
            Query(
                default=0,
                alias="minTotalBytes",
                description="Min total bytes threshold",
            ),
        ] = 0,
        limit: Annotated[
            int, Query(default=250, ge=1, le=1000, description="Page size")
        ] = 250,
        cursor: Annotated[
            str | None,
            Query(default=None, description="Cursor from previous response"),
        ] = None,
    ) -> GetInternalSquadUsageResponseDto:
        """Get internal squad usage (cursor pagination)"""

    @get(
        "/bandwidth-stats/internal-squads/{squadUuid}/users/{userId}/usage",
        response_class=GetInternalSquadUserUsageResponseDto,
    )
    async def get_internal_squad_user_usage(
        self,
        squad_uuid: Annotated[
            str, Path(alias="squadUuid", description="Internal squad UUID")
        ],
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
    ) -> GetInternalSquadUserUsageResponseDto:
        """Get user usage stats within an internal squad"""
