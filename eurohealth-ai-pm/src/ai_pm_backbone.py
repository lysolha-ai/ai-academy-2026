"""CLI entrypoint for AI-PM delivery backbone scaffolding."""

from __future__ import annotations

import argparse
import json
from typing import Any, Dict

from ai_pm.config import load_config
from ai_pm.logger import ActionLogger
from ai_pm.policy_hook import check_policy_hook
from ai_pm.scaffold import build_artifacts, write_artifact


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for scaffold generation."""
    parser = argparse.ArgumentParser(description="Generate AI-PM delivery backbone artifacts")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main() -> None:
    """Run scaffold generation with structured logs and error handling."""
    args = parse_args()

    try:
        config = load_config()
        logger = ActionLogger(config.log_path)
        artifacts = build_artifacts(config.project_dir)

        summary: Dict[str, Any] = {"ok": True, "results": {}}
        policy_check = check_policy_hook(config.policy_bundle_path)
        summary["policy_hook"] = policy_check.to_dict()
        logger.write(action="policy_hook_check", status="ok" if policy_check.ok else "error", details=policy_check.to_dict())
        if not policy_check.ok:
            summary["ok"] = False
            # Enforce fail-closed behavior: do not generate artifacts when policy hook fails.
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return

        for name, artifact in artifacts.items():
            try:
                status = write_artifact(artifact, overwrite=args.overwrite)
                summary["results"][name] = {
                    "status": status,
                    "path": str(artifact.path),
                }
                logger.write(
                    action="artifact_write",
                    status=status,
                    details={"artifact": name, "path": str(artifact.path)},
                )
            except Exception as exc:
                summary["ok"] = False
                summary["results"][name] = {
                    "status": "error",
                    "path": str(artifact.path),
                    "error": str(exc),
                }
                logger.write(
                    action="artifact_write",
                    status="error",
                    details={"artifact": name, "path": str(artifact.path), "error": str(exc)},
                )

        print(json.dumps(summary, ensure_ascii=False, indent=2))
    except Exception as exc:
        fallback: Dict[str, Any] = {
            "ok": False,
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }
        print(json.dumps(fallback, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
