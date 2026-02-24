# Pulling Upstream Updates

This repository uses **git subtree** to integrate external skill repositories while maintaining a single unified repo. This allows pulling upstream updates while keeping everything in one place.

---

## Marketing Skills (Corey Haines)

**Upstream**: https://github.com/coreyhaines31/marketingskills
**Your Fork**: https://github.com/jamieoarton/marketingskills (static snapshot)
**Subtree Path**: `skills-external/marketingskills/`

### Update Process (Recommended: Pull Directly from Upstream)

**Best Practice**: Pull directly from Corey's original repo to always get the latest:

```bash
cd ~/git/skills

# 1. Pull latest from upstream into subtree
git subtree pull --prefix=skills-external/marketingskills \
  https://github.com/coreyhaines31/marketingskills.git main --squash

# 2. Copy updated skills to main skills directory
cp -r skills-external/marketingskills/skills/* skills/

# 3. Stage and commit
git add skills/
git commit -m "feat: update marketing skills from upstream"

# 4. Push to your unified repo
git push origin main
```

**Result**: Updated marketing skills propagate to all AI systems via symlinks

**Why This Approach**: Simpler workflow, fewer steps, always current.

---

## Alternative: Update Via Your Fork (Only If You Need Customization)

**Use this approach ONLY if you need to**:
- Customize marketing skills before using them
- Test upstream changes in isolation before pulling
- Maintain a modified version with your own additions

**Note**: Your fork is a snapshot - it doesn't automatically sync with upstream.

```bash
# Step 1: Update your fork (one-time remote setup)
cd /tmp
git clone https://github.com/jamieoarton/marketingskills.git
cd marketingskills
git remote add upstream https://github.com/coreyhaines31/marketingskills.git

# Step 2: Pull upstream changes and push to your fork
git fetch upstream
git merge upstream/main
git push origin main

# Step 3: Pull from your fork into unified repo
cd ~/git/skills
git subtree pull --prefix=skills-external/marketingskills \
  https://github.com/jamieoarton/marketingskills.git main --squash
cp -r skills-external/marketingskills/skills/* skills/
git add skills/
git commit -m "feat: update marketing skills from fork"
git push
```

---

## Superpowers Skills (Jesse Vincent)

**Upstream**: https://github.com/obra/superpowers
**Subtree Path**: `skills-external/superpowers/`

### Update Process (Recommended: Pull Directly from Upstream)

**Best Practice**: Pull directly from Jesse's original repo to always get the latest:

```bash
cd ~/git/skills

# 1. Pull latest from upstream into subtree
git subtree pull --prefix=skills-external/superpowers \
  https://github.com/obra/superpowers.git main --squash

# 2. Copy updated skills to main skills directory
cp -r skills-external/superpowers/skills/* skills/

# 3. Stage and commit
git add skills/
git commit -m "feat: update superpowers skills from upstream"

# 4. Push to your unified repo
git push origin main
```

**Result**: Updated Superpowers skills propagate to all AI systems via symlinks

**Why This Approach**: Jesse actively maintains Superpowers with significant improvements (e.g., brainstorming skill now has hard gates, checklists, and process flows).

---

## Checking for Updates

**Marketing Skills** (check upstream directly):
```bash
# Check for new commits in Corey's original repo
cd /tmp
git clone https://github.com/coreyhaines31/marketingskills.git
cd marketingskills
git log --since="2026-02-24" --oneline

# Or use GitHub web interface
# https://github.com/coreyhaines31/marketingskills/commits/main
```

**Superpowers** (check upstream directly):
```bash
# Check for new commits in Jesse's original repo
cd /tmp
git clone https://github.com/obra/superpowers.git
cd superpowers
git log --since="2026-02-24" --oneline

# Or use GitHub web interface
# https://github.com/obra/superpowers/commits/main
```

---

## Git Subtree Reference

### Why Subtree?

- ✅ Keeps external code in your repo (single source of truth)
- ✅ Can pull upstream updates
- ✅ Works with symlinks (unlike submodules)
- ✅ No special commands for users (just `git clone`)

### Common Commands

**Initial add** (already done for both):
```bash
# Marketing skills
git subtree add --prefix=skills-external/marketingskills \
  https://github.com/jamieoarton/marketingskills.git main --squash

# Superpowers skills
git subtree add --prefix=skills-external/superpowers \
  https://github.com/obra/superpowers.git main --squash
```

**Pull updates**:
```bash
# Marketing skills
git subtree pull --prefix=skills-external/marketingskills \
  https://github.com/coreyhaines31/marketingskills.git main --squash

# Superpowers skills
git subtree pull --prefix=skills-external/superpowers \
  https://github.com/obra/superpowers.git main --squash
```

**Check subtree history**:
```bash
git log --all --graph --decorate --oneline --simplify-by-decoration \
  | grep marketingskills
```

---

## Workflow Summary

### For Marketing Skills (Recommended: Direct from Upstream)

**Every 1-2 months** or when Corey releases updates:

1. Check for updates in upstream: https://github.com/coreyhaines31/marketingskills/commits/main
2. Pull directly from upstream: `git subtree pull --prefix=skills-external/marketingskills https://github.com/coreyhaines31/marketingskills.git main --squash`
3. Copy to main skills: `cp -r skills-external/marketingskills/skills/* skills/`
4. Commit and push
5. **Result**: All machines and AI systems get updates automatically

**Your fork** (`jamieoarton/marketingskills`) is a static snapshot - only update it if you're customizing the skills.

### For Superpowers Skills (Recommended: Direct from Upstream)

**Every 1-2 months** or when Jesse releases updates:

1. Check for updates in upstream: https://github.com/obra/superpowers/commits/main
2. Pull directly from upstream: `git subtree pull --prefix=skills-external/superpowers https://github.com/obra/superpowers.git main --squash`
3. Copy to main skills: `cp -r skills-external/superpowers/skills/* skills/`
4. Commit and push
5. **Result**: All machines and AI systems get updates automatically

---

## Multi-Machine Impact

**After pushing upstream updates**:

On **other machines**:
```bash
cd ~/git/skills
git pull origin main
```

**All AI systems immediately updated** (via symlinks):
- ✅ Codex
- ✅ Antigravity
- ✅ Cursor
- ✅ Claude Code (updates next session)

---

## Troubleshooting

### Merge Conflicts During Subtree Pull

```bash
# If conflicts occur:
git status  # See conflicted files

# Resolve conflicts in skills-external/marketingskills/
# Then:
git add skills-external/marketingskills/
git commit

# Copy resolved skills to main directory
cp -r skills-external/marketingskills/skills/* skills/
git add skills/
git commit -m "feat: update marketing skills (resolved conflicts)"
```

### Subtree Not Found

```bash
# Re-add subtree (safe if already exists)
git subtree add --prefix=skills-external/marketingskills \
  https://github.com/jamieoarton/marketingskills.git main --squash
```

---

## Attribution

When pulling updates, maintain attribution in CREDITS.md:

```markdown
**Date Updated**: YYYY-MM-DD (via git subtree pull)
**Upstream Version**: [commit hash or tag]
```

---

**Last Updated**: 2026-02-24
**Marketing Skills**: Integrated via git subtree (2026-02-24)
**Superpowers Skills**: Integrated via git subtree (2026-02-24)
