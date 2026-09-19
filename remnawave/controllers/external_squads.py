from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateExternalSquadRequestDto,
    CreateExternalSquadResponseDto,
    GetExternalSquadByUuidResponseDto,
    GetExternalSquadsResponseDto,
    ReorderExternalSquadsRequestDto,
    ReorderExternalSquadsResponseDto,
    UpdateExternalSquadRequestDto,
    UpdateExternalSquadResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class ExternalSquadsController(BaseController):
    @get("/external-squads", response_class=GetExternalSquadsResponseDto)
    async def get_external_squads(self) -> GetExternalSquadsResponseDto:
        """Get all external squads"""

    @post("/external-squads", response_class=CreateExternalSquadResponseDto)
    async def create_external_squad(
        self,
        body: Annotated[CreateExternalSquadRequestDto, PydanticBody()],
    ) -> CreateExternalSquadResponseDto:
        """Create a new external squad"""

    @patch("/external-squads", response_class=UpdateExternalSquadResponseDto)
    async def update_external_squad(
        self,
        body: Annotated[UpdateExternalSquadRequestDto, PydanticBody()],
    ) -> UpdateExternalSquadResponseDto:
        """Update external squad"""

    @post(
        "/external-squads/actions/reorder",
        response_class=ReorderExternalSquadsResponseDto,
    )
    async def reorder_external_squads(
        self,
        body: Annotated[ReorderExternalSquadsRequestDto, PydanticBody()],
    ) -> ReorderExternalSquadsResponseDto:
        """Reorder external squads"""

    @get("/external-squads/{uuid}", response_class=GetExternalSquadByUuidResponseDto)
    async def get_external_squad_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the external squad")],
    ) -> GetExternalSquadByUuidResponseDto:
        """Get external squad by UUID"""

    @delete("/external-squads/{uuid}", response_class=None)
    async def delete_external_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the external squad")],
    ) -> None:
        """Delete external squad by UUID"""

    @post("/external-squads/{uuid}/bulk-actions/add-users", response_class=None)
    async def add_users_to_external_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the external squad")],
    ) -> None:
        """Add users to external squad (async)"""

    @delete("/external-squads/{uuid}/bulk-actions/remove-users", response_class=None)
    async def remove_users_from_external_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the external squad")],
    ) -> None:
        """Remove users from external squad (async)"""
