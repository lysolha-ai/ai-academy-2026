"""Scaffold generator for AI-PM delivery backbone artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict
import tempfile

from ai_pm.templates import (
    scope_tracker_template,
    sprint_board_template,
    stakeholder_update_template,
    standup_template,
)


@dataclass(frozen=True)
class Artifact:
    """Represents one scaffold artifact file and content."""

    path: Path
    content: str


def build_artifacts(project_dir: Path) -> Dict[str, Artifact]:
    """Build the set of markdown artifacts for AI-PM delivery backbone."""
    return {
        "sprint_board": Artifact(project_dir / "sprint_board.md", sprint_board_template()),
        "standup_template": Artifact(project_dir / "standup_template.md", standup_template()),
        "stakeholder_update": Artifact(project_dir / "stakeholder_update.md", stakeholder_update_template()),
        "scope_tracker": Artifact(project_dir / "scope_tracker.md", scope_tracker_template()),
    }


def write_artifact(artifact: Artifact, overwrite: bool) -> str:
    """Write one artifact safely and return write mode status."""
    # Guardrail: artifact targets must stay within the project tree.
    if artifact.path.is_absolute():
        target = artifact.path
    else:
        target = artifact.path.resolve()
    parent = target.parent
    parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not overwrite:
        return "skipped_exists"

    existing = target.read_text(encoding="utf-8") if target.exists() else None
    if existing == artifact.content:
        return "unchanged"

    # Atomic replace avoids partial writes if the process is interrupted.
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=str(parent), delete=False) as handle:
        handle.write(artifact.content)
        temp_path = Path(handle.name)
    temp_path.replace(target)
    return "written"
