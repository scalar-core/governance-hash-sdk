"""
Insurable Eval Pipeline — Phase 3: Functional Outcome Verification.

This phase is NON-BLOCKING (warnings only). It verifies whether the agent
achieved the desired end-state in the test environment.

Requirements:
  - FR-03: Verify task completion and correctness.

Usage:
  pytest tests/evals/test_functional.py -v
"""

import pytest


@pytest.fixture
def agent_outcome():
    """
    Stub: Replace with your actual agent runner.

    Should return an object with:
      - .success: bool — whether the task was completed
      - .result: Any — the output produced by the agent
      - .expected: Any — the expected output for comparison
    """
    raise NotImplementedError(
        "Replace this fixture with your agent runner. "
        "See docs/ENTERPRISE_EVALS_ARCHITECTURE.md Section 4."
    )


class TestPhase3FunctionalOutcome:
    """FR-03: Task completion verification (non-blocking)."""

    def test_task_completed(self, agent_outcome):
        assert agent_outcome.success is True, "Agent did not complete the assigned task"

    def test_output_matches_expected(self, agent_outcome):
        assert agent_outcome.result == agent_outcome.expected, (
            f"Output mismatch: got {agent_outcome.result}, expected {agent_outcome.expected}"
        )
