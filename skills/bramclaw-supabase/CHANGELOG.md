# Changelog - bramclaw-supabase

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-21

### Added
- Progressive disclosure structure (scripts/, references/, tests/, assets/)
- Explicit trigger patterns ("Supabase", "security advisors", "project logs", etc.)
- Success metrics framework (triggering accuracy, token reduction, API efficiency, security alert response)
- Decision framework (when to use vs. Supabase CLI, UI, MCP)
- Comprehensive reference documentation:
  - setup-guide.md (token authentication and configuration)
  - security-advisors.md (security monitoring and email alert workflow)
  - api-operations.md (complete API reference)
  - error-handling.md (error patterns, rate limits, monitoring)
  - success-metrics.md (measurement framework with baselines)
- Version metadata in frontmatter
- CHANGELOG.md
- Skill confidence levels (high/medium/low)
- Alternatives comparison table (bramclaw vs CLI vs UI vs MCP)

### Changed
- Moved supabase_agent.py to scripts/ directory
- Moved supabase_client.py to scripts/ directory
- Refactored SKILL.md to overview with cross-references (349 → 372 lines, +6.6% with added features)
- Updated description to include trigger keywords
- Security model emphasized direct API (no third-party proxy)

### Removed
- Detailed setup instructions from SKILL.md (moved to references/setup-guide.md)
- Security advisor details from SKILL.md (moved to references/security-advisors.md)
- API reference from SKILL.md (moved to references/api-operations.md)
- Error handling patterns from SKILL.md (moved to references/error-handling.md)
- Use case examples scattered in SKILL.md (consolidated in references/)

## [1.0.0] - 2026-02-20

### Added
- Initial production release
- Direct Supabase Management API access using Personal Access Token
- No third-party proxy
- Read operations (projects, security/performance advisors, logs, queries)
- Write operations with human approval requirement (create/pause/restore projects, migrations)
- supabase_agent.py CLI interface
- supabase_client.py API client library
- Security tier: approved-with-controls
- Production status

[2.0.0]: https://github.com/bramforth/bram-claw/compare/v1.0.0-supabase...v2.0.0-supabase
[1.0.0]: https://github.com/bramforth/bram-claw/releases/tag/v1.0.0-supabase
