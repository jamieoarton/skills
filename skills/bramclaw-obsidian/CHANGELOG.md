# Changelog - bramclaw-obsidian

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-21

### Added
- Progressive disclosure structure (scripts/, references/, tests/, assets/)
- Explicit trigger patterns ("Obsidian", "vault", "daily note", markdown notes on Drive)
- Success metrics framework (triggering accuracy, token reduction, setup time, security compliance)
- Decision framework (when to use vs. Obsidian desktop, MCP, filesystem mounts)
- Comprehensive reference documentation:
  - setup-guide.md (environment setup, folder ID extraction, service account configuration)
  - google-drive-integration.md (complete implementation pattern with code examples)
  - security-model.md (The Iron Law, decision tree, red flags, rationalization counter)
  - backup-strategies.md (5 backup methods, verification checklist, testing procedures)
  - api-operations.md (complete API reference, phased implementation guide)
  - common-mistakes.md (wrong patterns, correct responses, time estimates)
  - success-metrics.md (measurement framework with baselines and monitoring)
- Version metadata in frontmatter with version_history
- CHANGELOG.md
- Skill confidence levels (high/medium/low)
- Alternatives comparison table (bramclaw vs desktop vs MCP vs filesystem)
- TEST-PLAN.md with comprehensive test scenarios
- DISTRIBUTION.md for packaging and release workflow

### Changed
- Moved obsidian_vault.py to scripts/ directory
- Refactored SKILL.md to overview with cross-references (801 → 477 lines, -40.4%)
- Updated description to include trigger keywords
- Enhanced security model documentation with "The Iron Law" and red flags

### Removed
- Detailed implementation code from SKILL.md (moved to references/google-drive-integration.md)
- Backup strategy details from SKILL.md (moved to references/backup-strategies.md)
- Common mistakes patterns from SKILL.md (moved to references/common-mistakes.md)
- Security decision tree from SKILL.md (moved to references/security-model.md)
- Complete API reference from SKILL.md (moved to references/api-operations.md)

## [1.0.0] - 2026-02-20

### Added
- Initial production release
- Direct Google Drive API access using service account
- No third-party proxy or filesystem mounts
- Read operations (search, read, list)
- Write operations with confirmation gates (create, append)
- Convenience features (daily notes, frontmatter, internal links)
- Security features:
  - Confirmation gates (`confirmed=True` required)
  - Size limits (1MB per note)
  - Path validation (vault folder only)
  - Audit logging (`/root/logs/obsidian_vault.log`)
  - Rate limiting (10 creates/minute)
  - Backup verification warnings
- obsidian_vault.py implementation
- Domain-wide delegation support
- Phased implementation guide (Phase 1: read-only, Phase 2: enhanced, Phase 3: writes)
- Security tier: approved-with-controls
- Production status

[2.0.0]: https://github.com/bramforth-ai/bram-claw/compare/v1.0.0-obsidian...v2.0.0-obsidian
[1.0.0]: https://github.com/bramforth-ai/bram-claw/releases/tag/v1.0.0-obsidian
