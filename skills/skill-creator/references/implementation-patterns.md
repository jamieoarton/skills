# Implementation Patterns

**Purpose:** Practical patterns for building reliable skill workflows, especially when MCP calls are involved.

## Pattern 1: Sequential Workflow Orchestration

Use when each step depends on outputs from previous steps.

1. Validate prerequisites.
2. Run step N.
3. Validate output of step N.
4. Continue only on success.
5. Return a partial-progress summary on failure.

## Pattern 2: Multi-MCP Phase Coordination

Use when a workflow spans multiple MCP servers.

1. Split work into explicit phases per MCP domain.
2. Normalize outputs between phases (IDs, URLs, timestamps).
3. Add a verification gate before handoff to next phase.
4. Keep rollback instructions for side effects.

## Pattern 3: Iterative Refinement Loop

Use when quality improves through repeated review and correction.

1. Generate first pass.
2. Run deterministic checks (style/schema/consistency).
3. Repair failures.
4. Repeat until thresholds are met or max iterations reached.

## Pattern 4: Context-Aware Tool Selection

Use when multiple tools can solve the same task.

Decision order:
1. Pick the safest tool that satisfies requirements.
2. Prefer tools with structured output.
3. Prefer fewer network calls when quality is equivalent.
4. Fall back to manual guidance when tools are unavailable.

## Pattern 5: Domain-Specific Intelligence

Use when domain constraints should be enforced before execution.

1. Encode domain rules as preflight checks.
2. Block operations that violate compliance or policy.
3. Explain blocked actions and provide corrective steps.

## Checklist

- Workflow has explicit prerequisites.
- Every API/MCP phase has success and failure conditions.
- Output validation is deterministic where possible.
- User receives actionable errors, not generic failures.
- Metrics can be collected from each run.
