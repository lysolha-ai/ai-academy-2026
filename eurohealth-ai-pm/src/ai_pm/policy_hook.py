"""Governance policy hook checks for AI-PM seed execution."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List

try:
    import yaml
except Exception:  # pragma: no cover - graceful fallback if dependency is absent
    yaml = None  # type: ignore[assignment]


@dataclass(frozen=True)
class PolicyHookResult:
    """Result payload for governance policy hook validation."""

    ok: bool
    policy_file: str
    policy_name: str | None
    required_rule_id: str
    rule_present: bool
    error: str | None

    def to_dict(self) -> Dict[str, Any]:
        """Serialize result as a dictionary for logging and CLI output."""
        return asdict(self)


def _extract_rule_ids(payload: Dict[str, Any]) -> List[str]:
    """Extract rule IDs from policy YAML payload."""
    rules: List[Dict[str, Any]] = payload.get("rules", []) if isinstance(payload, dict) else []
    return [str(rule.get("id", "")) for rule in rules if isinstance(rule, dict)]


def check_policy_hook(policy_bundle_path: Path, required_rule_id: str = "block-salary-data") -> PolicyHookResult:
    """Verify governance policy bundle contains a required enforceable rule."""
    policy_file: Path = policy_bundle_path / "pii-protection.yaml"

    try:
        if not policy_file.exists():
            return PolicyHookResult(
                ok=False,
                policy_file=str(policy_file),
                policy_name=None,
                required_rule_id=required_rule_id,
                rule_present=False,
                error="Policy file not found",
            )

        with policy_file.open("r", encoding="utf-8") as handle:
            raw_text: str = handle.read()

        if yaml is None:
            # Fallback for environments without PyYAML: cheap textual check.
            rule_present = f"id: {required_rule_id}" in raw_text
            return PolicyHookResult(
                ok=rule_present,
                policy_file=str(policy_file),
                policy_name="pii-protection",
                required_rule_id=required_rule_id,
                rule_present=rule_present,
                error=None if rule_present else f"Required rule '{required_rule_id}' not found",
            )

        payload: Dict[str, Any] = yaml.safe_load(raw_text) or {}
        policy_name: str | None = None
        if isinstance(payload.get("policy"), dict):
            policy_name = str(payload["policy"].get("name")) if payload["policy"].get("name") else None

        rule_ids: List[str] = _extract_rule_ids(payload)
        rule_present: bool = required_rule_id in rule_ids

        return PolicyHookResult(
            ok=rule_present,
            policy_file=str(policy_file),
            policy_name=policy_name,
            required_rule_id=required_rule_id,
            rule_present=rule_present,
            error=None if rule_present else f"Required rule '{required_rule_id}' not found",
        )
    except Exception as exc:
        return PolicyHookResult(
            ok=False,
            policy_file=str(policy_file),
            policy_name=None,
            required_rule_id=required_rule_id,
            rule_present=False,
            error=str(exc),
        )
