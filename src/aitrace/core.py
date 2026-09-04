"""Trace event aggregation."""


def summarize(events: list[dict]) -> dict[str, int]:
    """Count trace events by type."""
    result: dict[str, int] = {}
    for event in events:
        kind = str(event.get("type", "unknown"))
        result[kind] = result.get(kind, 0) + 1
    return dict(sorted(result.items()))
