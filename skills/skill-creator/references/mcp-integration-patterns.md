# MCP Integration Patterns

**Purpose:** Design patterns and best practices for building skills that leverage Model Context Protocol (MCP) servers.

**Target audience:** Skill builders creating Category 3 skills (MCP enhancement/automation)

---

## Table of Contents

1. [Category 3 Definition](#category-3-definition)
2. [Single MCP Workflow Pattern](#single-mcp-workflow-pattern)
3. [Multi-MCP Coordination Pattern](#multi-mcp-coordination-pattern)
4. [Error Handling Patterns](#error-handling-patterns)
5. [Testing MCP-Dependent Skills](#testing-mcp-dependent-skills)
6. [Performance Optimization](#performance-optimization)

---

## Category 3 Definition

**Category 3: MCP Enhancement & Automation**

Skills that leverage MCP servers to provide specialized workflows, automations, or enhanced capabilities beyond what's available through direct MCP tool calls.

### Characteristics

- **Requires MCP connection** - Skill instructions reference specific MCP tools
- **Adds intelligence layer** - Provides decision-making, coordination, or domain expertise on top of raw MCP calls
- **Workflow automation** - Combines multiple MCP calls into cohesive workflows
- **Cross-MCP coordination** - May orchestrate multiple MCP servers together

### Examples

✅ **Good Category 3 skills:**
- Sprint planning skill (Linear MCP) - analyzes velocity, recommends scope, creates sprint
- Design handoff skill (Figma → Drive → Linear → Slack) - automates multi-tool workflow
- Data pipeline skill (Postgres → Snowflake → Slack) - coordinates ETL with notifications

❌ **Not Category 3:**
- Generic "use Figma MCP" skill - just tells user to call MCP tools (no added value)
- Skill that could work without MCP - Category 1 or 2 pattern

### When to Build Category 3

Build a Category 3 skill when:
- **Workflow is repeatable** - Same sequence of MCP calls happens regularly
- **Requires domain knowledge** - Need expertise to orchestrate tools correctly
- **Coordination is complex** - Multiple tools, conditional logic, error recovery
- **Time-saving is significant** - Manual workflow takes >10 minutes

---

## Single MCP Workflow Pattern

**Use when:** Skill leverages one MCP server to provide specialized workflow.

### Pattern Structure

```markdown
## Overview
Brief description of what this skill automates using [MCP Server Name]

## When to Use
Specific triggers that indicate this workflow is needed

## Prerequisites
- [MCP Server Name] connected and authenticated
- Required permissions (read/write/admin)
- Any domain-specific requirements

## Workflow

1. **Validate MCP connection**
   - Check [mcp_server_name] is connected
   - If not: Provide setup instructions

2. **Gather context** (optional)
   - Ask clarifying questions if needed
   - Validate input parameters

3. **Execute MCP calls**
   - [Specific tool call with purpose]
   - [Next tool call building on previous]
   - [Final tool call completing workflow]

4. **Verify results**
   - Confirm expected outcome achieved
   - Report to user with actionable summary

## Error Handling
See [Error Handling Patterns](#error-handling-patterns)

## Example Usage
[Concrete example of user request → skill execution → outcome]
```

### Example: Linear Sprint Planning Skill

```markdown
## Overview
Automates sprint planning by analyzing historical velocity, recommending backlog items, and creating a new sprint in Linear.

## When to Use
- User asks to "plan next sprint"
- Need to "calculate sprint capacity"
- Want to "create sprint based on velocity"

## Prerequisites
- Linear MCP connected (`mcp__linear` tools available)
- Access to historical sprints (last 3 sprints readable)
- Write access to create sprints and update issues

## Workflow

1. **Validate Linear connection**
   - Check `mcp__linear__list_teams` is available
   - If not: "Please connect Linear MCP server first: [setup instructions]"

2. **Gather context**
   - Ask: "Which team?" (if multiple teams)
   - Ask: "Sprint duration?" (default: 2 weeks)
   - Confirm current sprint end date

3. **Execute MCP calls**
   - **Fetch historical data:**
     ```
     mcp__linear__list_sprints(team_id, status="completed", limit=3)
     ```
     Purpose: Calculate average velocity from last 3 sprints

   - **Calculate velocity:**
     ```
     avg_points = sum(sprint.completed_points) / 3
     recommended_capacity = avg_points * 0.9  # 10% buffer
     ```

   - **Fetch backlog:**
     ```
     mcp__linear__list_issues(team_id, state="backlog", order_by="priority")
     ```
     Purpose: Get prioritized backlog items

   - **Recommend scope:**
     Filter backlog items where cumulative points <= recommended_capacity

   - **Create sprint:**
     ```
     mcp__linear__create_sprint(
       name=f"Sprint {next_number}",
       start_date=today,
       end_date=today + sprint_duration,
       goal="[Generated from top priorities]"
     )
     ```

   - **Assign issues:**
     ```
     For each recommended issue:
       mcp__linear__update_issue(issue_id, sprint_id=new_sprint.id)
     ```

4. **Verify results**
   - Confirm sprint created with ID
   - List issues assigned to sprint
   - Report: "Created Sprint X with Y points across Z issues (90% of velocity)"

## Error Handling
- **MCP disconnect:** Detect failed tool calls, instruct user to reconnect
- **Insufficient data:** If <3 completed sprints, use team's default capacity
- **Permission errors:** Provide specific Linear permission requirements

## Example Usage
**User:** "Plan next sprint based on our velocity"

**Skill executes:**
1. Validates Linear MCP connected ✓
2. Asks: "Which team?" → User: "Engineering"
3. Fetches last 3 sprints: 34, 38, 36 points completed
4. Calculates: avg 36 points, recommends 32 points (90%)
5. Fetches backlog: 15 issues prioritized
6. Recommends: Top 6 issues totaling 31 points
7. Creates "Sprint 24" with those 6 issues
8. Reports: "Sprint 24 created with 31 points (6 issues)"

**Result:** User saved ~15 minutes of manual planning work.
```

---

## Multi-MCP Coordination Pattern

**Use when:** Skill orchestrates multiple MCP servers to automate cross-tool workflows.

### Pattern Structure

```markdown
## Overview
Brief description of end-to-end workflow across [Tool A] → [Tool B] → [Tool C]

## MCP Servers Required
- [Server 1]: [Purpose in workflow]
- [Server 2]: [Purpose in workflow]
- [Server 3]: [Purpose in workflow]

## Workflow Phases

### Phase 1: [Source Tool]
[MCP calls to extract data from source]

### Phase 2: [Transformation]
[Any processing between source and target]

### Phase 3: [Target Tool]
[MCP calls to write data to target]

### Phase 4: [Notification/Completion]
[Optional: Notify stakeholders via Slack/email]

## Coordination Logic
[Decision points, conditional branching, data dependencies]

## Error Recovery
[What happens if Phase 2 fails? Can we resume? Rollback?]
```

### Example: Design Handoff Workflow

**Scenario:** Designer completes Figma mockups → Export to Google Drive → Create Linear tasks → Notify team in Slack

```markdown
## Overview
Automates design handoff by exporting Figma frames to Google Drive, creating Linear implementation tasks with design links, and notifying the team in Slack.

## MCP Servers Required
- **Figma MCP** (`mcp__figma`): Extract artboards, export images
- **Google Drive MCP** (`mcp__gdrive`): Upload files, get shareable links
- **Linear MCP** (`mcp__linear`): Create tasks with attachments
- **Slack MCP** (`mcp__slack`): Send channel notifications

## Workflow Phases

### Phase 1: Figma Extraction
```
# Get current Figma file
mcp__figma__get_file(file_id)

# List artboards marked "Ready for Dev"
artboards = mcp__figma__list_frames(file_id, filter="Ready for Dev")

# Export each artboard as PNG
for artboard in artboards:
  image_data = mcp__figma__export_frame(
    file_id,
    artboard.id,
    format="PNG",
    scale=2
  )
```

### Phase 2: Drive Upload
```
# Create folder: "[Project] Design Handoff - [Date]"
folder = mcp__gdrive__create_folder(
  name=f"{project_name} Design Handoff - {today}",
  parent_id=design_folder_id
)

# Upload each exported image
drive_links = []
for artboard, image_data in zip(artboards, images):
  file = mcp__gdrive__upload_file(
    name=f"{artboard.name}.png",
    data=image_data,
    parent_id=folder.id,
    mime_type="image/png"
  )

  # Get shareable link
  link = mcp__gdrive__create_share_link(file.id, role="viewer")
  drive_links.append((artboard.name, link))
```

### Phase 3: Linear Task Creation
```
# Create parent task
parent = mcp__linear__create_issue(
  title=f"Implement designs: {project_name}",
  description=f"Design folder: {folder.link}\n\nSub-tasks created for each screen.",
  team_id=team_id,
  project_id=project_id,
  labels=["design-handoff", "frontend"]
)

# Create sub-task for each design
for artboard_name, drive_link in drive_links:
  mcp__linear__create_issue(
    title=f"Implement: {artboard_name}",
    description=f"Design: {drive_link}\n\nImplement UI per Figma specs.",
    parent_id=parent.id,
    team_id=team_id,
    estimate=3  # Default 3 points, team can adjust
  )
```

### Phase 4: Slack Notification
```
mcp__slack__send_message(
  channel="#design-eng",
  message=f"""
🎨 Design Handoff Ready: {project_name}

**Designs:** {len(artboards)} screens exported
**Linear:** {parent.url}
**Drive:** {folder.link}

@frontend-team ready for implementation!
  """
)
```

## Coordination Logic

**Decision Points:**
1. **If no artboards marked "Ready for Dev":**
   - Abort with message: "No designs ready. Mark frames in Figma first."

2. **If Drive upload fails for some images:**
   - Continue with successful uploads
   - Note failed uploads in Linear task description
   - User can manually upload missing designs

3. **If Linear task creation fails:**
   - Still send Slack notification with Drive link
   - User can manually create tasks

4. **If Slack notification fails:**
   - Workflow still succeeded (Drive + Linear complete)
   - Log warning but don't block

**Data Dependencies:**
- Phase 2 needs Phase 1 image data
- Phase 3 needs Phase 2 Drive links
- Phase 4 needs Phase 3 task URLs
- **Sequential execution required** - can't parallelize

## Error Recovery

**Partial Failure Handling:**
- Each phase stores its outputs
- If Phase 3 fails, user has Drive folder from Phase 2
- Can resume from failed phase without re-running earlier phases

**Rollback Strategy:**
- **Don't automatically rollback** - partial progress is useful
- If user wants to abort:
  - Keep Drive folder (useful reference)
  - Delete Linear tasks if created
  - No Figma changes to undo

**Resume Capability:**
- If interrupted, ask user:
  - "I created Drive folder [link]. Continue to Linear tasks?"
  - Prevents duplicate work

## Example Usage

**User:** "Hand off the checkout flow designs to engineering"

**Skill executes:**
1. Finds 4 Figma artboards marked "Ready for Dev"
2. Exports as 2x PNG images
3. Creates Drive folder "Checkout Flow Handoff - 2026-02-21"
4. Uploads 4 images to folder
5. Creates Linear parent task + 4 sub-tasks
6. Sends Slack notification to #design-eng

**Result:** Designer saved ~30 minutes of manual handoff work. Engineering has organized tasks + designs ready.

**Error scenario:** Drive upload fails for 1 image
- Continues with 3 successful uploads
- Creates Linear tasks with note: "Image X failed upload - manually add to folder"
- User uploads 1 missing image, no big deal
```

---

## Error Handling Patterns

### Common MCP Errors

#### 1. MCP Disconnection

**Symptom:** Tool call returns `null` or "MCP server not found" error

**Detection:**
```markdown
Before executing workflow, validate MCP availability:

1. List available tools: Check if `mcp__[server]__*` tools exist
2. If not available:
   - Provide clear setup instructions
   - Link to MCP server documentation
   - Suggest user reconnect and retry

**Example check:**
"I need Linear MCP to run this skill. Please ensure:
1. Linear MCP server is connected
2. Restart Claude Code if just connected
3. Run this skill again"
```

**Recovery:** User must reconnect MCP server, skill cannot auto-fix

#### 2. Authentication Failure

**Symptom:** MCP tool call returns "401 Unauthorized" or "Invalid token"

**Detection:**
```markdown
MCP tool returns auth error → Skill detects error response

**Response:**
"Linear authentication failed. Please:
1. Check your Linear API token in MCP config
2. Verify token has required permissions: [list specific permissions]
3. Reconnect Linear MCP with updated token"
```

**Recovery:** User must fix auth credentials in MCP config

#### 3. Rate Limiting

**Symptom:** MCP tool returns "429 Too Many Requests" or "Rate limit exceeded"

**Detection:**
```markdown
MCP tool returns rate limit error

**Response:**
"Linear API rate limit reached. Options:
1. Wait [X minutes] and retry (recommended)
2. Reduce batch size (process fewer items)
3. Schedule for off-peak time if bulk operation"
```

**Recovery:**
- **Immediate:** Exponential backoff (wait 1s, 2s, 4s between retries)
- **User-facing:** Explain rate limit, suggest manual intervention if urgent

#### 4. Permission Errors

**Symptom:** MCP tool returns "403 Forbidden" or "Insufficient permissions"

**Detection:**
```markdown
MCP tool returns permission error

**Response:**
"Insufficient Linear permissions. This skill requires:
- Read access: Teams, Sprints, Issues
- Write access: Create Sprints, Update Issues

Please grant these permissions in Linear settings: [link]"
```

**Recovery:** User must update permissions in source tool (Linear, Figma, etc.)

#### 5. Data Not Found

**Symptom:** MCP tool returns empty result or "404 Not Found"

**Detection:**
```markdown
Expected data missing (e.g., no completed sprints for velocity calc)

**Response:**
"No completed sprints found for velocity calculation. Options:
1. Use team's default capacity (enter manually)
2. Create first sprint without velocity data
3. Wait until at least one sprint completes"
```

**Recovery:** Graceful degradation - offer alternative workflow

### Error Handling Template

```markdown
## Error Handling

### Prerequisites Validation
Before executing workflow:
- ✅ Check [MCP Server] is connected
- ✅ Validate required permissions
- ✅ Confirm data exists (e.g., historical records needed)

If prerequisites fail: **Abort with clear instructions** (don't attempt workflow)

### During Execution
For each MCP tool call:
1. **Detect error** - Check response for error codes
2. **Classify error** - Disconnect, auth, rate limit, permission, data
3. **Respond appropriately** - See patterns above
4. **Log context** - What was being attempted, what data was involved

### Partial Failure Strategy
[Skill-specific: Continue with degraded service? Abort? Rollback?]

### User Communication
Always explain:
- **What happened** - "Linear authentication failed"
- **Why it matters** - "Can't create sprint without auth"
- **What to do** - "Re-authorize Linear MCP: [steps]"
- **How to resume** - "Run skill again after fixing auth"
```

---

## Testing MCP-Dependent Skills

### Testing Approach

**Challenge:** MCP servers require external services (Linear, Figma, etc.) - can't easily mock

**Strategy:** Layered testing with real MCP connections

### Test Layers

#### Layer 1: Triggering Tests
**Goal:** Verify skill activates on correct user queries

**Approach:** Use `test-queries-template.txt`
- Test without MCP connection
- Focus on description matching

**Example:**
```
SHOULD_TRIGGER | Plan next sprint based on velocity
SHOULD_TRIGGER | Create Linear sprint with recommended scope
SHOULD_NOT_TRIGGER | Plan my vacation (not sprint planning)
```

#### Layer 2: MCP Validation Tests
**Goal:** Verify skill detects missing MCP and provides clear instructions

**Approach:**
1. Disconnect MCP server
2. Trigger skill
3. Verify skill provides setup instructions (not error crash)

**Example:**
```markdown
**Test:** Trigger with Linear MCP disconnected

**Expected response:**
"I need Linear MCP to run this skill. Please ensure:
1. Linear MCP server is connected: [setup link]
2. Restart Claude Code if just connected
3. Run this skill again"

**Fail criteria:**
- Generic error message
- Skill attempts to run anyway (crashes)
- No setup instructions provided
```

#### Layer 3: Integration Tests (Real MCP)
**Goal:** Verify skill works end-to-end with real MCP server

**Approach:**
1. Set up test environment (test Linear workspace, test Drive folder, etc.)
2. Run skill with test data
3. Verify expected outcomes in external tools
4. Clean up test data

**Example:**
```markdown
**Test: Linear Sprint Planning - Happy Path**

**Setup:**
- Linear test workspace: "Test Team"
- 3 completed sprints: 30, 32, 28 points
- 10 backlog issues: mix of 1, 2, 3, 5 point estimates

**Trigger:** "Plan next sprint for Test Team"

**Expected outcomes:**
1. Skill calculates velocity: avg 30 points, recommends 27 points
2. Creates "Sprint [N]" in Linear
3. Assigns ~27 points of backlog issues to sprint
4. Reports summary to user

**Verification:**
- Check Linear: Sprint created with correct dates
- Check Linear: Issues assigned to sprint
- Check totals: Sum of assigned issue points ≈ 27

**Cleanup:**
- Delete test sprint
- Unassign test issues
```

#### Layer 4: Error Scenario Tests
**Goal:** Verify graceful error handling

**Approach:** Intentionally cause errors and verify skill responds correctly

**Example:**
```markdown
**Test: Rate Limit Handling**

**Setup:**
- Trigger skill 10x rapidly to hit rate limit

**Expected response:**
- Skill detects "429 Too Many Requests"
- Provides clear message: "Linear rate limit reached. Wait 5 minutes."
- Doesn't crash or retry infinitely

**Test: Missing Data**

**Setup:**
- Linear workspace with 0 completed sprints

**Expected response:**
- Skill detects insufficient historical data
- Offers alternative: "No completed sprints. Enter capacity manually?"
- Doesn't crash trying to calculate velocity
```

### Test Checklist

Before deploying MCP-dependent skill:
- [ ] Triggering tests pass (90%+ accuracy)
- [ ] MCP disconnected scenario handled gracefully
- [ ] Integration test passes with real MCP (happy path)
- [ ] At least 3 error scenarios tested (auth, rate limit, missing data)
- [ ] Cleanup procedures documented (don't leave test data)

---

## Performance Optimization

### Batching MCP Calls

**Problem:** Multiple sequential API calls = slow execution

**Solution:** Batch reads when possible

**Example:**
```markdown
❌ **Slow (N+1 query problem):**
for issue_id in issue_ids:
  issue = mcp__linear__get_issue(issue_id)  # 10 separate API calls
  process(issue)

✅ **Fast (batched read):**
issues = mcp__linear__list_issues(ids=issue_ids)  # 1 API call
for issue in issues:
  process(issue)
```

### Parallel MCP Calls (When Safe)

**When safe:** Multiple independent reads (no data dependencies)

**Example:**
```markdown
✅ **Parallel (independent reads):**
# Fetch sprints and backlog simultaneously
sprints = mcp__linear__list_sprints(team_id, status="completed")
backlog = mcp__linear__list_issues(team_id, state="backlog")
# Both calls are independent, can run in parallel

❌ **Must be sequential (data dependency):**
# Must create sprint first, then assign issues to it
sprint = mcp__linear__create_sprint(...)  # Need sprint.id first
for issue in issues:
  mcp__linear__update_issue(issue.id, sprint_id=sprint.id)  # Depends on sprint.id
```

### Caching Expensive Calls

**When appropriate:** Data that doesn't change frequently

**Example:**
```markdown
✅ **Cache team list:**
# Teams rarely change, cache for session
teams = mcp__linear__list_teams()  # Call once
# Reuse `teams` for multiple operations in same skill execution

❌ **Don't cache volatile data:**
# Backlog changes frequently, always fetch fresh
backlog = mcp__linear__list_issues(state="backlog")  # Always fresh
```

### Performance Checklist

- [ ] Batch reads when fetching multiple items
- [ ] Parallelize independent MCP calls
- [ ] Cache static/slow-changing data (teams, projects)
- [ ] Always fetch fresh volatile data (issues, messages)
- [ ] Limit results (don't fetch 1000 issues if you need 10)

---

## Summary

### Key Takeaways

1. **Category 3 = MCP + Intelligence** - Add workflow automation and domain expertise on top of raw MCP tools
2. **Single MCP Pattern** - Validate, gather context, execute, verify
3. **Multi-MCP Pattern** - Phases with coordination logic and partial failure handling
4. **Error Handling** - Detect, classify, respond clearly, enable user recovery
5. **Testing** - Layer tests from triggering → validation → integration → errors
6. **Performance** - Batch, parallelize, cache appropriately

### Quick Reference

**Building a new MCP skill? Follow this sequence:**
1. Define use case and success criteria
2. Choose pattern (Single MCP or Multi-MCP)
3. Design workflow phases
4. Add error handling for common scenarios
5. Write integration tests
6. Optimize performance (batch/parallel/cache)
7. Deploy and measure effectiveness

**Referenced by:**
- `SKILL.md` - Step 2 (Choose pattern), Step 5 (Implement), Step 6 (MCP integration)
- `success-metrics-framework.md` - MCP-specific metrics
- `troubleshooting-guide.md` - MCP connection issues
