---
name: short-video
description: Turn a voice-note transcript into a 60-second talking-head video script for TikTok, Reels, or YouTube Shorts. Use when the user has a transcript and wants a short-form video script. Trigger on "turn this into a TikTok", "write a short video script", "make a Reel from this", "60-second script from transcript", or short-form video requests.
metadata:
  version: 1.0.0
  author: Jamie Oarton - jamieoarton.com
  updated: 2026-04-06
---

# Short Video Script from Transcript

Turn a 10-15 minute voice recording transcript into a 60-second talking-head video script for TikTok, Instagram Reels, or YouTube Shorts.

This skill is part of the **Content Engine** - a set of four skills that turn one transcript into a week of content. The other skills are: linkedin, long-video, and newsletter.

## When to Use

Use when the user:
- Has a transcript from a voice recording, podcast, or meeting
- Wants it turned into a short-form video script
- Mentions TikTok, Reels, Shorts, or "60-second video"

Do NOT use for:
- Full long-form YouTube videos (use `long-video` instead)
- Voiceover scripts for B-roll footage without talking head
- Multi-part video series

## How to Use This Skill

### Step 1: Get the transcript

If the user has not already shared a transcript, ask them to paste it in. Any format is fine.

### Step 2: Ask the angle question

Before drafting:

> "What is the single most surprising, contrarian, or useful thing from your recording? That is what the 60 seconds needs to be about."

Short video has to pick ONE idea and hit it hard. Trying to cover two things kills engagement.

### Step 3: Draft the script

Follow this exact structure. Aim for 140-160 spoken words (60 seconds at 150 wpm).

```
[HOOK - First 3 seconds. One sentence.
 Must create curiosity, surprise, or name the reader's problem.
 Examples:
 - "Your LinkedIn posts are getting ignored. Here is why."
 - "I stopped doing X and my Y doubled."
 - "Most business owners get this wrong."]

[PAYOFF - Next 5-7 seconds. One sentence.
 Tell them what you are about to explain. Do NOT tease.]

[BODY - 40-45 seconds. 3-4 short points.
 Each point = one short sentence.
 Use "you" throughout.
 Keep the user's own phrases where they sound natural.]

[CLOSE - Final 5-7 seconds. One sentence.
 Either a soft CTA ("Follow for more") or a loop back to the hook.
 No "like and subscribe" begging.]
```

### Step 4: Format for the user

Show the script broken into sections with estimated timing. Example:

```
[0:00-0:03] HOOK
Your LinkedIn posts are getting ignored. Here is why.

[0:03-0:08] PAYOFF
It is not the algorithm. It is that you sound like AI wrote it.

[0:08-0:50] BODY
You start with "In today's fast-paced world". 
You use words like "leverage", "seamless", and "unlock".
Your hook is a vague question nobody asked.
Your middle is three bullet points with no opinion.
And your ending is a recycled quote from Einstein.

Real humans do not write like that. 
You are copying a template that AI learned from other AI.
Then you wonder why nobody stops scrolling.

The fix is not a better prompt. 
The fix is starting from your own words, not a blank page.

[0:50-0:60] CLOSE
Record yourself explaining one idea for two minutes. 
Type that out. Cut it in half. 
That is your post, and it will sound like you.

---
Word count: 148 (about 60 seconds at normal pace)
```

### Step 5: Apply these rules

Read `../../references/style.md` for the shared Content Engine house style (voice, British English, banned hype words, banned AI phrases). All of it applies here.

Short-video-specific rules on top:

- **140-160 words.** That is about 60 seconds at normal speaking pace.
- **First 3 seconds are everything.** If the hook is weak, stop and rewrite.
- **Speakable, not readable.** No complex clauses, no tongue-twisters.
- **No hashtags in the script.** Add 3-5 at the bottom as a separate caption block.
- **No jargon.** If a business owner would not use the word, do not use the word.
- **No begging.** No "please like and subscribe", no "smash that follow button".

### Step 6: Add a caption

Provide a separate caption block the user can copy for the post description:

```
CAPTION:
[One sentence restating the hook.]

[Optional one sentence with a question to invite comments.]

#BusinessStrategy #Leadership #AI
```

## Quality Checklist

Before showing the draft:

- [ ] Hook is under 10 words and specific
- [ ] Payoff in the first 8 seconds (no teasing)
- [ ] 140-160 words total
- [ ] All short sentences (under 15 words each)
- [ ] "You" is used in the hook
- [ ] At least 2 phrases lifted from the transcript
- [ ] No banned hype words
- [ ] No hashtags in the script body
- [ ] Reads aloud naturally (no tongue-twisters)

## Related Skills

Part of the Content Engine bundle:
- `linkedin` - 150-word LinkedIn post from the same transcript
- `long-video` - 5-8 minute video outline from the same transcript
- `newsletter` - 1000-word newsletter from the same transcript
