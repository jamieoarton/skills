# Anthropic Complete Guide (2026) - Clean Working Notes

This file is a cleaned, operational reference copy for skill-building workflows.

## Contents

1. Fundamentals
2. Planning and design
3. Testing and iteration
4. Distribution and sharing
5. Patterns and troubleshooting
6. Quick references

## 1) Fundamentals

A skill packages reusable workflow knowledge into a directory.

Core files:
- `SKILL.md` (required)
- `scripts/` (optional, deterministic helpers)
- `references/` (optional, deep docs)
- `assets/` (optional, templates/checklists)

Principles:
- Progressive disclosure
- Composability with other skills
- Portability across environments

## 2) Planning and Design

Start from 2-3 concrete use cases.

For each use case define:
- Trigger phrase(s)
- Steps Claude should execute
- Required tool/MCP calls
- Success outcome

Common skill classes:
1. Document and asset creation
2. Workflow automation
3. MCP enhancement/orchestration

## 3) Testing and Iteration

Three practical test tracks:

1. Triggering tests
- skill should trigger on relevant prompts
- skill should not trigger on unrelated prompts

2. Functional tests
- expected outputs are produced
- API/MCP calls succeed
- edge cases and failure states are handled

3. Baseline comparison
- compare no-skill vs with-skill runs
- collect tokens, tool calls, failures, and duration

Suggested targets:
- Triggering accuracy >= 90%
- Meaningful token/call reduction
- Zero API failures in core flow

## 4) Distribution and Sharing

Distribution paths:
- `.skill` package for direct sharing
- GitHub repo for versioning and discoverability
- Org deployment for centralized team rollout
- API deployment for automation

Before release:
- validate structure and metadata
- test install flow
- publish usage and troubleshooting notes

## 5) Patterns and Troubleshooting

High-value workflow patterns:
- Sequential orchestration
- Multi-MCP coordination
- Iterative quality loops
- Context-aware tool selection
- Domain constraints before side effects

Common troubleshooting themes:
- YAML formatting issues
- weak descriptions (over/under-triggering)
- missing files referenced by `SKILL.md`
- missing MCP fallback behavior

## 6) Quick References

### Minimal frontmatter

```yaml
---
name: my-skill
description: Use when users need [outcome] in [context] with [trigger cues].
---
```

### Launch checklist

- [ ] `SKILL.md` valid and concise
- [ ] referenced files exist
- [ ] scripts run successfully
- [ ] trigger test set executed
- [ ] baseline comparison captured
- [ ] distribution path tested
