# Distribution Checklist

**Purpose:** Pre-deployment validation checklist to ensure skill is ready for distribution.

**Usage:** Check off each item before distributing your skill to users.

---

## Pre-Distribution Validation

### Skill Quality

- [ ] **Validation passed**
  ```bash
  python quick_validate.py /path/to/skill/
  # Output: "✅ Skill is valid!"
  ```

- [ ] **Triggering tested**
  - Created test query suite (12+ SHOULD_TRIGGER, 12+ SHOULD_NOT_TRIGGER)
  - Tested with Claude
  - Accuracy ≥90%

- [ ] **MCP integration tested** (if Category 3 skill)
  - MCP server connected
  - All MCP tools callable
  - Error handling tested (disconnect, auth failure, rate limit)
  - Graceful degradation for missing data

- [ ] **Error scenarios tested**
  - Tested with MCP disconnected (provides setup instructions)
  - Tested with bad auth (provides re-auth instructions)
  - Tested with missing data (graceful fallback)
  - Tested with rate limiting (retry logic works)

- [ ] **First-try success ≥80%**
  - Executed skill 10 times
  - At least 8 completed successfully without errors or user corrections

### Documentation

- [ ] **README.md complete**
  - Clear overview (what, who, why)
  - Installation instructions
  - Usage examples
  - Prerequisites listed
  - Trigger phrases documented
  - Troubleshooting section

- [ ] **SKILL.md has metadata**
  ```yaml
  ---
  name: skill-name
  description: Clear, searchable description
  metadata:
    version: 1.0.0
    author: Your Name
    created: 2026-02-21
    updated: 2026-02-21
  ---
  ```

- [ ] **CHANGELOG.md created**
  - Semantic versioning used
  - All versions documented
  - Breaking changes clearly marked

- [ ] **LICENSE added** (if open source)
  - MIT, Apache 2.0, or other appropriate license
  - License file included

- [ ] **Examples provided**
  - At least 2-3 concrete usage examples
  - Examples show common use cases
  - Examples demonstrate value/time saved

### Packaging

- [ ] **Skill packaged successfully**
  ```bash
  python package_skill.py /path/to/skill/
  # Output: "✅ Successfully packaged skill to: skill-name.skill"
  ```

- [ ] **Package size reasonable**
  - .skill file < 5MB (if larger, consider removing large assets)
  - All necessary files included
  - No unnecessary files (temp files, .DS_Store, etc.)

- [ ] **Version number correct**
  - SKILL.md metadata.version matches intended release
  - CHANGELOG.md documents this version
  - Git tag matches (if using GitHub)

---

## Distribution Method Setup

### Option A: Individual Distribution (.skill file)

- [ ] .skill file packaged and tested
- [ ] Installation instructions written for recipients
- [ ] Distribution method chosen (email, shared drive, Slack)
- [ ] Version number in filename: `skill-name-v1.0.0.skill`

### Option B: GitHub Hosting

- [ ] GitHub repo created
- [ ] Repo structure follows best practices
  - README.md
  - LICENSE
  - CHANGELOG.md
  - skill-name/ (skill directory)
  - examples/
  - tests/

- [ ] README template filled out completely
  - Overview
  - Installation (both upload and clone options)
  - Usage examples
  - Features list
  - Configuration (if any)
  - Troubleshooting
  - Contributing guidelines
  - License and author

- [ ] GitHub topics/tags added
  - `claude-skill`
  - `mcp-enhancement` (if Category 3)
  - Domain-specific tags (e.g., `project-management`, `linear`)

- [ ] GitHub Release created
  - Tag: `v1.0.0`
  - Release title: `v1.0.0 - [Brief description]`
  - Description: Changelog for this version
  - Attachment: .skill file

- [ ] GitHub Actions validation (optional but recommended)
  - CI workflow validates skill on push
  - Prevents accidental breakage

### Option C: Organization/Team Distribution

- [ ] Contacted organization admin
- [ ] Provided .skill file
- [ ] Provided description and use case
- [ ] Listed required MCP servers (if any)
- [ ] Specified target users/teams
- [ ] Created internal documentation (wiki/SharePoint)
- [ ] Scheduled training/demo session
- [ ] Set up feedback channel (#skill-name Slack)

### Option D: API-Based Distribution

- [ ] API credentials obtained
- [ ] API key stored securely (environment variable)
- [ ] Deployment script tested
- [ ] Skill uploaded successfully via API
- [ ] Verified upload with API GET request

---

## Cross-Linking (if Category 3 MCP skill)

- [ ] **Linked from MCP documentation**
  - Added to MCP server's README.md
  - PR submitted to MCP docs (if applicable)
  - Skill listed in "Related Skills" or "Use Cases" section

- [ ] **Skill references MCP**
  - SKILL.md Prerequisites lists MCP server with link
  - README.md links to MCP setup instructions
  - Examples show MCP connection requirement

---

## Positioning & Messaging

- [ ] **Description is clear and specific**
  - Format: [Action] + [Domain] + [Outcome/Benefit]
  - Example: "Automate sprint planning by analyzing historical velocity in Linear..."
  - NOT: "Helps with sprints" ❌

- [ ] **Skill name is searchable**
  - Includes tool/domain if Category 3
  - Action-oriented
  - NOT generic ("helper", "tool")

- [ ] **First paragraph of README answers:**
  - What does this skill do?
  - Who is it for?
  - Why should I use it? (time saved, problem solved)

- [ ] **Value proposition clear**
  - Shows time saved (e.g., "30 seconds instead of 15 minutes")
  - Explains automation benefit
  - Demonstrates concrete workflow improvement

---

## Post-Distribution Planning

### Feedback Collection

- [ ] **Feedback channel established**
  - GitHub Issues (if open source)
  - Internal Slack channel (if org distribution)
  - Email address (if individual distribution)

- [ ] **User survey planned**
  - "Would you use this skill again?" (Yes/No)
  - "What could be improved?"
  - "What use cases are we missing?"

### Support

- [ ] **Support plan documented**
  - Who answers questions? (you, team, community)
  - Expected response time
  - Support hours (if applicable)

- [ ] **Troubleshooting guide accessible**
  - Linked from README
  - Covers common issues
  - Provides self-service debugging

### Monitoring

- [ ] **Usage tracking plan**
  - How will you measure adoption?
  - Analytics available? (org skills have analytics)
  - Manual check-ins? (ask users directly)

- [ ] **Update notification method**
  - Email list for updates
  - GitHub Watch/Star notifications
  - Internal announcement channel

- [ ] **Re-measurement schedule**
  - Weekly feedback checks (first month)
  - Monthly usage review
  - Quarterly metrics re-measurement
  - Annual ROI recalculation

### Iteration Plan

- [ ] **Real user query collection**
  - Plan to collect queries that should have triggered but didn't
  - Add missed triggers to test suite
  - Update description if triggering accuracy drops

- [ ] **Version update process**
  - How will users get updates?
  - Automated (org skills) or manual notification?
  - Backward compatibility strategy

---

## Final Review

### Before You Click "Deploy"

- [ ] **Read your README as if you're a new user**
  - Is installation clear?
  - Are examples helpful?
  - Can you follow it without prior context?

- [ ] **Test the installation process yourself**
  - Download your .skill file
  - Upload to fresh Claude instance
  - Does it work as documented?

- [ ] **Run one final triggering test**
  - Use your test query suite
  - Confirm ≥90% accuracy
  - No regressions from recent changes

- [ ] **Check all links**
  - GitHub links work
  - MCP documentation links valid
  - Example repos accessible

---

## Checklist Summary

**Minimum requirements to distribute:**
- ✅ Skill validates
- ✅ Triggering tested (≥90%)
- ✅ README with installation instructions
- ✅ .skill file packaged
- ✅ Distribution method chosen

**Recommended for quality release:**
- ✅ All minimum requirements
- ✅ Error scenarios tested
- ✅ CHANGELOG.md created
- ✅ Examples provided
- ✅ License added (if open source)
- ✅ Feedback channel established

**Professional open source release:**
- ✅ All recommended items
- ✅ GitHub repo with proper structure
- ✅ GitHub Release with .skill file
- ✅ Linked from MCP docs (if Category 3)
- ✅ CI validation (GitHub Actions)
- ✅ Monitoring and iteration plan

---

## Post-Distribution Actions

**Immediately after distribution:**
- [ ] Announce in relevant communities/channels
- [ ] Monitor for initial feedback (first 24-48 hours)
- [ ] Respond to early questions promptly
- [ ] Fix critical bugs quickly (patch release if needed)

**Week 1:**
- [ ] Check usage metrics (if available)
- [ ] Collect initial user feedback
- [ ] Update FAQ based on common questions

**Month 1:**
- [ ] Survey users for satisfaction
- [ ] Analyze triggering accuracy in production
- [ ] Plan first minor update (v1.1.0) if needed

**Quarter 1:**
- [ ] Re-measure all metrics
- [ ] Calculate actual ROI vs. projected
- [ ] Decide: Continue, enhance, or deprecate

---

**Referenced by:**
- `distribution-deployment-guide.md` - Distribution checklist section
- `SKILL.md` - Step 10 (Document and distribute)
