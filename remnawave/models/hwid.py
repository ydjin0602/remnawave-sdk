# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime

from pydantic import BaseModel, Field


class DevicesDto(BaseModel):
    hwid: str
    user_id: int = Field(..., alias="userId")
    platform: str | None = None
    os_version: str | None = Field(None, alias="osVersion")
    device_model: str | None = Field(None, alias="deviceModel")
    user_agent: str | None = Field(None, alias="userAgent")
    request_ip: str | None = Field(None, alias="requestIp")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class GetHwidDevicesQueryResponseDto(BaseModel):
    devices: list[DevicesDto]
    total: float


class CreateUserHwidDeviceRequestDto(BaseModel):
    hwid: str
    user_id: int = Field(..., serialization_alias="userId")
    platform: str | None = None
    os_version: str | None = Field(None, serialization_alias="osVersion")
    device_model: str | None = Field(None, serialization_alias="deviceModel")
    user_agent: str | None = Field(None, serialization_alias="userAgent")
    request_ip: str | None = Field(None, serialization_alias="requestIp")


class CreateUserHwidDeviceResponseDto(BaseModel):
    total: float
    devices: list[DevicesDto]


class DeleteUserHwidDeviceRequestDto(BaseModel):
    user_id: int = Field(..., serialization_alias="userId")
    hwid: str


class DeleteUserHwidDeviceResponseDto(CreateUserHwidDeviceResponseDto):
    """Alias of CreateUserHwidDeviceResponseDto (envelope unwrapped)."""


class DeleteUserAllHwidDeviceRequestDto(BaseModel):
    user_id: int = Field(..., serialization_alias="userId")


class DeleteUserAllHwidDeviceResponseDto(CreateUserHwidDeviceResponseDto):
    """Alias of CreateUserHwidDeviceResponseDto (envelope unwrapped)."""


class ByAppDto(BaseModel):
    app: str
    count: int


class ByPlatformDto(BaseModel):
    platform: str
    count: int
    by_app: list[ByAppDto] = Field(..., alias="byApp")


class StatsDto(BaseModel):
    total_unique_devices: float = Field(..., alias="totalUniqueDevices")
    total_hwid_devices: float = Field(..., alias="totalHwidDevices")
    average_hwid_devices_per_user: float = Field(..., alias="averageHwidDevicesPerUser")


class GetHwidStatisticsResponseDto(BaseModel):
    by_platform: list[ByPlatformDto] = Field(..., alias="byPlatform")
    stats: StatsDto


class HwidUsersDto(BaseModel):
    id: int
    username: str
    devices_count: int = Field(..., alias="devicesCount")


class GetTopUsersByHwidDevicesResponseDto(BaseModel):
    users: list[HwidUsersDto]
    total: float


class GetUserHwidDevicesResponseDto(CreateUserHwidDeviceResponseDto):
    """Alias of CreateUserHwidDeviceResponseDto (envelope unwrapped)."""
