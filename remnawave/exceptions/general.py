from datetime import datetime
from typing import Any

from pydantic import AliasChoices, BaseModel, Field

from remnawave.enums import ErrorCode


class ApiErrorResponse(BaseModel):
    """Standard API error response model"""

    timestamp: datetime | None = Field(None, description="Время возникновения ошибки")
    path: str | None = Field(None, description="Путь запроса")
    message: str = Field(..., description="Сообщение об ошибке")
    code: ErrorCode | str | None = Field(
        None,
        validation_alias=AliasChoices("errorCode", "code", "error_code"),
        description="Код ошибки",
    )
    # Support for API v2 error format
    status_code: int | None = Field(None, alias="statusCode")
    errors: list[Any] | None = Field(None, description="Детали ошибок валидации")


class ApiError(Exception):
    """Base API error exception"""

    def __init__(self, status_code: int, error: ApiErrorResponse):
        self.status_code = status_code
        self.error = error
        super().__init__(
            f"API Error {error.code}: {error.message} (HTTP {status_code})"
        )

    @property
    def code(self) -> str | None:
        """Get error code"""
        return self.error.code

    @property
    def message(self) -> str:
        """Get error message"""
        return self.error.message

    @property
    def timestamp(self) -> datetime | None:
        """Get error timestamp"""
        return self.error.timestamp

    @property
    def path(self) -> str | None:
        """Get request path"""
        return self.error.path


class BadRequestError(ApiError):
    """Ошибки клиента (400)"""


class UnauthorizedError(ApiError):
    """Ошибка авторизации (401)"""


class ForbiddenError(ApiError):
    """Доступ запрещен (403)"""


class NotFoundError(ApiError):
    """Ресурс не найден (404)"""


class ConflictError(ApiError):
    """Конфликт (409)"""


class ValidationError(ApiError):
    """Ошибка валидации данных (422)"""


class ServerError(ApiError):
    """Серверная ошибка (500+)"""


# Новые специализированные исключения
class NetworkError(ApiError):
    """Сетевые ошибки"""


class AuthenticationError(ApiError):
    """Ошибки аутентификации"""


class BusinessLogicError(ApiError):
    """Ошибки бизнес-логики"""


class RateLimitError(BadRequestError):
    """Превышен лимит запросов"""


class MaintenanceError(ServerError):
    """Режим обслуживания"""


class QuotaExceededError(BusinessLogicError):
    """Превышена квота"""


class FeatureNotAvailableError(BusinessLogicError):
    """Функция недоступна"""
