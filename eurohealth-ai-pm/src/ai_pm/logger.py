"""JSONL action logging for AI-PM scaffold operations."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


@dataclass
class ActionLogger:
    """Writes structured operation records to a JSONL file."""

    log_path: Path

    def __post_init__(self) -> None:
        """Ensure parent log directory exists."""
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, action: str, status: str, details: Dict[str, Any]) -> None:
        """Append one action record to the JSONL log."""
        record: Dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "status": status,
            "details": details,
        }
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
