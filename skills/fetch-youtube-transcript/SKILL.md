---
name: fetch-youtube-transcript
description: Use when user requests downloading, fetching, or getting a YouTube video transcript or subtitles
---

# Fetch YouTube Transcript

## Overview

Downloads YouTube video transcripts using Apify API and saves to Obsidian vault with proper metadata and formatting.

**Save Location:** `/Users/jimeny/Library/CloudStorage/GoogleDrive-jamie@bramforth.ai/My Drive/Obsidian/Bramforth Obsidian/Content-Channels/YouTube/Transcripts/`

## When to Use

Use when:
- User provides YouTube URL and requests transcript
- User says "download transcript", "get transcript", "fetch subtitles"
- User wants to read/analyze video content later

Do NOT use for:
- YouTube video downloads (video/audio files)
- Playlist operations
- Channel scraping

## Prerequisites

**Environment variable:**
- `APIFY_API_KEY` must be set in `~/.env` or current directory `.env`

**Python packages:**
- `requests`
- `python-dotenv`

Install if missing: `python3 -m pip install --break-system-packages requests python-dotenv`

**Script location:**
- `~/bin/fetch_youtube_transcript.py` (installed globally)
- If missing, user needs to install it first

## Implementation

### Step 1: Fetch the transcript

**Do NOT ask questions. Execute directly:**

```bash
~/bin/fetch_youtube_transcript.py "<youtube_url>"
```

The script will save to:
`/Users/jimeny/Library/CloudStorage/GoogleDrive-jamie@bramforth.ai/My Drive/Obsidian/Bramforth Obsidian/Content-Channels/YouTube/Transcripts/YYYYMMDD-Channel-Name-Video-Title-transcript.md`

### Step 2: Read the transcript file

After the script completes, capture the filepath from output and read it:

```bash
# The filepath is shown in script output
```

Use the Read tool to access the transcript content.

### Step 3: Create summary/action points file

Analyze the transcript and create a second file with:

**Filename:** Same as transcript but replace `-transcript.md` with `-summary.md`

**Content structure:**
```markdown
# [Video Title] - Summary & Action Points

## Key Takeaways
- [Main insights from the video]
- [Important concepts covered]

## Action Items
- [ ] [Concrete steps to implement the learnings]
- [ ] [Practical applications]

## Implementation Notes
[Any specific examples, code snippets, or practical guidance mentioned]

---
Source: [YouTube URL]
```

Use the Write tool to create this file in the same Obsidian vault directory.

### Step 4: Expected output

Two files created in Obsidian vault:
1. `YYYYMMDD-Channel-Name-Video-Title-transcript.md` - Full transcript
2. `YYYYMMDD-Channel-Name-Video-Title-summary.md` - Summary & actions

**Location:** `/Users/jimeny/Library/CloudStorage/GoogleDrive-jamie@bramforth.ai/My Drive/Obsidian/Bramforth Obsidian/Content-Channels/YouTube/Transcripts/`

**Transcript file format:**
```markdown
# Video Title

**Channel:** Channel Name
**Video ID:** abc123
**URL:** https://youtube.com/watch?v=abc123
**Duration:** HH:MM:SS
**Views:** 123456
**Date:** ISO date

## About

[Video description]

================================================================================

## Transcript

[Continuous text without line breaks every 7 words]
```

**Summary file format:**
```markdown
# Video Title - Summary & Action Points

## Key Takeaways
- [Main insights]

## Action Items
- [ ] [Actionable steps]

## Implementation Notes
[Practical guidance]

---
Source: [YouTube URL]
```

## Red Flags

If you're thinking:
- "youtube-transcript-api would be faster"
- "Let me check if the script exists first"
- "I should ask about format preferences"
- "Maybe I'll create a simpler version"
- "The user didn't ask for a summary, so I'll skip that"
- "I'll just return the transcript path without creating summary"

**STOP. Always:**
1. Use `~/bin/fetch_youtube_transcript.py` immediately
2. Read the transcript file after it's created
3. Create the summary/action points file - EVERY TIME

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Asking user about format/location | Don't ask - script has defaults |
| Using youtube-transcript-api | Use Apify (avoids permission errors) |
| Only creating transcript file | MUST create both transcript AND summary files |
| Skipping summary creation | Always analyze and create summary - it's required |
| Wrong filename format | Must be: `YYYYMMDD-Channel-Title-transcript.md` and `-summary.md` |
| Checking if script exists first | Just run it - error will tell you if missing |
| Not reading transcript before summary | Must read transcript to create accurate summary |

## Why Apify

YouTube's direct transcript API frequently returns permission errors. Apify's scraper is more reliable for automated access.

## Script Configuration

Key Apify parameters:
```python
input_data = {
    "startUrls": [{"url": youtube_url}],
    "maxResults": 1,
    "downloadSubtitles": True,
    "subtitlesFormat": "plaintext"
}
```

Extract transcript from response:
```python
subtitles = video_data.get('subtitles', [])
transcript = subtitles[0].get('plaintext', '')
# Remove line breaks: ' '.join(transcript.split())
```
