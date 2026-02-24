# ClickUp Skill Success Metrics

## Triggering Accuracy

**Target:** >90% correct triggering

**Test Queries:**

| Query | Should Trigger? | Why |
|-------|----------------|-----|
| "Show me my ClickUp tasks" | ✅ Yes | Explicit "ClickUp" + "tasks" |
| "Create a task in ClickUp for deployment" | ✅ Yes | "ClickUp" + "create task" |
| "List tasks assigned to me" | ✅ Yes | "tasks" + "assigned" (task management context) |
| "What's my task status?" | ✅ Yes | "task" + "status" |
| "Check my calendar" | ❌ No | Calendar, not task management |
| "Send me a reminder" | ❌ No | Reminder system, not task management |
| "Create a document" | ❌ No | Document creation, not tasks |
| "Check status" | ⚠️ Ambiguous | Clarify: task status? server status? |

**Measurement:**
```bash
# Run test queries through Claude
# Count: (correct triggers) / (total queries) * 100
# Target: >90%
```

---

## Efficiency Metrics

### Token Reduction

**Without skill:**
- Claude explores ClickUp API docs (6K tokens)
- Tries authentication patterns (3K tokens)
- Learns task hierarchy (2K tokens)
- Iterates on query patterns (2K tokens)
- **Total:** ~13K tokens

**With skill:**
- Loads SKILL.md overview (~2K tokens)
- References loaded on-demand (if needed)
- Direct API usage with examples
- **Total:** ~3K tokens (with references)

**Target:** >70% token reduction (13K → <4K)

---

### API Call Reduction

**Without skill:**
- 4-6 calls exploring workspace hierarchy
- 3-4 calls testing authentication
- 2-3 calls learning task filters
- 1-2 calls handling errors
- **Total:** 10-15 failed/exploratory calls before success

**With skill:**
- 1 call: Direct query with correct parameters
- **Total:** 1 call (success on first attempt)

**Target:** >90% reduction in exploratory API calls

---

## Quality Metrics

### Task Completion Rate

**Target:** 100% for supported operations

**Scenarios:**
1. List my tasks → Success rate: 100%
2. Find tasks by assignee → Success rate: 100%
3. Get task details → Success rate: 100%
4. Create task (with approval) → Success rate: 100%
5. Handle rate limit gracefully → Success rate: 100%

---

### Error Handling

**Target:** 0 unhandled errors for common scenarios

**Test scenarios:**
- Missing API key → Clear error message ✅
- Invalid credentials → "Authentication failed" ✅
- No tasks found → Empty list (not error) ✅
- Rate limit hit → Graceful retry suggestion ✅
- Resource not found (404) → Clear "not found" message ✅

---

## Baseline Comparison

### Before Skill (Raw API Usage)

```python
# Developer tries to use ClickUp API without skill
# Typical conversation:

User: "Show me my open tasks"
Claude: "I'll help. Let me explore the ClickUp API..."
# → 20 messages, 15K tokens, 12 API calls, 4 errors, 7 minutes

Result: Eventually works, but inefficient
```

### With Skill

```python
# Developer uses skill

User: "Show me my open tasks"
Claude: [skill triggers] "I'll use bramclaw-clickup skill"
# Uses scripts/clickup_agent.py or direct API calls with examples
# → 4 messages, 3K tokens, 1 API call, 0 errors, 45 seconds

Result: Works immediately
```

---

## Measurement Commands

### Measure Triggering Accuracy

```bash
# Create test query file
cat > test-queries.txt <<EOF
Show me my ClickUp tasks
Create a task for deployment
List tasks assigned to me
Check my calendar
Send me a reminder
EOF

# Run through Claude, track triggers
# Calculate: correct / total
```

---

### Measure Token Usage

```bash
# Without skill:
# Start new Claude session, ask "List my ClickUp tasks" without loading skill
# Track token usage in conversation

# With skill:
# Load skill, ask same question
# Compare token counts
```

---

### Measure API Efficiency

```bash
# Enable API logging
export CLICKUP_LOG_LEVEL=DEBUG

# Run query, count API calls
python3 scripts/clickup_agent.py workspaces

# Expected: 1 API call (get_workspaces)
```

---

## Security Metrics

### Write Operation Approval Rate

**Target:** 100% of write operations require approval

**Test:**
- Agent attempts to create task → Should ask for approval first ✅
- Agent attempts to update task → Should ask for approval first ✅
- Agent attempts to delete task → Should ALWAYS ask for approval ✅

**Measurement:**
```
(write operations with approval) / (total write operations) * 100
Target: 100%
```

---

### Audit Log Completeness

**Target:** 100% of write operations logged

**Test:**
- Create task → Logged ✅
- Update task → Logged ✅
- Delete task → Logged ✅
- Error occurred → Logged ✅

**Measurement:**
```bash
# Check audit log for write operations
grep "CREATE_TASK\|UPDATE_TASK\|DELETE_TASK" /var/log/bramclaw/clickup-audit.log | wc -l

# Should match number of actual write operations
```

---

## Continuous Improvement

**Monthly review:**
1. Check triggering accuracy with real queries
2. Measure average token usage per task
3. Track failed API calls (should approach 0%)
4. Review approval workflow effectiveness
5. Audit log completeness check
6. Update skill based on common failure patterns

---

## Success Criteria for v2.0

**Performance:**
- Triggering accuracy: >95% (currently >90%)
- Token reduction: >80% (currently >70%)
- Zero failed API calls for valid queries
- Sub-5 second response time for common queries

**Security:**
- 100% write operation approval rate
- 100% audit log completeness
- Zero credential leaks
- Zero unauthorized write operations

**Reliability:**
- 99.9% uptime for read operations
- Graceful degradation on rate limits
- Clear error messages for all failure modes

---

## Dashboard

**Ideal monitoring dashboard should show:**

**Performance:**
- API calls per hour
- Average response time
- Token usage trend
- Cache hit rate

**Security:**
- Write operations (with/without approval)
- Failed authentication attempts
- Audit log completeness %

**Errors:**
- Rate limit hits
- 404/500 errors
- Failed operations

**Usage:**
- Most common operations
- Peak usage times
- Top users/agents

---

## Resources

- **ClickUp API Status:** https://status.clickup.com/
- **API Metrics:** https://clickup.com/api/developer-portal/analytics/
- **Rate Limits:** https://clickup.com/api/developer-portal/rate-limits/
