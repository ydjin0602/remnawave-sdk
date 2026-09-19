from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    BulkAllExtendExpirationDateRequestDto,
    BulkAllUpdateUsersRequestDto,
    BulkDeleteUsersByStatusRequestDto,
    BulkDeleteUsersRequestDto,
    BulkExtendExpirationDateRequestDto,
    BulkResetTrafficUsersRequestDto,
    BulkRevokeUsersSubscriptionRequestDto,
    BulkUpdateUsersRequestDto,
    BulkUpdateUsersSquadsRequestDto,
)
from remnawave.rapid import BaseController, post


class UsersBulkActionsController(BaseController):
    @post("/users/bulk/all/extend-expiration-date", response_class=None)
    async def bulk_all_extend_expiration_date(
        self,
        body: Annotated[BulkAllExtendExpirationDateRequestDto, PydanticBody()],
    ) -> None:
        """Extend expiration date for ALL users"""

    @post("/users/bulk/all/reset-traffic", response_class=None)
    async def bulk_all_reset_user_traffic(self) -> None:
        """Reset traffic for ALL users"""

    @post("/users/bulk/all/update", response_class=None)
    async def bulk_all_update_users(
        self,
        body: Annotated[BulkAllUpdateUsersRequestDto, PydanticBody()],
    ) -> None:
        """Update ALL users"""

    @post("/users/bulk/delete", response_class=None)
    async def bulk_delete_users(
        self,
        body: Annotated[BulkDeleteUsersRequestDto, PydanticBody()],
    ) -> None:
        """Bulk delete users by IDs"""

    @post("/users/bulk/delete-by-status", response_class=None)
    async def bulk_delete_users_by_status(
        self,
        body: Annotated[BulkDeleteUsersByStatusRequestDto, PydanticBody()],
    ) -> None:
        """Bulk delete users by status"""

    @post("/users/bulk/extend-expiration-date", response_class=None)
    async def bulk_extend_expiration_date(
        self,
        body: Annotated[BulkExtendExpirationDateRequestDto, PydanticBody()],
    ) -> None:
        """Bulk extend expiration date"""

    @post("/users/bulk/reset-traffic", response_class=None)
    async def bulk_reset_user_traffic(
        self,
        body: Annotated[BulkResetTrafficUsersRequestDto, PydanticBody()],
    ) -> None:
        """Bulk reset user traffic"""

    @post("/users/bulk/revoke-subscription", response_class=None)
    async def bulk_revoke_users_subscription(
        self,
        body: Annotated[BulkRevokeUsersSubscriptionRequestDto, PydanticBody()],
    ) -> None:
        """Bulk revoke users subscription"""

    @post("/users/bulk/update", response_class=None)
    async def bulk_update_users(
        self,
        body: Annotated[BulkUpdateUsersRequestDto, PydanticBody()],
    ) -> None:
        """Bulk update users"""

    @post("/users/bulk/update-squads", response_class=None)
    async def bulk_update_users_squads(
        self,
        body: Annotated[BulkUpdateUsersSquadsRequestDto, PydanticBody()],
    ) -> None:
        """Bulk update users internal squads"""
