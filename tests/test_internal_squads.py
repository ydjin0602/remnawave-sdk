from uuid import UUID

import pytest

from remnawave.models import (
    AddManyUsersToInternalSquadRequestDto,
    CreateInternalSquadRequestDto,
    CreateInternalSquadResponseDto,
    DeleteManyUsersFromInternalSquadRequestDto,
    GetAllInternalSquadsResponseDto,
    GetInternalSquadByUuidResponseDto,
    GetInternalSquadUsageResponseDto,
    ReorderInternalSquadItem,
    ReorderInternalSquadsRequestDto,
    ReorderInternalSquadsResponseDto,
    UpdateInternalSquadRequestDto,
    UpdateInternalSquadResponseDto,
)
from tests.utils import generate_date_range, generate_random_string


@pytest.mark.asyncio
async def test_internal_squads(remnawave, panel) -> None:
    squad_name = f"test_squad_{generate_random_string(length=6)}"

    # Test create internal squad
    create_squad = await remnawave.internal_squads.create_internal_squad(
        CreateInternalSquadRequestDto(
            name=squad_name, inbounds=[UUID(panel["inbound_uuid"])]
        )
    )

    assert isinstance(create_squad, CreateInternalSquadResponseDto)
    assert create_squad.name == squad_name

    squad_uuid = str(create_squad.uuid)

    # Test get all internal squads
    all_squads = await remnawave.internal_squads.get_internal_squads()
    assert isinstance(all_squads, GetAllInternalSquadsResponseDto)
    assert len(all_squads.internal_squads) > 0

    # Test get internal squad by uuid
    squad_by_uuid = await remnawave.internal_squads.get_internal_squad_by_uuid(
        squad_uuid
    )
    assert isinstance(squad_by_uuid, GetInternalSquadByUuidResponseDto)
    assert squad_by_uuid.name == squad_name

    # Test update internal squad
    update_squad = await remnawave.internal_squads.update_internal_squad(
        UpdateInternalSquadRequestDto(
            uuid=create_squad.uuid,
            inbounds=[UUID(panel["inbound_uuid"])],
        )
    )

    assert isinstance(update_squad, UpdateInternalSquadResponseDto)
    assert str(update_squad.inbounds[0].uuid) == panel["inbound_uuid"]

    # v3: add/remove users have no body, 202 no content
    await remnawave.internal_squads.add_users_to_internal_squad(squad_uuid)
    await remnawave.internal_squads.remove_users_from_internal_squad(squad_uuid)

    # v3: add-many / remove-many take explicit non-empty user id lists (202 no content)
    ref_user_id = panel["user_id"]
    await remnawave.internal_squads.add_many_users_to_internal_squad(
        squad_uuid,
        body=AddManyUsersToInternalSquadRequestDto(user_ids=[ref_user_id]),
    )
    await remnawave.internal_squads.remove_many_users_from_internal_squad(
        squad_uuid,
        body=DeleteManyUsersFromInternalSquadRequestDto(user_ids=[ref_user_id]),
    )

    # Test squad usage (v3)
    start, end = generate_date_range()
    usage = await remnawave.internal_squads.get_internal_squad_usage(
        uuid=squad_uuid, start=start, end=end
    )
    assert isinstance(usage, GetInternalSquadUsageResponseDto)

    # Test reorder internal squads
    all_squads = await remnawave.internal_squads.get_internal_squads()
    if len(all_squads.internal_squads) >= 2:
        items = [
            ReorderInternalSquadItem(
                uuid=squad.uuid,
                view_position=idx,
            )
            for idx, squad in enumerate(all_squads.internal_squads)
        ]
        reorder_result = await remnawave.internal_squads.reorder_internal_squads(
            ReorderInternalSquadsRequestDto(items=items)
        )
        assert isinstance(reorder_result, ReorderInternalSquadsResponseDto)

    # Test delete internal squad (v3: 204 no content)
    result = await remnawave.internal_squads.delete_internal_squad(squad_uuid)
    assert result is None
