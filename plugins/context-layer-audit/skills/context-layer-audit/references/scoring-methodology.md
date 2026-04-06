# Context Layer Audit — Scoring Methodology

Use this reference to score an organisation's knowledge management health across six dimensions, calculate an overall Context Health Score, and interpret the results.

---

## 1. The Six Dimensions

Each dimension is rated **1–10** by the person taking the audit.

| # | Dimension | What It Measures |
|---|-----------|-----------------|
| 1 | **Retrievability** | Can people actually find what they need, when they need it? |
| 2 | **Connectedness** | Is knowledge linked across systems, teams, and tools — or siloed? |
| 3 | **Bus Factor Risk** | What happens when key people leave, go on holiday, or change roles? |
| 4 | **Freshness** | Is documentation current, or is it quietly rotting? |
| 5 | **AI-Readiness** | Is knowledge structured so AI tools can consume and reason over it? |
| 6 | **Cross-team Synthesis** | Can different teams access and build on each other's context? |

---

## 2. Weighted Scoring Formula

Not all dimensions matter equally. Bus Factor Risk and Connectedness carry the heaviest weight because they represent the biggest organisational vulnerabilities — the kind that cause crises, not just inconvenience.

### Weights

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Retrievability | 0.15 | Important, but most organisations at least attempt search |
| Connectedness | 0.20 | Cross-system linkage is where most knowledge strategies fail |
| Bus Factor Risk | 0.25 | The single highest-impact risk — knowledge loss is irreversible |
| Freshness | 0.10 | Stale docs are a symptom; the cause is usually elsewhere |
| AI-Readiness | 0.10 | Increasingly important but still emerging for most orgs |
| Cross-team Synthesis | 0.20 | Directly impacts decision quality and speed at scale |

**Weights sum to 1.00.**

### Formula

```
Context Health Score = (
    Retrievability   x 0.15 +
    Connectedness    x 0.20 +
    Bus Factor Risk  x 0.25 +
    Freshness        x 0.10 +
    AI-Readiness     x 0.10 +
    Cross-team Synthesis x 0.20
) x 10
```

Each dimension score is 1–10. The weighted sum produces a value between 1.0 and 10.0. Multiplying by 10 gives a **Context Health Score out of 100**.

### Worked Example

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Retrievability | 6 | 0.15 | 0.90 |
| Connectedness | 4 | 0.20 | 0.80 |
| Bus Factor Risk | 3 | 0.25 | 0.75 |
| Freshness | 5 | 0.10 | 0.50 |
| AI-Readiness | 2 | 0.10 | 0.20 |
| Cross-team Synthesis | 4 | 0.20 | 0.80 |
| **Total** | | | **3.95** |

**Context Health Score: 3.95 x 10 = 39.5 out of 100** (Fragmented)

---

## 3. Scoring Rubrics

### 3.1 Retrievability

*Can people actually find what they need?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | People regularly spend 20+ minutes searching for something they know exists. Common response to "where is X?" is a Slack message or shoulder tap. Multiple copies of the same document float around with no clear canonical version. New starters describe onboarding as "archaeology." |
| **Fragmented** | 4–6 | Most things are findable if you know where to look. Power users can navigate the systems, but casual users get lost. Search works for recent items but fails for anything older than a few months. There is a wiki or shared drive, but it is only partially adopted. |
| **Developing** | 7–8 | There is a clear primary system for documentation. Search usually returns useful results. Most teams follow a consistent structure. New starters can self-serve for about 70% of what they need in their first month. |
| **Strong** | 9–10 | Knowledge is findable in under two minutes for any employee. There are clear naming conventions, tagging, and a single search entry point. People trust the system enough to look there first, not ask a person. New starters rarely need to ask "where do I find...?" |

### 3.2 Connectedness

*Is knowledge linked across systems and teams?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | Each team uses its own tools with zero integration. A decision made in one system (e.g., Jira) has no link to the context behind it (e.g., a Notion doc or Slack thread). To understand why something was done, you need to interview the person who did it. |
| **Fragmented** | 4–6 | Some teams link related resources, but it is inconsistent. You can trace a decision back to its context maybe half the time. There are integrations between some tools (e.g., Slack notifications from Jira) but they are one-directional and shallow. |
| **Developing** | 7–8 | Most decisions, projects, and documents have links to related context. There is a conscious practice of connecting information across systems. You can usually follow a thread from outcome back to rationale without asking someone. |
| **Strong** | 9–10 | Knowledge forms a navigable graph. Every significant decision links to its inputs, discussion, and outcomes. Cross-references are standard practice, not exceptional effort. Someone new to a project can reconstruct the full context from the documentation alone. |

### 3.3 Bus Factor Risk

*What happens when key people leave?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | If your team says "ask Sarah, she knows" more than once a week, you are probably here. Critical processes live in one person's head. When someone goes on holiday, decisions stall or get made blind. A resignation would trigger genuine panic about what knowledge walks out the door. |
| **Fragmented** | 4–6 | Key knowledge holders exist, but there is some documentation backing them up. If someone left, you would lose speed but not capability entirely. Handovers happen but are rushed and incomplete. You have had at least one "oh no, they left and nobody knows how this works" moment in the past year. |
| **Developing** | 7–8 | Most critical processes are documented well enough that someone else could take over within a week. There are designated backups for key roles. Knowledge sharing is a regular practice (e.g., team walkthroughs, pair work, recorded demos). Departures cause inconvenience, not crises. |
| **Strong** | 9–10 | No single person is a critical point of failure. Knowledge is systematically distributed through documentation, cross-training, and rotation. When someone leaves, the transition plan is straightforward. The team has tested this — not just theorised about it. |

### 3.4 Freshness

*Is documentation current or rotting?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | Most documentation is out of date. People have learned not to trust it ("don't look at the wiki, it's all wrong"). No one owns updating docs. The last meaningful update to your main knowledge base was months ago. Onboarding materials reference tools or processes you no longer use. |
| **Fragmented** | 4–6 | Some documentation is current, some is stale, and there is no easy way to tell which is which. Updates happen reactively — someone fixes a doc when they get bitten by wrong information. There is no review cadence. About half your docs would pass a spot-check for accuracy. |
| **Developing** | 7–8 | Documentation has owners or review dates. There is a regular cadence for checking and updating key docs. Stale content is flagged or archived rather than left to mislead. Most docs are accurate enough to act on without double-checking. |
| **Strong** | 9–10 | Documentation is treated as a live product. Updates happen as part of the workflow, not as a separate chore. There are automated staleness checks or review triggers. People trust the docs because they have been burned by stale information exactly zero times recently. |

### 3.5 AI-Readiness

*Is knowledge structured for AI consumption?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | Knowledge lives in formats AI cannot easily parse: handwritten notes, screenshots of Slack threads, PDFs of scanned documents, or tribal knowledge in people's heads. There is no consistent structure, metadata, or taxonomy. Attempting to point an AI tool at your knowledge base would produce mostly hallucinated or irrelevant results. |
| **Fragmented** | 4–6 | Some knowledge is in text-searchable, structured formats. But a significant portion is locked in video calls without transcripts, images without descriptions, or tools with no API access. There is no consistent metadata or tagging scheme. An AI tool would work for some queries but fail unpredictably for others. |
| **Developing** | 7–8 | Most knowledge is in structured, text-based formats with reasonable metadata. Key systems have API access. There is enough consistency in naming and structure that an AI tool could index and retrieve meaningfully. You have experimented with AI search or assistants and they work acceptably. |
| **Strong** | 9–10 | Knowledge is stored in well-structured, API-accessible formats with consistent metadata, clear taxonomies, and explicit relationships. You have successfully deployed AI tools (search, assistants, summarisers) over your knowledge base and they produce reliable results. Knowledge creation processes consider machine readability as a requirement, not an afterthought. |

### 3.6 Cross-team Synthesis

*Can different teams access each other's context?*

| Band | Score | What This Looks Like |
|------|-------|---------------------|
| **Critical** | 1–3 | Teams operate as information islands. Engineering does not know what sales is hearing from customers. Product decisions are made without input from support data. Getting context from another team requires knowing who to ask and hoping they have time. Cross-functional projects regularly fail because teams are working from different assumptions. |
| **Fragmented** | 4–6 | Some cross-team visibility exists — perhaps through shared Slack channels or all-hands updates. But synthesising information across teams requires a specific person (often a manager or PM) to manually broker context. Insights from one team rarely make it to another unless someone champions it. |
| **Developing** | 7–8 | There are established mechanisms for cross-team knowledge sharing: shared dashboards, cross-functional standups, accessible project spaces. Most teams can find another team's key decisions and rationale without asking. Cross-functional projects have a shared information space. |
| **Strong** | 9–10 | Any team can discover what other teams are working on, why, and what they have learned — without needing a person to translate. There is a deliberate practice of making team-level knowledge organisationally accessible. Insights flow between teams fast enough to influence decisions in near real-time. |

---

## 4. Interpretation Guide

### Overall Context Health Score Bands

| Score Range | Rating | Summary | What It Means |
|-------------|--------|---------|---------------|
| **0–25** | Critical | "You're one resignation away from a crisis." | Knowledge is overwhelmingly tacit and person-dependent. Systems are fragmented or unused. Finding information depends on knowing the right person and catching them at the right time. This is not just an efficiency problem — it is an operational risk. Priority action: identify the top three single-points-of-failure people and begin extracting their critical knowledge immediately. |
| **26–50** | Fragmented | "Knowledge exists but connecting it requires human heroics." | There are pockets of good documentation and some functional systems, but the overall picture is inconsistent. Some teams are ahead, others are behind. The biggest gap is usually between what is known and what is findable. Priority action: audit the gaps between your best and worst teams and standardise the practices that are already working somewhere. |
| **51–75** | Developing | "You have foundations, now systematise." | The basics are in place. Most knowledge is documented somewhere, most systems are connected somehow, and most people can find what they need most of the time. The challenge now is consistency, maintenance, and scaling. Priority action: move from ad-hoc good practice to embedded process — review cadences, ownership models, and automated checks. |
| **76–100** | Strong | "You're ahead of 90% of companies." | Knowledge flows reliably across people, teams, and systems. Documentation is trusted and maintained. The organisation can absorb departures, scale teams, and adopt AI tools with confidence. Priority action: maintain what you have built, and look for the next frontier — typically AI-augmented synthesis and predictive knowledge management. |

### Common Score Patterns and What They Reveal

| Pattern | Likely Cause |
|---------|-------------|
| High Retrievability, low Connectedness | You have a good tool (e.g., Notion, Confluence) but no linking discipline. Knowledge exists in neat silos. |
| High Freshness, low Bus Factor | One person is keeping the docs alive. When they stop, freshness collapses too. |
| High Cross-team Synthesis, low AI-Readiness | You have strong human communication culture (meetings, Slack) but it is not captured in a durable, structured format. |
| Low everything except Retrievability | You probably invested in a knowledge management tool but not in the practices around it. The tool is not the problem. |
| Bus Factor below 4 with everything else above 6 | You have the systems but not the habits. Knowledge extraction is not embedded in workflows — it depends on individual motivation. |

---

## 5. Administering the Audit

### Who Should Score

Ideally, gather scores from **3–5 people** across different roles and seniority levels in the same organisation. Average their scores per dimension. The variance between scorers is as informative as the score itself — high variance on a dimension means different parts of the organisation experience it very differently.

### Suggested Prompt Approach

For each dimension, ask the participant to:

1. Read the dimension description and rubric bands.
2. Think of a specific recent example (last 30 days) that illustrates their experience.
3. Pick the score that best matches their lived reality, not their aspiration.

### Red Flags to Surface

Regardless of overall score, flag these as urgent concerns:

- **Any single dimension at 1–2**: Even one critical dimension can undermine everything else.
- **Bus Factor Risk below 3**: This is a ticking clock, not a to-do item.
- **Variance of 4+ points between scorers on the same dimension**: The organisation does not have a shared understanding of its own knowledge health — which is itself a knowledge problem.
