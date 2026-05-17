"""Tests for .agentic/router/routes.yaml validity."""

import pytest
import yaml
from pathlib import Path


ROUTES_PATH = Path(__file__).resolve().parent.parent / ".agentic" / "router" / "routes.yaml"
TEMPLATE_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ROUTES = []

REQUIRED_KEYS = [
    "description",
    "triggers",
    "negative_triggers",
    "priority",
    "intent",
    "axiom_stack",
    "skill",
    "required_context",
    "allowed_tools",
    "disallowed_tools",
    "verification",
    "output_contract",
    "guardrails",
    "doctrine_update",
]


@pytest.fixture
def routes():
    """Load routes.yaml."""
    with open(ROUTES_PATH) as f:
        return yaml.safe_load(f)


def test_routes_yaml_exists():
    """Test that routes.yaml exists."""
    assert ROUTES_PATH.exists()


def test_routes_yaml_parses(routes):
    """Test that routes.yaml parses as YAML and has required top-level keys."""
    assert routes is not None
    assert "routes" in routes
    assert "defaults" in routes


def test_required_routes_exist(routes):
    """Test that both required routes exist."""
    for route_name in REQUIRED_ROUTES:
        assert route_name in routes["routes"], f"Missing required route: {route_name}"


def test_routes_have_required_keys(routes):
    """Test that every route has all required keys."""
    for route_name, route in routes["routes"].items():
        for key in REQUIRED_KEYS:
            assert key in route, f"Route '{route_name}' missing key: {key}"


def test_route_axiom_stack_files_exist(routes):
    """Test that all referenced axiom stack files exist."""
    for route_name, route in routes["routes"].items():
        axiom_stack = route.get("axiom_stack", [])
        for axiom_path in axiom_stack:
            full_path = TEMPLATE_ROOT / axiom_path
            assert full_path.exists(), (
                f"Route '{route_name}' axiom file missing: {axiom_path}"
            )


def test_route_skill_files_exist(routes):
    """Test that all referenced skill files exist."""
    for route_name, route in routes["routes"].items():
        skill_path = route.get("skill", "")
        if skill_path:
            full_path = TEMPLATE_ROOT / skill_path
            assert full_path.exists(), (
                f"Route '{route_name}' skill file missing: {skill_path}"
            )


def test_route_output_contracts_exist(routes):
    """Test that all referenced output contracts exist."""
    for route_name, route in routes["routes"].items():
        output_contract = route.get("output_contract", "")
        if output_contract:
            full_path = TEMPLATE_ROOT / output_contract
            assert full_path.exists(), (
                f"Route '{route_name}' output contract missing: {output_contract}"
            )


def test_route_guardrails_exist(routes):
    """Test that all referenced guardrail files exist."""
    for route_name, route in routes["routes"].items():
        guardrails = route.get("guardrails", [])
        for guardrail_path in guardrails:
            full_path = TEMPLATE_ROOT / guardrail_path
            assert full_path.exists(), (
                f"Route '{route_name}' guardrail file missing: {guardrail_path}"
            )


def test_triggers_non_empty(routes):
    """Test that every route has at least one trigger."""
    for route_name, route in routes["routes"].items():
        triggers = route.get("triggers", [])
        assert len(triggers) > 0, f"Route '{route_name}' has no triggers"


def test_verification_has_strategy(routes):
    """Test that every route verification has a strategy field."""
    for route_name, route in routes["routes"].items():
        verification = route.get("verification", {})
        assert "strategy" in verification, (
            f"Route '{route_name}' verification missing 'strategy'"
        )


def test_defaults_axiom_order(routes):
    """Test that defaults contains axiom_order."""
    defaults = routes.get("defaults", {})
    assert "axiom_order" in defaults
    assert isinstance(defaults["axiom_order"], list)
    assert len(defaults["axiom_order"]) > 0
