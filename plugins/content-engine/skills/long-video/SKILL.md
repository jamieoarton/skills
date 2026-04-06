---
name: long-video
description: Turn a voice-note transcript into a 5-8 minute talking-head YouTube video outline with intro, sections, and CTA. Use when the user has a transcript and wants a long-form video outline. Trigger on "turn this into a YouTube video", "write a long video script", "YouTube outline from transcript", or long-form video requests.
metadata:
  version: 1.0.0
  author: Jamie Oarton - jamieoarton.com
  updated: 2026-04-06
---

# Long Video Outline from Transcript

Turn a 10-15 minute voice recording transcript into a structured 5-8 minute YouTube video outline with an intro hook, main sections, and a call to action.

This skill is part of the **Content Engine** - a set of four skills that turn one transcript into a week of content. The other skills are: linkedin, short-video, and newsletter.

## When to Use

Use when the user:
- Has a transcript from a voice recording, podcast, or meeting
- Wants a long-form YouTube video outline (5-8 minutes)
- Mentions "long video", "YouTube video", "video outline", or similar

Do NOT use for:
- Short-form video (under 90 seconds) - use `short-video` instead
- Written articles - use `newsletter` instead
- Full word-for-word scripts (this skill produces outlines, not scripts)

## Output Format

This skill produces an **outline**, not a full script. A good outline has:
- Clear section boundaries with timing
- Bullet points for each section
- The user's own phrases highlighted where they should be delivered verbatim
- Notes on what to say but not exact wording for every sentence

Why an outline and not a script? Scripts make talking heads sound robotic. Outlines let the user speak naturally while hitting the key points.

## How to Use This Skill

### Step 1: Get the transcript

If the user has not already shared a transcript, ask them to paste it in.

### Step 2: Ask the scoping questions

Before drafting, ask:

> "Two quick questions:
> 1. What is the main thing you want viewers to take away?
> 2. Who is the ideal viewer - business owner, practitioner, leader?"

This shapes the framing and the CTA.

### Step 3: Extract the structure

Read through the transcript and identify:

- The strongest single insight (this becomes the thesis)
- 3-4 supporting points (these become sections)
- Any concrete examples, stories, or numbers (these go in the relevant section)
- Any strong phrases the user said (mark these for verbatim delivery)

### Step 4: Build the outline

Use this structure exactly:

```
# Video Title: [Specific, curiosity-driven, under 60 characters]

**Target length:** 5-8 minutes
**Audience:** [From user's answer]
**Core thesis:** [One sentence - the main takeaway]

---

## 0:00-0:30 - Intro Hook (30 seconds)

**Goal:** Make the viewer need to watch the next 7 minutes.

- Open with [specific hook from the transcript, preferably a surprising stat or contrarian claim]
- Say: "[exact phrase to use verbatim]"
- Name the problem the viewer has
- Tell them what they will learn (no teasing)

---

## 0:30-1:30 - Context / Why This Matters (60 seconds)

**Goal:** Ground the thesis in the viewer's reality.

- [Bullet point]
- [Bullet point]
- Key phrase to use: "[lifted from transcript]"
- Personal anchor: [if the transcript includes one, note it here]

---

## 1:30-3:30 - Main Point 1: [Section Title] (2 minutes)

**Goal:** [What this section proves]

- [Bullet point from transcript]
- [Bullet point]
- Example to reference: [from transcript]
- Stat or number to cite: [if applicable]
- Transition line: "[lead into next section]"

---

## 3:30-5:30 - Main Point 2: [Section Title] (2 minutes)

[Same structure as above]

---

## 5:30-7:00 - Main Point 3 or Counterpoint: [Section Title] (90 seconds)

[Same structure as above]

---

## 7:00-8:00 - Close and CTA (60 seconds)

**Goal:** Leave one clear action in the viewer's head.

- Summarise the thesis in one sentence
- State what the viewer should do differently
- Soft CTA: [based on user's platform and audience]
  - E.g., "Subscribe for more practical AI content"
  - E.g., "If this was useful, the full guide is at [link]"
- End on a strong line - ideally a callback to the opening hook

---

## Shot Notes (Optional)

- Talking head throughout, no B-roll required
- Mark any moments where a graphic or stat overlay would help
- Suggest a thumbnail concept based on the strongest visual idea

---

## Notes for Delivery

- **Do not read the bullets word-for-word.** Use them as a map, speak naturally.
- **The quoted phrases should be delivered verbatim** - they are the lines from your own transcript that worked best.
- **Pause between sections.** Gives breathing room for edits.
- **If you go off-script and it is better, keep going.** The outline is a safety net, not a cage.
```

### Step 5: Apply these rules

Read `../../references/style.md` for the shared Content Engine house style (voice, British English, banned hype words, banned AI phrases). All of it applies here.

Long-video-specific rules on top:

- **5-8 minutes target.** Longer than 8 minutes loses retention; shorter than 5 feels thin.
- **Clear section timing.** Every section gets an explicit time window.
- **Lift at least 3-5 strong phrases verbatim** from the transcript and mark them for verbatim delivery.
- **Outline, not script.** Bullets for content, full sentences only for verbatim deliveries.
- **No hashtags anywhere.** This is a YouTube video, not a social post.

### Step 6: Offer metadata

After the outline, offer to generate:
- 3 title options (different angles)
- A video description (200 words, with timestamps)
- 5 chapter markers

Ask the user if they want these before generating.

## Quality Checklist

Before showing the outline:

- [ ] Target length is 5-8 minutes
- [ ] Intro hook is specific (not "in this video I will explain")
- [ ] 3-4 main sections with clear timing
- [ ] Each section has bullet points from the transcript
- [ ] At least 3-5 verbatim phrases marked for delivery
- [ ] CTA is soft and specific, not generic
- [ ] No banned hype words
- [ ] British spelling throughout

## Related Skills

Part of the Content Engine bundle:
- `linkedin` - 150-word LinkedIn post from the same transcript
- `short-video` - 60-second TikTok/Reels script from the same transcript
- `newsletter` - 1000-word newsletter from the same transcript
