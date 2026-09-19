from enum import StrEnum


class NodeUsageType(StrEnum):
    """Usage type of a node IP (swagger: Node.ips[].type)."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    MANAGEMENT = "MANAGEMENT"
    TRANSIT = "TRANSIT"
    MONITORING = "MONITORING"
    RESERVE = "RESERVE"
    BLOCKED = "BLOCKED"
    FLAGGED = "FLAGGED"
    DEPRECATED = "DEPRECATED"
    UNKNOWN = "UNKNOWN"
