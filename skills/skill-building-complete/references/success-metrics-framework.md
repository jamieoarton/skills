# Success Metrics Framework

**Purpose:** Define how to measure skill effectiveness and decide when to iterate vs. accept current performance.

**Target audience:** Skill builders who need to validate their skills are working as intended.

---

## Table of Contents

1. [Why Metrics Matter](#why-metrics-matter)
2. [Quantitative Metrics](#quantitative-metrics)
3. [Qualitative Metrics](#qualitative-metrics)
4. [Baseline Comparison Methodology](#baseline-comparison-methodology)
5. [When to Iterate vs. Accept](#when-to-iterate-vs-accept)
6. [Measurement Workflow](#measurement-workflow)

---

## Why Metrics Matter

### The Problem

Without measurement, you can't answer:
- **Is this skill actually working?** (Did I build what I intended?)
- **Is this skill providing value?** (Are users better off with it?)
- **Should I invest more time improving it?** (Is iteration worth the effort?)

### The Solution

Define success criteria BEFORE building, measure AFTER deploying, iterate based on data.

### Skill Success Formula

```
Skill Value = (Time Saved × Frequency) - (Development Time + Maintenance Time)
```

**Components:**
- **Time Saved:** How much faster is the task with the skill vs. manual?
- **Frequency:** How often is the skill used?
- **Development Time:** How long did it take to build?
- **Maintenance Time:** How much ongoing effort to keep working?

**Positive value = worthwhile skill. Negative value = reconsider or simplify.**

---

## Quantitative Metrics

### 1. Triggering Accuracy

**Definition:** Percentage of relevant user queries that correctly activate the skill.

**Target:** ≥90% accuracy

**How to measure:**
1. Create test query suite using `test-queries-template.txt`
2. Run each query through Claude
3. Count: (Correct triggers + Correct skips) / Total queries
4. Calculate: Accuracy = (Correct / Total) × 100%

**Example:**
```
Test suite: 24 queries (12 SHOULD_TRIGGER, 12 SHOULD_NOT_TRIGGER)
Results:
- 11/12 SHOULD_TRIGGER correctly triggered (91.7%)
- 11/12 SHOULD_NOT_TRIGGER correctly skipped (91.7%)
- Overall: 22/24 = 91.7% ✅ Meets 90% target
```

**When to iterate:**
- < 80%: Critical issue, must fix description
- 80-89%: Should improve, description too broad or narrow
- ≥90%: Acceptable, monitor for edge cases
- ≥95%: Excellent, no action needed

### 2. API/Tool Call Efficiency

**Definition:** Number of API calls or tool invocations required to complete the workflow.

**Target:** Minimize calls while maintaining functionality

**How to measure:**
1. Execute skill workflow
2. Count total API/MCP calls made
3. Compare to theoretical minimum (if you designed perfectly)
4. Calculate: Efficiency = (Theoretical minimum / Actual calls) × 100%

**Example (Linear Sprint Planning):**
```
Theoretical minimum:
- 1 call: Fetch last 3 sprints
- 1 call: Fetch backlog items
- 1 call: Create sprint
- N calls: Assign N issues to sprint
Total minimum: 3 + N calls

Actual implementation:
- 1 call: Fetch sprints ✅
- 1 call: Fetch backlog ✅
- 1 call: Create sprint ✅
- 6 calls: Assign 6 issues individually (could batch?)
Total actual: 9 calls

Efficiency: (9 theoretical / 9 actual) = 100% ✅ Optimal

If we had fetched sprints one-by-one:
- 3 calls: Fetch each sprint individually ❌
- Efficiency: (3 / 3) = 33% ⚠️ Needs optimization
```

**When to iterate:**
- < 50%: Critical inefficiency, refactor to batch calls
- 50-79%: Should optimize, look for batching opportunities
- ≥80%: Acceptable efficiency
- 100%: Optimal, no improvement possible

### 3. Execution Time

**Definition:** How long does the skill take to complete the workflow?

**Target:** Depends on complexity, but generally <60 seconds for most workflows

**How to measure:**
1. Start timer when user submits query
2. End timer when skill reports completion
3. Average over 5-10 executions
4. Compare to manual workflow time

**Example:**
```
Skill execution: ~30 seconds
Manual workflow: ~15 minutes (900 seconds)
Time saved: 870 seconds (14.5 minutes)
Speedup: 30× faster ✅
```

**When to iterate:**
- Slower than manual: Skill is counterproductive, must optimize
- 2-5× faster: Marginal improvement, consider if worth maintenance
- 5-20× faster: Good value, users will adopt
- >20× faster: Excellent value, high ROI

### 4. MCP API Success Rate

**Definition:** Percentage of MCP API calls that succeed (don't return errors).

**Target:** ≥95% success rate (some failures expected due to network, auth refresh, etc.)

**How to measure:**
1. Track total MCP calls attempted
2. Track successful responses (no error codes)
3. Calculate: Success rate = (Successful / Total) × 100%

**Example:**
```
10 skill executions:
- Total MCP calls: 90
- Successful: 87
- Failed: 3 (2× auth token expired, 1× rate limit)
Success rate: 87/90 = 96.7% ✅ Acceptable
```

**When to iterate:**
- < 80%: Critical issue, investigate error handling
- 80-94%: Should improve, add retry logic or better auth
- ≥95%: Acceptable, monitor trends
- ≥99%: Excellent robustness

### 5. Token Efficiency (Advanced)

**Definition:** How many tokens does the skill use compared to manual conversation?

**Target:** ≥50% reduction in tokens vs. manual guidance

**How to measure:**
1. Execute task WITH skill, note token count
2. Execute same task WITHOUT skill (manual guidance), note token count
3. Calculate: Reduction = ((Manual - Skill) / Manual) × 100%

**Example:**
```
With skill:
- User query: "Plan next sprint" (4 tokens)
- Skill execution: 1,200 tokens
- Total: 1,204 tokens

Without skill (manual):
- User asks: "How do I plan a sprint in Linear?" (8 tokens)
- Claude explains process: 800 tokens
- User: "Ok, what's our velocity?" (5 tokens)
- Claude fetches and explains: 600 tokens
- User: "Create sprint with those items" (6 tokens)
- Claude creates: 400 tokens
- Total: 1,819 tokens

Token reduction: (1,819 - 1,204) / 1,819 = 33.8% ✅ Decent
```

**When to iterate:**
- Negative reduction (skill uses MORE tokens): Simplify skill, too verbose
- 0-25% reduction: Marginal benefit, consider if worth complexity
- 25-50% reduction: Good efficiency
- >50% reduction: Excellent, skill is concise and effective

---

## Qualitative Metrics

### 1. User Autonomy

**Question:** Can users accomplish the task WITHOUT needing to clarify, correct, or supplement the skill's work?

**Assessment scale:**
- **Dependent (1):** User must heavily guide skill, multiple clarifications needed
- **Assisted (2):** User provides some guidance, 1-2 clarifications typical
- **Independent (3):** User provides clear request, skill completes autonomously
- **Proactive (4):** Skill anticipates needs, asks smart clarifying questions

**Target:** ≥3 (Independent)

**How to measure:**
1. Observe 5-10 skill executions
2. Count clarifying questions needed per execution
3. Rate autonomy level

**Example:**
```
Execution 1: "Plan next sprint" → Asks "Which team?" → Creates sprint ✅ (3 - Independent)
Execution 2: "Plan sprint for Eng" → Creates sprint directly ✅ (3 - Independent)
Execution 3: "Create sprint" → Asks team, asks duration → Creates sprint ✅ (3 - Independent)

Average: 3/4 = Independent ✅ Target met
```

**When to iterate:**
- Score 1: Skill needs major rework, instructions unclear
- Score 2: Improve instructions, reduce ambiguity
- Score 3: Acceptable, monitor edge cases
- Score 4: Excellent, skill is highly usable

### 2. Output Consistency

**Question:** Does the skill produce the same quality output for similar inputs?

**Assessment scale:**
- **Inconsistent (1):** Different runs produce significantly different results
- **Variable (2):** Some variation, but generally consistent
- **Consistent (3):** Reliably produces expected output
- **Deterministic (4):** Identical inputs always produce identical outputs

**Target:** ≥3 (Consistent)

**How to measure:**
1. Run same/similar query 5 times
2. Compare outputs
3. Rate consistency

**Example:**
```
Query: "Plan next sprint for Engineering team"

Run 1: Creates Sprint 24, assigns 6 issues (31 points)
Run 2: Creates Sprint 25, assigns 6 issues (31 points)
Run 3: Creates Sprint 26, assigns 5 issues (29 points) ⚠️ Different
Run 4: Creates Sprint 27, assigns 6 issues (32 points)
Run 5: Creates Sprint 28, assigns 6 issues (31 points)

Consistency: 4/5 runs similar (80%) → Score 3 ✅ Acceptable
Run 3 variation due to backlog change (expected)
```

**When to iterate:**
- Score 1: Skill logic is too random, add deterministic rules
- Score 2: Reduce variability in decision-making
- Score 3: Acceptable for dynamic data
- Score 4: Excellent for static workflows

### 3. First-Try Success Rate

**Question:** What percentage of skill executions succeed without errors or user intervention on first attempt?

**Target:** ≥80% first-try success

**How to measure:**
1. Track skill executions
2. Count successes (no errors, no user corrections needed)
3. Calculate: Success rate = (Successes / Total) × 100%

**Example:**
```
10 executions:
- 8 completed successfully first try ✅
- 1 failed (MCP auth expired) ❌
- 1 completed but user corrected sprint date ❌

First-try success: 8/10 = 80% ✅ Meets target
```

**When to iterate:**
- < 60%: Critical usability issue
- 60-79%: Should improve error handling
- ≥80%: Acceptable
- ≥90%: Excellent reliability

### 4. User Satisfaction (Post-Deployment)

**Question:** Do users prefer the skill vs. manual workflow?

**Assessment method:**
- Ask users: "Would you use this skill again?" (Yes/No)
- Observe: Do users invoke skill when appropriate, or avoid it?
- Measure: Skill usage frequency over time (increasing = good, decreasing = bad)

**Target:** ≥80% would use again

**Example:**
```
Survey: 5 users tried Linear Sprint Planning skill
- 4 said "Yes, I'll use this every sprint" ✅
- 1 said "Maybe, but I prefer manual control" ⚠️

Satisfaction: 80% ✅ Meets target
```

**When to iterate:**
- < 60%: Fundamental skill problem, investigate user feedback
- 60-79%: Improve based on specific user complaints
- ≥80%: Acceptable adoption
- ≥90%: Excellent user satisfaction

---

## Baseline Comparison Methodology

### Why Compare to Baseline?

You can't know if a skill is "good" without knowing what "normal" looks like.

**Baseline = How users accomplish the task WITHOUT the skill**

### Baseline Measurement Process

**1. Identify representative task**
   - Choose typical use case for the skill
   - Example: "Plan next 2-week sprint for Engineering team"

**2. Execute manually (no skill)**
   - Have user complete task through normal Claude conversation
   - Track:
     - Time taken (seconds)
     - Number of messages exchanged
     - Token count
     - Errors encountered
     - User satisfaction (1-5 scale)

**3. Record baseline metrics**
   - Example:
     ```
     Manual workflow baseline:
     - Time: 15 minutes (900s)
     - Messages: 8 back-and-forth exchanges
     - Tokens: ~1,800
     - Errors: 1 (forgot to check permissions, had to retry)
     - Satisfaction: 3/5 (works but tedious)
     ```

**4. Execute with skill**
   - Same user, same task
   - Track same metrics

**5. Compare**
   - Example:
     ```
     With skill:
     - Time: 30 seconds (30s)
     - Messages: 1 (user query)
     - Tokens: ~1,200
     - Errors: 0
     - Satisfaction: 4/5 (fast but less control)

     Improvement:
     - 30× faster ✅
     - 87.5% fewer messages ✅
     - 33% fewer tokens ✅
     - Fewer errors ✅
     - Higher satisfaction ✅
     ```

**6. Calculate ROI**
   ```
   Time saved per use: 870 seconds (14.5 minutes)
   Frequency: 1× per 2 weeks = ~26 uses/year
   Annual time saved: 26 × 14.5 min = 377 minutes (6.3 hours)

   Development time: 4 hours
   Payback period: 4 hours / 6.3 hours/year = 0.63 years (~8 months)

   After 8 months: Net positive ROI ✅
   ```

### Baseline Comparison Template

```markdown
## Baseline vs. Skill Comparison

**Task:** [Description of representative task]
**User:** [Who performed test]
**Date:** [When measured]

### Baseline (Manual Workflow)

| Metric              | Baseline |
|---------------------|----------|
| Time (seconds)      | 900      |
| Messages exchanged  | 8        |
| Token count         | 1,800    |
| Errors encountered  | 1        |
| User satisfaction   | 3/5      |

### With Skill

| Metric              | With Skill | Improvement   |
|---------------------|------------|---------------|
| Time (seconds)      | 30         | 30× faster    |
| Messages exchanged  | 1          | 87.5% fewer   |
| Token count         | 1,200      | 33% fewer     |
| Errors encountered  | 0          | 100% fewer    |
| User satisfaction   | 4/5        | 33% higher    |

### ROI Analysis

- Time saved per use: 14.5 minutes
- Expected frequency: 26×/year
- Annual time saved: 6.3 hours
- Development time: 4 hours
- **Payback period: 8 months** ✅
```

---

## When to Iterate vs. Accept

### Decision Framework

Use this matrix to decide if iteration is needed:

| Metric               | Critical (Must Fix) | Should Improve  | Acceptable      | Excellent       |
|----------------------|---------------------|-----------------|-----------------|-----------------|
| Triggering accuracy  | <80%                | 80-89%          | 90-94%          | ≥95%            |
| API efficiency       | <50%                | 50-79%          | 80-99%          | 100%            |
| Execution time       | Slower than manual  | 2-5× faster     | 5-20× faster    | >20× faster     |
| MCP success rate     | <80%                | 80-94%          | 95-98%          | ≥99%            |
| Token efficiency     | Negative            | 0-25% reduction | 25-50% reduction| >50% reduction  |
| User autonomy        | 1 (Dependent)       | 2 (Assisted)    | 3 (Independent) | 4 (Proactive)   |
| Output consistency   | 1 (Inconsistent)    | 2 (Variable)    | 3 (Consistent)  | 4 (Deterministic)|
| First-try success    | <60%                | 60-79%          | 80-89%          | ≥90%            |
| User satisfaction    | <60%                | 60-79%          | 80-89%          | ≥90%            |

### Iteration Priority

**Fix immediately (Critical):**
- ANY metric in "Critical" column
- User satisfaction <60%
- Skill slower than manual workflow
- First-try success <60%

**Improve when time allows (Should Improve):**
- 2+ metrics in "Should Improve" column
- Specific user complaints about workflow
- Inconsistent output quality

**Accept current performance (Acceptable/Excellent):**
- All metrics in "Acceptable" or better
- Users are satisfied and using skill regularly
- ROI is positive

**Don't over-optimize (Diminishing Returns):**
- Metric is already "Excellent" → Focus elsewhere
- Improvement would take >10 hours but save <1 hour/year
- Skill is rarely used (low frequency) → Don't invest heavily

### Iteration Signals

**When to keep iterating:**
- First-try success improving with each change
- User complaints decreasing
- Usage frequency increasing
- ROI getting more positive

**When to stop iterating:**
- All metrics "Acceptable" or better
- Last 3 iterations showed no improvement
- Users stopped reporting issues
- Usage plateau (stable, consistent use)

---

## Measurement Workflow

### Pre-Development (Planning)

**1. Define success criteria**
   - What metrics matter for this skill?
   - What are acceptable thresholds?
   - How will I measure them?

**2. Establish baseline**
   - Measure manual workflow
   - Record time, tokens, errors, satisfaction
   - Calculate theoretical ROI

**3. Set targets**
   - Must achieve: X× faster than manual
   - Should achieve: ≥90% triggering accuracy
   - Nice to have: ≥50% token reduction

### Post-Development (Validation)

**4. Measure quantitative metrics**
   - Run test query suite (triggering accuracy)
   - Execute workflow 5× (time, API efficiency, success rate)
   - Compare to baseline

**5. Measure qualitative metrics**
   - Observe real usage (autonomy, consistency)
   - Collect user feedback (satisfaction)
   - Calculate first-try success

**6. Analyze results**
   - Which metrics met targets?
   - Which metrics need improvement?
   - Is ROI positive?

**7. Decide: Ship, Iterate, or Abandon**
   - **Ship:** All critical metrics acceptable, ROI positive
   - **Iterate:** 1-2 metrics in "Should Improve", fixable issues
   - **Abandon:** Critical metrics failed, negative ROI, too much effort to fix

### Post-Deployment (Monitoring)

**8. Track usage over time**
   - How often is skill used?
   - Is usage increasing (good) or decreasing (bad)?
   - Are errors occurring in production?

**9. Collect real user queries**
   - Add missed triggers to test suite
   - Update description if triggering degrades
   - Fix edge cases discovered

**10. Periodic re-measurement**
   - Every 3 months: Re-run test suite
   - Every 6 months: Re-measure baseline comparison
   - Annually: Calculate actual ROI vs. projected

---

## Quick Reference

### Minimum Viable Measurement

**If you only measure 3 things, measure these:**
1. **Triggering accuracy** (90%+ target) - Use test-queries-template.txt
2. **Time saved** (≥5× faster than manual) - Stopwatch comparison
3. **User satisfaction** (≥80% would use again) - Ask users directly

### Comprehensive Measurement

**For production skills, measure all 9 metrics:**
- 5 quantitative: Triggering, API efficiency, execution time, MCP success, tokens
- 4 qualitative: Autonomy, consistency, first-try success, satisfaction

### When to Re-Measure

- **After every description change:** Re-test triggering accuracy
- **After MCP/workflow changes:** Re-measure API efficiency and execution time
- **Monthly:** Check usage frequency and user satisfaction
- **Quarterly:** Full re-measurement of all metrics

---

## Referenced By

- `SKILL.md` - Step 8 (Measure effectiveness), Step 9 (Iterate)
- `test-queries-template.txt` - Triggering accuracy measurement
- `mcp-integration-patterns.md` - MCP-specific metrics
- `troubleshooting-guide.md` - Using metrics to identify issues
