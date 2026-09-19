from datetime import datetime, timedelta

import pytest
import pytz

from remnawave.models import BulkUpdateUsersRequestDto, BulkUsersFieldsDto


@pytest.mark.asyncio
async def test_users_bulk_actions(remnawave):
    expire_at = datetime.now(tz=pytz.utc) + timedelta(days=14)
    description = "TEST_DESCRIPTION"

    # v3: bulk actions return 202/204 with no body
    await remnawave.users_bulk_actions.bulk_update_users(
        body=BulkUpdateUsersRequestDto(
            user_ids=[1],
            fields=BulkUsersFieldsDto(
                expire_at=expire_at,
                description=description,
            ),
        ),
    )
