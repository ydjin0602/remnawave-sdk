# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.enums import SecurityLayer, TemplateType


class BulkDeleteHostsRequestDto(BaseModel):
    uuids: list[UUID]


class BulkDisableHostsRequestDto(BaseModel):
    uuids: list[UUID]


class BulkEnableHostsRequestDto(BaseModel):
    uuids: list[UUID]


class BulkHostsInboundDto(BaseModel):
    config_profile_uuid: UUID = Field(..., alias="configProfileUuid")
    config_profile_inbound_uuid: UUID = Field(..., alias="configProfileInboundUuid")


class UpdateManyHostsRequestDto(BaseModel):
    inbound: BulkHostsInboundDto | None = None
    remark: str | None = None
    address: str | None = None
    port: int | None = None
    path: str | None = None
    sni: str | None = None
    host: str | None = None
    alpn: str | None = None
    fingerprint: str | None = None
    is_disabled: bool | None = Field(None, serialization_alias="isDisabled")
    security_layer: SecurityLayer | None = Field(
        None, serialization_alias="securityLayer"
    )
    xhttp_extra_params: Any | None = Field(None, serialization_alias="xhttpExtraParams")
    mux_params: Any | None = Field(None, serialization_alias="muxParams")
    sockopt_params: Any | None = Field(None, serialization_alias="sockoptParams")
    final_mask: Any | None = Field(None, serialization_alias="finalMask")
    server_description: str | None = Field(
        None, serialization_alias="serverDescription"
    )
    tags: list[str] | None = None
    is_hidden: bool | None = Field(None, serialization_alias="isHidden")
    override_sni_from_address: bool | None = Field(
        None, serialization_alias="overrideSniFromAddress"
    )
    keep_sni_blank: bool | None = Field(None, serialization_alias="keepSniBlank")
    vless_route_id: int | None = Field(None, serialization_alias="vlessRouteId")
    pinned_peer_cert_sha256: str | None = Field(
        None, serialization_alias="pinnedPeerCertSha256"
    )
    verify_peer_cert_by_name: str | None = Field(
        None, serialization_alias="verifyPeerCertByName"
    )
    shuffle_host: bool | None = Field(None, serialization_alias="shuffleHost")
    mihomo_x25519: bool | None = Field(None, serialization_alias="mihomoX25519")
    mihomo_ip_version: str | None = Field(None, serialization_alias="mihomoIpVersion")
    nodes: list[UUID] | None = None
    xray_json_template_uuid: UUID | None = Field(
        None, serialization_alias="xrayJsonTemplateUuid"
    )
    excluded_internal_squads: list[UUID] | None = Field(
        None, serialization_alias="excludedInternalSquads"
    )
    exclude_from_subscription_types: list[TemplateType] | None = Field(
        None, serialization_alias="excludeFromSubscriptionTypes"
    )
    uuids: list[UUID]
