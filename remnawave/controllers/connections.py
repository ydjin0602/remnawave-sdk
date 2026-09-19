from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    ConnectionsByNodeResponseDto,
    ConnectionsByNodeResultResponseDto,
    ConnectionsByUserResponseDto,
    ConnectionsByUserResultResponseDto,
    DropConnectionsRequestDto,
)
from remnawave.rapid import BaseController, get, post


class ConnectionsController(BaseController):
    """Connections jobs API (replaces IP Control in Remnawave API v3.x)."""

    @post("/connections/by-user/{userId}", response_class=ConnectionsByUserResponseDto)
    async def connections_by_user(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> ConnectionsByUserResponseDto:
        """Start async job: collect IPs used by a user across nodes"""

    @get(
        "/connections/by-user/{jobId}",
        response_class=ConnectionsByUserResultResponseDto,
    )
    async def connections_by_user_result(
        self,
        job_id: Annotated[str, Path(alias="jobId", description="Job ID")],
    ) -> ConnectionsByUserResultResponseDto:
        """Fetch result of the by-user connections job"""

    @post(
        "/connections/by-node/{nodeUuid}", response_class=ConnectionsByNodeResponseDto
    )
    async def connections_by_node(
        self,
        node_uuid: Annotated[str, Path(alias="nodeUuid", description="Node UUID")],
    ) -> ConnectionsByNodeResponseDto:
        """Start async job: collect users connected to a node"""

    @get(
        "/connections/by-node/{jobId}",
        response_class=ConnectionsByNodeResultResponseDto,
    )
    async def connections_by_node_result(
        self,
        job_id: Annotated[str, Path(alias="jobId", description="Job ID")],
    ) -> ConnectionsByNodeResultResponseDto:
        """Fetch result of the by-node connections job"""

    @post("/connections/drop", response_class=None)
    async def drop_connections(
        self,
        body: Annotated[DropConnectionsRequestDto, PydanticBody()],
    ) -> None:
        """Drop active connections by user IDs or IP addresses (async)"""
