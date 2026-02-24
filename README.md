# Jamie's Skills

Personal productivity and automation skills for Claude Code and other AI systems.

## Overview

This plugin provides **34 skills** across four categories:

**Workflow & Collaboration** (Superpowers)
- Test-driven development, systematic debugging, code review
- Planning, execution, and parallel agent coordination
- Git workflows and branch management

**Business Systems** (Work The System methodology)
- Process documentation and systems thinking
- Strategic planning and operating principles

**BramClaw MCP Integrations**
- ClickUp, Gmail, Obsidian, Supabase, GitHub automation
- Delegated operations and multi-account support

**Development Tools**
- Agent creation and skill building frameworks
- Cursor IDE utilities

See [CREDITS.md](CREDITS.md) for attribution and sources.

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

### Workflow & Collaboration (Superpowers)

**Testing & Quality**
- `test-driven-development` - TDD methodology
- `systematic-debugging` - Structured debugging
- `verification-before-completion` - Pre-completion checks

**Planning & Execution**
- `brainstorming` - Creative exploration
- `writing-plans` - Multi-step planning
- `executing-plans` - Plan execution
- `dispatching-parallel-agents` - Concurrent coordination
- `subagent-driven-development` - Independent tasks

**Code Review**
- `requesting-code-review` - Submit for review
- `receiving-code-review` - Process feedback

**Git Workflows**
- `using-git-worktrees` - Isolated workspaces
- `finishing-a-development-branch` - Branch completion

**Meta-Skills**
- `using-superpowers` - Skill system introduction
- `writing-skills` - Skill creation
- `skill-creator` - Skill toolkit

### Business & Productivity

- `fetch-youtube-transcript` - YouTube transcript extraction
- `work-the-system-mindset` - Systems thinking framework
- `strategic-objective-creation` - Strategic planning
- `operating-principles-development` - Decision principles
- `working-procedures-documentation` - Process documentation

### BramClaw MCP Skills

- `bramclaw-clickup` - ClickUp task management
- `bramclaw-gmail` - Gmail read operations
- `bramclaw-gmail-delegated-send` - Gmail delegated sending
- `bramclaw-obsidian` - Obsidian vault management
- `bramclaw-supabase` - Supabase database operations
- `bramclaw-github` - GitHub operations

### Development Tools

- `bramclaw-agent-creation` - BramClaw agent creation framework
- `skill-building-complete` - Complete skill building toolkit
- `create-rule` - Cursor rule creation
- `create-skill` - Cursor skill creation
- `create-subagent` - Cursor subagent creation
- `migrate-to-skills` - Migrate to skills system
- `update-cursor-settings` - Update Cursor config

For detailed descriptions, see individual skill SKILL.md files.

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
