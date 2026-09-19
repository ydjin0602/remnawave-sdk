"""Tests that all required endpoints exist in controllers."""

from remnawave.controllers.bandwidthstats import BandWidthStatsController
from remnawave.controllers.connections import ConnectionsController
from remnawave.controllers.internal_squads import InternalSquadsController
from remnawave.controllers.system import SystemController
from remnawave.controllers.users import UsersController
from remnawave.controllers.users_bulk_actions import UsersBulkActionsController


class TestUsersControllerEndpoints:
    def test_has_resolve_user(self):
        assert callable(UsersController.resolve_user)

    def test_has_revoke_user_subscription(self):
        assert callable(UsersController.revoke_user_subscription)

    def test_has_disable_user(self):
        assert callable(UsersController.disable_user)

    def test_has_enable_user(self):
        assert callable(UsersController.enable_user)

    def test_has_reset_user_traffic(self):
        assert callable(UsersController.reset_user_traffic)

    def test_has_extend_user_expiration_date(self):
        assert callable(UsersController.extend_user_expiration_date)

    def test_has_create_user(self):
        assert callable(UsersController.create_user)

    def test_has_update_user(self):
        assert callable(UsersController.update_user)

    def test_has_delete_user(self):
        assert callable(UsersController.delete_user)

    def test_has_get_all_users(self):
        assert callable(UsersController.get_all_users)

    def test_has_get_users_stream(self):
        assert callable(UsersController.get_users_stream)

    def test_has_get_user_by_short_uuid(self):
        assert callable(UsersController.get_user_by_short_uuid)

    def test_has_get_user_by_username(self):
        assert callable(UsersController.get_user_by_username)

    def test_has_get_user_by_id(self):
        assert callable(UsersController.get_user_by_id)

    def test_has_get_users_tags(self):
        assert callable(UsersController.get_users_tags)

    def test_has_get_user_accessible_nodes(self):
        assert callable(UsersController.get_user_accessible_nodes)

    def test_has_get_user_subscription_request_history(self):
        assert callable(UsersController.get_user_subscription_request_history)

    def test_removed_lookups_are_gone(self):
        """v3 removed by-telegram-id / by-email / by-tag lookups (use resolve_user)."""
        assert not hasattr(UsersController, "get_users_by_telegram_id")
        assert not hasattr(UsersController, "get_users_by_email")
        assert not hasattr(UsersController, "get_users_by_tag")


class TestConnectionsControllerEndpoints:
    def test_has_all_methods(self):
        for m in (
            "connections_by_user",
            "connections_by_user_result",
            "connections_by_node",
            "connections_by_node_result",
            "drop_connections",
        ):
            assert callable(getattr(ConnectionsController, m)), m


class TestUsersBulkActionsEndpoints:
    def test_has_all_bulk_methods(self):
        for m in (
            "bulk_all_extend_expiration_date",
            "bulk_all_reset_user_traffic",
            "bulk_all_update_users",
            "bulk_delete_users",
            "bulk_delete_users_by_status",
            "bulk_extend_expiration_date",
            "bulk_reset_user_traffic",
            "bulk_revoke_users_subscription",
            "bulk_update_users",
            "bulk_update_users_squads",
        ):
            assert callable(getattr(UsersBulkActionsController, m)), m


class TestSystemControllerEndpoints:
    def test_has_new_v3_methods(self):
        for m in (
            "get_configuration",
            "get_stats_digest",
            "get_http_stats",
            "debug_srr_matcher",
        ):
            assert callable(getattr(SystemController, m)), m


class TestInternalSquadsEndpoints:
    def test_has_many_users_methods(self):
        for m in (
            "add_many_users_to_internal_squad",
            "remove_many_users_from_internal_squad",
            "get_internal_squad_usage",
        ):
            assert callable(getattr(InternalSquadsController, m)), m


class TestBandwidthStatsEndpoints:
    def test_has_v3_methods(self):
        for m in (
            "get_nodes_usage",
            "get_node_usage",
            "get_stats_user_usage",
            "get_internal_squad_usage",
            "get_internal_squad_user_usage",
        ):
            assert callable(getattr(BandWidthStatsController, m)), m

    def test_legacy_methods_removed(self):
        assert not hasattr(BandWidthStatsController, "get_user_usage_legacy_old")
        assert not hasattr(BandWidthStatsController, "get_nodes_realtime_usage")


class TestRemovedControllers:
    def test_dead_controllers_are_gone(self):
        import remnawave.controllers as C

        assert not hasattr(C, "InboundsController")
        assert not hasattr(C, "InboundsBulkActionsController")
        assert not hasattr(C, "IpControlController")
        assert not hasattr(C, "XrayConfigController")

    def test_sdk_attrs(self):
        import inspect

        from remnawave import RemnawaveSDK

        src = inspect.getsource(RemnawaveSDK.__init__)
        assert "self.connections" in src
        assert "self.ip_control" not in src
        assert "self.inbounds" not in src
