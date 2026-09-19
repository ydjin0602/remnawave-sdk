from typing import Annotated, Any

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateUserHwidDeviceRequestDto,
    CreateUserHwidDeviceResponseDto,
    DeleteUserAllHwidDeviceRequestDto,
    DeleteUserAllHwidDeviceResponseDto,
    DeleteUserHwidDeviceRequestDto,
    DeleteUserHwidDeviceResponseDto,
    GetHwidDevicesQueryResponseDto,
    GetHwidStatisticsResponseDto,
    GetTopUsersByHwidDevicesResponseDto,
    GetUserHwidDevicesResponseDto,
)
from remnawave.rapid import BaseController, get, post


class HWIDUserController(BaseController):
    @get("/hwid/devices", response_class=GetHwidDevicesQueryResponseDto)
    async def get_all_users(
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
                description="Table filters, e.g. [{'id': 'platform', 'value': 'ios'}] (JSON-encoded)",
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
    ) -> GetHwidDevicesQueryResponseDto:
        """Get all HWID devices (paginated, filterable, sortable)"""

    @get("/hwid/devices/{userId}", response_class=GetUserHwidDevicesResponseDto)
    async def get_user_hwid_devices(
        self,
        user_id: Annotated[int, Path(alias="userId", description="User ID")],
    ) -> GetUserHwidDevicesResponseDto:
        """Get HWID devices of a user"""

    @get("/hwid/devices/stats", response_class=GetHwidStatisticsResponseDto)
    async def get_hwid_devices_stats(self) -> GetHwidStatisticsResponseDto:
        """Get HWID devices statistics"""

    @get("/hwid/devices/top-users", response_class=GetTopUsersByHwidDevicesResponseDto)
    async def get_top_users_by_hwid_devices(
        self,
        start: Annotated[
            int, Query(default=0, description="Offset for pagination")
        ] = 0,
        size: Annotated[int, Query(default=5, ge=1, description="Page size")] = 5,
    ) -> GetTopUsersByHwidDevicesResponseDto:
        """Get top users by HWID devices count"""

    @post("/hwid/devices", response_class=CreateUserHwidDeviceResponseDto)
    async def create_user_hwid_device(
        self,
        body: Annotated[CreateUserHwidDeviceRequestDto, PydanticBody()],
    ) -> CreateUserHwidDeviceResponseDto:
        """Create (register) a HWID device"""

    @post("/hwid/devices/delete", response_class=DeleteUserHwidDeviceResponseDto)
    async def delete_user_hwid_device(
        self,
        body: Annotated[DeleteUserHwidDeviceRequestDto, PydanticBody()],
    ) -> DeleteUserHwidDeviceResponseDto:
        """Delete a specific HWID device"""

    @post("/hwid/devices/delete-all", response_class=DeleteUserAllHwidDeviceResponseDto)
    async def delete_all_user_hwid_devices(
        self,
        body: Annotated[DeleteUserAllHwidDeviceRequestDto, PydanticBody()],
    ) -> DeleteUserAllHwidDeviceResponseDto:
        """Delete all HWID devices of a user"""
