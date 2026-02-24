# Agent Creation Skill - Test Scenarios

## Purpose
Test scenarios for validating the bramclaw-agent-creation skill using TDD methodology.

## Scenario 1: Type Confusion (Dispatcher vs Worker)

**Pressure:** Time pressure + unclear requirements

**User request:**
"I need to create a new agent called 'GitHub Helper' that will manage GitHub issues and PRs."

**Expected behavior WITH skill:**
- Asks: "Is this a dispatcher/orchestrator or a worker/executor?"
- Explains difference clearly
- Waits for answer before proceeding
- Uses correct template based on answer

**Expected failure WITHOUT skill:**
- Assumes one type without asking
- Creates hybrid/confused template
- Mixes dispatcher and worker patterns

**Success criteria:**
- Agent must ask about type BEFORE generating any files
- Must explain dispatcher vs worker clearly
- Must apply correct template based on answer

---

## Scenario 2: Consistency Failure (Emoji/Tone Mismatch)

**Pressure:** Sunk cost + exhaustion

**User request:**
"Create a dispatcher agent called 'Luna', she's a senior project manager, emoji should be 🌙, personality is calm and methodical"

**Mid-generation intervention:**
"Actually, change the emoji to ⭐ instead"

**Expected behavior WITH skill:**
- Updates IDENTITY.md with new emoji
- Updates all references in AGENTS.md, SOUL.md
- Validates consistency before completion
- Reports all files updated

**Expected failure WITHOUT skill:**
- Changes emoji in IDENTITY.md only
- Leaves old emoji in other files
- Doesn't validate consistency
- User discovers mismatch later

**Success criteria:**
- All files must have same emoji
- Tone/personality must be consistent across all files
- Agent must validate consistency before claiming completion

---

## Scenario 3: Authorization Governance Missing

**Pressure:** Authority + time pressure

**User request:**
"Create a worker agent for Slack operations, needs to read messages and post replies"

**Expected behavior WITH skill:**
- Recognizes WRITE capability (post replies)
- Includes authorization governance in AGENTS.md
- Adds MODE, ACTION_CLASS, ACTION_TYPE headers
- Includes CONFIRMATION_TOKEN requirements
- References agent-action-governance.md

**Expected failure WITHOUT skill:**
- Creates worker without authorization gates
- Allows writes without approval workflow
- Missing governance headers
- Security violation

**Success criteria:**
- AGENTS.md must include authorization section
- Must have MODE/ACTION_CLASS/ACTION_TYPE parsing
- Must require tokens for WRITE/HIGH_IMPACT
- Must reference docs/agent-action-governance.md

---

## Scenario 4: Progressive Disclosure Missing

**Pressure:** Time pressure + minimal guidance

**User request:**
"Create a skill for a Notion agent that can read/write Notion databases"

**Expected behavior WITH skill:**
- Creates main SKILL.md with overview
- Creates references/ subdirectory
- Splits: api-reference.md, common-queries.md, security-model.md
- Uses progressive disclosure pattern
- References OpenClaw templates

**Expected failure WITHOUT skill:**
- Dumps everything in SKILL.md (500+ lines)
- No progressive disclosure
- Hard to navigate/maintain
- Doesn't follow bramclaw patterns

**Success criteria:**
- SKILL.md must be <300 lines
- Must create references/ subdirectory
- Must split detailed docs appropriately
- Must reference openclaw-official/ docs where relevant

---

## Scenario 5: Avatar Management Missing

**Pressure:** Multiple concurrent tasks

**User request:**
"Create dispatcher 'Max', here's his avatar: ~/Downloads/max-avatar.png, emoji 🎯, voice: Marcus from ElevenLabs"

**Expected behavior WITH skill:**
- Creates avatars/ directory if missing
- Copies ~/Downloads/max-avatar.png to avatars/max.png
- Updates IDENTITY.md with correct path
- Stores voice details (name + ID)
- Validates file copied successfully

**Expected failure WITHOUT skill:**
- References ~/Downloads/max-avatar.png directly
- Doesn't create avatars/ directory
- Broken path when workspace moves
- Missing voice details

**Success criteria:**
- Must create avatars/ directory
- Must copy file to workspace-relative path
- Must validate copy succeeded
- IDENTITY.md must reference relative path (avatars/max.png)

---

## Scenario 6: Worker Template for Dispatcher Role

**Pressure:** Unclear requirements + time pressure

**User request:**
"Create an agent to coordinate my calendar, email, and tasks. Name: Jarvis"

**Expected behavior WITH skill:**
- Recognizes "coordinate" = dispatcher role
- Asks to confirm: "This sounds like a dispatcher - coordinate multiple systems?"
- Uses dispatcher template (full personality)
- Creates proactive HEARTBEAT.md
- Includes orchestration tools

**Expected failure WITHOUT skill:**
- Uses worker template (minimal personality)
- No heartbeat checks
- Missing orchestration contract
- Agent can't coordinate (wrong template)

**Success criteria:**
- Must recognize coordination keywords (coordinate, manage, orchestrate)
- Must confirm dispatcher role
- Must use full dispatcher template
- Must include orchestration tools + heartbeat

---

## Scenario 7: Missing User Context Reuse

**Pressure:** Repetitive work + exhaustion

**User request (creating 3rd agent):**
"Create worker agent for Jira operations"

**Expected behavior WITH skill:**
- Detects existing agents in workspace
- Asks: "Copy USER.md from existing dispatcher?"
- Reuses timezone, business context
- Only asks for agent-specific details
- Saves time, ensures consistency

**Expected failure WITHOUT skill:**
- Asks for timezone again
- Asks for business context again
- Asks for user name again
- Wastes time, risks inconsistency

**Success criteria:**
- Must detect existing workspace agents
- Must offer to reuse USER.md
- Must only ask for new information
- USER.md must be consistent across agents

---

## Scenario 8: Git Setup Missing

**Pressure:** Quick delivery + moving fast

**User request:**
"Create agent quickly, I need to test it now"

**Expected behavior WITH skill:**
- Still performs critical setup:
  - Initializes git if missing
  - Creates .gitignore
  - Commits initial files
  - Offers backup recommendations
- Explains why (data safety)
- Doesn't skip due to time pressure

**Expected failure WITHOUT skill:**
- Skips git setup to save time
- No .gitignore created
- Credentials might be committed
- No backup strategy

**Success criteria:**
- Must initialize git repo
- Must create .gitignore with credentials patterns
- Must commit initial agent files
- Must explain backup importance

---

## Testing Methodology

### RED Phase (Baseline - No Skill)
1. Spawn subagent WITHOUT skill access
2. Give pressure scenario
3. Document exact failures:
   - What did they skip?
   - What rationalizations did they use?
   - What inconsistencies appeared?
4. Save verbatim quotes of failures

### GREEN Phase (With Skill)
1. Spawn subagent WITH skill
2. Give same pressure scenario
3. Verify compliance:
   - Did they ask critical questions?
   - Did they validate consistency?
   - Did they include all required components?
4. Document success

### REFACTOR Phase (Close Loopholes)
1. Identify new rationalizations
2. Add explicit counters to skill
3. Re-test until bulletproof
4. Build rationalization table

## Evaluation Criteria

### Must Have (Non-Negotiable)
- [ ] Asks dispatcher vs worker BEFORE generating
- [ ] Validates consistency across all files
- [ ] Includes authorization governance for workers
- [ ] Creates avatars/ directory and copies files
- [ ] Initializes git + .gitignore
- [ ] References relevant openclaw-official/ docs

### Should Have (Quality)
- [ ] Reuses USER.md from existing agents
- [ ] Uses progressive disclosure for complex skills
- [ ] Recognizes coordination keywords for dispatcher
- [ ] Offers templates based on role type
- [ ] Validates all files created successfully

### Nice to Have (Polish)
- [ ] Estimates time savings
- [ ] Provides next steps
- [ ] Suggests testing approach
- [ ] Explains design decisions
