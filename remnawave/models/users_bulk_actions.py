# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from remnawave.enums import TrafficLimitStrategy, UserStatus


class BulkDeleteUsersByStatusRequestDto(BaseModel):
    status: UserStatus


class BulkDeleteUsersRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")


class BulkRevokeUsersSubscriptionRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")


class BulkResetTrafficUsersRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")


class BulkUsersFieldsDto(BaseModel):
    status: UserStatus | None = None
    traffic_limit_bytes: float | None = Field(None, alias="trafficLimitBytes")
    traffic_limit_strategy: TrafficLimitStrategy | None = Field(
        None, alias="trafficLimitStrategy"
    )
    expire_at: datetime | None = Field(None, alias="expireAt")
    description: str | None = None
    telegram_id: int | None = Field(None, alias="telegramId")
    email: str | None = None
    tag: str | None = None
    hwid_device_limit: int | None = Field(None, alias="hwidDeviceLimit")
    external_squad_uuid: UUID | None = Field(None, alias="externalSquadUuid")


class BulkUpdateUsersRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")
    fields: BulkUsersFieldsDto


class BulkUpdateUsersSquadsRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")
    active_internal_squads: list[UUID] = Field(
        ..., serialization_alias="activeInternalSquads"
    )


class BulkExtendExpirationDateRequestDto(BaseModel):
    user_ids: list[int] = Field(..., serialization_alias="userIds")
    extend_days: int = Field(..., serialization_alias="extendDays")


class BulkAllUpdateUsersRequestDto(BaseModel):
    status: UserStatus | None = None
    traffic_limit_bytes: float | None = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    traffic_limit_strategy: TrafficLimitStrategy | None = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    expire_at: datetime | None = Field(None, serialization_alias="expireAt")
    description: str | None = None
    telegram_id: int | None = Field(None, serialization_alias="telegramId")
    email: EmailStr | None = None
    tag: str | None = None
    hwid_device_limit: int | None = Field(None, serialization_alias="hwidDeviceLimit")


class BulkAllExtendExpirationDateRequestDto(BaseModel):
    extend_days: int = Field(..., serialization_alias="extendDays")
