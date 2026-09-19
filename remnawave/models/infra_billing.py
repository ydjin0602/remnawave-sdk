# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BillingHistoryDto(BaseModel):
    total_amount: float = Field(..., alias="totalAmount")
    total_bills: float = Field(..., alias="totalBills")


class DetailsDto(BaseModel):
    node_uuid: UUID = Field(..., alias="nodeUuid")
    country_code: str = Field(..., alias="countryCode")


class BillingNodesDto(BaseModel):
    name: str
    details: DetailsDto | None = None


class ProvidersDto(BaseModel):
    uuid: UUID
    name: str
    favicon_link: str | None = Field(None, alias="faviconLink")
    login_url: str | None = Field(None, alias="loginUrl")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    billing_history: BillingHistoryDto = Field(..., alias="billingHistory")
    billing_nodes: list[BillingNodesDto] = Field(..., alias="billingNodes")


class GetAllInfraProvidersResponseDto(BaseModel):
    total: float
    providers: list[ProvidersDto]


class GetInfraProviderByUuidResponseDto(ProvidersDto):
    """Alias of ProvidersDto (envelope unwrapped)."""


class CreateInfraProviderRequestDto(BaseModel):
    name: str
    favicon_link: str | None = Field(None, serialization_alias="faviconLink")
    login_url: str | None = Field(None, serialization_alias="loginUrl")


class CreateInfraProviderResponseDto(ProvidersDto):
    """Alias of ProvidersDto (envelope unwrapped)."""


class UpdateInfraProviderRequestDto(BaseModel):
    uuid: UUID
    name: str | None = None
    favicon_link: str | None = Field(None, serialization_alias="faviconLink")
    login_url: str | None = Field(None, serialization_alias="loginUrl")


class UpdateInfraProviderResponseDto(ProvidersDto):
    """Alias of ProvidersDto (envelope unwrapped)."""


class CreateInfraBillingHistoryRecordRequestDto(BaseModel):
    provider_uuid: UUID = Field(..., serialization_alias="providerUuid")
    amount: float
    billed_at: datetime = Field(..., serialization_alias="billedAt")


class ProviderDto(BaseModel):
    uuid: UUID
    name: str
    favicon_link: str | None = Field(None, alias="faviconLink")


class RecordsDto(BaseModel):
    uuid: UUID
    provider_uuid: UUID = Field(..., alias="providerUuid")
    amount: float
    billed_at: datetime = Field(..., alias="billedAt")
    provider: ProviderDto


class CreateInfraBillingHistoryRecordResponseDto(BaseModel):
    records: list[RecordsDto]
    total: float


class GetAllInfraBillingHistoryResponseDto(CreateInfraBillingHistoryRecordResponseDto):
    """Alias of CreateInfraBillingHistoryRecordResponseDto (envelope unwrapped)."""


class GetAllInfraBillingNodesResponseProviderDto(BaseModel):
    uuid: UUID
    name: str
    login_url: str | None = Field(None, alias="loginUrl")
    favicon_link: str | None = Field(None, alias="faviconLink")


class NodeDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(..., alias="countryCode")


class GetAllInfraBillingNodesResponseBillingNodesDto(BaseModel):
    uuid: UUID
    node_uuid: UUID | None = Field(None, alias="nodeUuid")
    name: str | None = None
    provider_uuid: UUID = Field(..., alias="providerUuid")
    provider: GetAllInfraBillingNodesResponseProviderDto
    node: NodeDto | None = None
    next_billing_at: datetime = Field(..., alias="nextBillingAt")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class AvailableBillingNodesDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(..., alias="countryCode")


class InfraBillingStatsDto(BaseModel):
    upcoming_nodes_count: int = Field(..., alias="upcomingNodesCount")
    current_month_payments: float = Field(..., alias="currentMonthPayments")
    total_spent: float = Field(..., alias="totalSpent")


class GetAllInfraBillingNodesResponseDto(BaseModel):
    total_billing_nodes: float = Field(..., alias="totalBillingNodes")
    billing_nodes: list[GetAllInfraBillingNodesResponseBillingNodesDto] = Field(
        ..., alias="billingNodes"
    )
    available_billing_nodes: list[AvailableBillingNodesDto] = Field(
        ..., alias="availableBillingNodes"
    )
    total_available_billing_nodes: float = Field(
        ..., alias="totalAvailableBillingNodes"
    )
    stats: InfraBillingStatsDto


class UpdateInfraBillingNodeRequestDto(BaseModel):
    uuids: list[UUID]
    next_billing_at: datetime = Field(..., serialization_alias="nextBillingAt")


class UpdateInfraBillingNodeResponseDto(GetAllInfraBillingNodesResponseDto):
    """Alias of GetAllInfraBillingNodesResponseDto (envelope unwrapped)."""


class CreateInfraBillingNodeRequestDto(BaseModel):
    provider_uuid: UUID = Field(..., serialization_alias="providerUuid")
    node_uuid: UUID | None = Field(None, serialization_alias="nodeUuid")
    name: str | None = None
    next_billing_at: datetime = Field(..., serialization_alias="nextBillingAt")


class CreateInfraBillingNodeResponseDto(GetAllInfraBillingNodesResponseDto):
    """Alias of GetAllInfraBillingNodesResponseDto (envelope unwrapped)."""
