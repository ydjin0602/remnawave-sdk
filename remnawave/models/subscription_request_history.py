# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class SubReqHistoryRecordsDto(BaseModel):
    id: int
    user_id: int = Field(..., alias="userId")
    srr_response_type: str = Field(..., alias="srrResponseType")
    srr_rule_name: str | None = Field(None, alias="srrRuleName")
    request_ip: str | None = Field(None, alias="requestIp")
    user_agent: str | None = Field(None, alias="userAgent")
    request_at: datetime = Field(..., alias="requestAt")


class GetSubscriptionRequestHistoryResponseDto(BaseModel):
    records: list[SubReqHistoryRecordsDto]
    total: float


class ByParsedAppDto(BaseModel):
    app: str
    count: int


class HourlyRequestStatsDto(BaseModel):
    date_time: datetime = Field(..., alias="dateTime")
    request_count: int = Field(..., alias="requestCount")


class GetSubscriptionRequestHistoryStatsResponseDto(BaseModel):
    by_parsed_app: list[ByParsedAppDto] = Field(..., alias="byParsedApp")
    hourly_request_stats: list[HourlyRequestStatsDto] = Field(
        ..., alias="hourlyRequestStats"
    )


class RemnawaveSubscriptionRequestStreamMessageDto(BaseModel):
    v: Literal["1"]
    user_id: str = Field(..., alias="userId")
    request_at: datetime = Field(..., alias="requestAt")
    request_ip: str | None = Field(None, alias="requestIp")
    user_agent: str | None = Field(None, alias="userAgent")
    srr_rule_name: str | None = Field(None, alias="srrRuleName")
    srr_response_type: str = Field(..., alias="srrResponseType")
