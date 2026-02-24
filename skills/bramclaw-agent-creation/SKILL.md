---
name: bramclaw-agent-creation
description: Use when creating new OpenClaw agents for bramclaw, including dispatcher/orchestrator agents and worker/executor agents. Triggers on agent creation, workspace setup, or multi-agent system expansion requests.
---

**Version:** 1.0.0 | **Status:** ✅ Production

---

# Creating Bramclaw Agents

Systematic workflow for creating production-ready OpenClaw agents with proper governance, security, and documentation.

## When This Skill Should Trigger

**✅ Should trigger for:**
- "Create a new agent for X"
- "Set up an agent to handle Y"
- "I need an agent that manages Z"
- "Build a worker agent for W"
- "Create a dispatcher to coordinate..."

**❌ Should NOT trigger for:**
- "Create a Claude Code skill" (different from OpenClaw agent)
- "Add a new feature to existing agent" (use that agent's skill)
- "Fix agent behavior" (debugging, not creation)

---

## Core Decision: Agent Type

**STOP. Before creating ANY files, ask the user:**

```
Is this agent a:
A) Dispatcher/Orchestrator - coordinates other agents, has personality
B) Worker/Executor - performs specific domain tasks, minimal personality
```

**Do NOT assume. Do NOT guess. ASK FIRST.**

### Type A: Dispatcher/Orchestrator

**Examples:** Pepper (Chief of Staff), personal assistant, coordinator

**Characteristics:**
- Has full personality (name, character, avatar, voice)
- Coordinates multiple worker agents
- Proactive (heartbeat checks, memory management)
- Uses orchestration tools (`sessions_spawn`, `sessions_list`, `sessions_history`)
- Rich documentation (full SOUL.md, detailed AGENTS.md)

### Type B: Worker/Executor

**Examples:** bram-clickup, bram-gmail, bram-github, bram-obsidian

**Characteristics:**
- Minimal/no personality (functional tool)
- Performs domain-specific operations (ClickUp, Gmail, GitHub, etc.)
- Reactive only (no heartbeat, no proactive work)
- Uses domain tools (API clients, CLIs)
- Lean documentation (functional SOUL.md, execution-focused AGENTS.md)

---

## Required Files (All Agent Types)

Every agent workspace needs these 7 core files:

| File | Dispatcher | Worker | Purpose |
|------|------------|--------|---------|
| **IDENTITY.md** | Rich | Minimal | Name, role, emoji, avatar, voice |
| **SOUL.md** | Philosophical | Functional | Personality/principles |
| **USER.md** | Detailed | Brief | User context |
| **AGENTS.md** | Orchestration + personality | Execution contract | Operating instructions |
| **TOOLS.md** | Orchestration tools | Domain tools | Tool usage patterns |
| **HEARTBEAT.md** | Proactive checklist | Empty | Periodic duties |
| **BOOTSTRAP.md** | Skip (for new workspaces only) | Skip | First-run ritual |

**Reference templates:** @docs/openclaw-official/reference/templates/

---

## Critical: Authorization Governance

**For ALL worker agents that perform writes, reference:**

@docs/agent-action-governance.md

**Required in AGENTS.md for workers:**

```markdown
## Authorization Gates (Strict)

You must parse task headers when present:

1. `MODE: observe|propose|execute|execute_high_impact`
2. `ACTION_CLASS: READ|WRITE|HIGH_IMPACT`
3. `ACTION_TYPE: CREATE|UPDATE|DELETE|SEND|OTHER`
4. `CONFIRMATION_TOKEN: ...` (required when policy says so)
5. `ACCOUNT_SCOPE: principal|assistant|auto` (for account-bound systems)

Enforcement:
1. If `ACTION_CLASS` is `READ`, execute read-only.
2. If `ACTION_CLASS` is `WRITE`, check if trusted internal system...
   [See full pattern in docs/agent-action-governance.md]
```

**Trusted internal systems exception:**
- `bram-clickup` and `bram-obsidian` allow `CREATE/UPDATE` without token
- All other actions (`DELETE`, `SEND`, `HIGH_IMPACT`) ALWAYS require tokens

---

## Progressive Disclosure (For Complex Agents)

**If agent has significant API surface or documentation needs, use:**

```
.claude/skills/bramclaw-{name}/
├── SKILL.md (main, <300 lines)
├── references/
│   ├── api-reference.md
│   ├── common-queries.md
│   ├── security-model.md
│   ├── error-handling.md
│   └── success-metrics.md
└── scripts/
    ├── {name}_client.py
    └── {name}_agent.py
```

**See example:** @.claude/skills/bramclaw-clickup/SKILL.md

**Pattern:**
- SKILL.md: Overview, when to use, quick reference
- references/: Deep dive docs (API, queries, security, errors, metrics)
- scripts/: Implementation

---

## Creation Workflow

**Use this exact sequence:**

### Phase 1: Discovery (Ask Questions)

**For ALL agents:**
1. Agent type? (dispatcher vs worker) **← MUST ASK FIRST**
2. Agent name? (human-readable)
3. Role/purpose? (one sentence)
4. Domain/specialty? (e.g., "ClickUp operations", "Gmail management")

**Additional for dispatchers:**
5. Personality vibe? (3-5 adjectives or paragraph)
6. Emoji? (represents character)
7. Avatar path? (if applicable)
8. Voice? (ElevenLabs name + ID, if applicable)
9. Proactive duties? (heartbeat checks?)

**Additional for workers:**
10. What APIs/services? (ClickUp API, Gmail API, etc.)
11. Read-only or writes? (determines authorization governance)
12. Account-bound? (determines ACCOUNT_SCOPE requirements)

### Phase 2: Context Reuse

**Check for existing agents:**

```bash
ls -la config/agent-contracts/
```

**If other agents exist, ask:**
- "Copy USER.md from existing dispatcher?" (saves time, ensures consistency)
- "Reuse authorization patterns from similar worker?" (e.g., Gmail → Slack)

### Phase 3: File Generation

**Create in this order:**

1. **Workspace directory:** `config/agent-contracts/{agent-name}/`
2. **IDENTITY.md** (template based on type)
3. **SOUL.md** (template based on type + personality)
4. **USER.md** (copy or create)
5. **AGENTS.md** (critical - includes authorization for workers)
6. **TOOLS.md** (domain-specific)
7. **HEARTBEAT.md** (proactive for dispatchers, empty for workers)

**If creating skill:**

8. `.claude/skills/bramclaw-{name}/SKILL.md`
9. `references/` subdirectory (if complex)
10. `scripts/` subdirectory (implementation)

### Phase 4: Supporting Infrastructure

**REQUIRED (not optional):**

**Avatar management (dispatchers only):**
```bash
mkdir -p config/agent-contracts/{agent-name}/avatars/
cp {source-path} config/agent-contracts/{agent-name}/avatars/{name}.{ext}
# Verify copy succeeded
ls -la config/agent-contracts/{agent-name}/avatars/
```

**Git setup (MANDATORY):**
```bash
cd config/agent-contracts/{agent-name}/
git init
cat > .gitignore << 'EOF'
.DS_Store
.env
**/*.key
**/*.pem
**/secrets*
EOF
git add .
git commit -m "feat: create {agent-name} agent"
# Verify commit succeeded
git log -1 --oneline
```

**Testing setup (MANDATORY for workers with writes):**

Create test plan following bramclaw-clickup pattern:

```bash
mkdir -p .claude/skills/bramclaw-{name}/tests/
cat > .claude/skills/bramclaw-{name}/tests/TEST-PLAN.md << 'EOF'
# {Name} Agent Test Plan

## Authorization Gate Tests
- [ ] READ without headers → executes
- [ ] WRITE without headers → defaults read-only
- [ ] WRITE with valid token → executes
- [ ] HIGH_IMPACT without token → proposes only
- [ ] HIGH_IMPACT with valid token → executes

## Domain Tests
- [ ] List/search operations work
- [ ] Create operations work (with authorization)
- [ ] Update operations work (with authorization)
- [ ] Error handling for 401, 404, 429, 500

## Integration Tests
- [ ] Dispatcher can delegate successfully
- [ ] Output format matches requirements
- [ ] Account scope handling works (if applicable)
EOF
```

**Reference:** @.claude/skills/bramclaw-clickup/tests/TEST-PLAN.md

### Phase 5: Validation

**Consistency checks:**
- [ ] Emoji same in IDENTITY.md and AGENTS.md closing
- [ ] Personality tone consistent across IDENTITY, SOUL, AGENTS
- [ ] Authorization governance included (if worker with writes)
- [ ] Progressive disclosure used (if complex skill)
- [ ] Avatar copied to workspace-relative path (if applicable)
- [ ] All 7 core files present

**Production readiness:**
- [ ] Authorization gates tested
- [ ] Sample commands work
- [ ] Git repo initialized
- [ ] .gitignore prevents credential leaks
- [ ] References to openclaw-official/ docs included

---

## Red Flags - STOP and Ask

**If you find yourself:**
- Creating files without asking agent type → STOP, ask first
- Copy-pasting without understanding → STOP, validate pattern applies
- Skipping authorization governance → STOP, it's required for workers
- Creating 500+ line SKILL.md → STOP, use progressive disclosure
- Assuming user context → STOP, ask or copy from existing
- Skipping git init "to save time" → STOP, it's MANDATORY
- Skipping tests "for MVP" → STOP, required for workers with writes
- Skipping validation "it's probably fine" → STOP, run the checklist

**All of these mean: Go back to Phase 1 (Discovery).**

---

## Common Rationalizations (STOP These)

| Excuse | Reality |
|--------|---------|
| "Time pressure - skip tests" | Tests prevent hours of debugging. 5 min now saves hours later. |
| "Git setup can wait" | Credentials might leak without .gitignore. Do it now. |
| "I'll validate later" | Inconsistencies compound. Validate before moving on. |
| "Authorization is obvious" | Security requires explicit compliance, not assumptions. |
| "Progressive disclosure is overkill" | 500+ line docs are unreadable. Split now or refactor later. |
| "Worker doesn't need TOOLS.md" | Template requires it. Empty is fine, missing is not. |
| "I know the pattern from other agents" | Patterns evolve. Use current template. |
| "Just copy existing agent" | Copy risks propagating old bugs. Use template. |

**All of these are shortcuts that create technical debt. The skill prevents this.**

---

## Working Under Time Pressure

**User says: "I need this quickly"**

**DO NOT skip:**
- [ ] Asking agent type (dispatcher vs worker)
- [ ] Authorization governance (security requirement)
- [ ] Git initialization + .gitignore (prevents credential leaks)
- [ ] Validation checklist (catches errors before completion)

**CAN defer (but document):**
- [ ] Test implementation (create TEST-PLAN.md, implement later)
- [ ] Detailed API reference (create stub in references/)
- [ ] Common queries cookbook (create stub)
- [ ] Avatar copying (dispatcher only - can add later)

**Communicate trade-offs:**
- "I can deliver a working MVP in X minutes with these deferred items: [list]"
- "To reach production-ready, you'll need to: [list remaining work]"
- "Estimated time to production-ready from MVP: [estimate]"

**NEVER say:**
- "It's ready for production" (when tests missing)
- "No need for tests, it's simple" (all code needs tests)
- "Git can wait" (credentials might leak)
- "I'll validate later" (inconsistencies compound)

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Assumed worker when should be dispatcher | Always ask type first |
| Missing authorization governance | Use agent-action-governance.md template |
| Inconsistent emoji across files | Validate consistency in Phase 5 |
| Avatar at non-relative path | Copy to avatars/ in workspace |
| No progressive disclosure for complex agent | Create references/ subdirectory |
| Skipped USER.md reuse | Check existing agents first |
| No git setup | Initialize repo with .gitignore |

---

## Templates by Type

**Dispatcher/Orchestrator:**
- Base: @docs/openclaw-official/reference/templates/AGENTS.md
- Example: @config/agent-contracts/bram-router/AGENTS.md (Pepper)
- Pattern doc: @docs/plans/2026-02-22-agent-creation-patterns.md

**Worker/Executor:**
- Base: @docs/openclaw-official/reference/templates/AGENTS.md (simplified)
- Examples:
  - @config/agent-contracts/bram-clickup/AGENTS.md
  - @config/agent-contracts/bram-gmail/AGENTS.md
- Pattern doc: @docs/plans/2026-02-22-agent-creation-patterns.md
- Skill example: @.claude/skills/bramclaw-clickup/SKILL.md

---

## Success Criteria

**Quantitative:**
- Time to create: <15 minutes (vs 45-60 manual)
- Questions asked: <10 upfront (vs 15-20 scattered)
- Files created correctly: 7/7 (100%)
- Consistency errors: 0

**Qualitative:**
- First-try success: Agent starts without fixes
- Personality coherence: Feels like one character (dispatchers)
- Authorization compliance: Passes security audit
- Documentation quality: Clear, navigable, progressive

---

## Resources

**OpenClaw Official Docs:**
- [AGENT_GUIDE.md](../../docs/openclaw-official/AGENT_GUIDE.md) - Complete agent reference
- [Agent Runtime](../../docs/openclaw-official/concepts/agent.md) - How agents work
- [Agent Workspace](../../docs/openclaw-official/concepts/agent-workspace.md) - File structure
- [Templates](../../docs/openclaw-official/reference/templates/) - Official templates

**Bramclaw Patterns:**
- [Agent Creation Patterns](../../docs/plans/2026-02-22-agent-creation-patterns.md) - Case study (Pepper)
- [Agent Action Governance](../../docs/agent-action-governance.md) - Authorization standard
- [ClickUp Delegation Pattern](../../docs/CLICKUP-TASK-DELEGATION-PATTERN.md) - Account scope example

**Examples:**
- Dispatcher: `config/agent-contracts/bram-router/` (Pepper)
- Workers: `config/agent-contracts/bram-{clickup,gmail,obsidian,supabase}/`
- Skill: `.claude/skills/bramclaw-clickup/` (progressive disclosure example)

---

## Skill Self-Validation

**After using this skill to create an agent, verify:**

1. **Did I ask agent type BEFORE creating files?** (YES/NO)
2. **Did I include authorization governance?** (YES/NO - workers only)
3. **Did I use progressive disclosure?** (YES/NO - if complex)
4. **Did I validate consistency?** (YES/NO - always)
5. **Did I initialize git?** (YES/NO - always)
6. **Did I create TEST-PLAN.md?** (YES/NO - workers with writes)

**If any answer is NO, go back and fix it.**

**Skill is working if:**
- All YES for applicable questions
- Production readiness >80% on first attempt
- No major rework needed after creation
- Security compliance passes audit

**Report skill issues at:** @.claude/skills/bramclaw-agent-creation/test-scenarios.md

---

**Status:** ✅ Production-ready workflow
**Security:** Enforces authorization governance
**Testing:** Validated with GitHub agent creation (baseline vs skill)
**Last updated:** 2026-02-23
