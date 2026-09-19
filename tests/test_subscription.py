import pytest

from remnawave.enums import ClientType
from remnawave.models import (
    GetAllSubscriptionsResponseDto,
    GetRawSubscriptionByShortUuidResponseDto,
    GetSubpageConfigByShortUuidRequestBodyDto,
    GetSubpageConfigByShortUuidResponseDto,
    GetSubscriptionByUsernameResponseDto,
    GetSubscriptionInfoResponseDto,
)


class TestSubscriptionInfo:
    """Тесты для получения информации о подписках"""

    @pytest.mark.asyncio
    async def test_get_subscription_info_by_short_uuid(self, remnawave, panel):
        """Тест получения информации о подписке по короткому UUID"""
        subscription_info = (
            await remnawave.subscription.get_subscription_info_by_short_uuid(
                short_uuid=panel["short_uuid"]
            )
        )
        assert isinstance(subscription_info, GetSubscriptionInfoResponseDto)
        assert subscription_info.is_found is True
        assert hasattr(subscription_info, "user")

    @pytest.mark.asyncio
    async def test_get_raw_subscription_by_short_uuid(self, remnawave, panel):
        """Тест получения сырой подписки по короткому UUID"""
        raw_subscription = await remnawave.subscriptions.get_raw_subscription(
            short_uuid=panel["short_uuid"]
        )
        assert isinstance(raw_subscription, GetRawSubscriptionByShortUuidResponseDto)


class TestSubscriptionContent:
    """Тесты для получения контента подписок"""

    @pytest.mark.asyncio
    async def test_get_subscription(self, remnawave, panel):
        """Тест получения подписки по короткому UUID"""
        subscription = await remnawave.subscription.get_subscription(
            short_uuid=panel["short_uuid"]
        )
        assert isinstance(subscription, str)

    @pytest.mark.asyncio
    async def test_get_subscription_by_client_type(self, remnawave, panel):
        """Тест получения подписки для конкретного клиента"""
        for client_type in ClientType:
            sub = await remnawave.subscription.get_subscription_by_client_type(
                short_uuid=panel["short_uuid"],
                client_type=client_type,
            )
            assert isinstance(sub, str)


class TestSubscriptionsManagement:
    """Тесты для управления подписками"""

    @pytest.mark.asyncio
    async def test_get_all_subscriptions(self, remnawave, panel):
        """Тест получения всех подписок"""
        all_subscriptions = await remnawave.subscriptions.get_all_subscriptions()
        assert isinstance(all_subscriptions, GetAllSubscriptionsResponseDto)
        assert hasattr(all_subscriptions, "subscriptions")
        assert hasattr(all_subscriptions, "total")

    @pytest.mark.asyncio
    async def test_get_subscription_by_username(self, remnawave, panel):
        """Тест получения подписки по имени пользователя"""
        subscription_by_username = (
            await remnawave.subscriptions.get_subscription_by_username(
                username=panel["user_username"]
            )
        )
        assert isinstance(
            subscription_by_username, GetSubscriptionByUsernameResponseDto
        )

    @pytest.mark.asyncio
    async def test_get_subpage_config(self, remnawave, panel):
        """Тест получения конфига страницы подписки по short UUID"""
        body = GetSubpageConfigByShortUuidRequestBodyDto(request_headers={})
        subpage_config = await remnawave.subscriptions.get_subpage_config(
            short_uuid=panel["short_uuid"],
            body=body,
        )
        assert isinstance(subpage_config, GetSubpageConfigByShortUuidResponseDto)
        assert hasattr(subpage_config, "webpage_allowed")
