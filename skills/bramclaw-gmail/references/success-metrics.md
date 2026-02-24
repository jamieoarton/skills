# Gmail Skill Success Metrics

## Triggering Accuracy

**Target:** >90% correct triggering

**Test Queries:**

| Query | Should Trigger? | Why |
|-------|----------------|-----|
| "Show me my recent Gmail" | ✅ Yes | Explicit "Gmail" |
| "Check inbox for unread messages" | ✅ Yes | "inbox", "messages" |
| "Search emails from alice@example.com" | ✅ Yes | "emails", "search" |
| "Get emails with invoices" | ✅ Yes | "emails" |
| "Send an email to Bob" | ❌ No | Write operation (not supported) |
| "Create email draft" | ❌ No | Write operation |
| "Check my calendar" | ❌ No | Different service |
| "Search for project notes" | ❌ No | Ambiguous (files? docs?) |

**Measurement:**
```bash
# Run test queries through Claude
# Count: (correct triggers) / (total queries) * 100
# Target: >90%
```

## Efficiency Metrics

### Token Reduction

**Without skill:**
- Claude explores API docs (5K tokens)
- Tries authentication patterns (3K tokens)
- Iterates on query syntax (2K tokens)
- **Total:** ~10K tokens

**With skill:**
- Loads SKILL.md (150 lines, ~1.5K tokens)
- References loaded on-demand (if needed)
- Direct API usage
- **Total:** ~2K tokens (with references)

**Target:** >70% token reduction (10K → <3K)

### API Call Reduction

**Without skill:**
- 3-5 calls exploring auth methods
- 2-3 calls testing query syntax
- 1-2 calls handling errors
- **Total:** 6-10 failed/exploratory calls before success

**With skill:**
- 1 call: Direct query with correct syntax
- **Total:** 1 call (success on first attempt)

**Target:** >80% reduction in exploratory API calls

## Quality Metrics

### Task Completion Rate

**Target:** 100% for supported operations

**Scenarios:**
1. List recent emails → Success rate: 100%
2. Search with filters → Success rate: 100%
3. Get specific message → Success rate: 100%
4. Handle no results gracefully → Success rate: 100%

### Error Handling

**Target:** 0 unhandled errors for common scenarios

**Test scenarios:**
- Missing env vars → Clear error message ✅
- Invalid credentials → "Authentication failed" ✅
- No results found → Empty list (not error) ✅
- Rate limit hit → Graceful retry suggestion ✅

## Baseline Comparison

### Before Skill (Raw API Usage)

```python
# Developer tries to use Gmail API without skill
# Typical conversation:

User: "Get my recent emails"
Claude: "I'll help. Let me explore the Gmail API..."
# → 15 messages, 12K tokens, 8 API calls, 3 errors, 5 minutes

Result: Eventually works, but inefficient
```

### With Skill

```python
# Developer uses skill

User: "Get my recent emails"
Claude: [skill triggers] "I'll use bramclaw-gmail skill"
# Uses scripts/gmail_agent.py subjects 5
# → 3 messages, 2K tokens, 1 API call, 0 errors, 30 seconds

Result: Works immediately
```

## Measurement Commands

### Measure Triggering Accuracy

```bash
# Create test query file
cat > test-queries.txt <<EOF
Show me recent Gmail subjects
Check inbox for unread messages
Search emails from alice@example.com
Send an email to Bob
Check my calendar
EOF

# Run through Claude, track triggers
# Calculate: correct / total
```

### Measure Token Usage

```bash
# Without skill:
# Start new Claude session, ask "Get my recent emails" without loading skill
# Track token usage in conversation

# With skill:
# Load skill, ask same question
# Compare token counts
```

### Measure API Efficiency

```bash
# Enable API logging
export GOOGLE_API_LOG_LEVEL=DEBUG

# Run query, count API calls
python3 scripts/gmail_agent.py subjects 10

# Expected: 1 API call (messages.list)
```

## Continuous Improvement

**Monthly review:**
1. Check triggering accuracy with real queries
2. Measure average token usage per task
3. Track failed API calls (should be 0%)
4. Update skill based on common failure patterns

**Success criteria for v2.0:**
- Triggering accuracy: >95% (currently >90%)
- Token reduction: >80% (currently >70%)
- Zero failed API calls for valid queries
- Sub-10 second response time for common queries
