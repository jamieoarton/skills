# Distribution & Deployment Guide

**Purpose:** Step-by-step guide for deploying skills to make them available to Claude users.

**Target audience:** Skill builders ready to share their completed skills with individuals, teams, or the wider community.

---

## Table of Contents

1. [Distribution Options Overview](#distribution-options-overview)
2. [Individual Distribution (.skill file)](#individual-distribution-skill-file)
3. [GitHub Hosting](#github-hosting)
4. [Organization/Team Distribution](#organizationteam-distribution)
5. [API-Based Distribution](#api-based-distribution)
6. [Linking from MCP Documentation](#linking-from-mcp-documentation)
7. [Positioning & Messaging](#positioning--messaging)
8. [Version Management](#version-management)
9. [Distribution Checklist](#distribution-checklist)

---

## Distribution Options Overview

### Decision Matrix

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| **Individual .skill file** | Personal use, small sharing | Simple, no hosting needed | Manual distribution, hard to update |
| **GitHub repo** | Open source, community skills | Version control, discoverable | Requires GitHub knowledge |
| **Organization upload** | Company/team internal skills | Centralized, easy updates | Requires org admin access |
| **API distribution** | Automated deployment | Programmatic, scalable | Complex setup, requires API key |

### Choosing Distribution Method

**Use Individual .skill file when:**
- Skill is for personal use only
- Sharing with 1-2 people
- Prototyping/testing before wider release

**Use GitHub hosting when:**
- Skill is open source
- Want community contributions
- Need version history
- Want skill to be discoverable

**Use Organization distribution when:**
- Skill is for company/team use
- Need centralized management
- Want easy updates for all team members

**Use API distribution when:**
- Automating skill deployment
- Managing many skills programmatically
- Building skill marketplace/catalog

---

## Individual Distribution (.skill file)

### When to Use

- Quick sharing with specific people
- Testing before public release
- Internal tools not ready for open source

### Process

**1. Package your skill**

```bash
python /path/to/package_skill.py /path/to/your-skill-directory/
```

This creates `your-skill-name.skill` file.

**2. Validate the package**

```bash
python /path/to/quick_validate.py /path/to/your-skill-directory/
```

Should output: "✅ Skill is valid!"

**3. Share the .skill file**

Methods:
- Email attachment
- Shared drive (Dropbox, Google Drive)
- Slack/Teams file upload
- USB drive (air-gapped environments)

**4. Installation instructions for recipients**

Provide these instructions:

```markdown
## How to Install This Skill

1. Download the .skill file: `[skill-name].skill`
2. Open Claude Code (or claude.ai with skills enabled)
3. Navigate to Skills settings
4. Click "Upload Skill"
5. Select the downloaded .skill file
6. Confirm installation
7. Restart Claude if prompted

The skill will now be available for use.
```

### Limitations

- **No automatic updates** - Recipients must manually download new versions
- **Hard to track usage** - No analytics on who's using the skill
- **Version confusion** - Recipients may have different versions
- **Not discoverable** - Only people you send it to can find it

### Best Practices

- Include version number in filename: `linear-sprint-planner-v1.2.0.skill`
- Provide changelog in distribution message
- Set up email list for update notifications
- Consider GitHub hosting if more than 5 people need the skill

---

## GitHub Hosting

### When to Use

- Skill is open source
- Want version control
- Want community to find and contribute
- Need professional presentation

### Repository Structure

```
your-skill-repo/
├── README.md                 # Overview, installation, usage
├── LICENSE                   # MIT, Apache 2.0, etc.
├── CHANGELOG.md              # Version history
├── skill-name/
│   ├── SKILL.md             # Main skill file
│   ├── references/          # Supporting docs
│   ├── scripts/             # Helper scripts (optional)
│   └── assets/              # Templates, examples
├── examples/
│   └── example-usage.md     # Concrete examples
├── tests/
│   └── test-queries.txt     # Triggering test suite
└── .github/
    └── workflows/
        └── validate.yml      # CI to validate on push
```

### README Template

```markdown
# [Skill Name]

**One-sentence description of what this skill does.**

## Overview

[2-3 paragraph explanation of use case and value]

## Prerequisites

- [MCP Server Name] connected (if Category 3 skill)
- [Required permissions/access]

## Installation

### Option 1: Direct Upload

1. Download the latest .skill file from [Releases](link)
2. Upload to Claude via Skills settings

### Option 2: Clone and Package

```bash
git clone https://github.com/yourusername/your-skill-repo.git
cd your-skill-repo
python /path/to/package_skill.py skill-name/
# Upload generated .skill file to Claude
```

## Usage

**Trigger phrases:**
- "Plan next sprint based on velocity"
- "Create Linear sprint with recommended scope"

**Example interaction:**

```
User: Plan next sprint for Engineering team
Skill: [Executes workflow, creates sprint]
Output: Created Sprint 24 with 31 points across 6 issues
```

## Features

- ✅ Analyzes historical velocity
- ✅ Recommends optimal scope
- ✅ Creates sprint automatically
- ✅ Handles edge cases (no history, auth errors)

## Configuration

[If skill has configurable options, document them]

## Troubleshooting

**Skill doesn't trigger:**
- Ensure [MCP Server] is connected
- Try more specific phrasing: "..."

**Error: "MCP not found":**
- Check [MCP Server] connection
- Restart Claude Code

[Link to full troubleshooting guide if extensive]

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create feature branch
3. Submit PR with description

## Changelog

See [CHANGELOG.md](CHANGELOG.md)

## License

[MIT/Apache/etc.] - See [LICENSE](LICENSE)

## Author

[Your Name] - [Contact/Social]

## Acknowledgments

- Built with [skill-building-complete](link)
- Inspired by [related work]
```

### GitHub Releases Workflow

**1. Tag version in git**

```bash
git tag -a v1.0.0 -m "Release v1.0.0: Initial public release"
git push origin v1.0.0
```

**2. Create GitHub Release**

- Go to Releases → "Create new release"
- Choose tag: `v1.0.0`
- Release title: `v1.0.0 - [Brief description]`
- Description: Copy from CHANGELOG.md for this version
- Attach: `skill-name.skill` file
- Publish release

**3. Update README with release link**

Point users to latest release for download

### GitHub Actions Validation (Optional)

Create `.github/workflows/validate.yml`:

```yaml
name: Validate Skill

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Validate skill structure
        run: |
          # Add validation script here
          # python validate_skill.py skill-name/
```

### Discoverability

**Make skill findable:**
- Add topic tags: `claude-skill`, `mcp-enhancement`, `[domain]`
- Include "Claude" and "skill" in repo description
- Link from MCP server documentation (if Category 3)
- Share in Claude community forums/Discord
- Tweet/blog about release

---

## Organization/Team Distribution

### When to Use

- Skill is for company/team use only
- Need centralized updates
- Want usage analytics
- Internal tools/workflows

### Process (High-Level)

**Note:** Exact process depends on your organization's Claude deployment.

**1. Contact your Claude organization admin**

Provide:
- .skill file
- Description and use case
- Required MCP servers (if any)
- Target users/teams

**2. Admin uploads to organization skills**

- Admin access required
- Can scope to specific teams/users
- Can track usage analytics

**3. Skill appears automatically for team**

- No manual installation needed
- Updates pushed automatically
- Consistent version across team

### Internal Distribution Best Practices

**Documentation:**
- Create internal wiki page
- Include use cases specific to your company
- Provide company-specific examples
- Link to internal support channel

**Training:**
- Demo skill at team meeting
- Create Loom/video walkthrough
- Offer office hours for questions

**Feedback Loop:**
- Create #skill-name Slack channel
- Regular survey: "Is this skill useful?"
- Iterate based on real usage

---

## API-Based Distribution

### When to Use

- Automating skill deployment
- Managing catalog of many skills
- Building skill marketplace
- Programmatic version management

### Process

**1. Get API credentials**

- Generate API key from Claude dashboard
- Store securely (environment variable, secrets manager)

**2. Use Skills API endpoint**

```bash
curl -X POST https://api.anthropic.com/v1/skills \
  -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "skill=@skill-name.skill" \
  -F "name=skill-name" \
  -F "description=Brief description" \
  -F "version=1.0.0"
```

**3. Verify upload**

```bash
curl https://api.anthropic.com/v1/skills/skill-name \
  -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

**4. Update version**

```bash
curl -X PUT https://api.anthropic.com/v1/skills/skill-name \
  -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
  -F "skill=@skill-name-v1.1.0.skill" \
  -F "version=1.1.0"
```

### Automation Script Example

```python
#!/usr/bin/env python3
"""Deploy skill to Claude via API"""

import os
import requests

API_KEY = os.environ['ANTHROPIC_API_KEY']
BASE_URL = 'https://api.anthropic.com/v1'

def deploy_skill(skill_file, skill_name, version, description):
    """Upload or update skill via API"""

    headers = {'Authorization': f'Bearer {API_KEY}'}

    # Check if skill exists
    response = requests.get(
        f'{BASE_URL}/skills/{skill_name}',
        headers=headers
    )

    if response.status_code == 404:
        # Create new skill
        print(f"Creating new skill: {skill_name}")
        method = 'POST'
        url = f'{BASE_URL}/skills'
    else:
        # Update existing skill
        print(f"Updating skill: {skill_name} to v{version}")
        method = 'PUT'
        url = f'{BASE_URL}/skills/{skill_name}'

    # Upload
    with open(skill_file, 'rb') as f:
        files = {'skill': f}
        data = {
            'name': skill_name,
            'version': version,
            'description': description
        }

        if method == 'POST':
            response = requests.post(url, headers=headers, files=files, data=data)
        else:
            response = requests.put(url, headers=headers, files=files, data=data)

    if response.status_code in [200, 201]:
        print(f"✅ Skill deployed successfully: v{version}")
        return response.json()
    else:
        print(f"❌ Deployment failed: {response.status_code}")
        print(response.text)
        return None

if __name__ == '__main__':
    deploy_skill(
        skill_file='skill-name.skill',
        skill_name='skill-name',
        version='1.0.0',
        description='Brief description'
    )
```

---

## Linking from MCP Documentation

### When to Link

**Always link if:**
- Your skill is a Category 3 (MCP enhancement)
- Skill adds significant value on top of raw MCP calls
- Skill is open source or publicly available

### Where to Link

**1. MCP Server README**

Add to MCP server's README.md:

```markdown
## Related Skills

Skills that enhance this MCP server:

- **[Skill Name](link)** - Brief description of what skill does
- **[Another Skill](link)** - Another enhancement
```

**2. MCP Documentation Site**

If MCP has official docs, submit PR to add skill to:
- "Skills" section
- "Examples" section
- "Use Cases" section

**3. Skill Mentions MCP**

In your skill's README, link back:

```markdown
## Prerequisites

This skill requires **[MCP Server Name](link)** to be connected.

**Installation:**
1. Install [MCP Server](setup-link)
2. Connect to Claude
3. Install this skill
```

### Positioning for MCP Enhancement Skills

**Explain the value-add:**

❌ **Bad:** "This skill uses Linear MCP"
✅ **Good:** "This skill automates sprint planning by combining Linear MCP's sprint and issue APIs with velocity calculation logic"

**Show concrete workflow:**

```markdown
**Without this skill:**
1. User asks Claude to check sprint history
2. Claude calls Linear MCP: list_sprints
3. User manually calculates average velocity
4. User asks Claude to fetch backlog
5. Claude calls Linear MCP: list_issues
6. User manually selects items
7. User asks Claude to create sprint
8. Claude calls Linear MCP: create_sprint
9. User manually assigns each issue
10. Claude calls Linear MCP: update_issue (x6)

**With this skill:**
1. User: "Plan next sprint"
2. Skill: [Executes full workflow automatically]
3. Done in 30 seconds vs. 15 minutes
```

---

## Positioning & Messaging

### Crafting Skill Description

**Formula:** `[Action] + [Domain] + [Outcome/Benefit]`

**Examples:**

❌ **Too vague:** "Helps with sprints"
✅ **Specific:** "Automate sprint planning by analyzing historical velocity in Linear, recommending backlog scope, and creating the next sprint with optimal capacity allocation."

❌ **Too technical:** "Calls Linear MCP APIs to execute sprint creation workflow"
✅ **User-focused:** "Plan your next sprint in 30 seconds instead of 15 minutes by automatically calculating team velocity and recommending work scope."

### README First Impression

**First paragraph should answer:**
1. What does this skill do? (concrete action)
2. Who is it for? (target user)
3. Why should I use it? (time saved, pain solved)

**Example:**

```markdown
# Linear Sprint Planner

Automate sprint planning for software teams using Linear. Instead of manually
calculating velocity, browsing backlogs, and creating sprints, this skill does
it all in one command—saving 15 minutes per sprint.

Perfect for engineering teams running 2-week sprints who want data-driven
planning without the busywork.
```

### Skill Naming

**Good names:**
- Clear domain: `linear-sprint-planner` (not just `planner`)
- Action-oriented: `design-handoff-automation` (describes what it does)
- Searchable: Include tool name if Category 3

**Avoid:**
- Generic: `helper`, `tool`, `utility`
- Jargon: `agile-velocity-synthesizer`
- Too long: `linear-sprint-planning-and-backlog-recommendation-system`

---

## Version Management

### Semantic Versioning

Use `MAJOR.MINOR.PATCH` format:

- **MAJOR (1.0.0 → 2.0.0):** Breaking changes (skill interface changes, different MCP server)
- **MINOR (1.0.0 → 1.1.0):** New features, backward compatible
- **PATCH (1.0.0 → 1.0.1):** Bug fixes, no new features

**Examples:**

- `1.0.0` - Initial release
- `1.0.1` - Fixed error handling for missing sprints
- `1.1.0` - Added support for custom sprint durations
- `2.0.0` - Changed from Linear MCP v1 to v2 (breaking change)

### Changelog Format

Create `CHANGELOG.md`:

```markdown
# Changelog

All notable changes to this skill will be documented in this file.

## [Unreleased]

### Added
- Planning...

## [1.1.0] - 2026-03-15

### Added
- Custom sprint duration support
- Velocity trend visualization

### Changed
- Improved error messages for auth failures

### Fixed
- Bug where backlog items weren't sorted by priority

## [1.0.1] - 2026-02-28

### Fixed
- Crash when team has <3 completed sprints
- Now offers manual capacity input as fallback

## [1.0.0] - 2026-02-21

### Added
- Initial public release
- Historical velocity calculation
- Automated sprint creation
- Backlog recommendation
```

### Version Update Process

**1. Make changes to skill**

**2. Update version in SKILL.md frontmatter**

```yaml
---
name: skill-name
description: ...
metadata:
  version: 1.1.0  # ← Update this
  author: Your Name
  updated: 2026-03-15
---
```

**3. Update CHANGELOG.md**

Document what changed

**4. Re-package skill**

```bash
python package_skill.py skill-name/
```

**5. Tag and release**

```bash
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0
```

**6. Create GitHub Release** (if using GitHub)

Attach new `.skill` file

**7. Notify users** (if using individual distribution)

Email update announcement

---

## Distribution Checklist

Use this checklist before distributing your skill:

### Pre-Distribution

- [ ] Skill validated with `quick_validate.py`
- [ ] Triggering tested (≥90% accuracy)
- [ ] MCP integration tested (if Category 3)
- [ ] Error handling tested (disconnect, auth, rate limit)
- [ ] Documentation complete (README, examples)
- [ ] Version number set in SKILL.md metadata
- [ ] CHANGELOG.md created and up-to-date
- [ ] LICENSE chosen and added (if open source)

### Distribution Setup

- [ ] .skill file packaged with `package_skill.py`
- [ ] Distribution method chosen (individual/GitHub/org/API)
- [ ] If GitHub: Repo created with proper structure
- [ ] If GitHub: README template filled out
- [ ] If GitHub: GitHub Release created
- [ ] If MCP skill: Linked from MCP documentation

### Post-Distribution

- [ ] Installation instructions provided to users
- [ ] Feedback channel set up (GitHub Issues, Slack, email)
- [ ] Usage tracking plan (analytics, surveys)
- [ ] Update notification method established
- [ ] Support plan documented (who answers questions?)

### Monitoring

- [ ] Check for user feedback weekly (first month)
- [ ] Track usage metrics (if available)
- [ ] Collect real user triggering queries
- [ ] Update test suite with missed triggers
- [ ] Plan quarterly re-measurement

---

## Quick Reference

### Common Distribution Patterns

**Personal use only:**
1. Package with `package_skill.py`
2. Upload to Claude
3. Done

**Share with 2-5 people:**
1. Package skill
2. Send .skill file via email/Slack
3. Provide installation instructions

**Open source release:**
1. Create GitHub repo
2. Use README template
3. Create Release with .skill file
4. Share on social/forums

**Company-wide deployment:**
1. Package skill
2. Contact org admin
3. Admin uploads to org skills
4. Team gets automatic access

### Resources

- [skill-creator skill](link) - Interactive skill building
- [writing-skills skill](link) - Writing workflow assistance
- [Anthropic Skills Documentation](link) - Official docs
- [Claude Code Skills](link) - Examples and inspiration

---

**Referenced by:**
- `SKILL.md` - Step 10 (Document and distribute)
- `troubleshooting-guide.md` - Upload errors
- `success-metrics-framework.md` - Post-deployment monitoring
