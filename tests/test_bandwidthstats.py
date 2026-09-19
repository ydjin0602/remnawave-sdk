import pytest

from remnawave.models import (
    GetInternalSquadUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodesUsersUsageRequestDto,
    GetStatsNodesUsersUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,
)
from tests.utils import generate_date_range


@pytest.mark.asyncio
async def test_nodes_usage(remnawave):
    """Test GET /bandwidth-stats/nodes"""
    start, end = generate_date_range()
    usage = await remnawave.bandwidthstats.get_nodes_usage(start=start, end=end)
    assert isinstance(usage, GetStatsNodesUsageResponseDto)
    assert hasattr(usage, "categories")
    assert hasattr(usage, "top_nodes")


@pytest.mark.asyncio
async def test_stats_user_usage(remnawave):
    """Test GET /bandwidth-stats/users/{userId}"""
    users = await remnawave.users.get_all_users(size=1)
    if not users.users:
        pytest.skip("No users available for testing")
    user_id = users.users[0].id
    start, end = generate_date_range()
    usage = await remnawave.bandwidthstats.get_stats_user_usage(
        user_id=user_id, start=start, end=end
    )
    assert isinstance(usage, GetStatsUserUsageResponseDto)
    assert hasattr(usage, "top_nodes")


@pytest.mark.asyncio
async def test_stats_node_users_usage(remnawave):
    """Test GET /bandwidth-stats/nodes/{uuid}/users"""
    nodes = await remnawave.nodes.get_all_nodes()
    if not nodes.root:
        pytest.skip("No nodes available for testing")
    node_uuid = str(nodes.root[0].uuid)
    start, end = generate_date_range()
    usage = await remnawave.bandwidthstats.get_stats_node_users_usage(
        uuid=node_uuid, start=start, end=end
    )
    assert isinstance(usage, GetStatsNodeUsersUsageResponseDto)
    assert hasattr(usage, "top_users")


@pytest.mark.asyncio
async def test_stats_nodes_users_usage(remnawave):
    """Test POST /bandwidth-stats/nodes/users"""
    nodes = await remnawave.nodes.get_all_nodes()
    if not nodes.root:
        pytest.skip("No nodes available for testing")
    node_uuids = [str(n.uuid) for n in nodes.root[:3]]
    start, end = generate_date_range()
    usage = await remnawave.bandwidthstats.get_stats_nodes_users_usage(
        start=start,
        end=end,
        body=GetStatsNodesUsersUsageRequestDto(nodes_uuids=node_uuids),
    )
    assert isinstance(usage, GetStatsNodesUsersUsageResponseDto)
    assert hasattr(usage, "top_users")


@pytest.mark.asyncio
async def test_internal_squad_usage_via_bandwidthstats(remnawave):
    """Test GET /bandwidth-stats/internal-squads/{uuid}/usage"""
    squads = await remnawave.internal_squads.get_internal_squads()
    if not squads.internal_squads:
        pytest.skip("No internal squads available for testing")
    squad_uuid = str(squads.internal_squads[0].uuid)
    start, end = generate_date_range()
    usage = await remnawave.bandwidthstats.get_internal_squad_usage(
        uuid=squad_uuid, start=start, end=end
    )
    assert isinstance(usage, GetInternalSquadUsageResponseDto)
    assert hasattr(usage, "users")
