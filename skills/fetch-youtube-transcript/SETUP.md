# Setup Instructions for fetch-youtube-transcript Skill

This skill enables Claude Code to download YouTube transcripts using Apify API.

## Installation (for other computers)

### 1. Copy the skill

```bash
# On this computer, package the skill
cd ~/.claude/skills
tar -czf fetch-youtube-transcript.tar.gz fetch-youtube-transcript/

# Transfer to other computer, then:
cd ~/.claude/skills
tar -xzf fetch-youtube-transcript.tar.gz
```

Or manually copy `~/.claude/skills/fetch-youtube-transcript/` directory.

### 2. Install the script

Copy `~/bin/fetch_youtube_transcript.py` to the same location on the new computer:

```bash
# Make sure ~/bin exists
mkdir -p ~/bin

# Copy script (from this computer)
scp ~/bin/fetch_youtube_transcript.py user@other-computer:~/bin/

# Or manually copy the file
# Make it executable
chmod +x ~/bin/fetch_youtube_transcript.py
```

### 3. Set up environment

Add your Apify API key to `~/.env`:

```bash
echo "APIFY_API_KEY=your_apify_api_key_here" >> ~/.env
```

### 4. Install Python dependencies

```bash
python3 -m pip install --break-system-packages requests python-dotenv
```

### 5. Test it

From any directory:

```bash
~/bin/fetch_youtube_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Should create file in Obsidian vault at:
`/Users/jimeny/Library/CloudStorage/GoogleDrive-jamie@bramforth.ai/My Drive/Obsidian/Bramforth Obsidian/Content-Channels/YouTube/Transcripts/YYYYMMDD-Channel-Title-transcript.md`

## What Gets Installed

- **Skill**: `~/.claude/skills/fetch-youtube-transcript/SKILL.md` (Claude Code reference)
- **Script**: `~/bin/fetch_youtube_transcript.py` (executable script)
- **API Key**: `~/.env` (contains APIFY_API_KEY)
- **Dependencies**: Python packages `requests` and `python-dotenv`

## How It Works

1. User asks Claude Code to download a YouTube transcript
2. Skill triggers automatically (no `/` command needed)
3. Claude executes `~/bin/fetch_youtube_transcript.py "<url>"`
4. Script uses Apify API to fetch transcript with metadata
5. Saves to Obsidian vault: `/Users/jimeny/Library/CloudStorage/GoogleDrive-jamie@bramforth.ai/My Drive/Obsidian/Bramforth Obsidian/Content-Channels/YouTube/Transcripts/`

## Troubleshooting

**"Command not found"**
- Ensure script is in `~/bin/` and is executable: `chmod +x ~/bin/fetch_youtube_transcript.py`

**"APIFY_API_KEY not found"**
- Check `~/.env` exists and contains: `APIFY_API_KEY=your_key_here`

**"No module named 'requests'"**
- Install dependencies: `python3 -m pip install --break-system-packages requests python-dotenv`

**Skill not triggering**
- Skill file must be at: `~/.claude/skills/fetch-youtube-transcript/SKILL.md`
- Restart Claude Code after adding skill
