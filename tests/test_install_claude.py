"""Tests for the install_claude.py script."""

import os
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

# Add scripts to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import install_claude


@pytest.fixture
def target_dir():
    """Create a temporary target directory."""
    d = tempfile.mkdtemp(prefix="test_install_")
    yield Path(d)
    shutil.rmtree(d)


def test_install_creates_expected_files(target_dir):
    """Test that install creates all expected files."""
    result = install_claude.install(str(target_dir), force=False, dry_run=False)
    assert result == 0

    # Check top-level CLAUDE.md
    assert (target_dir / "CLAUDE.md").exists()

    # Check .agentic/ router
    assert (target_dir / ".agentic" / "router" / "routes.yaml").exists()
    assert (target_dir / ".agentic" / "router" / "routing-rules.md").exists()

    # Check .agentic/ axioms
    assert (target_dir / ".agentic" / "axioms" / "universal.md").exists()
    assert (target_dir / ".agentic" / "axioms" / "domains" / "engineering.md").exists()
    assert (target_dir / ".agentic" / "axioms" / "skills" / "skill-creator.md").exists()
    assert (target_dir / ".agentic" / "axioms" / "skills" / "axiom-creator.md").exists()

    # Check .agentic/ skills
    assert (target_dir / ".agentic" / "skills" / "skill-creator" / "skill.md").exists()
    assert (target_dir / ".agentic" / "skills" / "skill-creator" / "axioms.md").exists()
    assert (target_dir / ".agentic" / "skills" / "skill-creator" / "checklist.md").exists()
    assert (target_dir / ".agentic" / "skills" / "skill-creator" / "output.md").exists()
    assert (target_dir / ".agentic" / "skills" / "axiom-creator" / "skill.md").exists()

    # Check .agentic/ guardrails
    assert (target_dir / ".agentic" / "guardrails" / "dangerous-actions.md").exists()
    assert (target_dir / ".agentic" / "guardrails" / "doctrine-mutation.md").exists()

    # Check .claude/ skills
    assert (target_dir / ".claude" / "skills" / "skill-creator" / "SKILL.md").exists()
    assert (target_dir / ".claude" / "skills" / "axiom-creator" / "SKILL.md").exists()
    assert (target_dir / ".claude" / "skills" / "route" / "SKILL.md").exists()


def test_dry_run_does_not_write(target_dir):
    """Test that --dry-run does not create any files."""
    result = install_claude.install(str(target_dir), force=False, dry_run=True)
    assert result == 0

    # Check that no files were written
    assert not (target_dir / "CLAUDE.md").exists()
    assert not (target_dir / ".agentic").exists()
    assert not (target_dir / ".claude").exists()


def test_existing_claude_md_not_overwritten(target_dir):
    """Test that existing CLAUDE.md is not overwritten without --force."""
    # Create a pre-existing CLAUDE.md
    existing_md = target_dir / "CLAUDE.md"
    existing_md.parent.mkdir(parents=True, exist_ok=True)
    existing_md.write_text("# My existing CLAUDE.md")

    result = install_claude.install(str(target_dir), force=False, dry_run=False)
    assert result == 0

    # CLAUDE.md should still be the original
    content = existing_md.read_text()
    assert content == "# My existing CLAUDE.md"


def test_force_overwrites_claude_md(target_dir):
    """Test that --force overwrites existing CLAUDE.md."""
    # Create a pre-existing CLAUDE.md
    existing_md = target_dir / "CLAUDE.md"
    existing_md.parent.mkdir(parents=True, exist_ok=True)
    existing_md.write_text("# My existing CLAUDE.md")

    result = install_claude.install(str(target_dir), force=True, dry_run=False)
    assert result == 0

    # CLAUDE.md should be overwritten
    content = existing_md.read_text()
    assert "agent-doctrine" in content.lower() or ".agentic/" in content


def test_force_overwrites_agentic_files(target_dir):
    """Test that --force overwrites existing .agentic/ files."""
    # Create a pre-existing file under .agentic/
    agentic_dir = target_dir / ".agentic" / "router"
    agentic_dir.mkdir(parents=True, exist_ok=True)
    existing_routes = agentic_dir / "routes.yaml"
    existing_routes.write_text("# old routes")

    result = install_claude.install(str(target_dir), force=True, dry_run=False)
    assert result == 0

    # routes.yaml should be overwritten
    content = existing_routes.read_text()
    assert "version:" in content


def test_missing_target_returns_error():
    """Test that install returns non-zero for missing target."""
    result = install_claude.install("/nonexistent/path/12345", force=False, dry_run=False)
    assert result != 0


def test_get_template_root():
    """Test that get_template_root returns a valid path."""
    root = install_claude.get_template_root()
    assert root.exists()
    assert (root / ".agentic").exists()
    assert (root / ".claude").exists()
