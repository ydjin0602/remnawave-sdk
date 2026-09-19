from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateConfigProfileRequestDto,
    CreateConfigProfileResponseDto,
    GetAllConfigProfilesResponseDto,
    GetAllInboundsResponseDto,
    GetComputedConfigProfileByUuidResponseDto,
    GetConfigProfileByUuidResponseDto,
    GetInboundsByProfileUuidResponseDto,
    ReorderConfigProfilesRequestDto,
    ReorderConfigProfilesResponseDto,
    UpdateConfigProfileRequestDto,
    UpdateConfigProfileResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class ConfigProfilesController(BaseController):
    @get("/config-profiles", response_class=GetAllConfigProfilesResponseDto)
    async def get_config_profiles(self) -> GetAllConfigProfilesResponseDto:
        """Get all config profiles"""

    @post("/config-profiles", response_class=CreateConfigProfileResponseDto)
    async def create_config_profile(
        self,
        body: Annotated[CreateConfigProfileRequestDto, PydanticBody()],
    ) -> CreateConfigProfileResponseDto:
        """Create a new config profile"""

    @patch("/config-profiles", response_class=UpdateConfigProfileResponseDto)
    async def update_config_profile(
        self,
        body: Annotated[UpdateConfigProfileRequestDto, PydanticBody()],
    ) -> UpdateConfigProfileResponseDto:
        """Update config profile"""

    @post(
        "/config-profiles/actions/reorder",
        response_class=ReorderConfigProfilesResponseDto,
    )
    async def reorder_config_profiles(
        self,
        body: Annotated[ReorderConfigProfilesRequestDto, PydanticBody()],
    ) -> ReorderConfigProfilesResponseDto:
        """Reorder config profiles"""

    @get("/config-profiles/inbounds", response_class=GetAllInboundsResponseDto)
    async def get_all_inbounds(self) -> GetAllInboundsResponseDto:
        """Get all inbounds across config profiles"""

    @get("/config-profiles/{uuid}", response_class=GetConfigProfileByUuidResponseDto)
    async def get_config_profile_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config profile")],
    ) -> GetConfigProfileByUuidResponseDto:
        """Get config profile by UUID"""

    @delete("/config-profiles/{uuid}", response_class=None)
    async def delete_config_profile_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config profile")],
    ) -> None:
        """Delete config profile by UUID"""

    @get(
        "/config-profiles/{uuid}/computed-config",
        response_class=GetComputedConfigProfileByUuidResponseDto,
    )
    async def get_computed_config_profile_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config profile")],
    ) -> GetComputedConfigProfileByUuidResponseDto:
        """Get computed Xray config of a profile"""

    @get(
        "/config-profiles/{uuid}/inbounds",
        response_class=GetInboundsByProfileUuidResponseDto,
    )
    async def get_inbounds_by_profile_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config profile")],
    ) -> GetInboundsByProfileUuidResponseDto:
        """Get inbounds of a config profile"""
