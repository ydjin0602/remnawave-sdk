from typing import Annotated, Any

from rapid_api_client import Query

from remnawave.models import (
    GetSubscriptionRequestHistoryResponseDto,
    GetSubscriptionRequestHistoryStatsResponseDto,
)
from remnawave.rapid import BaseController, get


class SubscriptionRequestHistoryController(BaseController):
    @get(
        "/subscription-request-history",
        response_class=GetSubscriptionRequestHistoryResponseDto,
    )
    async def get_subscription_request_history(
        self,
        start: Annotated[
            int, Query(default=0, description="Offset for pagination")
        ] = 0,
        size: Annotated[
            int, Query(default=25, ge=1, le=1000, description="Page size")
        ] = 25,
        filters: Annotated[
            list[dict[str, Any]] | None,
            Query(
                default=None,
                description="Table filters (JSON-encoded)",
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
    ) -> GetSubscriptionRequestHistoryResponseDto:
        """Get subscription request history (paginated, filterable, sortable)"""

    @get(
        "/subscription-request-history/stats",
        response_class=GetSubscriptionRequestHistoryStatsResponseDto,
    )
    async def get_subscription_request_history_stats(
        self,
    ) -> GetSubscriptionRequestHistoryStatsResponseDto:
        """Get subscription request history stats"""
