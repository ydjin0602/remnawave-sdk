# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from typing import Any

from pydantic import BaseModel, Field

from remnawave.enums import OAuth2Provider


class VerifyPasskeyRegistrationRequestDto(BaseModel):
    pass


class LoginRequestDto(BaseModel):
    username: str
    password: str


class LoginResponseDto(BaseModel):
    access_token: str = Field(..., alias="accessToken")


class RegisterRequestDto(BaseModel):
    username: str
    password: str


class RegisterResponseDto(LoginResponseDto):
    """Alias of LoginResponseDto (envelope unwrapped)."""


class PasskeyDto(BaseModel):
    enabled: bool


class Oauth2Dto(BaseModel):
    providers: dict[str, Any]


class AuthenticationDto(BaseModel):
    passkey: PasskeyDto
    oauth2: Oauth2Dto
    password: PasskeyDto


class BrandingDto(BaseModel):
    title: str | None = None
    logo_url: str | None = Field(None, alias="logoUrl")


class GetStatusResponseDto(BaseModel):
    is_login_allowed: bool = Field(..., alias="isLoginAllowed")
    is_register_allowed: bool = Field(..., alias="isRegisterAllowed")
    authentication: AuthenticationDto | None = None
    branding: BrandingDto


class OAuth2AuthorizeRequestDto(BaseModel):
    provider: OAuth2Provider


class OAuth2AuthorizeResponseDto(BaseModel):
    authorization_url: str | None = Field(None, alias="authorizationUrl")


class OAuth2CallbackRequestDto(BaseModel):
    provider: OAuth2Provider
    code: str
    state: str


class OAuth2CallbackResponseDto(LoginResponseDto):
    """Alias of LoginResponseDto (envelope unwrapped)."""


class GetPasskeyAuthenticationOptionsResponseDto(VerifyPasskeyRegistrationRequestDto):
    """Alias of VerifyPasskeyRegistrationRequestDto (envelope unwrapped)."""


class VerifyPasskeyAuthenticationRequestDto(VerifyPasskeyRegistrationRequestDto):
    """Alias of VerifyPasskeyRegistrationRequestDto (envelope unwrapped)."""


class VerifyPasskeyAuthenticationResponseDto(LoginResponseDto):
    """Alias of LoginResponseDto (envelope unwrapped)."""
