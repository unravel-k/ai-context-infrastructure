"""Tests that creator skill files contain required workflow steps and templates."""

from pathlib import Path


TEMPLATE_ROOT = Path(__file__).resolve().parent.parent


def read_skill(name: str) -> str:
    """Read a skill file from .agentic/skills/<name>/skill.md."""
    path = TEMPLATE_ROOT / ".agentic" / "skills" / name / "skill.md"
    return path.read_text()


def read_claude_skill(name: str) -> str:
    """Read a Claude Code SKILL.md."""
    path = TEMPLATE_ROOT / ".claude" / "skills" / name / "SKILL.md"
    return path.read_text()


class TestSkillCreatorContract:
    """Tests for the skill-creator skill.md contract."""

    def test_mentions_inspect_skills_directory(self):
        content = read_skill("skill-creator")
        assert ".agentic/skills/" in content

    def test_mentions_create_vs_modify_decision(self):
        content = read_skill("skill-creator")
        assert "modify" in content.lower()
        assert "create" in content.lower()

    def test_mentions_four_skill_files(self):
        content = read_skill("skill-creator")
        assert "skill.md" in content
        assert "axioms.md" in content
        assert "checklist.md" in content
        assert "output.md" in content

    def test_mentions_claude_adapter(self):
        content = read_skill("skill-creator")
        assert ".claude/skills/" in content
        assert "SKILL.md" in content

    def test_mentions_route_registration(self):
        content = read_skill("skill-creator")
        assert "routes.yaml" in content

    def test_mentions_summary_format(self):
        content = read_skill("skill-creator")
        assert "files created" in content.lower()
        assert "files modified" in content.lower()
        assert "route changes" in content.lower()
        assert "unresolved questions" in content.lower()

    def test_claude_adapter_references_agentic(self):
        content = read_claude_skill("skill-creator")
        assert ".agentic/" in content


class TestAxiomCreatorContract:
    """Tests for the axiom-creator skill.md contract."""

    def test_mentions_classification_options(self):
        content = read_skill("axiom-creator")
        assert "universal" in content.lower()
        assert "domain-specific" in content.lower()
        assert "job-specific" in content.lower()
        assert "skill-specific" in content.lower()
        assert "project-specific" in content.lower()

    def test_mentions_target_locations(self):
        content = read_skill("axiom-creator")
        assert ".agentic/axioms/universal.md" in content
        assert ".agentic/axioms/domains/" in content
        assert ".agentic/axioms/jobs/" in content
        assert ".agentic/axioms/skills/" in content
        assert ".agentic/axioms/projects/" in content

    def test_mentions_axiom_id_convention(self):
        content = read_skill("axiom-creator")
        assert "AX-UNIV-" in content
        assert "AX-DOM-" in content
        assert "AX-JOB-" in content
        assert "AX-SKILL-" in content
        assert "AX-PROJ-" in content

    def test_mentions_duplicate_detection(self):
        content = read_skill("axiom-creator")
        assert "similar" in content.lower()
        assert "modify" in content.lower()
        assert "skip" in content.lower()

    def test_mentions_route_integration(self):
        content = read_skill("axiom-creator")
        assert "route" in content.lower()
        assert "axiom_stack" in content

    def test_mentions_summary_format(self):
        content = read_skill("axiom-creator")
        assert "classification" in content.lower()
        assert "file changed" in content.lower()
        assert "axiom id" in content.lower()
        assert "unresolved questions" in content.lower()

    def test_claude_adapter_references_agentic(self):
        content = read_claude_skill("axiom-creator")
        assert ".agentic/" in content


class TestClaudeAdapterContracts:
    """Tests for Claude Code adapter SKILL.md files."""

    def test_skill_creator_has_frontmatter(self):
        content = read_claude_skill("skill-creator")
        assert content.startswith("---")

    def test_axiom_creator_has_frontmatter(self):
        content = read_claude_skill("axiom-creator")
        assert content.startswith("---")

    def test_route_has_frontmatter(self):
        path = TEMPLATE_ROOT / ".claude" / "skills" / "route" / "SKILL.md"
        content = path.read_text()
        assert content.startswith("---")

    def test_skill_creator_has_name_in_frontmatter(self):
        content = read_claude_skill("skill-creator")
        assert "name: skill-creator" in content

    def test_axiom_creator_has_name_in_frontmatter(self):
        content = read_claude_skill("axiom-creator")
        assert "name: axiom-creator" in content

    def test_route_has_name_in_frontmatter(self):
        path = TEMPLATE_ROOT / ".claude" / "skills" / "route" / "SKILL.md"
        content = path.read_text()
        assert "name: route" in content
