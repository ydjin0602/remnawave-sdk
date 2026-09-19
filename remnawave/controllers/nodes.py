from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    BulkNodesActionsRequestDto,
    BulkNodesUpdateRequestDto,
    CreateNodeRequestDto,
    GetAllNodesResponseDto,
    GetAllNodesTagsResponseDto,
    NodeResponseDto,
    ProfileModificationRequestDto,
    ReorderNodeResponseDto,
    ReorderNodesRequestDto,
    RestartAllNodesRequestDto,
    RestartNodeRequestDto,
    UpdateNodeRequestDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class NodesController(BaseController):
    @post("/nodes", response_class=NodeResponseDto)
    async def create_node(
        self,
        body: Annotated[CreateNodeRequestDto, PydanticBody()],
    ) -> NodeResponseDto:
        """Create a new node"""

    @get("/nodes", response_class=GetAllNodesResponseDto)
    async def get_all_nodes(self) -> GetAllNodesResponseDto:
        """Get all nodes"""

    @get("/nodes/tags", response_class=GetAllNodesTagsResponseDto)
    async def get_nodes_tags(self) -> GetAllNodesTagsResponseDto:
        """Get all nodes tags"""

    @get("/nodes/{uuid}", response_class=NodeResponseDto)
    async def get_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
    ) -> NodeResponseDto:
        """Get node by UUID"""

    @patch("/nodes", response_class=NodeResponseDto)
    async def update_node(
        self,
        body: Annotated[UpdateNodeRequestDto, PydanticBody()],
    ) -> NodeResponseDto:
        """Update node"""

    @delete("/nodes/{uuid}", response_class=None)
    async def delete_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
    ) -> None:
        """Delete node by UUID"""

    @post("/nodes/{uuid}/actions/enable", response_class=NodeResponseDto)
    async def enable_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
    ) -> NodeResponseDto:
        """Enable node"""

    @post("/nodes/{uuid}/actions/disable", response_class=NodeResponseDto)
    async def disable_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
    ) -> NodeResponseDto:
        """Disable node"""

    @post("/nodes/{uuid}/actions/restart", response_class=None)
    async def restart_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
        body: Annotated[RestartNodeRequestDto, PydanticBody()],
    ) -> None:
        """Restart Xray on the node (async)"""

    @post("/nodes/actions/restart-all", response_class=None)
    async def restart_all_nodes(
        self,
        body: Annotated[RestartAllNodesRequestDto, PydanticBody()],
    ) -> None:
        """Restart Xray on all connected nodes (async)"""

    @post("/nodes/{uuid}/actions/reset-traffic", response_class=None)
    async def reset_node_traffic(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
    ) -> None:
        """Reset node traffic counters"""

    @post("/nodes/actions/reorder", response_class=ReorderNodeResponseDto)
    async def reorder_nodes(
        self,
        body: Annotated[ReorderNodesRequestDto, PydanticBody()],
    ) -> ReorderNodeResponseDto:
        """Reorder nodes"""

    @post("/nodes/bulk-actions", response_class=None)
    async def bulk_nodes_actions(
        self,
        body: Annotated[BulkNodesActionsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk nodes actions (enable/disable/restart/reset traffic)"""

    @post("/nodes/bulk-actions/update", response_class=None)
    async def bulk_nodes_update(
        self,
        body: Annotated[BulkNodesUpdateRequestDto, PydanticBody()],
    ) -> None:
        """Bulk update nodes"""

    @post("/nodes/bulk-actions/profile-modification", response_class=None)
    async def profile_modification(
        self,
        body: Annotated[ProfileModificationRequestDto, PydanticBody()],
    ) -> None:
        """Bulk modify config profiles on nodes"""
