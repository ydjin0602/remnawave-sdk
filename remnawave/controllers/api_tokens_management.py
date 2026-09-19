from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateApiTokenRequestDto,
    CreateApiTokenResponseDto,
    FindAllApiTokensResponseDto,
    GetApiTokenScopesResponseDto,
)
from remnawave.rapid import BaseController, delete, get, post


class APITokensManagementController(BaseController):
    @get("/tokens", response_class=FindAllApiTokensResponseDto)
    async def get_api_tokens(self) -> FindAllApiTokensResponseDto:
        """Get all API tokens"""

    @get("/tokens/scopes", response_class=GetApiTokenScopesResponseDto)
    async def get_scopes(self) -> GetApiTokenScopesResponseDto:
        """Get available API token scopes"""

    @post("/tokens", response_class=CreateApiTokenResponseDto)
    async def create_api_token(
        self,
        body: Annotated[CreateApiTokenRequestDto, PydanticBody()],
    ) -> CreateApiTokenResponseDto:
        """Create a new API token"""

    @delete("/tokens/{uuid}", response_class=None)
    async def delete_api_token(
        self,
        uuid: Annotated[str, Path(description="UUID of the token")],
    ) -> None:
        """Delete API token by UUID"""
