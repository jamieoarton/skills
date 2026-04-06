---
name: linkedin
description: Turn a voice-note transcript into a 150-word LinkedIn post for business owners. Use when the user has a transcript (from a recording, video, or meeting) and wants a LinkedIn post drafted from it. Trigger on "turn this into a LinkedIn post", "write a LinkedIn post from this transcript", "draft a LinkedIn post", or when the user shares a transcript and mentions LinkedIn.
metadata:
  version: 1.0.0
  author: Jamie Oarton - jamieoarton.com
  updated: 2026-04-06
---

# LinkedIn Post from Transcript

Turn a 10-15 minute voice recording transcript into a clear, 150-word LinkedIn post that business owners will actually read.

This skill is part of the **Content Engine** - a set of four skills that turn one transcript into a week of content. The other skills are: short-video, long-video, and newsletter.

## When to Use

Use when the user:
- Has a transcript from a voice recording, podcast, video, or meeting
- Wants it turned into a LinkedIn post
- Asks for "a LinkedIn post from this" or similar

Do NOT use for:
- Posts written from scratch without source material (the whole point is to preserve the user's voice)
- Multi-post LinkedIn threads or articles
- LinkedIn comments or replies

## How to Use This Skill

### Step 1: Get the transcript

If the user has not already shared a transcript, ask them to paste it in. Accept any format - cleaned or raw with "ums" and false starts is fine.

### Step 2: Check if the user wants a specific angle

Before drafting, ask one question:

> "What is the single most important thing you want the reader to take away from this post?"

This matters because a 10-minute transcript usually contains 3-5 distinct ideas. The user needs to pick one. If they cannot, pick the idea that appears most often or has the strongest opinion behind it.

### Step 3: Draft the post

Follow this structure exactly. 150 words total, not more.

```
[HOOK - 1 or 2 short sentences. A clear opinion, observation, or question. 
 No "hot take", no "here is the truth". Just say the thing.]

[CONTEXT - 2 or 3 sentences. Why this matters to the reader. 
 Use "you" not "we" or "people".]

[THE POINT - 2 or 3 sentences. The main insight from the transcript. 
 Keep the user's phrasing where possible.]

[PRACTICAL TAKEAWAY - 1 or 2 sentences. What the reader should do, 
 think about, or stop doing.]

[SOFT CLOSE - 1 short sentence. Optional question inviting a comment.]
```

### Step 4: Apply these rules

Read `../../references/style.md` for the shared Content Engine house style (voice, British English, banned hype words, banned AI phrases). All of it applies here.

LinkedIn-specific rules on top:

- **150 words maximum.** Count them. Cut adjectives before cutting ideas.
- **Grade 6-8 reading level.** Short sentences. Simple words. If you can say it in one syllable, do.
- **One idea only.** Do not try to cover three things.
- **Hashtags at the very end** on their own line, 3-5 of them.

### Step 5: Show the draft

Show the post with a word count at the bottom. Ask if the user wants changes.

Example output format:

```
[POST TEXT HERE]

#BusinessStrategy #Leadership #AI

---
Word count: 148 / 150
```

### Step 6: Iterate if needed

If the user asks for changes, keep the voice consistent with the transcript. Do not "improve" the user's phrasing unless it is unclear.

## Quality Checklist

Before showing the draft, verify:

- [ ] 150 words or fewer
- [ ] Hook is specific, not generic
- [ ] The reader is addressed as "you"
- [ ] At least one phrase is lifted directly from the transcript
- [ ] No banned hype words
- [ ] No em-dashes
- [ ] British spelling throughout
- [ ] One clear takeaway
- [ ] Sounds like a real person, not AI

## Why This Works

Most LinkedIn posts sound like AI because they start with "write a LinkedIn post about [topic]". The AI then invents content that has no opinion, no voice, and no specific perspective.

Starting with a transcript means:
- The opinion is already yours
- The voice is already yours
- The examples and stories are real

The skill's job is to compress, not create. That is why the output sounds like you.

## Related Skills

Part of the Content Engine bundle:
- `short-video` - 60-second script from the same transcript
- `long-video` - 5-8 minute video outline from the same transcript
- `newsletter` - 1000-word newsletter from the same transcript

All four work from the same source transcript. Record once, publish four times.
