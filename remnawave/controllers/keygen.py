from remnawave.models import GetNodeSecretKeyResponseDto
from remnawave.rapid import BaseController, get


class KeygenController(BaseController):
    @get("/keygen", response_class=GetNodeSecretKeyResponseDto)
    async def generate_key(self) -> GetNodeSecretKeyResponseDto:
        """Generate a node secret key"""
