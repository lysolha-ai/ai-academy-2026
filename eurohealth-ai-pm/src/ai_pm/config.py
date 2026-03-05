"""Configuration helpers for AI-PM delivery backbone scaffolding."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - fallback for environments without python-dotenv
    def load_dotenv(*_args: object, **_kwargs: object) -> bool:
        """Fallback no-op loader when python-dotenv is unavailable."""
        return False


@dataclass(frozen=True)
class AIPMConfig:
    """Runtime configuration for AI-PM scaffold generation."""

    project_dir: Path
    log_path: Path
    policy_bundle_path: Path


def load_config() -> AIPMConfig:
    """Load configuration from .env files and environment variables."""
    load_dotenv("config/.env")
    load_dotenv(".env")

    project_dir_raw: str = os.getenv("AI_PM_PROJECT_DIR", "project")
    log_path_raw: str = os.getenv("AI_PM_LOG_PATH", "logs/ai_pm_actions.jsonl")
    policy_bundle_path_raw: str = os.getenv("POLICY_BUNDLE_PATH", "governance/policies")

    return AIPMConfig(
        project_dir=Path(project_dir_raw),
        log_path=Path(log_path_raw),
        policy_bundle_path=Path(policy_bundle_path_raw),
    )
