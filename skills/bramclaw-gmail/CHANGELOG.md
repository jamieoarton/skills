# Changelog - bramclaw-gmail

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-21

### Added
- Progressive disclosure structure (scripts/, references/, assets/)
- Explicit trigger patterns ("Gmail", "email", "inbox", etc.)
- Success metrics framework (triggering accuracy, token reduction, API efficiency)
- Decision framework (when to use vs. Gmail UI, MCP, raw API)
- Detailed reference documentation:
  - setup-guide.md (service account configuration)
  - search-queries.md (Gmail query syntax cookbook)
  - api-operations.md (API reference)
  - success-metrics.md (measurement framework)
- Version metadata in frontmatter
- CHANGELOG.md

### Changed
- Moved gmail_agent.py to scripts/ directory
- Kept gmail_test.py in tests/ directory and aligned docs with test location
- Refactored SKILL.md to overview with cross-references (150 lines)
- Updated description to include trigger keywords

### Removed
- Detailed setup instructions from SKILL.md (moved to references/setup-guide.md)
- Gmail query syntax from SKILL.md (moved to references/search-queries.md)
- API reference from SKILL.md (moved to references/api-operations.md)

## [1.0.0] - 2026-02-20

### Added
- Initial production release
- Service account + domain-wide delegation authentication
- Read-only operations (list, get, search)
- gmail_agent.py CLI interface
- gmail_test.py test harness
- Security tier: approved
- Production status

[2.0.0]: https://github.com/bramforth/bram-claw/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/bramforth/bram-claw/releases/tag/v1.0.0
