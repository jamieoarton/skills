---
name: newsletter
description: Turn a voice-note transcript into a 1000-word newsletter or blog post. Use when the user has a transcript and wants a long-form written piece. Trigger on "turn this into a newsletter", "write a blog post from this transcript", "newsletter from transcript", or long-form written content requests.
metadata:
  version: 1.0.0
  author: Jamie Oarton - jamieoarton.com
  updated: 2026-04-06
---

# Newsletter from Transcript

Turn a 10-15 minute voice recording transcript into a 1000-word newsletter or blog post that keeps the user's voice and opinions intact.

This skill is part of the **Content Engine** - a set of four skills that turn one transcript into a week of content. The other skills are: linkedin, short-video, and long-video.

## When to Use

Use when the user:
- Has a transcript from a voice recording, podcast, or meeting
- Wants it turned into a newsletter edition or blog post
- Mentions "newsletter", "blog post", "Substack edition", "Beehiiv post", or "long-form article"

Do NOT use for:
- Short social posts (use `linkedin`)
- Video scripts (use `short-video` or `long-video`)
- Full books or e-books (way beyond scope)

## How to Use This Skill

### Step 1: Get the transcript

If the user has not already shared a transcript, ask them to paste it in.

### Step 2: Ask the scoping questions

Before drafting, ask these three:

> "Three quick questions to shape the piece:
> 1. What is the single most important thing you want the reader to take away?
> 2. Who is the reader - business owner, practitioner, leader, creator?
> 3. What should they do differently after reading it?"

These three answers give you: thesis, voice, and CTA.

### Step 3: Build the structure

Use this structure exactly. Target 950-1050 words total.

```
# [Title]

[Subtitle or one-line description]

---

[INTRO - 100-150 words]
Open with the strongest single idea from the transcript.
Not a question. Not "in this post I will". Just say the thing.
End the intro with a one-sentence promise of what the reader will get.

## [First Section Heading - the "what"]

[150-200 words]
Establish the problem or the observation.
Use the reader's situation, not yours.
Include at least one specific phrase lifted verbatim from the transcript.

## [Second Section Heading - the "why"]

[200-250 words]
Explain what is actually going on.
Include a number, example, or comparison from the transcript if there is one.
This is where the main insight goes.

## [Third Section Heading - the "how"]

[200-250 words]
What the reader can do about it.
Make it concrete. "Stop doing X" is better than "consider stopping X".
If there are 2-3 practical steps, use a short numbered list.

## [Fourth Section Heading - the twist, counterpoint, or nuance]

[100-150 words]
Add one layer of depth. What most people get wrong about this.
Where the advice does not apply. A common objection you would expect.
Gives the piece more weight than a "5 tips" article.

## [Close Heading - optional]

[50-100 words]
Loop back to the intro thesis.
State what the reader should do differently this week.
End on one strong line.

---

[SIGN-OFF]
Jamie
```

### Step 4: Apply these rules

Read `../../references/style.md` for the shared Content Engine house style (voice, British English, banned hype words, banned AI phrases). All of it applies here.

Newsletter-specific rules on top:

- **950-1050 words total.** Count them. If over, cut adjectives and transitions before cutting ideas.
- **Grade 8-10 reading level.** Slightly more sophisticated than social posts, but still accessible to a busy business owner.
- **Lift at least 4-6 phrases verbatim** from the transcript.
- **One key idea per section.** If a section has two ideas, split it or cut one.
- **Headings should be descriptive, not cute.** "Why most AI pilots fail" beats "The pilot problem".

### Step 5: Show the draft

Show the full newsletter with:
- Title
- Word count at the bottom
- Reading time estimate (words / 200)

Example footer:

```
---
Word count: 1,020
Reading time: 5 minutes
```

### Step 6: Offer to generate supporting assets

After the draft, offer to generate:
- **Subject line options** (3 variations, under 50 characters each)
- **Preview text** (one line, under 100 characters)
- **Social share snippet** (1-2 sentences the user can copy for LinkedIn or X)

Ask before generating.

## Quality Checklist

Before showing the draft:

- [ ] 950-1050 words
- [ ] Title is specific, not generic
- [ ] Intro makes a clear promise
- [ ] 4-5 sections with descriptive headings
- [ ] At least 4 phrases lifted verbatim from the transcript
- [ ] Each section has one clear point
- [ ] "You" is the main pronoun
- [ ] Practical takeaway in the "how" section
- [ ] No banned hype words
- [ ] No em-dashes
- [ ] British spelling throughout
- [ ] Sounds like the user, not a content farm

## Related Skills

Part of the Content Engine bundle:
- `linkedin` - 150-word LinkedIn post from the same transcript
- `short-video` - 60-second TikTok/Reels script from the same transcript
- `long-video` - 5-8 minute YouTube video outline from the same transcript

All four work from the same source transcript. Record once, publish four times.
