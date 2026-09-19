# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from remnawave.enums import (
    EncryptionMethod,
    ResponseRuleConditionOperator,
    ResponseRuleOperator,
    ResponseType,
)


class BuildDto(BaseModel):
    time: str
    number: str


class BackendDto(BaseModel):
    commit_sha: str = Field(..., alias="commitSha")
    branch: str
    commit_url: str = Field(..., alias="commitUrl")


class FrontendDto(BaseModel):
    commit_sha: str = Field(..., alias="commitSha")
    commit_url: str = Field(..., alias="commitUrl")


class GitDto(BaseModel):
    backend: BackendDto
    frontend: FrontendDto


class GetMetadataResponseDto(BaseModel):
    version: str
    build: BuildDto
    git: GitDto


class NotificationsDto(BaseModel):
    webhook: bool
    bandwidth_usage: list[float] | None = Field(None, alias="bandwidthUsage")
    not_connected_after: list[float] | None = Field(None, alias="notConnectedAfter")
    expiration_notifications: list[float] | None = Field(
        None, alias="expirationNotifications"
    )


class ServiceDto(BaseModel):
    clean_usage_history: bool = Field(..., alias="cleanUsageHistory")
    disable_user_usage_records: bool = Field(..., alias="disableUserUsageRecords")
    disable_srh_records: bool = Field(..., alias="disableSrhRecords")
    export_to_redis_stream: bool = Field(..., alias="exportToRedisStream")


class MiscDto(BaseModel):
    short_uuid_length: float = Field(..., alias="shortUuidLength")
    sub_public_domain: str = Field(..., alias="subPublicDomain")
    user_usage_ignore_below_bytes: float = Field(..., alias="userUsageIgnoreBelowBytes")


class GetConfigurationResponseDto(BaseModel):
    notifications: NotificationsDto
    service: ServiceDto
    misc: MiscDto


class CPUStatistic(BaseModel):
    cores: float


class MemoryStatistic(BaseModel):
    total: float
    free: float
    used: float


class UsersStatistic(BaseModel):
    status_counts: dict[str, Any] = Field(..., alias="statusCounts")
    total_users: float = Field(..., alias="totalUsers")


class OnlineStatistic(BaseModel):
    last_day: float = Field(..., alias="lastDay")
    last_week: float = Field(..., alias="lastWeek")
    never_online: float = Field(..., alias="neverOnline")
    online_now: float = Field(..., alias="onlineNow")


class NodesStatisticDto(BaseModel):
    total_online: float = Field(..., alias="totalOnline")
    total_bytes_lifetime: str = Field(..., alias="totalBytesLifetime")


class GetStatsResponseDto(BaseModel):
    cpu: CPUStatistic
    memory: MemoryStatistic
    uptime: float
    timestamp: float
    users: UsersStatistic
    online_stats: OnlineStatistic = Field(..., alias="onlineStats")
    nodes: NodesStatisticDto


class BandwidthLastTwoDaysDto(BaseModel):
    current: str
    previous: str
    difference: str


class BandwidthStatisticResponseDto(BaseModel):
    bandwidth_last_two_days: BandwidthLastTwoDaysDto = Field(
        ..., alias="bandwidthLastTwoDays"
    )
    bandwidth_last_seven_days: BandwidthLastTwoDaysDto = Field(
        ..., alias="bandwidthLastSevenDays"
    )
    bandwidth_last30_days: BandwidthLastTwoDaysDto = Field(
        ..., alias="bandwidthLast30Days"
    )
    bandwidth_calendar_month: BandwidthLastTwoDaysDto = Field(
        ..., alias="bandwidthCalendarMonth"
    )
    bandwidth_current_year: BandwidthLastTwoDaysDto = Field(
        ..., alias="bandwidthCurrentYear"
    )


class LastSevenDaysDto(BaseModel):
    node_name: str = Field(..., alias="nodeName")
    date: str
    total_bytes: str = Field(..., alias="totalBytes")


class GetNodesStatisticsResponseDto(BaseModel):
    last_seven_days: list[LastSevenDaysDto] = Field(..., alias="lastSevenDays")


class RuntimeMetricsDto(BaseModel):
    rss: float
    heap_used: float = Field(..., alias="heapUsed")
    heap_total: float = Field(..., alias="heapTotal")
    external: float
    array_buffers: float = Field(..., alias="arrayBuffers")
    event_loop_delay_ms: float = Field(..., alias="eventLoopDelayMs")
    event_loop_p99_ms: float = Field(..., alias="eventLoopP99Ms")
    active_handles: float = Field(..., alias="activeHandles")
    uptime: float
    pid: int
    timestamp: float
    instance_id: str = Field(..., alias="instanceId")
    instance_type: str = Field(..., alias="instanceType")


class GetRemnawaveHealthResponseDto(BaseModel):
    runtime_metrics: list[RuntimeMetricsDto] = Field(..., alias="runtimeMetrics")


class InboundsStatsDto(BaseModel):
    tag: str
    upload: str
    download: str


class SystemNodesDto(BaseModel):
    node_uuid: str = Field(..., alias="nodeUuid")
    node_name: str = Field(..., alias="nodeName")
    country_emoji: str = Field(..., alias="countryEmoji")
    provider_name: str = Field(..., alias="providerName")
    users_online: float = Field(..., alias="usersOnline")
    inbounds_stats: list[InboundsStatsDto] = Field(..., alias="inboundsStats")
    outbounds_stats: list[InboundsStatsDto] = Field(..., alias="outboundsStats")


class GetNodesMetricsResponseDto(BaseModel):
    nodes: list[SystemNodesDto]


class KeypairsDto(BaseModel):
    public_key: str = Field(..., alias="publicKey")
    private_key: str = Field(..., alias="privateKey")


class GetX25519KeyPairResponseDto(BaseModel):
    keypairs: list[KeypairsDto]


class SystemSettingsDto(BaseModel):
    disable_subscription_access_by_path: bool | None = Field(
        None, alias="disableSubscriptionAccessByPath"
    )


class SystemConditionsDto(BaseModel):
    header_name: str = Field(..., alias="headerName")
    operator: ResponseRuleConditionOperator
    value: str
    case_sensitive: bool = Field(..., alias="caseSensitive")


class SystemHeadersDto(BaseModel):
    key: str
    value: str


class SystemEncryptionDto(BaseModel):
    method: EncryptionMethod
    key: str


class SystemResponseModificationsDto(BaseModel):
    headers: list[SystemHeadersDto] | None = None
    apply_headers_to_end: bool | None = Field(None, alias="applyHeadersToEnd")
    subscription_template: str | None = Field(None, alias="subscriptionTemplate")
    ignore_host_xray_json_template: bool | None = Field(
        None, alias="ignoreHostXrayJsonTemplate"
    )
    ignore_serve_json_at_base_subscription: bool | None = Field(
        None, alias="ignoreServeJsonAtBaseSubscription"
    )
    additional_extended_clients_regex: list[str] | None = Field(
        None, alias="additionalExtendedClientsRegex"
    )
    disable_hwid_check: bool | None = Field(None, alias="disableHwidCheck")
    encryption: SystemEncryptionDto | None = None
    exclude_hosts_by_tags: list[str] | None = Field(None, alias="excludeHostsByTags")


class SystemRulesDto(BaseModel):
    name: str
    description: str | None = None
    enabled: bool
    operator: ResponseRuleOperator
    conditions: list[SystemConditionsDto]
    response_type: ResponseType = Field(..., alias="responseType")
    response_modifications: SystemResponseModificationsDto | None = Field(
        None, alias="responseModifications"
    )


class SystemResponseRulesDto(BaseModel):
    version: Literal["1"]
    settings: SystemSettingsDto | None = None
    rules: list[SystemRulesDto]


class DebugSrrMatcherRequestDto(BaseModel):
    response_rules: SystemResponseRulesDto = Field(
        ..., serialization_alias="responseRules"
    )


class MatchedRuleDto(BaseModel):
    name: str
    description: str | None = None
    enabled: bool
    operator: ResponseRuleOperator
    conditions: list[SystemConditionsDto]
    response_type: ResponseType = Field(..., alias="responseType")
    response_modifications: SystemResponseModificationsDto | None = Field(
        None, alias="responseModifications"
    )


class DebugSrrMatcherResponseDto(BaseModel):
    matched: bool
    response_type: ResponseType = Field(..., alias="responseType")
    matched_rule: MatchedRuleDto | None = Field(None, alias="matchedRule")
    input_headers: dict[str, Any] = Field(..., alias="inputHeaders")
    output_headers: dict[str, Any] = Field(..., alias="outputHeaders")


class RecapThisMonth(BaseModel):
    users: float
    traffic: str


class RecapTotal(BaseModel):
    users: float
    nodes: float
    traffic: str
    nodes_ram: str = Field(..., alias="nodesRam")
    nodes_cpu_cores: float = Field(..., alias="nodesCpuCores")
    distinct_countries: float = Field(..., alias="distinctCountries")


class GetRecapResponseDto(BaseModel):
    this_month: RecapThisMonth = Field(..., alias="thisMonth")
    total: RecapTotal
    version: str
    init_date: datetime = Field(..., alias="initDate")


class SystemUsersDto(BaseModel):
    created_count: int = Field(..., alias="createdCount")
    expired_count: int = Field(..., alias="expiredCount")


class TrafficDto(BaseModel):
    total_bytes: str = Field(..., alias="totalBytes")
    by_users_created_in_range_bytes: str = Field(
        ..., alias="byUsersCreatedInRangeBytes"
    )


class HwidDevicesDto(BaseModel):
    created_count: int = Field(..., alias="createdCount")


class GetStatsDigestResponseDto(BaseModel):
    users: SystemUsersDto
    traffic: TrafficDto
    hwid_devices: HwidDevicesDto = Field(..., alias="hwidDevices")


class RoutesDto(BaseModel):
    method: str
    route: str
    count: int


class GetHttpStatsResponseDto(BaseModel):
    routes: list[RoutesDto]
    total: int
