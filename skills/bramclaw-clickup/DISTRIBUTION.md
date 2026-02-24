# Distribution Guide - bramclaw-clickup

## Packaging the Skill

### Prerequisites

- Anthropic skill-creator tools available
- All files committed to git
- Version updated in SKILL.md frontmatter
- CHANGELOG.md updated

### Package Command

```bash
cd /Users/jimeny/git/bram-claw/.claude/skills/bramclaw-clickup

# Use Anthropic's package_skill.py
python3 ~/.claude/plugins/marketplaces/anthropic-agent-skills/skills/skill-creator/scripts/package_skill.py

# Creates: bramclaw-clickup.skill
```

**Output:**
- `bramclaw-clickup.skill` - Packaged skill file
- Includes: SKILL.md, scripts/, references/, tests/, CHANGELOG.md

### Verify Package

```bash
# Check package contents
unzip -l bramclaw-clickup.skill

# Should contain:
# - SKILL.md
# - scripts/clickup_agent.py
# - scripts/clickup_client.py
# - references/api-reference.md
# - references/common-queries.md
# - references/security-model.md
# - references/error-handling.md
# - references/success-metrics.md
# - tests/TEST-PLAN.md
# - CHANGELOG.md
# - DISTRIBUTION.md
```

---

## Installation

### For Users

```bash
# Install packaged skill
claude skill install bramclaw-clickup.skill

# Or install from directory
ln -s /path/to/bramclaw-clickup ~/.claude/skills/bramclaw-clickup
```

### Verify Installation

```bash
# Check skill is available
claude skill list | grep bramclaw-clickup

# Test in Claude session
# Ask: "Show me my ClickUp tasks"
# Skill should trigger
```

---

## GitHub Release

### Create Release

```bash
# Tag version
cd /Users/jimeny/git/bram-claw
git tag -a v2.0.0-clickup -m "bramclaw-clickup v2.0.0 - Progressive disclosure refactor"
git push origin v2.0.0-clickup

# Create GitHub release
gh release create v2.0.0-clickup \
  --title "bramclaw-clickup v2.0.0" \
  --notes-file .claude/skills/bramclaw-clickup/CHANGELOG.md \
  .claude/skills/bramclaw-clickup.skill
```

### Release Checklist

- [ ] Version updated in SKILL.md
- [ ] CHANGELOG.md updated
- [ ] All tests passing (tests/TEST-PLAN.md scenarios)
- [ ] Skill packaged (bramclaw-clickup.skill created)
- [ ] Git tag created
- [ ] GitHub release published
- [ ] Release notes from CHANGELOG.md
- [ ] .skill file attached to release

---

## Publishing to Anthropic Marketplace (Future)

### Prerequisites

- Anthropic developer account
- Skill meets marketplace guidelines
- License file included (MIT recommended)
- README.md with installation instructions

### Submission Process

1. Review Anthropic skill guidelines
2. Add LICENSE file (MIT or Apache 2.0)
3. Create marketplace-friendly README.md
4. Submit via Anthropic developer portal
5. Respond to review feedback

### Marketplace Requirements

- [ ] Clear description
- [ ] Usage examples
- [ ] Security audit documentation
- [ ] Open source license
- [ ] Versioned releases
- [ ] Test coverage >80%
- [ ] No hardcoded credentials

---

## Version Management

### Semantic Versioning

Follow [semver.org](https://semver.org):

- **MAJOR** (X.0.0): Breaking changes
  - Changed API interface
  - Removed features
  - Incompatible changes

- **MINOR** (1.X.0): New features (backward compatible)
  - Added new operations
  - New reference docs
  - Enhanced functionality

- **PATCH** (1.0.X): Bug fixes (backward compatible)
  - Fixed bugs
  - Security patches
  - Documentation fixes

### Version Workflow

```bash
# 1. Update version in SKILL.md frontmatter
# version: 2.1.0

# 2. Update CHANGELOG.md
## [2.1.0] - 2026-03-01
### Added
- New task search filters

# 3. Commit
git add .claude/skills/bramclaw-clickup/
git commit -m "chore(clickup): bump version to 2.1.0"

# 4. Tag and release
git tag v2.1.0-clickup
git push origin v2.1.0-clickup
gh release create v2.1.0-clickup ...
```

---

## Distribution Channels

### 1. GitHub Releases

**Pros:**
- Version control
- Public access
- Download statistics

**Installation:**
```bash
# Download from release
curl -L -o bramclaw-clickup.skill \
  https://github.com/bramforth/bram-claw/releases/download/v2.0.0-clickup/bramclaw-clickup.skill

# Install
claude skill install bramclaw-clickup.skill
```

### 2. Direct Repository

**Pros:**
- Always latest version
- Easy updates (git pull)

**Installation:**
```bash
# Clone and symlink
git clone https://github.com/bramforth/bram-claw.git
ln -s $(pwd)/bram-claw/.claude/skills/bramclaw-clickup ~/.claude/skills/bramclaw-clickup
```

### 3. Anthropic Marketplace (Future)

**Pros:**
- Discoverable
- Trusted source
- Automatic updates

**Installation:**
```bash
# Via Claude marketplace
claude skill install anthropic/bramclaw-clickup
```

---

## Maintenance

### Update Workflow

When making changes:

1. **Branch:** Create feature branch
2. **Change:** Make updates
3. **Test:** Run full test suite
4. **Version:** Bump version appropriately
5. **Changelog:** Document changes
6. **Package:** Create new .skill file
7. **Release:** Tag and publish

### Support

**Issues:** https://github.com/bramforth/bram-claw/issues
**Discussions:** https://github.com/bramforth/bram-claw/discussions
**Security:** security@bramforth.ai

---

## License

MIT License - See LICENSE file

Users can:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Private use

Must:
- Include license and copyright notice
- State changes made

---

## Contributors

See CONTRIBUTORS.md for attribution

**How to contribute:**
1. Fork repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request
5. Wait for review

---

**Last updated:** 2026-02-21
**Distribution version:** 2.0.0
**Minimum Claude version:** 1.0.0
