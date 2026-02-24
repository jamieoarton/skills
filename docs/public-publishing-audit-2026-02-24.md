# Public/Publishing Readiness Audit

Date: 2026-02-24
Repository: https://github.com/jamieoarton/skills
Scope: Risks and blockers for making this repository public.

## Findings

### 1) High: Unverified redistribution rights for Cursor built-in skill content
The repository states Cursor utility content is "proprietary but redistributable" and still marked "verify with Cursor team," meaning the legal basis is not yet confirmed.

Evidence:
- `CREDITS.md` line 116
- `CREDITS.md` line 119
- `README.md` line 103

Why this matters:
Publishing before license permission is confirmed can create immediate legal exposure.

Recommended action:
- Obtain explicit written redistribution permission.
- If unavailable, remove those copied files from public distribution.
- Update attribution/licensing docs to remove ambiguity.

### 2) High: Bundled scraped ClickUp API documentation without explicit redistribution basis
The repository contains a large scraped copy of ClickUp documentation and a scraper script, but no clear redistribution permission statement in-repo.

Evidence:
- `skills/bramclaw-clickup/docs/clickup-api-reference/README.md` line 3
- `skills/bramclaw-clickup/scripts/scrape_clickup_docs.py` line 3

Why this matters:
Scraped vendor docs are often copyrighted; redistribution terms may be restricted.

Recommended action:
- Confirm ClickUp terms explicitly allow republishing scraped markdown.
- If not allowed, remove vendored docs and link to official docs instead.
- Keep only code/reference summaries written originally.

### 3) Medium: Public exposure of personal/company identifiers
The repository includes personal email, owner identity, and company domain associations in plugin metadata and docs.

Evidence:
- `README.md` line 215
- `CREDITS.md` line 130
- `.claude-plugin/plugin.json` line 7
- `.claude-plugin/marketplace.json` line 5

Why this matters:
Not a legal blocker by itself, but a privacy/reputation choice that should be intentional before public release.

Recommended action:
- Decide whether to retain direct email/public contact in all metadata.
- Replace with project alias/support channel if preferred.

### 4) Medium: Local/internal path leakage in published docs
Several docs expose machine-specific paths and local environment layout.

Evidence:
- `skills/bramclaw-clickup/DISTRIBUTION.md` line 15
- `UNIFIED-SKILLS-COMPLETE.md` line 83
- `IMPLEMENTATION-COMPLETE.md` line 33

Why this matters:
Not critical, but reduces polish and exposes unnecessary local environment details.

Recommended action:
- Replace absolute/local examples with portable placeholders.
- Keep user-home examples generic where needed.

### 5) Low: Documentation inconsistency (marketplace path)
README structure still references `marketplace.json` at repo root while changelog states it moved to `.claude-plugin/`.

Evidence:
- `README.md` line 191
- `CHANGELOG.md` line 11

Why this matters:
Creates confusion for users/installers and hurts publish quality.

Recommended action:
- Update README structure block to match current layout.

### 6) Low: Untracked `.system` content risk during release workflow
Untracked `skills/.system/` content was present in working tree during audit; accidental add/commit could expand licensing surface unexpectedly.

Evidence:
- Observed in `git status` during audit (`?? skills/.system/`)

Why this matters:
Potential accidental inclusion of third-party/system content without full review.

Recommended action:
- Explicitly ignore or explicitly review and track with clear attribution/licensing.
- Add release checklist step to verify `git status --short` is clean/intended.

## What was checked
- Secret/token/key pattern scan across repository
- Sensitive file type scan (`.env`, key files, DB artifacts)
- Metadata and legal docs review (`README`, `CREDITS`, `LICENSE`, plugin manifests)
- Publish-readiness scan for private/internal references and local path leakage

## Result summary
- No obvious live secrets were found in tracked files.
- Primary blockers are legal/licensing and redistribution clarity, not credential leakage.
- Repo visibility has already been switched to private pending remediation.
