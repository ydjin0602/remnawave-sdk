from typing import Annotated, Any

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CloneNodePluginRequestDto,
    CloneNodePluginResponseDto,
    CreateNodePluginRequestDto,
    CreateNodePluginResponseDto,
    GetNodePluginResponseDto,
    GetNodePluginsResponseDto,
    GetTorrentBlockerReportsResponseDto,
    GetTorrentBlockerReportsStatsResponseDto,
    PluginExecutorRequestDto,
    ReorderNodePluginsRequestDto,
    ReorderNodePluginsResponseDto,
    UpdateNodePluginRequestDto,
    UpdateNodePluginResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class NodePluginsController(BaseController):
    @get("/node-plugins", response_class=GetNodePluginsResponseDto)
    async def get_all_node_plugins(self) -> GetNodePluginsResponseDto:
        """Get all node plugin configs"""

    @get("/node-plugins/{uuid}", response_class=GetNodePluginResponseDto)
    async def get_node_plugin_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the plugin config")],
    ) -> GetNodePluginResponseDto:
        """Get node plugin config by UUID"""

    @post("/node-plugins", response_class=CreateNodePluginResponseDto)
    async def create_node_plugin(
        self,
        body: Annotated[CreateNodePluginRequestDto, PydanticBody()],
    ) -> CreateNodePluginResponseDto:
        """Create a new node plugin config"""

    @patch("/node-plugins", response_class=UpdateNodePluginResponseDto)
    async def update_node_plugin(
        self,
        body: Annotated[UpdateNodePluginRequestDto, PydanticBody()],
    ) -> UpdateNodePluginResponseDto:
        """Update node plugin config"""

    @delete("/node-plugins/{uuid}", response_class=None)
    async def delete_node_plugin(
        self,
        uuid: Annotated[str, Path(description="UUID of the plugin config")],
    ) -> None:
        """Delete node plugin config by UUID"""

    @post("/node-plugins/actions/clone", response_class=CloneNodePluginResponseDto)
    async def clone_node_plugin(
        self,
        body: Annotated[CloneNodePluginRequestDto, PydanticBody()],
    ) -> CloneNodePluginResponseDto:
        """Clone node plugin config"""

    @post("/node-plugins/actions/reorder", response_class=ReorderNodePluginsResponseDto)
    async def reorder_node_plugins(
        self,
        body: Annotated[ReorderNodePluginsRequestDto, PydanticBody()],
    ) -> ReorderNodePluginsResponseDto:
        """Reorder node plugins"""

    @post("/node-plugins/executor", response_class=None)
    async def plugin_executor(
        self,
        body: Annotated[PluginExecutorRequestDto, PydanticBody()],
    ) -> None:
        """Execute a node plugin command (blockIps/unblockIps/recreateTables)"""

    # ---- Torrent blocker reports ----
    @get(
        "/node-plugins/torrent-blocker",
        response_class=GetTorrentBlockerReportsResponseDto,
    )
    async def get_torrent_blocker_reports(
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
    ) -> GetTorrentBlockerReportsResponseDto:
        """Get torrent blocker reports (paginated, filterable, sortable)"""

    @get(
        "/node-plugins/torrent-blocker/stats",
        response_class=GetTorrentBlockerReportsStatsResponseDto,
    )
    async def get_torrent_blocker_reports_stats(
        self,
    ) -> GetTorrentBlockerReportsStatsResponseDto:
        """Get torrent blocker reports stats"""

    @delete("/node-plugins/torrent-blocker/truncate", response_class=None)
    async def truncate_torrent_blocker_reports(self) -> None:
        """Truncate torrent blocker reports"""
