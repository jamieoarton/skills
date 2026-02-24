# Troubleshooting Guide

**Purpose:** Diagnose and fix common skill development and deployment issues.

**Target audience:** Skill builders encountering errors during creation, testing, or deployment.

---

## Table of Contents

1. [Upload Errors](#upload-errors)
2. [Triggering Issues](#triggering-issues)
3. [MCP Connection Problems](#mcp-connection-problems)
4. [Instructions Not Followed](#instructions-not-followed)
5. [Large Context Issues](#large-context-issues)
6. [Performance Problems](#performance-problems)
7. [Debugging Workflow](#debugging-workflow)

---

## Upload Errors

### Error: "Invalid YAML frontmatter"

**Symptom:** Skill validation or upload fails with YAML parsing error

**Causes:**
- Missing opening `---` or closing `---`
- Indentation errors (YAML requires 2-space indents)
- Special characters not escaped
- Missing required fields

**Solution:**

```yaml
# ❌ Bad YAML
---
name: my-skill
description This is wrong
---

# ✅ Good YAML
---
name: my-skill
description: This is correct
---
```

**Debugging steps:**
1. Check YAML syntax with online validator (yamllint.com)
2. Ensure exact 2-space indentation (no tabs)
3. Quote strings with special characters: `description: "Skill with: colons"`
4. Verify all required fields present: `name`, `description`

**Prevention:**
- Use template from skill-creator
- Copy working YAML from existing skills
- Use editor with YAML validation (VSCode with YAML extension)

---

### Error: "Validation failed: Description too long"

**Symptom:** `quick_validate.py` fails with "Description exceeds 1024 characters"

**Cause:** YAML `description` field > 1024 character limit

**Solution:**

```yaml
# ❌ Too long (1100 chars)
---
description: This skill automates sprint planning by analyzing historical velocity data from the last three completed sprints in Linear, calculating average points completed per sprint with a 10% safety buffer to account for variability, fetching all backlog items sorted by priority, intelligently recommending which items fit within the calculated capacity, creating a new sprint with appropriate dates and goals, automatically assigning the recommended issues to the newly created sprint, and providing a comprehensive summary report to the user showing exactly what was planned and why...
---

# ✅ Concise (200 chars)
---
description: Automate sprint planning by analyzing historical velocity in Linear, recommending backlog scope, and creating the next sprint with optimal capacity allocation.
---
```

**Debugging steps:**
1. Count characters: `echo "description text" | wc -c`
2. Identify redundant words
3. Remove implementation details (save for workflow section)
4. Focus on what/who/why, not how

**Formula for concise descriptions:**
`[Action verb] + [domain/tool] + [key benefit]`

**Prevention:**
- Draft description, then cut 30%
- Test with `quick_validate.py` before uploading
- Use trigger keywords, not full sentences

---

### Error: "File not found: SKILL.md"

**Symptom:** Packaging script can't find skill file

**Causes:**
- Incorrect filename (must be exactly `SKILL.md`, all caps)
- Skill file in wrong location
- Incorrect path provided to package script

**Solution:**

```bash
# ❌ Wrong filename
skill-directory/
├── skill.md  # Wrong! Must be SKILL.md
└── readme.md

# ✅ Correct filename
skill-directory/
├── SKILL.md  # Correct!
└── README.md # Optional supporting files can use any case
```

**Debugging steps:**
1. Check exact filename: `ls skill-directory/`
2. Verify case-sensitive: `ls | grep SKILL`
3. Check path is correct: `ls /full/path/to/skill-directory/SKILL.md`

**Prevention:**
- Use `init_skill.py` from skill-creator (creates correct structure)
- Never rename SKILL.md to something else
- Check with `ls` before packaging

---

### Error: "Skill package is empty"

**Symptom:** .skill file is created but has no content (0 bytes or very small)

**Causes:**
- SKILL.md is empty
- Packaging script permission error
- Disk space issue

**Solution:**

1. Check SKILL.md has content:
   ```bash
   wc -l skill-directory/SKILL.md
   # Should show line count > 0
   ```

2. Check disk space:
   ```bash
   df -h
   # Ensure available space
   ```

3. Check file permissions:
   ```bash
   ls -la skill-directory/
   # SKILL.md should be readable
   ```

4. Re-run packaging with verbose output

**Prevention:**
- Save SKILL.md before packaging
- Verify content with text editor before running package script

---

## Triggering Issues

### Problem: Skill triggers when it shouldn't (False Positives)

**Symptom:** Skill activates on unrelated user queries

**Diagnosis:**

1. Collect false positive queries
2. Identify pattern:
   - Too generic? ("help me with X" → skill triggers on ALL help requests)
   - Missing exclusions? (Skill for "create" but triggers on "delete")
   - Overlaps with other skill?

**Solution:**

```yaml
# ❌ Too generic
description: Helps with project management tasks in Linear

# ✅ Specific with exclusions
description: Automate sprint planning in Linear by calculating velocity and creating sprints. Use for planning new sprints, NOT for reporting, updating existing sprints, or managing individual issues.
```

**Techniques:**
- Add negative examples: "NOT for [X]"
- Specify exact use case: "Use when planning NEW sprints"
- Include domain keywords: "sprint planning" not just "planning"
- Add qualifying context: "based on historical velocity"

**Testing:**
1. Add false positive to SHOULD_NOT_TRIGGER list
2. Re-test triggering accuracy
3. Iterate description until false positive rate < 10%

---

### Problem: Skill doesn't trigger when it should (False Negatives)

**Symptom:** Relevant queries don't activate the skill

**Diagnosis:**

1. Collect missed queries
2. Identify pattern:
   - Too specific? (Only triggers on exact phrasing)
   - Missing synonyms? ("create" but users say "make" or "set up")
   - Missing implicit forms? ("I need a sprint" doesn't mention "planning")

**Solution:**

```yaml
# ❌ Too narrow
description: Use when user requests sprint velocity calculation

# ✅ Broader, includes variations
description: Automate sprint planning by analyzing velocity, recommending scope, creating sprints. Triggers on requests to plan sprints, calculate capacity, set up iterations, or create new sprints based on team velocity.
```

**Techniques:**
- Include common synonyms: "create/make/set up/generate"
- Add implicit phrasings: "I need a sprint" = "plan a sprint"
- Include question forms: "What should we plan?" = "Plan sprint"
- Add domain terminology variations: "sprint/iteration/cycle"

**Testing:**
1. Add missed query to SHOULD_TRIGGER list
2. Update description with synonym/variation
3. Re-test until triggering rate ≥ 90%

---

### Problem: Triggering accuracy degraded after update

**Symptom:** Skill used to trigger correctly, now misses queries or triggers incorrectly

**Diagnosis:**

1. Compare old vs. new description
2. Identify what changed
3. Check if change was intentional

**Solution:**

1. Review git diff:
   ```bash
   git diff HEAD~1 skill-directory/SKILL.md
   ```

2. Identify breaking change

3. Options:
   - Revert to previous description (if change was accidental)
   - Adjust new description to maintain triggering behavior
   - Accept trade-off if intentional (e.g., reducing false positives might increase false negatives)

**Prevention:**
- Always re-run test query suite after changing description
- Track triggering accuracy over versions in changelog
- Use version control (git) to track description changes

---

## MCP Connection Problems

### Problem: "MCP server not found" error

**Symptom:** Skill reports MCP server is not connected during execution

**Causes:**
- MCP server not installed
- MCP server not configured in Claude settings
- MCP server name mismatch in skill vs. actual server name

**Solution:**

1. **Check MCP server is installed:**
   - Open Claude Code settings
   - Go to MCP Servers tab
   - Verify server appears in list

2. **Verify server name matches:**
   ```markdown
   # In your skill:
   mcp__linear__list_teams

   # Must match actual server name in settings:
   Server name: "linear" → Tools: mcp__linear__*
   ```

3. **Restart Claude Code:**
   - Some MCP changes require restart
   - Quit and reopen Claude Code

4. **Check server is running:**
   - Some MCP servers are external processes
   - Verify server process is running: `ps aux | grep mcp`

**Prevention:**
- Document exact MCP server name in skill Prerequisites
- Test skill immediately after connecting MCP (before distributing)
- Include MCP connection check in skill workflow:
  ```markdown
  1. Validate [MCP name] connection
     - Check `mcp__[name]__[tool]` is available
     - If not: Provide setup instructions
  ```

---

### Problem: MCP calls failing with authentication errors

**Symptom:** Skill executes but MCP tool calls return "401 Unauthorized" or "Invalid token"

**Causes:**
- MCP server auth token expired
- MCP server auth credentials incorrect
- Insufficient permissions for MCP operations

**Solution:**

1. **Check auth credentials:**
   - Open MCP server settings
   - Verify API token/key is current
   - Test token manually (e.g., curl API endpoint)

2. **Re-authenticate:**
   - Disconnect MCP server
   - Reconnect with fresh credentials
   - Test skill again

3. **Verify permissions:**
   - Check MCP server has required permissions (read/write)
   - Example: Linear token needs "read:issues", "write:sprints"

**Error handling in skill:**
```markdown
## Error Handling

**Auth failure:**
"Linear authentication failed. Please:
1. Check your Linear API token in MCP config
2. Verify token has required permissions: read:sprints, write:sprints, read:issues, write:issues
3. Reconnect Linear MCP with updated token
4. Run this skill again"
```

**Prevention:**
- Document required permissions in Prerequisites
- Include auth failure handling in skill error scenarios
- Test with expired token to verify error message is helpful

---

### Problem: MCP calls timing out

**Symptom:** Skill hangs or returns timeout error during MCP operation

**Causes:**
- MCP server is slow/overloaded
- Network connectivity issues
- Large data fetch (thousands of items)

**Solution:**

1. **Add timeout handling:**
   ```markdown
   If MCP call times out:
   - Wait 10 seconds
   - Retry once
   - If still fails: Suggest manual operation
   ```

2. **Optimize queries:**
   - Use `limit` parameter to fetch fewer items
   - Batch reads instead of individual calls
   - Cache static data (teams, projects)

3. **Increase timeout:**
   - Some MCP servers allow timeout configuration
   - Check MCP server docs

**Prevention:**
- Test skill with large datasets
- Add pagination for big data fetches
- Provide user feedback: "Fetching large dataset, this may take 30 seconds..."

---

## Instructions Not Followed

### Problem: Claude doesn't follow skill instructions exactly

**Symptom:** Skill provides workflow, but Claude skips steps or deviates

**Causes:**
- Instructions too vague ("analyze data" - how?)
- Instructions too long (Claude summarizes instead of following)
- Instructions conflict with Claude's default behavior

**Solution:**

**Make instructions concrete and step-by-step:**

```markdown
# ❌ Vague
Analyze velocity and create sprint

# ✅ Concrete steps
1. Call `mcp__linear__list_sprints(status="completed", limit=3)`
2. Calculate: avg_points = sum(sprint.points) / 3
3. Calculate: capacity = avg_points * 0.9
4. Call `mcp__linear__list_issues(state="backlog")`
5. Filter: issues where cumsum(points) <= capacity
6. Call `mcp__linear__create_sprint(name, dates)`
7. For each selected issue:
   Call `mcp__linear__update_issue(issue_id, sprint_id)`
```

**Use numbered steps, explicit tool calls, clear calculations**

**Prevention:**
- Test skill execution 5-10 times
- Note where Claude deviates
- Make those steps more explicit
- Add "IMPORTANT:" prefix for critical steps

---

### Problem: Skill skips error handling

**Symptom:** When MCP fails, skill crashes instead of handling gracefully

**Causes:**
- Error handling instructions buried in text
- Error handling not explicit enough

**Solution:**

**Create dedicated Error Handling section:**

```markdown
## Error Handling

**CRITICAL: Check for these errors before proceeding**

1. **MCP Connection:**
   Before any Linear calls, verify `mcp__linear__list_teams` exists
   If not: STOP and instruct user to connect Linear MCP

2. **Auth Failure:**
   If any call returns 401: STOP and provide re-auth instructions

3. **Missing Data:**
   If <3 completed sprints: STOP and ask user for manual capacity

4. **Rate Limit:**
   If call returns 429: WAIT 60 seconds and retry ONCE
```

**Use structured format, caps for emphasis, explicit checks**

**Prevention:**
- Test each error scenario individually
- Verify skill provides helpful error message (not generic failure)
- Make error checks the first thing in each workflow phase

---

## Large Context Issues

### Problem: Skill truncated or incomplete

**Symptom:** SKILL.md is long, but Claude doesn't see entire skill content

**Causes:**
- Skill > context window limit
- Too much reference material loaded
- Competing with user's large conversation history

**Solution:**

1. **Reduce skill size:**
   - Move detailed examples to separate reference files
   - Link to reference docs instead of including inline
   - Use "Deep dive:" pattern to point to references/

2. **Optimize structure:**
   ```markdown
   ## Quick Reference
   [Concise tables, bullet points - always visible]

   ## Detailed Guide
   **Deep dive**: See `references/implementation-patterns.md` for:
   - [Specific topics...]
   ```

3. **Test with minimal conversation:**
   - Fresh chat with only skill trigger
   - Verify all sections are followed

**Prevention:**
- Keep SKILL.md < 500 lines (aim for 300-400)
- Use references/ for deep content (can be 1000+ lines)
- Test skill in fresh conversation (no competing context)

---

### Problem: Skill conflicts with conversation history

**Symptom:** Skill provides instructions, but Claude follows previous conversation instead

**Causes:**
- User gave conflicting instructions before skill triggered
- Conversation history is very long (10k+ tokens)
- Previous error in conversation confuses skill execution

**Solution:**

1. **Strong skill introduction:**
   ```markdown
   # [Skill Name]

   **IMPORTANT: This skill provides a complete workflow. Follow these steps exactly, even if previous conversation suggests otherwise.**
   ```

2. **Explicit override:**
   ```markdown
   ## Workflow

   **Ignore previous conversation context. Start fresh with this workflow:**
   1. [Step 1]
   2. [Step 2]
   ```

3. **User workaround:**
   - Start fresh conversation for skill execution
   - Or: User says "forget previous context, use skill"

**Prevention:**
- Test skill in both fresh and long conversations
- Add "Start fresh" instruction if necessary
- Consider skill complexity (simpler = less context conflict)

---

## Performance Problems

### Problem: Skill is slow to execute

**Symptom:** Skill takes >2 minutes to complete workflow

**Diagnosis:**

1. Time each phase:
   - MCP calls: How long?
   - Calculations: How long?
   - Response generation: How long?

2. Identify bottleneck

**Solution based on bottleneck:**

**If MCP calls are slow:**
- Batch API calls (fetch many items in one call vs. loop)
- Use pagination wisely (don't fetch 10k items if you need 10)
- Cache static data (teams, projects)

**If calculations are slow:**
- Simplify algorithm
- Move complex calculations to external script (call via tool)

**If response generation is slow:**
- Reduce output verbosity
- Use tables instead of paragraphs
- Summarize instead of listing all items

**Prevention:**
- Measure baseline execution time
- Set performance target (e.g., <60s)
- Test with realistic data volumes
- Optimize before distributing

---

## Debugging Workflow

### When You're Stuck

**Follow this systematic process:**

1. **Isolate the problem**
   - Is it triggering? → Use test query suite
   - Is it MCP? → Test MCP connection separately
   - Is it instructions? → Read skill output carefully
   - Is it validation? → Run `quick_validate.py`

2. **Reproduce consistently**
   - Can you make it fail every time?
   - Or is it intermittent (harder to fix)?

3. **Check the basics**
   - YAML formatting valid?
   - SKILL.md filename correct?
   - MCP server connected?
   - Recent changes broke it?

4. **Narrow down the cause**
   - What changed since it last worked?
   - Does it work in fresh conversation?
   - Does it work with simpler query?

5. **Test the fix**
   - Make one change at a time
   - Re-test after each change
   - Verify fix doesn't break something else

6. **Document the solution**
   - Add to troubleshooting guide (yours or this one)
   - Update tests to catch regression
   - Share in community if others might hit it

---

### Getting Help

**When self-debugging doesn't work:**

1. **Gather information:**
   - Exact error message (screenshot or copy-paste)
   - SKILL.md frontmatter (sanitize sensitive info)
   - Steps to reproduce
   - What you've already tried

2. **Ask in right place:**
   - Claude Code Discord (general issues)
   - MCP server GitHub Issues (MCP-specific)
   - skill-creator skill (interactive debugging)

3. **Provide context:**
   - "When I X, Y happens. Expected: Z."
   - Include skill version, Claude version, OS
   - Share minimal reproducible example

4. **Follow up:**
   - Mark solution if found
   - Share workaround for others
   - Contribute fix back if applicable

---

## Quick Reference

### Most Common Issues

| Issue | Quick Fix |
|-------|-----------|
| "Invalid YAML" | Check indentation, quotes, closing `---` |
| "Description too long" | Cut to <1024 chars, remove implementation details |
| "File not found" | Rename to `SKILL.md` (all caps) |
| Skill doesn't trigger | Add trigger keywords/synonyms to description |
| Skill triggers wrongly | Add exclusions: "NOT for [X]" |
| "MCP not found" | Check server name, restart Claude Code |
| MCP auth error | Refresh token in MCP settings |
| Instructions skipped | Make steps numbered, explicit, concrete |
| Skill too slow | Batch MCP calls, reduce data fetched |
| Context truncated | Move details to references/, keep SKILL.md <500 lines |

### Debugging Checklist

When skill isn't working:
- [ ] Run `quick_validate.py` (catches YAML/structure issues)
- [ ] Test in fresh conversation (eliminates context conflicts)
- [ ] Check MCP connection if Category 3 (separate from skill issue)
- [ ] Review recent git changes (identify what broke)
- [ ] Test with simplest possible query (isolate triggering vs. execution)
- [ ] Read actual error message carefully (don't assume)
- [ ] Try one fix at a time (don't change multiple things)

---

**Referenced by:**
- `SKILL.md` - Troubleshooting section
- `distribution-deployment-guide.md` - Pre-distribution validation
- `mcp-integration-patterns.md` - MCP error handling
