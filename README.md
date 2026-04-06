# Claude Skills by Jamie Oarton

Free Claude Code plugins for business owners, consultants, and AI strategy.

Built by [Jamie Oarton](https://jamieoarton.com), fractional Chief AI Officer at [Bramforth AI](https://bramforth.ai).

This repo is a Claude Code **marketplace** hosting two plugins:

- **content-engine** - Turn one voice-note transcript into a week of content (LinkedIn, short video, long video, newsletter)
- **context-layer-audit** - Audit where your organisation's knowledge lives

---

## Install

### Add the marketplace

In Claude Code:

```
/plugin marketplace add jamieoarton/skills
```

### Install a plugin

```
/plugin install content-engine@jamieoarton-skills
/plugin install context-layer-audit@jamieoarton-skills
```

---

## The Content Engine

Turn one 10-15 minute voice recording into a week of content across LinkedIn, short-form video, long-form video, and newsletter. Four skills, one transcript, four outputs.

Most creators spend 10-15 hours a week making content. There is a faster way.

**The workflow:**
1. Record yourself talking about one topic for 10-15 minutes (phone voice recorder is fine)
2. Transcribe it (any AI assistant can do this)
3. Feed the transcript to each skill and get platform-ready content
4. Review, tweak, and publish

**The skills:**

### `linkedin`
Turn a transcript into a 150-word LinkedIn post for business owners. Short sentences, one clear opinion, no AI hype words, British English.

**Say:** "Turn this transcript into a LinkedIn post"

### `short-video`
Turn a transcript into a 60-second talking-head script for TikTok, Reels, or YouTube Shorts. Specific hook in the first 3 seconds, no teasing, one idea hit hard.

**Say:** "Turn this into a short video script"

### `long-video`
Turn a transcript into a 5-8 minute YouTube video outline with intro hook, 3-4 main sections, and CTA. Outline not script - so you deliver naturally.

**Say:** "Turn this into a YouTube video outline"

### `newsletter`
Turn a transcript into a 1000-word newsletter or blog post. Five sections, descriptive headings, your voice preserved throughout.

**Say:** "Turn this into a newsletter"

---

## Context Layer Audit

Audit where your organisation's real knowledge lives. Produces a scored, benchmarked report with a prioritised action plan - the kind of deliverable you would normally pay a consultant for.

**What it does:**
- Maps where your knowledge lives across tools and teams
- Scores 6 dimensions with a weighted Context Health Score (out of 100)
- Benchmarks you against companies at your stage
- Identifies your top 3 knowledge gaps
- Generates a structured report you can share with leadership

**Say:** "Run a context layer audit"

---

## Test locally

If you have cloned this repo and want to test before publishing:

```
/plugin marketplace add ./skills
/plugin install content-engine@jamieoarton-skills
```

---

## Philosophy

These skills are designed to deliver real value, not just prompts. Each skill has a clear workflow, guardrails against generic AI output, and a quality checklist. They are written for busy business owners who want usable output, not creators chasing viral hacks.

If you get value from these, I write a weekly newsletter on practical AI strategy for mid-market businesses at [jamieoarton.com](https://jamieoarton.com). Free, no hype.

---

## License

MIT - use them however you like.
