# The Context Layer: A Practical Guide to Organisational Knowledge

## Why Your Company Knows Less Than It Thinks

Every organisation has more data than it can use — and less understanding than it needs. This guide explains why, and what to do about it.

---

## 1. The Filing Cabinet Problem

Think of every tool your company uses as a filing cabinet.

- **GitHub** — a cabinet full of code, pull requests, and deployment history
- **Slack** — a cabinet full of conversations, decisions made in passing, and tribal knowledge
- **Jira** — a cabinet full of tickets, priorities, and what got shipped when
- **Salesforce** — a cabinet full of deals, customer feedback, and revenue signals
- **Notion / Confluence** — a cabinet full of documentation (some current, much of it stale)

None of these cabinets are empty. If anything, they are overflowing. Storage is not the problem. Your company does not have a data problem.

**The problem is the space between the cabinets.**

When a support ticket comes in about a recurring bug, who connects it to the engineering decision made six months ago, the customer segment it affects, and the product roadmap item that was supposed to fix it? When a senior engineer leaves, who holds the reasoning behind the architecture choices they made?

A person does. Maybe two or three people. They are your synthesis layer — the ones who carry context across tools, across teams, across time. They connect the dots that no single filing cabinet contains.

This is the most valuable function in your organisation, and it runs on the most constrained resource you have: human attention. It is bandwidth-limited, impaired by context-switching, and — critically — it walks out the door when people leave.

**The synthesis layer is not a nice-to-have. It is the thing that turns a collection of filing cabinets into a functioning organisation.**

---

## 2. Data vs Understanding

Most companies confuse having data with having understanding. They are not the same thing, and the difference matters enormously.

Here is a concrete example — the same fact at four levels of depth:

| Level | Example |
|---|---|
| **Data** | "We use PostgreSQL for our main database" |
| **Information** | "We migrated from MongoDB to PostgreSQL in Q3 2024" |
| **Knowledge** | "We migrated because MongoDB's consistency model caused data loss during peak load" |
| **Understanding** | "The migration was driven by a specific customer incident. The same consistency pattern exists in our payment service — which hasn't been migrated yet and is a ticking time bomb" |

Notice what happens as you move down the table:

- **Data** lives in config files and infrastructure docs. Any new hire can find it.
- **Information** lives in project trackers and migration plans. It takes some digging, but it is retrievable.
- **Knowledge** lives in decision records — if you wrote them. More often it lives in the heads of the people who were in the room.
- **Understanding** lives almost exclusively in people's heads. It connects past incidents to future risks. It sees patterns across systems. It is the most valuable layer, and it is the least durable.

Most companies store data and information reasonably well. Knowledge is patchy. Understanding evaporates — gradually when people get busy, suddenly when they leave.

**The goal of a context layer is to capture and preserve understanding, not just data.**

---

## 3. The Comprehension Lock-in Effect

This is not just an operational concern. It is a strategic one.

Companies like OpenAI and Anthropic are building AI systems designed to capture organisational understanding — not just store documents, but genuinely comprehend how a business works. The reasoning behind decisions. The connections between systems. The patterns that predict problems.

Here is why that matters strategically:

### Data lock-in is yesterday's moat

If your CRM vendor holds your customer data hostage, you can export it. CSV files, API dumps, migration tools — data is portable. Switching costs exist, but they are manageable. Regulators are increasingly mandating data portability.

### Comprehension lock-in is the new moat

Understanding is not portable. You cannot export "this AI deeply understands our business" into a CSV. When an AI system has spent two years learning your architecture decisions, your customer patterns, your internal politics, your technical debt — that comprehension does not transfer. You would have to rebuild it from scratch with a new system, and that takes time you probably do not have.

### The compound effect

Every day an AI system operates within your organisation, its understanding deepens. Day one, it knows your documentation. Day thirty, it knows your patterns. Day three hundred, it knows your business in ways that would take a new employee years to learn.

This creates a flywheel: the more you use it, the more it understands. The more it understands, the more useful it becomes. The more useful it becomes, the more you use it.

**The strategic implication:** Whether you build your context layer with external AI tools or internal systems, start now. The compound effect means that every month you delay is a month of understanding you will never get back. And if a competitor starts before you, their AI will understand their business better than yours understands yours — and that gap widens over time.

---

## 4. Building Your Own Context Layer — Four Levels

You do not need to leap to AI-powered knowledge synthesis on day one. There are four levels, and each one delivers value independently. Start where you are, and build up.

### Level 1: Documentation (The Baseline)

**What it is:** Structured, searchable, current documentation.

**Why it matters:** This is the foundation everything else builds on. Without it, you are asking AI to synthesise from chaos. Garbage in, garbage out.

**What "good" looks like:**
- Documentation lives close to the thing it describes (code docs in the repo, process docs in the wiki, not scattered across five tools)
- There is a clear owner for each major section
- Stale docs are archived or updated, not left to mislead
- New team members can find what they need without asking three people

**The honest truth:** Most companies think they are at Level 1 but are not. If your onboarding process involves a week of "just ask Sarah, she knows where everything is," you have not reached Level 1 yet.

### Level 2: Decision Logging (Where Most Companies Fail)

**What it is:** Capturing WHY decisions were made, not just WHAT was decided.

**Why it matters:** This is the layer that preserves knowledge — the reasoning, the trade-offs, the alternatives considered and rejected. Without it, future teams relitigate decisions endlessly or, worse, reverse good ones because they do not understand why they were made.

**What "good" looks like:**
- Major technical decisions have written records (Architecture Decision Records, or ADRs)
- Product decisions capture the reasoning, not just the outcome
- Sales and commercial decisions record the logic ("we offered this discount because...")
- The records are findable and linked to the work they relate to

**Why companies fail here:** Decision logging feels like overhead in the moment. The person making the decision already understands the reasoning — writing it down feels redundant. It only becomes valuable later, when that person is busy, has moved teams, or has left. This is a discipline problem, not a tooling problem.

### Level 3: Connected Knowledge (The Bridge)

**What it is:** Linking decisions to code to customer feedback to strategy — creating connections across your filing cabinets.

**Why it matters:** This is where you start to build genuine understanding at an organisational level. Individual pieces of knowledge become a network. Patterns emerge. Risks become visible before they become incidents.

**What "good" looks like:**
- Engineering decisions link to the customer feedback that prompted them
- Product roadmap items trace back to specific pain points and forward to specific code changes
- Post-mortems reference the architectural context that contributed to the incident
- Cross-team context is explicit, not implicit

**The challenge:** This requires effort across teams, not just within them. It is inherently cross-functional work, and most organisations are structured in ways that make cross-functional knowledge sharing difficult.

### Level 4: AI-Augmented Synthesis (The Future — Available Now)

**What it is:** Using AI to actively synthesise understanding from your accumulated knowledge — not just searching documents, but connecting dots across them.

**Why it matters:** This is where you begin to replicate (and eventually exceed) the synthesis function that currently lives in a few key people's heads. The AI can hold more context, does not forget, does not get tired, and does not leave.

**What "good" looks like:**
- AI workspaces loaded with company context that can answer "why" questions, not just "what" questions
- RAG (Retrieval-Augmented Generation) systems that pull from multiple sources to provide synthesised answers
- Context-aware agents that understand your codebase, your decisions, and your customers
- The AI gets better over time as more context is captured

**The prerequisite:** Levels 1-3 are the fuel. AI-augmented synthesis without good documentation, decision records, and connected knowledge is just a faster way to get wrong answers.

---

## 5. Practical Patterns for Each Level

Theory is useless without action. Here are specific, implementable patterns for each level. Pick one or two from wherever you are and start this week.

### Level 1 Patterns: Documentation

**Pattern: The "New Starter Test"**
Ask your most recent hire: "What was hardest to find when you joined?" Whatever they say, fix it. Repeat with every new starter. Your documentation improves continuously, driven by real pain.

**Pattern: Documentation as Code**
Store documentation alongside the code it describes, in the same repository. It gets reviewed in the same pull requests. When the code changes, the docs are right there, staring at the reviewer. This does not guarantee updates, but it makes neglect visible.

**Pattern: The Quarterly Purge**
Once a quarter, every team spends two hours archiving or updating stale documentation. Set a calendar reminder. Make it a team activity, not a solo chore. Stale docs are worse than no docs — they erode trust in all documentation.

### Level 2 Patterns: Decision Logging

**Pattern: Lightweight ADRs (Architecture Decision Records)**
For engineering teams, adopt a simple ADR template:

```
# ADR-[number]: [Title]

## Status
[Proposed / Accepted / Deprecated / Superseded]

## Context
What is the situation that requires a decision?

## Decision
What did we decide?

## Reasoning
Why did we choose this over the alternatives?

## Alternatives Considered
What else did we evaluate, and why did we reject it?

## Consequences
What are the known trade-offs and risks of this decision?
```

Keep them short. A good ADR is half a page, not five pages. The goal is to capture reasoning, not to write a thesis. Store them in the repository they relate to.

**Pattern: The "Future Us" Rule**
Before closing a decision, ask: "If someone joins the team in 18 months and asks why we did this, will they be able to find the answer without asking anyone?" If not, write it down. Frame it as a gift to your future selves, not as bureaucracy.

**Pattern: Product Decision Records**
The same principle applies outside engineering. Product decisions, pricing changes, go-to-market pivots — all benefit from a brief written record of the reasoning. Adapt the ADR template: replace "Architecture" with "Product" or "Commercial." The format matters less than the habit.

**Pattern: Meeting Notes That Capture Reasoning**
Stop writing meeting notes that are just action items. Add a "Decisions and Reasoning" section. When the group decides something, capture not just what was decided but the two or three key arguments that drove the decision. This takes an extra five minutes and saves hours of future confusion.

### Level 3 Patterns: Connected Knowledge

**Pattern: Context-Rich Commit Messages and PR Descriptions**
A commit message like "fix bug" is worthless. A commit message like "Fix race condition in payment processing that caused duplicate charges for customers on the enterprise plan — see incident report INC-2847 and ADR-031" is a node in your knowledge graph. It connects code to incidents to decisions. Make this a team norm, not a suggestion.

**Pattern: Cross-Reference Links**
When writing a decision record, link to the Jira ticket, the Slack thread, the customer feedback, and the code change. When closing a support ticket, link to the fix. When writing a post-mortem, link to the ADR that created the architecture involved. Each link is a connection in your context layer. It takes seconds and compounds over months.

**Pattern: Cross-Team Context Syncs**
Once a month, get engineering, product, and customer-facing teams in a room (or a call) for 30 minutes. Not a status update — a context sync. Engineering shares what technical decisions are coming. Product shares what customer patterns they are seeing. Support shares what keeps breaking. The goal is to surface the connections that no single team can see alone.

**Pattern: Incident-to-Architecture Mapping**
After every significant incident, explicitly map it back to the architectural or process decision that contributed. This is not about blame — it is about building a visible link between decisions and their real-world consequences. Over time, this creates a powerful feedback loop that improves decision-making.

### Level 4 Patterns: AI-Augmented Synthesis

**Pattern: Claude Projects as Team Knowledge Bases**
Create a Claude Project for your team or domain. Upload your key documents: architecture diagrams, ADRs, onboarding guides, recent post-mortems. Now you have an AI that can answer questions about your specific context, not just general knowledge. Update it monthly as new decisions are made.

**Pattern: Simple RAG Over Critical Documents**
You do not need a massive infrastructure project. Start with your most critical documents — architecture docs, runbooks, decision records — and set up a basic RAG (Retrieval-Augmented Generation) pipeline. Tools like LlamaIndex or LangChain make this achievable in a few days. The goal is not perfection; it is making your existing knowledge queryable in natural language.

**Pattern: Context-Aware Code Review**
Feed your ADRs and coding standards into an AI assistant that participates in code reviews. It can flag when a change contradicts an existing architectural decision, when a pattern has been tried before and failed, or when a similar approach caused an incident in a different service. This turns your historical knowledge into an active safeguard.

**Pattern: The "What Would Sarah Know?" Test**
Think of the person on your team who holds the most context — the one everyone goes to with questions. What do they know that is not written down anywhere? Start capturing that knowledge, either through structured interviews or by having them work alongside an AI assistant that learns from their explanations. Your goal is to make their understanding durable and shareable, not to replace them.

---

## Where to Start

If you are feeling overwhelmed, here is the simplest possible starting point:

1. **This week:** Write one decision record for the last significant decision your team made. Use the ADR template above. Store it where your team will find it.

2. **This month:** Run the "New Starter Test" and fix the top three documentation gaps.

3. **This quarter:** Set up a Claude Project with your team's key documents and start using it for onboarding questions and context retrieval.

4. **This half:** Introduce cross-team context syncs and context-rich PR descriptions as team norms.

None of these require budget approval, new tooling, or a transformation programme. They require discipline and the conviction that understanding — not just data — is what makes an organisation effective.

---

## The Bottom Line

Your filing cabinets are full. Your synthesis layer is fragile. The companies that build durable context layers — capturing not just what happened but why, and connecting knowledge across teams and tools — will compound their organisational intelligence over time.

The ones that do not will keep losing understanding every time someone changes role, goes on leave, or hands in their notice. They will keep making the same mistakes, relitigating the same decisions, and wondering why the new hire is taking so long to get up to speed.

The context layer is not a technology problem. It is a discipline problem with a technology accelerant. Start with the discipline. The technology will meet you halfway.
