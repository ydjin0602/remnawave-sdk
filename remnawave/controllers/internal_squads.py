from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    AddManyUsersToInternalSquadRequestDto,
    CreateInternalSquadRequestDto,
    CreateInternalSquadResponseDto,
    DeleteManyUsersFromInternalSquadRequestDto,
    GetAllInternalSquadsResponseDto,
    GetInternalSquadAccessibleNodesResponseDto,
    GetInternalSquadByUuidResponseDto,
    GetInternalSquadUsageResponseDto,
    ReorderInternalSquadsRequestDto,
    ReorderInternalSquadsResponseDto,
    UpdateInternalSquadRequestDto,
    UpdateInternalSquadResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class InternalSquadsController(BaseController):
    @get("/internal-squads", response_class=GetAllInternalSquadsResponseDto)
    async def get_internal_squads(self) -> GetAllInternalSquadsResponseDto:
        """Get all internal squads"""

    @post("/internal-squads", response_class=CreateInternalSquadResponseDto)
    async def create_internal_squad(
        self,
        body: Annotated[CreateInternalSquadRequestDto, PydanticBody()],
    ) -> CreateInternalSquadResponseDto:
        """Create a new internal squad"""

    @patch("/internal-squads", response_class=UpdateInternalSquadResponseDto)
    async def update_internal_squad(
        self,
        body: Annotated[UpdateInternalSquadRequestDto, PydanticBody()],
    ) -> UpdateInternalSquadResponseDto:
        """Update internal squad"""

    @post(
        "/internal-squads/actions/reorder",
        response_class=ReorderInternalSquadsResponseDto,
    )
    async def reorder_internal_squads(
        self,
        body: Annotated[ReorderInternalSquadsRequestDto, PydanticBody()],
    ) -> ReorderInternalSquadsResponseDto:
        """Reorder internal squads"""

    @get("/internal-squads/{uuid}", response_class=GetInternalSquadByUuidResponseDto)
    async def get_internal_squad_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> GetInternalSquadByUuidResponseDto:
        """Get internal squad by UUID"""

    @delete("/internal-squads/{uuid}", response_class=None)
    async def delete_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> None:
        """Delete internal squad by UUID"""

    @get(
        "/internal-squads/{uuid}/accessible-nodes",
        response_class=GetInternalSquadAccessibleNodesResponseDto,
    )
    async def get_internal_squad_accessible_nodes(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> GetInternalSquadAccessibleNodesResponseDto:
        """Get nodes accessible to the internal squad"""

    @get(
        "/internal-squads/{uuid}/usage", response_class=GetInternalSquadUsageResponseDto
    )
    async def get_internal_squad_usage(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
        min_total_bytes: Annotated[int, Query(default=0, alias="minTotalBytes")] = 0,
        limit: Annotated[int, Query(default=250, ge=1, le=1000)] = 250,
        cursor: Annotated[str | None, Query(default=None)] = None,
    ) -> GetInternalSquadUsageResponseDto:
        """Get internal squad usage (see also BandwidthStatsController)"""

    @post("/internal-squads/{uuid}/bulk-actions/add-users", response_class=None)
    async def add_users_to_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> None:
        """Add all squad-bound users to internal squad (async)"""

    @post("/internal-squads/{uuid}/bulk-actions/add-many-users", response_class=None)
    async def add_many_users_to_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
        body: Annotated[AddManyUsersToInternalSquadRequestDto, PydanticBody()],
    ) -> None:
        """Add many users to internal squad (chunked, async)"""

    @delete("/internal-squads/{uuid}/bulk-actions/remove-users", response_class=None)
    async def remove_users_from_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> None:
        """Remove users from internal squad (async)"""

    @delete(
        "/internal-squads/{uuid}/bulk-actions/remove-many-users", response_class=None
    )
    async def remove_many_users_from_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
        body: Annotated[DeleteManyUsersFromInternalSquadRequestDto, PydanticBody()],
    ) -> None:
        """Remove many users from internal squad (chunked, async)"""
