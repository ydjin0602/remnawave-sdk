# GENERATED FROM Remnawave API v3.2.3 swagger - review ok


from pydantic import BaseModel, Field


class PasskeySettingsDto(BaseModel):
    enabled: bool
    rp_id: str | None = Field(None, alias="rpId")
    origin: str | None = None


class GithubDto(BaseModel):
    enabled: bool
    client_id: str | None = Field(None, alias="clientId")
    client_secret: str | None = Field(None, alias="clientSecret")
    allowed_emails: list[str] = Field(..., alias="allowedEmails")


class PocketidDto(BaseModel):
    enabled: bool
    client_id: str | None = Field(None, alias="clientId")
    client_secret: str | None = Field(None, alias="clientSecret")
    frontend_domain: str | None = Field(None, alias="frontendDomain")
    plain_domain: str | None = Field(None, alias="plainDomain")
    allowed_emails: list[str] = Field(..., alias="allowedEmails")


class KeycloakDto(BaseModel):
    enabled: bool
    realm: str | None = None
    client_id: str | None = Field(None, alias="clientId")
    client_secret: str | None = Field(None, alias="clientSecret")
    frontend_domain: str | None = Field(None, alias="frontendDomain")
    keycloak_domain: str | None = Field(None, alias="keycloakDomain")
    allowed_emails: list[str] = Field(..., alias="allowedEmails")


class GenericDto(BaseModel):
    enabled: bool
    client_id: str | None = Field(None, alias="clientId")
    client_secret: str | None = Field(None, alias="clientSecret")
    with_pkce: bool = Field(..., alias="withPkce")
    authorization_url: str | None = Field(None, alias="authorizationUrl")
    token_url: str | None = Field(None, alias="tokenUrl")
    frontend_domain: str | None = Field(None, alias="frontendDomain")
    allowed_emails: list[str] = Field(..., alias="allowedEmails")


class TelegramDto(BaseModel):
    enabled: bool
    client_id: str | None = Field(None, alias="clientId")
    client_secret: str | None = Field(None, alias="clientSecret")
    allowed_ids: list[str] = Field(..., alias="allowedIds")
    frontend_domain: str | None = Field(None, alias="frontendDomain")


class Oauth2SettingsDto(BaseModel):
    github: GithubDto
    pocketid: PocketidDto
    yandex: GithubDto
    keycloak: KeycloakDto | None = None
    generic: GenericDto | None = None
    telegram: TelegramDto | None = None


class PasswordSettingsDto(BaseModel):
    enabled: bool


class BrandingSettingsDto(BaseModel):
    title: str | None = None
    logo_url: str | None = Field(None, alias="logoUrl")


class GetRemnawaveSettingsResponseDto(BaseModel):
    passkey_settings: PasskeySettingsDto | None = Field(None, alias="passkeySettings")
    oauth2_settings: Oauth2SettingsDto | None = Field(None, alias="oauth2Settings")
    password_settings: PasswordSettingsDto | None = Field(
        None, alias="passwordSettings"
    )
    branding_settings: BrandingSettingsDto | None = Field(
        None, alias="brandingSettings"
    )


class UpdateRemnawaveSettingsRequestPasskeySettingsDto(BaseModel):
    enabled: bool
    rp_id: str | None = Field(None, alias="rpId")
    origin: str | None = None


class UpdateRemnawaveSettingsRequestOauth2SettingsDto(BaseModel):
    github: GithubDto
    pocketid: PocketidDto
    yandex: GithubDto
    keycloak: KeycloakDto | None = None
    generic: GenericDto | None = None
    telegram: TelegramDto | None = None


class UpdateRemnawaveSettingsRequestPasswordSettingsDto(BaseModel):
    enabled: bool


class UpdateRemnawaveSettingsRequestBrandingSettingsDto(BaseModel):
    title: str | None = None
    logo_url: str | None = Field(None, alias="logoUrl")


class UpdateRemnawaveSettingsRequestDto(BaseModel):
    passkey_settings: UpdateRemnawaveSettingsRequestPasskeySettingsDto | None = Field(
        None, serialization_alias="passkeySettings"
    )
    oauth2_settings: UpdateRemnawaveSettingsRequestOauth2SettingsDto | None = Field(
        None, serialization_alias="oauth2Settings"
    )
    password_settings: UpdateRemnawaveSettingsRequestPasswordSettingsDto | None = Field(
        None, serialization_alias="passwordSettings"
    )
    branding_settings: UpdateRemnawaveSettingsRequestBrandingSettingsDto | None = Field(
        None, serialization_alias="brandingSettings"
    )


class UpdateRemnawaveSettingsResponseDto(GetRemnawaveSettingsResponseDto):
    """Alias of GetRemnawaveSettingsResponseDto (envelope unwrapped)."""
