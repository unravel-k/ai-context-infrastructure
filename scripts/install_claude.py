#!/usr/bin/env python3
"""Install the agent-doctrine template into a target repository."""

import argparse
import os
import shutil
import sys
from pathlib import Path


def get_template_root() -> Path:
    """Return the absolute path to the template root (where this script lives)."""
    return Path(__file__).resolve().parent.parent


def copy_dir(src: Path, dst: Path, force: bool = False, dry_run: bool = False) -> dict:
    """Copy a directory tree. Returns dict of {action: [paths]}."""
    result = {"created": [], "skipped": [], "overwritten": []}
    if not src.exists():
        return result
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        target = dst / rel
        if dry_run:
            if target.exists() and not force:
                result["skipped"].append(str(rel))
            else:
                action = "overwritten" if target.exists() else "created"
                result[action].append(str(rel))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and not force:
                result["skipped"].append(str(rel))
            else:
                action = "overwritten" if target.exists() else "created"
                shutil.copy2(item, target)
                result[action].append(str(rel))
    return result


def copy_file(src: Path, dst: Path, force: bool = False, dry_run: bool = False) -> dict:
    """Copy a single file. Returns dict of {action: [paths]}."""
    result = {"created": [], "skipped": [], "overwritten": []}
    if dry_run:
        if dst.exists() and not force:
            result["skipped"].append(str(dst))
        else:
            action = "overwritten" if dst.exists() else "created"
            result[action].append(str(dst))
    else:
        if dst.exists() and not force:
            result["skipped"].append(str(dst))
        else:
            action = "overwritten" if dst.exists() else "created"
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            result[action].append(str(dst))
    return result


def merge_results(*dicts: dict) -> dict:
    """Merge multiple result dicts."""
    merged = {"created": [], "skipped": [], "overwritten": []}
    for d in dicts:
        for key in merged:
            merged[key].extend(d.get(key, []))
    return merged


def install(target: str, force: bool = False, dry_run: bool = False) -> int:
    """Run the installation. Returns exit code."""
    template_root = get_template_root()
    target_path = Path(target).resolve()

    if not target_path.exists():
        print(f"Error: target directory does not exist: {target_path}")
        return 1

    print(f"Installing agent-doctrine template to: {target_path}")
    if dry_run:
        print("  (dry-run mode: no files will be written)")
    if force:
        print("  (force mode: existing files will be overwritten)")
    print()

    # Collect results
    all_results = {"created": [], "skipped": [], "overwritten": []}

    # 1. Copy .agentic/ directory
    src_agentic = template_root / ".agentic"
    dst_agentic = target_path / ".agentic"
    r = copy_dir(src_agentic, dst_agentic, force=force, dry_run=dry_run)
    all_results = merge_results(all_results, r)

    # 2. Copy .claude/skills/ directory
    src_claude_skills = template_root / ".claude" / "skills"
    dst_claude_skills = target_path / ".claude" / "skills"
    r = copy_dir(src_claude_skills, dst_claude_skills, force=force, dry_run=dry_run)
    all_results = merge_results(all_results, r)

    # 3. Copy CLAUDE.md (special: do not overwrite without --force)
    src_claude_md = template_root / "adapters" / "claude-code" / "CLAUDE.md"
    dst_claude_md = target_path / "CLAUDE.md"

    # Check for pre-existing CLAUDE.md before copying
    claude_md_existed = dst_claude_md.exists()

    r = copy_file(src_claude_md, dst_claude_md, force=force, dry_run=dry_run)
    all_results = merge_results(all_results, r)

    if claude_md_existed and not force:
        print("WARNING: CLAUDE.md already exists in target. Use --force to overwrite.")
        print()

    # Print summary
    print("=== Install Summary ===")
    print(f"  Created:     {len(all_results['created'])} files")
    print(f"  Overwritten: {len(all_results['overwritten'])} files")
    print(f"  Skipped:     {len(all_results['skipped'])} files")

    if all_results["skipped"]:
        print()
        print("Skipped files (already exist, use --force to overwrite):")
        for f in all_results["skipped"]:
            print(f"  - {f}")

    if dry_run:
        print()
        print("Dry-run complete. No files were modified.")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Install the agent-doctrine template into a target repository."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Path to the target repository",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing files",
    )
    args = parser.parse_args()

    sys.exit(install(args.target, force=args.force, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
