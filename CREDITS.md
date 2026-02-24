# Attribution & Credits

This repository contains skills from multiple sources. We are grateful to all contributors who have built excellent patterns that we build upon.

---

## Superpowers Skills (MIT License)

**Source**: https://github.com/obra/superpowers
**Author**: Jesse Vincent (@obra)
**License**: MIT
**Date Integrated**: 2026-02-24 (via git subtree)

The following 14 skills are integrated from the Superpowers project:

### Testing & Quality
- `test-driven-development` - TDD methodology for implementation
- `systematic-debugging` - Structured debugging workflow
- `verification-before-completion` - Pre-completion verification checklist

### Planning & Execution
- `brainstorming` - Creative exploration before implementation
- `writing-plans` - Multi-step task planning
- `executing-plans` - Plan execution workflow
- `dispatching-parallel-agents` - Concurrent agent coordination
- `subagent-driven-development` - Independent task execution

### Code Review & Collaboration
- `requesting-code-review` - Submit work for review
- `receiving-code-review` - Process review feedback

### Git & Branch Management
- `using-git-worktrees` - Isolated workspace creation
- `finishing-a-development-branch` - Branch completion workflow

### Meta-Skills
- `using-superpowers` - Introduction to skill usage
- `writing-skills` - Skill creation methodology

**Integration Method**: Git subtree - allows pulling upstream updates from Jesse's repo

**Updating from upstream**:
```bash
cd ~/git/skills
git subtree pull --prefix=skills-external/superpowers https://github.com/obra/superpowers.git main --squash
cp -r skills-external/superpowers/skills/* skills/
git add skills/
git commit -m "feat: update superpowers skills from upstream"
```

**Appreciation**: We are deeply grateful to Jesse Vincent for creating these excellent workflow patterns. The Superpowers project has significantly influenced how we think about agentic collaboration.

**Sponsorship**: If you benefit from these skills, consider sponsoring Jesse's open source work: https://github.com/sponsors/obra

---

## Cursor Utility Skills

**Source**: Cursor IDE built-in skills
**Date Copied**: 2026-02-24

The following utility skills are from Cursor:

- `create-rule` - Create Cursor rules
- `create-skill` - Create Cursor skills
- `create-subagent` - Create Cursor subagents
- `migrate-to-skills` - Migrate to skills system
- `update-cursor-settings` - Update Cursor configuration

**Note**: These are Cursor-specific utilities and may only work within Cursor IDE.

---

## Marketing Skills (MIT License)

**Source**: https://github.com/coreyhaines31/marketingskills
**Author**: Corey Haines (https://corey.co)
**License**: MIT
**Date Integrated**: 2026-02-24 (via git subtree)
**Your Fork**: https://github.com/jamieoarton/marketingskills

The following marketing skills are integrated from Corey Haines' excellent marketingskills repository:

### Conversion Optimization (6 skills)
- `page-cro` - Optimize any marketing page for conversions
- `signup-flow-cro` - Improve registration and signup flows
- `onboarding-cro` - Enhance post-signup activation
- `form-cro` - Optimize lead capture and contact forms
- `popup-cro` - Create and optimize popups and modals
- `paywall-upgrade-cro` - In-app paywalls and upgrade screens

### Content & Copy (4 skills)
- `copywriting` - Write compelling marketing copy
- `copy-editing` - Edit and polish existing copy
- `email-sequence` - Build email drip campaigns
- `social-content` - Create social media content

### SEO & Discovery (3 skills)
- `seo-audit` - Technical and on-page SEO audits
- `programmatic-seo` - Build SEO pages at scale
- `schema-markup` - Add structured data and rich snippets

### Paid & Distribution (1 skill)
- `paid-ads` - Google, Meta, LinkedIn ad campaigns

### Measurement & Testing (2 skills)
- `analytics-tracking` - Event tracking and measurement
- `ab-test-setup` - A/B test planning and implementation

### Growth Engineering (2 skills)
- `free-tool-strategy` - Marketing tools and calculators
- `referral-program` - Referral and affiliate programs

### Strategy & Monetization (5 skills)
- `marketing-ideas` - 140 SaaS marketing strategies
- `marketing-psychology` - 70+ marketing mental models
- `pricing-strategy` - Pricing, packaging, monetization
- `launch-strategy` - Product launches and announcements
- `competitor-alternatives` - Competitor comparison pages

**Integration Method**: Git subtree - allows pulling upstream updates from Corey's original repo

**Updating from upstream**:
```bash
cd ~/git/skills
git subtree pull --prefix=skills-external/marketingskills https://github.com/coreyhaines31/marketingskills.git main --squash
cp -r skills-external/marketingskills/skills/* skills/
git add skills/
git commit -m "feat: update marketing skills from upstream"
```

**Appreciation**: Huge thanks to Corey Haines for creating these practical, battle-tested marketing skills. If you use these for revenue-generating work, consider supporting Corey at https://conversionfactory.co

---

## Original Skills (MIT License)

**Author**: Jamie Oarton
**Repository**: https://github.com/jamieoarton/skills

The following skills are original work:

### Business & Productivity (Work The System Methodology)
- `work-the-system-mindset` - Systems thinking framework
- `strategic-objective-creation` - Strategic planning
- `operating-principles-development` - Decision-making principles
- `working-procedures-documentation` - Process documentation
- `fetch-youtube-transcript` - YouTube transcript extraction

### BramClaw MCP Integrations
- `bramclaw-clickup` - ClickUp task management
- `bramclaw-gmail` - Gmail read operations
- `bramclaw-gmail-delegated-send` - Gmail delegated sending
- `bramclaw-obsidian` - Obsidian vault management
- `bramclaw-supabase` - Supabase database operations
- `bramclaw-github` - GitHub operations

### Development Tools
- `bramclaw-agent-creation` - BramClaw agent creation framework
- `skill-building-complete` - Complete skill building toolkit

---

## Modifications & Enhancements

As we improve and enhance skills over time, we will document changes here:

### [Date] - [Skill Name]
- [Description of modifications]
- [Reason for changes]

---

## Future Direction

We plan to:

1. **Maintain attribution** for all source material
2. **Gradually enhance** skills with BramClaw-specific patterns
3. **Build new skills** following established patterns
4. **Contribute back** improvements where applicable
5. **Document modifications** transparently

---

## License Compatibility

All skills in this repository are under MIT License or compatible licenses:

- **Superpowers**: MIT License (compatible)
- **Cursor utilities**: Proprietary but redistributable (verify with Cursor team)
- **Original work**: MIT License

The unified repository is licensed under MIT License - see [LICENSE](LICENSE) file.

---

## Contact & Contributions

**Repository**: https://github.com/jamieoarton/skills
**Issues**: https://github.com/jamieoarton/skills/issues
**Author**: Jamie Oarton (jamie@bramforth.ai)

If you identify any attribution issues or have questions about licensing, please open an issue.

---

**Last Updated**: 2026-02-24
**Total Skills**: 34
**Sources**: Superpowers (15), Cursor (5), Original (14)
