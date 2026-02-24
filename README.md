# Jamie's Skills

Personal productivity and automation skills for Claude Code and other AI systems.

## Overview

This plugin provides 13 skills across three categories:

**Business Systems** (Work The System methodology)
- Process documentation and systems thinking
- Strategic planning and operating principles

**BramClaw MCP Integrations**
- ClickUp, Gmail, Obsidian, Supabase, GitHub automation
- Delegated operations and multi-account support

**Development Tools**
- Agent creation and skill building frameworks

## Installation

### Claude Code

```bash
# Add marketplace
/plugin marketplace add jamieoarton/skills

# Install plugin
/plugin install jamie-skills@jamieoarton
```

### Other AI Systems (Codex, Gemini, etc.)

```bash
# Clone repository
cd ~/git
git clone git@github.com:jamieoarton/skills.git

# Create symlink to your AI system
ln -s ~/git/skills/skills ~/.codex/skills
ln -s ~/git/skills/skills ~/.gemini/skills
# ... adjust path for your system
```

## Skills Included

### Business & Productivity

**`fetch-youtube-transcript`**
Download and extract YouTube video transcripts for analysis.

**`work-the-system-mindset`**
Apply systems thinking methodology to business challenges. Use when feeling overwhelmed, reactive, or unable to identify root causes.

**`strategic-objective-creation`**
Create concrete strategic objectives with measurable outcomes. Use when organization lacks clear direction or has conflicting priorities.

**`operating-principles-development`**
Develop decision-making principles and values frameworks. Use when decisions lack consistency across team members.

**`working-procedures-documentation`**
Document repeatable procedures to reduce training time and execution inconsistency. Use when same problems recur or quality varies.

### BramClaw MCP Skills

**`bramclaw-clickup`**
ClickUp task management via API. Read/write tasks, lists, workspaces with authorization governance.

**`bramclaw-gmail`**
Gmail operations (read messages, search, mark read). Separate from delegated-send for security.

**`bramclaw-gmail-delegated-send`**
Send emails on behalf of principal with explicit confirmation workflow.

**`bramclaw-obsidian`**
Obsidian vault management via Google Drive API. Read/write notes, search, frontmatter updates.

**`bramclaw-supabase`**
Supabase database operations with security gates for schema changes.

**`bramclaw-github`**
GitHub operations (repositories, issues, PRs) with authorization governance.

### Development Tools

**`bramclaw-agent-creation`**
Create new BramClaw OpenClaw agents with complete bootstrap files, authorization governance, and validation checklists.

**`skill-building-complete`**
Complete skill building framework with MCP integration patterns, success metrics, distribution workflows, and troubleshooting guides.

## Usage

### Claude Code

Skills are automatically namespaced as `/jamie-skills:skill-name`:

```bash
# Example: Fetch YouTube transcript
/jamie-skills:fetch-youtube-transcript https://youtube.com/watch?v=...

# Example: Create strategic objective
/jamie-skills:strategic-objective-creation

# Example: Create BramClaw agent
/jamie-skills:bramclaw-agent-creation
```

### Other AI Systems

Skills are available directly by name (no namespace):

```
User: "I need help creating a strategic objective for Q2"
AI: [automatically triggers strategic-objective-creation skill]
```

## Updates

### Claude Code

Plugin updates automatically when new versions are released. Check installed version:

```bash
/plugin list
```

Force update:

```bash
/plugin update jamie-skills@jamieoarton
```

### Other AI Systems

```bash
cd ~/git/skills
git pull origin main
```

Changes are immediately available via symlink.

## Development

### Making Changes

```bash
cd ~/git/skills

# Make changes to skills/some-skill/SKILL.md
git add .
git commit -m "feat: improve some-skill"

# Bump version in .claude-plugin/plugin.json
# Then commit and push
git push origin main
```

### Testing Locally

```bash
# Test plugin without installing
claude --plugin-dir ~/git/skills
```

## Structure

```
~/git/skills/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── marketplace.json           # Marketplace catalog
├── skills/                    # All skills (auto-discovered)
│   ├── fetch-youtube-transcript/
│   │   └── SKILL.md
│   ├── bramclaw-agent-creation/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   └── ... (11 more skills)
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Jamie Oarton (jamie@bramforth.ai)
- GitHub: [@jamieoarton](https://github.com/jamieoarton)
- Repository: [jamieoarton/skills](https://github.com/jamieoarton/skills)

## Support

For issues or questions:
1. Check skill documentation (each skill has detailed SKILL.md)
2. Review troubleshooting guide in `skill-building-complete/references/troubleshooting-guide.md`
3. Open an issue on [GitHub](https://github.com/jamieoarton/skills/issues)
