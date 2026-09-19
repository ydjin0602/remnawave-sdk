from typing import Annotated

from rapid_api_client import Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    BandwidthStatisticResponseDto,
    DebugSrrMatcherRequestDto,
    DebugSrrMatcherResponseDto,
    GetConfigurationResponseDto,
    GetHttpStatsResponseDto,
    GetMetadataResponseDto,
    GetNodesMetricsResponseDto,
    GetNodesStatisticsResponseDto,
    GetRecapResponseDto,
    GetRemnawaveHealthResponseDto,
    GetStatsDigestResponseDto,
    GetStatsResponseDto,
    GetX25519KeyPairResponseDto,
)
from remnawave.rapid import BaseController, get, post


class SystemController(BaseController):
    @get("/system/health", response_class=GetRemnawaveHealthResponseDto)
    async def get_health(self) -> GetRemnawaveHealthResponseDto:
        """Get panel health status"""

    @get("/system/stats", response_class=GetStatsResponseDto)
    async def get_stats(self) -> GetStatsResponseDto:
        """Get panel stats"""

    @get("/system/stats/bandwidth", response_class=BandwidthStatisticResponseDto)
    async def get_bandwidth_stats(
        self,
        tz: Annotated[
            str, Query(description="IANA timezone, e.g. Europe/London")
        ] = "UTC",
    ) -> BandwidthStatisticResponseDto:
        """Get bandwidth stats"""

    @get("/system/stats/digest", response_class=GetStatsDigestResponseDto)
    async def get_stats_digest(
        self,
        start: Annotated[str, Query(description="Start date (YYYY-MM-DD, UTC)")],
        end: Annotated[str, Query(description="End date (YYYY-MM-DD, UTC)")],
    ) -> GetStatsDigestResponseDto:
        """Get stats digest for a period"""

    @get("/system/stats/http", response_class=GetHttpStatsResponseDto)
    async def get_http_stats(self) -> GetHttpStatsResponseDto:
        """Get HTTP (routes) stats"""

    @get("/system/nodes/metrics", response_class=GetNodesMetricsResponseDto)
    async def get_nodes_metrics(self) -> GetNodesMetricsResponseDto:
        """Get nodes metrics (Prometheus format)"""

    @get("/system/stats/nodes", response_class=GetNodesStatisticsResponseDto)
    async def get_nodes_statistics(self) -> GetNodesStatisticsResponseDto:
        """Get nodes statistics (last seven days)"""

    @get("/system/stats/recap", response_class=GetRecapResponseDto)
    async def get_recap(self) -> GetRecapResponseDto:
        """Get panel recap"""

    @get("/system/metadata", response_class=GetMetadataResponseDto)
    async def get_metadata(self) -> GetMetadataResponseDto:
        """Get panel metadata (version, commit, etc.)"""

    @get("/system/configuration", response_class=GetConfigurationResponseDto)
    async def get_configuration(self) -> GetConfigurationResponseDto:
        """Get effective panel configuration"""

    @get("/system/tools/x25519/generate", response_class=GetX25519KeyPairResponseDto)
    async def generate_x25519_keypairs(self) -> GetX25519KeyPairResponseDto:
        """Generate X25519 keypair"""

    @post("/system/testers/srr-matcher", response_class=DebugSrrMatcherResponseDto)
    async def debug_srr_matcher(
        self,
        body: Annotated[DebugSrrMatcherRequestDto, PydanticBody()],
    ) -> DebugSrrMatcherResponseDto:
        """Test SRR (Subscription Response Rules) matcher against headers"""
