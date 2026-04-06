---
name: context-layer-audit
description: Use when a user wants to audit where their organisation's knowledge and understanding lives, assess knowledge fragmentation, or build a plan to capture organisational context before it's lost. Trigger on requests about knowledge management, organisational understanding, context capture, onboarding knowledge loss, or team knowledge silos.
metadata:
  version: 1.0.0
  author: Jamie Oarton — Bramforth
  updated: 2026-03-06
---

# Context Layer Audit

Audit where your organisation's real understanding lives — not just data, but synthesis, decision context, and the "why" behind how things work. Produces a scored, benchmarked report with a prioritised action plan.

## When to Use

Use when the user says things like:
- "Where does our team's knowledge actually live?"
- "We keep losing context when people leave"
- "Our onboarding takes too long"
- "I want to audit our knowledge management"
- "How do I build a context layer for my team?"
- "Our knowledge is scattered across too many tools"

Do NOT use for:
- Setting up specific tools (Notion, Confluence, etc.)
- General AI strategy unrelated to knowledge capture
- Individual productivity or personal knowledge management

## How to Run the Audit

Walk through 4 phases as a conversation. Ask one section at a time — don't dump all questions at once. Be direct and practical, not consultative fluff.

Adapt to company size:
- **<10 people**: Keep it simple. They don't need enterprise architecture.
- **10-50 people**: Focus on cross-team handoffs and documentation gaps.
- **50+ people**: Emphasise cross-team synthesis — that's where the real value leaks.

---

## Phase 1: Discovery

### A. The Stack

Ask:
1. What tools does your team use day-to-day? (Slack, Notion, GitHub, Jira, Confluence, Google Docs, Salesforce, HubSpot, Linear, Figma, etc.)
2. Where does your code live? (If applicable)
3. Where do you document decisions? Or do you?
4. Where do real-time conversations happen?

### B. The People

Ask:
5. How big is your team? Roughly how many technical vs non-technical?
6. When someone senior leaves, what happens to their knowledge? How painful is onboarding their replacement?
7. How do different teams share context with each other today?

### C. The AI Layer

Ask:
8. What AI tools are people using? (ChatGPT, Claude, Gemini, Copilot, etc.)
9. Is everyone on the same tool, or fragmented across teams?
10. Are any AI interactions being captured or reused? (Saved prompts, Claude projects, shared conversations?)

---

## Phase 2: Analysis

After gathering answers, produce three outputs. Be specific to THEIR answers — reference their actual tools, team size, and situation throughout.

### 1. Knowledge Map

Create a table showing where each type of organisational knowledge currently lives. Fill this in based on their answers:

| Knowledge Type | Primary Location | Backup Location | Retrievable? | Connected? |
|---|---|---|---|---|
| Code & architecture decisions | | | Yes/Partial/No | Yes/No |
| Customer context & history | | | | |
| Product decisions & rationale | | | | |
| Team processes & workflows | | | | |
| Strategic priorities & goals | | | | |
| Informal knowledge ("tribal") | | | | |

### 2. Dimension Scores

Score each of the 6 dimensions (1-10) using the detailed rubrics in `references/scoring-methodology.md`. Calculate the weighted Context Health Score out of 100.

The six dimensions are:
- **Retrievability** (weight: 0.15) — Can people find what they need?
- **Connectedness** (weight: 0.20) — Is knowledge linked across systems?
- **Bus Factor Risk** (weight: 0.25) — What happens when key people leave?
- **Freshness** (weight: 0.10) — Is documentation current?
- **AI-Readiness** (weight: 0.10) — Is knowledge structured for AI?
- **Cross-team Synthesis** (weight: 0.20) — Can teams access each other's context?

For each dimension, explain the score with specific examples from their answers. Consult `references/scoring-methodology.md` for the full rubrics and scoring bands.

### 3. Top 3 Gaps

Identify the three places where valuable understanding is most at risk. Be blunt. Reference their specific situation.

---

## Phase 3: Benchmarks

Compare their results against peers using `references/industry-benchmarks.md`.

Based on their company size and team type, provide:
- How their scores compare to typical companies at their stage
- Which breakdown pattern applies to them (15-Person Wall, 50-Person Cliff, or 200-Person Maze)
- How their onboarding times compare to benchmarks for their size
- Tool stack assessment — are they within normal ranges or showing fragmentation risk?

---

## Phase 4: Action Plan & Report

### Generate the Report

Use the template in `assets/audit-report-template.md` to produce a complete, structured report. Fill in EVERY section with their specific data — no placeholders left blank.

The report includes:
- Executive Summary (CEO-readable in 10 seconds)
- Knowledge Map
- Dimension Scores with weighted Context Health Score
- Top 3 Gaps with risk levels
- Benchmarks Comparison
- Prioritised Action Plan (This Week / This Month / This Quarter)
- Context Layer Maturity assessment (Levels 1-4)
- "The One Thing" — their single most impactful action
- Next Steps checklist with 90-day review date

### The Action Plan

Organise actions by time horizon:

**This Week** (< 2 hours each): 3-4 quick wins they can start immediately
**This Month**: 3-4 actions requiring some setup but delivering compounding value
**This Quarter**: 2-3 strategic moves

For practical patterns to recommend at each level, consult `references/context-layer-patterns.md` — particularly the "Practical Patterns for Each Level" section.

### The One Thing

End with their single most impactful action. Be decisive:

> "If you do nothing else: **[specific action]**. This alone will [specific benefit] because [reason tied to their specific gaps]."

---

## Style Rules

- Be direct and practical — no consulting jargon
- Use THEIR specific tools, team sizes, and situations in every output
- Don't oversell AI — some problems need process fixes, not technology
- Be honest if something is working well. Not everything needs fixing
- Keep language simple. The user may not be technical
- Format the final report cleanly — it should be shareable with leadership as-is
- The report must feel like a $5,000 consulting deliverable, not a chatbot response

---

## Resources

- `references/scoring-methodology.md` — Detailed rubrics for all 6 dimensions, weighted formula, interpretation guide
- `references/industry-benchmarks.md` — Benchmarks by company size, team type, tool stacks, onboarding times
- `references/context-layer-patterns.md` — The filing cabinet framework, 4 maturity levels, practical implementation patterns
- `assets/audit-report-template.md` — Complete report template for final output
