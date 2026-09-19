from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    BulkDeleteHostsRequestDto,
    BulkDisableHostsRequestDto,
    BulkEnableHostsRequestDto,
    UpdateManyHostsRequestDto,
)
from remnawave.rapid import BaseController, patch, post


class HostsBulkActionsController(BaseController):
    @post("/hosts/bulk/delete", response_class=None)
    async def bulk_delete_hosts(
        self,
        body: Annotated[BulkDeleteHostsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk delete hosts"""

    @post("/hosts/bulk/disable", response_class=None)
    async def bulk_disable_hosts(
        self,
        body: Annotated[BulkDisableHostsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk disable hosts"""

    @post("/hosts/bulk/enable", response_class=None)
    async def bulk_enable_hosts(
        self,
        body: Annotated[BulkEnableHostsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk enable hosts"""

    @patch("/hosts/bulk/update", response_class=None)
    async def set_port_to_hosts(
        self,
        body: Annotated[UpdateManyHostsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk update hosts (e.g. set port)"""
