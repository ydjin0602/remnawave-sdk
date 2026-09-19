# GENERATED FROM Remnawave API v3.2.3 swagger - review ok

from pydantic import BaseModel, Field


class GetNodeSecretKeyResponseDto(BaseModel):
    secret_key: str = Field(..., alias="secretKey")
