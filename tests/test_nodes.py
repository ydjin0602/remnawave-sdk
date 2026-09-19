import random

import pytest

from remnawave.models import (
    CreateNodeRequestDto,
    GetAllNodesResponseDto,
    NodeResponseDto,
    ReorderNodeResponseDto,
    ReorderNodesRequestDto,
    UpdateNodeRequestDto,
)
from remnawave.models.nodes import ReorderNodeItem
from tests.utils import generate_random_string


@pytest.mark.asyncio
async def test_nodes(remnawave, panel):
    all_nodes = await remnawave.nodes.get_all_nodes()
    assert isinstance(all_nodes, GetAllNodesResponseDto)

    random_ip: str = (
        f"10.{random.randint(0, 254)}.{random.randint(0, 254)}.{random.randint(1, 254)}"
    )
    random_port: int = random.randint(5000, 8000)
    random_name: str = generate_random_string()
    create_node = await remnawave.nodes.create_node(
        CreateNodeRequestDto(
            name=random_name,
            address=random_ip,
            port=random_port,
            config_profile={
                "activeConfigProfileUuid": panel["config_profile_uuid"],
                "activeInbounds": [panel["inbound_uuid"]],
            },
            ips=[{"ip": random_ip, "status": "INBOUND"}],
        )
    )
    assert isinstance(create_node, NodeResponseDto)

    string_uuid = str(create_node.uuid)

    node = await remnawave.nodes.get_node(uuid=string_uuid)
    assert isinstance(node, NodeResponseDto)

    reorder_node = await remnawave.nodes.reorder_nodes(
        ReorderNodesRequestDto(
            nodes=[
                ReorderNodeItem(
                    view_position=random.randint(1, 1000), uuid=create_node.uuid
                )
            ]
        )
    )
    print(reorder_node)
    assert isinstance(reorder_node, ReorderNodeResponseDto)
    # assert any(node.uuid == create_node.uuid for node in reorder_node.root)

    update_name: str = "TEST_NAME"
    update_node = await remnawave.nodes.update_node(
        UpdateNodeRequestDto(uuid=string_uuid, name=update_name)
    )
    assert isinstance(update_node, NodeResponseDto)
    assert update_node.uuid == create_node.uuid
    assert update_node.name == update_name

    # v3: reset traffic and delete return 204 no content
    assert await remnawave.nodes.reset_node_traffic(uuid=string_uuid) is None
    assert await remnawave.nodes.delete_node(uuid=string_uuid) is None
