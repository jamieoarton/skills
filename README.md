# Jamie's Skills

Personal productivity and automation skills for Claude Code and other AI systems.

## Overview

This marketplace provides **63 skills** organized into **6 modular plugins**. Install only what you need, or install all for the complete toolkit.

### Available Plugins

**jamie-skills-superpowers** (14 skills - from obra/superpowers)
- Test-driven development, systematic debugging, code review
- Planning, execution, and parallel agent coordination
- Git workflows and branch management

**jamie-skills-marketing** (29 skills - from coreyhaines31/marketingskills)
- Conversion optimization (CRO), copywriting, email marketing
- SEO, programmatic content, paid advertising
- Pricing strategy, launch planning, referral programs
- Marketing psychology, analytics, A/B testing

**jamie-skills-bramclaw** (6 skills)
- ClickUp, Gmail, Obsidian, Supabase, GitHub automation
- Delegated operations and multi-account support

**jamie-skills-business** (5 skills - Work The System methodology)
- Process documentation and systems thinking
- Strategic planning and operating principles

**jamie-skills-dev-tools** (8 skills)
- Agent creation and skill building frameworks
- Cursor IDE utilities

**jamie-skills-examples** (1 skill)
- Reference implementations

See [CREDITS.md](CREDITS.md) for attribution and sources.

## Installation

### Claude Code

**Step 1: Add the marketplace** (one time)
```bash
/plugin marketplace add jamieoarton/skills
```

**Step 2: Install plugins** (choose what you need)
```bash
# Workflow & Collaboration (14 skills)
/plugin install jamie-skills-superpowers@jamieoarton

# Marketing & Growth (29 skills)
/plugin install jamie-skills-marketing@jamieoarton

# BramClaw MCP Integrations (6 skills)
/plugin install jamie-skills-bramclaw@jamieoarton

# Business Systems (5 skills)
/plugin install jamie-skills-business@jamieoarton

# Development Tools (8 skills)
/plugin install jamie-skills-dev-tools@jamieoarton

# Examples (1 skill)
/plugin install jamie-skills-examples@jamieoarton
```

**Or install all plugins at once**:
```bash
/plugin install jamie-skills-superpowers@jamieoarton && \
  /plugin install jamie-skills-marketing@jamieoarton && \
  /plugin install jamie-skills-bramclaw@jamieoarton && \
  /plugin install jamie-skills-business@jamieoarton && \
  /plugin install jamie-skills-dev-tools@jamieoarton
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

Skills are automatically namespaced by plugin name:

```bash
# Superpowers skills
/jamie-skills-superpowers:brainstorming
/jamie-skills-superpowers:test-driven-development

# Marketing skills
/jamie-skills-marketing:page-cro
/jamie-skills-marketing:copywriting

# BramClaw MCP skills
/jamie-skills-bramclaw:bramclaw-clickup
/jamie-skills-bramclaw:bramclaw-gmail

# Business skills
/jamie-skills-business:strategic-objective-creation
/jamie-skills-business:fetch-youtube-transcript

# Dev Tools skills
/jamie-skills-dev-tools:skill-building-complete
/jamie-skills-dev-tools:bramclaw-agent-creation
```

### Other AI Systems

Skills are available directly by name (no namespace):

```
User: "I need help creating a strategic objective for Q2"
AI: [automatically triggers strategic-objective-creation skill]
```

## Updates

### Claude Code

Plugins update automatically when new versions are released. Check installed plugins:

```bash
/plugin list
```

Force update specific plugins:

```bash
# Update individual plugins
/plugin update jamie-skills-superpowers@jamieoarton
/plugin update jamie-skills-marketing@jamieoarton
/plugin update jamie-skills-bramclaw@jamieoarton

# Or update all at once
/plugin update jamie-skills-superpowers@jamieoarton && \
  /plugin update jamie-skills-marketing@jamieoarton && \
  /plugin update jamie-skills-bramclaw@jamieoarton && \
  /plugin update jamie-skills-business@jamieoarton && \
  /plugin update jamie-skills-dev-tools@jamieoarton
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
