# Changelog - bramclaw-clickup

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-21

### Added
- Progressive disclosure structure (scripts/, references/, tests/, assets/)
- Explicit trigger patterns ("ClickUp", "tasks", "create task", "workspace")
- Success metrics framework (triggering accuracy, token reduction, API efficiency, security)
- Decision framework (when to use vs. ClickUp UI, MCP, Maton proxy)
- Comprehensive reference documentation:
  - api-reference.md (complete API method documentation)
  - common-queries.md (cookbook of query patterns)
  - security-model.md (defense in depth architecture + comparison table)
  - error-handling.md (error patterns + rate limits + monitoring)
  - success-metrics.md (measurement framework + baselines)
- Version metadata in frontmatter
- CHANGELOG.md
- Skill confidence levels (high/medium/low)
- Alternatives comparison table (bramclaw vs UI vs MCP vs Maton)

### Changed
- Moved clickup_agent.py to scripts/ directory
- Moved clickup_client.py to scripts/ directory
- Refactored SKILL.md to overview with cross-references (438 → 355 lines, 19% reduction)
- Updated description to include trigger keywords
- Security model emphasized direct API (no Maton.ai proxy)

### Removed
- Detailed API reference from SKILL.md (moved to references/api-reference.md)
- Common query examples from SKILL.md (moved to references/common-queries.md)
- Security comparison table from SKILL.md (moved to references/security-model.md)
- Error handling patterns from SKILL.md (moved to references/error-handling.md)
- Monitoring guidance from SKILL.md (moved to references/error-handling.md)
- Testing examples from SKILL.md (moved to tests/TEST-PLAN.md)

## [1.0.0] - 2026-02-20

### Added
- Initial production release
- Direct ClickUp API access using API key authentication
- No third-party proxy (unlike ClawHub Maton skill)
- Read operations (workspaces, spaces, folders, lists, tasks, users)
- Write operations with human approval requirement (create/update/delete tasks)
- clickup_agent.py CLI interface
- clickup_client.py API client library
- Security tier: approved-with-controls
- Production status

[2.0.0]: https://github.com/bramforth/bram-claw/compare/v1.0.0-clickup...v2.0.0-clickup
[1.0.0]: https://github.com/bramforth/bram-claw/releases/tag/v1.0.0-clickup
