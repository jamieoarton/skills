# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-02-24

### Fixed
- Moved `marketplace.json` to `.claude-plugin/` directory (Claude expects it there, not at root)
- Fixes marketplace installation error

## [1.1.0] - 2026-02-24

### Added

**Superpowers Skills Integration (15 skills)**
- Integrated excellent workflow skills from https://github.com/obra/superpowers
- Testing: test-driven-development, systematic-debugging, verification-before-completion
- Planning: brainstorming, writing-plans, executing-plans, dispatching-parallel-agents, subagent-driven-development
- Code Review: requesting-code-review, receiving-code-review
- Git: using-git-worktrees, finishing-a-development-branch
- Meta: using-superpowers, writing-skills, skill-creator

**Cursor Utility Skills (5 skills)**
- create-rule, create-skill, create-subagent, migrate-to-skills, update-cursor-settings

**Documentation**
- CREDITS.md - Complete attribution for all sources
- Updated README with all 34 skills organized by category

### Changed
- Total skills: 13 → 34 (+161% growth)
- Reorganized README into four categories
- Added proper MIT License attribution for Superpowers

## [1.0.0] - 2026-02-24

### Added

**Initial plugin release with 13 skills**

#### Business & Productivity Skills
- `fetch-youtube-transcript` - Download YouTube transcripts
- `work-the-system-mindset` - Systems thinking methodology
- `strategic-objective-creation` - Strategic planning framework
- `operating-principles-development` - Decision-making principles
- `working-procedures-documentation` - Process documentation

#### BramClaw MCP Skills
- `bramclaw-clickup` - ClickUp task management
- `bramclaw-gmail` - Gmail read operations
- `bramclaw-gmail-delegated-send` - Gmail delegated sending
- `bramclaw-obsidian` - Obsidian vault management
- `bramclaw-supabase` - Supabase database operations
- `bramclaw-github` - GitHub operations

#### Development Tools
- `bramclaw-agent-creation` - BramClaw agent creation framework
- `skill-building-complete` - Complete skill building toolkit

### Infrastructure
- Plugin manifest configuration
- Marketplace catalog setup
- Multi-AI system support (symlinks)
- README and documentation
- MIT License

---

## Future Releases

### Planned Features
- Split into specialized plugins by use case (business, automation, dev-tools)
- Additional BramClaw MCP integrations
- Enhanced metrics and measurement tools
- Automated testing and validation

---

[1.0.0]: https://github.com/jamieoarton/skills/releases/tag/v1.0.0
