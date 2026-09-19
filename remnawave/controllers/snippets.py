from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateSnippetRequestDto,
    CreateSnippetResponseDto,
    DeleteSnippetRequestDto,
    GetSnippetsResponseDto,
    SyncSnippetRequestDto,
    UpdateSnippetRequestDto,
    UpdateSnippetResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class SnippetsController(BaseController):
    @get("/snippets", response_class=GetSnippetsResponseDto)
    async def get_snippets(self) -> GetSnippetsResponseDto:
        """Get all snippets"""

    @post("/snippets", response_class=CreateSnippetResponseDto)
    async def create_snippet(
        self,
        body: Annotated[CreateSnippetRequestDto, PydanticBody()],
    ) -> CreateSnippetResponseDto:
        """Create a new snippet"""

    @patch("/snippets", response_class=UpdateSnippetResponseDto)
    async def update_snippet(
        self,
        body: Annotated[UpdateSnippetRequestDto, PydanticBody()],
    ) -> UpdateSnippetResponseDto:
        """Update snippet"""

    @delete("/snippets", response_class=None)
    async def delete_snippet_by_name(
        self,
        body: Annotated[DeleteSnippetRequestDto, PydanticBody()],
    ) -> None:
        """Delete snippet by name"""

    @post("/snippets/actions/sync", response_class=None)
    async def sync_snippet(
        self,
        body: Annotated[SyncSnippetRequestDto, PydanticBody()],
    ) -> None:
        """Sync snippet (async)"""
