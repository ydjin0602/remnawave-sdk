from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateHostRequestDto,
    GetAllHostsResponseDto,
    GetAllHostTagsResponseDto,
    HostResponseDto,
    ReorderHostRequestDto,
    ReorderHostsResponseDto,
    UpdateHostRequestDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class HostsController(BaseController):
    @post("/hosts", response_class=HostResponseDto)
    async def create_host(
        self,
        body: Annotated[CreateHostRequestDto, PydanticBody()],
    ) -> HostResponseDto:
        """Create a new host"""

    @patch("/hosts", response_class=HostResponseDto)
    async def update_host(
        self,
        body: Annotated[UpdateHostRequestDto, PydanticBody()],
    ) -> HostResponseDto:
        """Update host"""

    @get("/hosts", response_class=GetAllHostsResponseDto)
    async def get_all_hosts(self) -> GetAllHostsResponseDto:
        """Get all hosts"""

    @get("/hosts/tags", response_class=GetAllHostTagsResponseDto)
    async def get_hosts_tags(self) -> GetAllHostTagsResponseDto:
        """Get all hosts tags"""

    @get("/hosts/{uuid}", response_class=HostResponseDto)
    async def get_one_host(
        self,
        uuid: Annotated[str, Path(description="UUID of the host")],
    ) -> HostResponseDto:
        """Get host by UUID"""

    @delete("/hosts/{uuid}", response_class=None)
    async def delete_host(
        self,
        uuid: Annotated[str, Path(description="UUID of the host")],
    ) -> None:
        """Delete host by UUID"""

    @post("/hosts/actions/reorder", response_class=ReorderHostsResponseDto)
    async def reorder_hosts(
        self,
        body: Annotated[ReorderHostRequestDto, PydanticBody()],
    ) -> ReorderHostsResponseDto:
        """Reorder hosts"""
