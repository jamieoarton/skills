# Combined Workflow

Use this workflow when combining `skill-creator`, `writing-skills`, and `skill-building-complete`.

## 1. Scope and baseline

1. Define 2-3 concrete use cases.
2. Run baseline tasks without the new skill.
3. Record where failures or inefficiencies occur.

## 2. Build and structure

1. Scaffold skill using `skill-creator` tooling.
2. Keep `SKILL.md` concise and link deep content in `references/`.
3. Add scripts only when deterministic behavior is needed.

## 3. Validate behavior

1. Build trigger test set from `assets/test-queries-template.txt`.
2. Record results and run `scripts/check_triggering_accuracy.py`.
3. Measure baseline vs with-skill metrics using `scripts/measure_skill_performance.py`.

## 4. Validate integration

1. Check environment and executables using `scripts/validate_mcp_integration.py`.
2. Run smoke commands for connected MCP services.
3. Confirm graceful fallback path when MCP is unavailable.

## 5. Package and distribute

1. Run packaging and validation tools from `skill-creator`.
2. Complete `assets/distribution-checklist.md`.
3. Publish with clear versioning and install instructions.
