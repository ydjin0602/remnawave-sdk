from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetPasskeyAuthenticationOptionsResponseDto,
    GetStatusResponseDto,
    LoginRequestDto,
    LoginResponseDto,
    OAuth2AuthorizeRequestDto,
    OAuth2AuthorizeResponseDto,
    OAuth2CallbackRequestDto,
    OAuth2CallbackResponseDto,
    RegisterRequestDto,
    RegisterResponseDto,
    VerifyPasskeyAuthenticationRequestDto,
    VerifyPasskeyAuthenticationResponseDto,
)
from remnawave.rapid import BaseController, get, post


class AuthController(BaseController):
    @get("/auth/status", response_class=GetStatusResponseDto)
    async def get_status(self) -> GetStatusResponseDto:
        """Get auth status (login/register allowed, branding, providers)"""

    @post("/auth/login", response_class=LoginResponseDto)
    async def login(
        self,
        body: Annotated[LoginRequestDto, PydanticBody()],
    ) -> LoginResponseDto:
        """Login with username and password"""

    @post("/auth/register", response_class=RegisterResponseDto)
    async def register(
        self,
        body: Annotated[RegisterRequestDto, PydanticBody()],
    ) -> RegisterResponseDto:
        """Register the first admin"""

    @post("/auth/oauth2/authorize", response_class=OAuth2AuthorizeResponseDto)
    async def oauth2_authorize(
        self,
        body: Annotated[OAuth2AuthorizeRequestDto, PydanticBody()],
    ) -> OAuth2AuthorizeResponseDto:
        """Get OAuth2 authorization URL"""

    @post("/auth/oauth2/callback", response_class=OAuth2CallbackResponseDto)
    async def oauth2_callback(
        self,
        body: Annotated[OAuth2CallbackRequestDto, PydanticBody()],
    ) -> OAuth2CallbackResponseDto:
        """Exchange OAuth2 callback payload for a JWT"""

    @get(
        "/auth/passkey/authentication/options",
        response_class=GetPasskeyAuthenticationOptionsResponseDto,
    )
    async def passkey_authentication_options(
        self,
    ) -> GetPasskeyAuthenticationOptionsResponseDto:
        """Get passkey authentication options"""

    @post(
        "/auth/passkey/authentication/verify",
        response_class=VerifyPasskeyAuthenticationResponseDto,
    )
    async def passkey_authentication_verify(
        self,
        body: Annotated[VerifyPasskeyAuthenticationRequestDto, PydanticBody()],
    ) -> VerifyPasskeyAuthenticationResponseDto:
        """Verify passkey authentication"""
