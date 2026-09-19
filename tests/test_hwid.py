import random
import uuid

import pytest

from remnawave.models import (
    CreateUserHwidDeviceRequestDto,
    CreateUserHwidDeviceResponseDto,
    DeleteUserAllHwidDeviceRequestDto,
    DeleteUserHwidDeviceRequestDto,
    DeleteUserHwidDeviceResponseDto,
    GetHwidStatisticsResponseDto,
    GetUserHwidDevicesResponseDto,
)


class TestHwidInfo:
    """Тесты для получения информации о HWID устройствах"""

    @pytest.mark.asyncio
    async def test_get_user_hwid_devices(self, remnawave, panel):
        """Тест получения HWID устройств конкретного пользователя (v3: by user id)"""
        devices = await remnawave.hwid.get_user_hwid_devices(user_id=panel["user_id"])
        assert isinstance(devices, GetUserHwidDevicesResponseDto)
        assert hasattr(devices, "devices")

    @pytest.mark.asyncio
    async def test_get_all_users(self, remnawave):
        """Тест получения всех HWID устройств с пагинацией"""
        response = await remnawave.hwid.get_all_users(start=0, size=10)
        assert hasattr(response, "devices")
        assert hasattr(response, "total")

    @pytest.mark.asyncio
    async def test_get_hwid_devices_stats(self, remnawave):
        """Тест получения статистики по HWID устройствам"""
        stats = await remnawave.hwid.get_hwid_devices_stats()
        assert isinstance(stats, GetHwidStatisticsResponseDto)

    @pytest.mark.asyncio
    async def test_get_top_users_by_hwid_devices(self, remnawave):
        """Тест топа пользователей по количеству HWID устройств"""
        response = await remnawave.hwid.get_top_users_by_hwid_devices(start=0, size=5)
        assert hasattr(response, "users")
        assert hasattr(response, "total")


class TestHwidDevices:
    """Тесты CRUD HWID устройств"""

    @pytest.mark.asyncio
    async def test_create_and_delete_hwid_device(self, remnawave, panel):
        """Тест создания и удаления HWID устройства пользователя"""
        user_id = panel["user_id"]
        test_hwid = str(uuid.uuid4())
        device_model = f"Test Model {random.randint(0, 1000)}"

        # v3: body uses userId
        created = await remnawave.hwid.create_user_hwid_device(
            CreateUserHwidDeviceRequestDto(
                user_id=user_id,
                hwid=test_hwid,
                platform="TestPlatform",
                device_model=device_model,
            )
        )
        assert isinstance(created, CreateUserHwidDeviceResponseDto)
        assert any(d.hwid == test_hwid for d in created.devices)

        # Delete specific device
        deleted = await remnawave.hwid.delete_user_hwid_device(
            DeleteUserHwidDeviceRequestDto(user_id=user_id, hwid=test_hwid)
        )
        assert isinstance(deleted, DeleteUserHwidDeviceResponseDto)
        assert not any(d.hwid == test_hwid for d in deleted.devices)

    @pytest.mark.asyncio
    async def test_delete_all_user_hwid_devices(self, remnawave, panel):
        """Тест удаления всех HWID устройств пользователя"""
        user_id = panel["user_id"]
        test_hwid = str(uuid.uuid4())

        await remnawave.hwid.create_user_hwid_device(
            CreateUserHwidDeviceRequestDto(
                user_id=user_id,
                hwid=test_hwid,
                platform="TestPlatform",
                device_model="Bulk Test",
            )
        )

        await remnawave.hwid.delete_all_user_hwid_devices(
            DeleteUserAllHwidDeviceRequestDto(user_id=user_id)
        )
        # Verify devices are gone for the user
        after = await remnawave.hwid.get_user_hwid_devices(user_id=user_id)
        assert isinstance(after, GetUserHwidDevicesResponseDto)
        assert after.total == 0
