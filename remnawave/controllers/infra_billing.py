from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateInfraBillingHistoryRecordRequestDto,
    CreateInfraBillingHistoryRecordResponseDto,
    CreateInfraBillingNodeRequestDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderRequestDto,
    CreateInfraProviderResponseDto,
    GetAllInfraBillingHistoryResponseDto,
    GetAllInfraBillingNodesResponseDto,
    GetAllInfraProvidersResponseDto,
    GetInfraProviderByUuidResponseDto,
    UpdateInfraBillingNodeRequestDto,
    UpdateInfraBillingNodeResponseDto,
    UpdateInfraProviderRequestDto,
    UpdateInfraProviderResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class InfraBillingController(BaseController):
    # ---- Providers ----
    @get("/infra-billing/providers", response_class=GetAllInfraProvidersResponseDto)
    async def get_infra_providers(self) -> GetAllInfraProvidersResponseDto:
        """Get all infra providers"""

    @post("/infra-billing/providers", response_class=CreateInfraProviderResponseDto)
    async def create_infra_provider(
        self,
        body: Annotated[CreateInfraProviderRequestDto, PydanticBody()],
    ) -> CreateInfraProviderResponseDto:
        """Create a new infra provider"""

    @patch("/infra-billing/providers", response_class=UpdateInfraProviderResponseDto)
    async def update_infra_provider(
        self,
        body: Annotated[UpdateInfraProviderRequestDto, PydanticBody()],
    ) -> UpdateInfraProviderResponseDto:
        """Update infra provider"""

    @get(
        "/infra-billing/providers/{uuid}",
        response_class=GetInfraProviderByUuidResponseDto,
    )
    async def get_infra_provider(
        self,
        uuid: Annotated[str, Path(description="UUID of the provider")],
    ) -> GetInfraProviderByUuidResponseDto:
        """Get infra provider by UUID"""

    @delete("/infra-billing/providers/{uuid}", response_class=None)
    async def delete_infra_provider(
        self,
        uuid: Annotated[str, Path(description="UUID of the provider")],
    ) -> None:
        """Delete infra provider by UUID"""

    # ---- Billing nodes ----
    @get("/infra-billing/nodes", response_class=GetAllInfraBillingNodesResponseDto)
    async def get_billing_nodes(self) -> GetAllInfraBillingNodesResponseDto:
        """Get all billing nodes"""

    @post("/infra-billing/nodes", response_class=CreateInfraBillingNodeResponseDto)
    async def create_infra_billing_node(
        self,
        body: Annotated[CreateInfraBillingNodeRequestDto, PydanticBody()],
    ) -> CreateInfraBillingNodeResponseDto:
        """Create a new billing node"""

    @patch("/infra-billing/nodes", response_class=UpdateInfraBillingNodeResponseDto)
    async def update_infra_billing_node(
        self,
        body: Annotated[UpdateInfraBillingNodeRequestDto, PydanticBody()],
    ) -> UpdateInfraBillingNodeResponseDto:
        """Update billing node"""

    @delete("/infra-billing/nodes/{uuid}", response_class=None)
    async def delete_infra_billing_node(
        self,
        uuid: Annotated[str, Path(description="UUID of the billing node")],
    ) -> None:
        """Delete billing node by UUID"""

    # ---- History ----
    @get("/infra-billing/history", response_class=GetAllInfraBillingHistoryResponseDto)
    async def get_infra_billing_records(
        self,
        start: Annotated[
            int, Query(default=0, description="Offset for pagination")
        ] = 0,
        size: Annotated[int, Query(default=50, ge=1, description="Page size")] = 50,
    ) -> GetAllInfraBillingHistoryResponseDto:
        """Get billing history records"""

    @post(
        "/infra-billing/history",
        response_class=CreateInfraBillingHistoryRecordResponseDto,
    )
    async def create_infra_billing_record(
        self,
        body: Annotated[CreateInfraBillingHistoryRecordRequestDto, PydanticBody()],
    ) -> CreateInfraBillingHistoryRecordResponseDto:
        """Create a billing history record"""

    @delete("/infra-billing/history/{uuid}", response_class=None)
    async def delete_infra_billing_record(
        self,
        uuid: Annotated[str, Path(description="UUID of the record")],
    ) -> None:
        """Delete billing history record by UUID"""
