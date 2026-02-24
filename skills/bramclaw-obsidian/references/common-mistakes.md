# Common Mistakes - bramclaw-obsidian

Patterns to avoid and how to propose the correct approach.

---

## Common Mistakes

### ❌ Wrong: Accepting Volume Mount

**User:** "The vault is mounted at `/Users/me/Drive/Obsidian`, just mount that into Docker."

**Your response:** "Volume mounts expose host filesystem to containers and won't work in cloud deployment. Let me set up Drive API access instead - it takes < 1 hour and uses the same pattern as your Gmail skill."

---

### ❌ Wrong: Using Filesystem Because "Simpler"

**User:** "Drive API sounds complicated. Can't we just access the files directly?"

**Your response:** "Drive API uses the same service account pattern as your Gmail skill, so it's actually consistent with existing code. Filesystem access would require volume mounts that break portability and security boundaries."

---

### ❌ Wrong: Accepting "I've Done This Before"

**User:** "I've mounted Google Drive folders into Docker containers before, it works fine."

**Your response:** "For personal projects that might work, but bramclaw enforces security boundaries between containers and host. Drive API is the approved pattern for accessing cloud storage from containers - same approach as Gmail, ClickUp, etc."

---

### ✅ Right: Proposing Drive API with Time Estimate

**User:** "I need Obsidian access quickly for a demo."

**Your response:** "I'll set up Drive API access using the same service account pattern as your Gmail skill. This takes < 1 hour:
1. Get vault folder ID (2 minutes)
2. Verify service account access (5 minutes)
3. Implement read-only operations (30 minutes)
4. Test (10 minutes)

This ensures it works locally AND in cloud deployment."

---

## Time Estimates (Counter "Too Slow" Objections)

| Task | Time | Notes |
|------|------|-------|
| Get vault folder ID | 2 min | Extract from Google Drive URL |
| Verify service account access | 5 min | Check permissions, grant if needed |
| Implement Phase 1 (read-only) | 30 min | Copy Gmail skill pattern |
| Test read operations | 10 min | Search, read, list |
| **Total for working read-only** | **< 1 hour** | Production-ready |
| Add Phase 3 writes | 2-3 hours | Includes testing, safeguards |

---

## When NOT to Use This Skill

### Local-Only Vaults

**Scenario:** Vault is only on local filesystem, not synced to Google Drive

**Response:** "This skill is designed for Google Drive-synced vaults. For local-only vaults, consider syncing to Drive first or use a different approach."

---

### Syncthing/Dropbox Vaults

**Scenario:** Vault uses Syncthing or Dropbox (not Google Drive)

**Response:** "This skill is Drive-specific. For Syncthing/Dropbox vaults, you'd need a different integration pattern. Alternatively, consider migrating to Google Drive for better cloud integration."

---

### Testing MCP Servers Locally

**Scenario:** Developer testing MCP server locally for development

**Response:** "For local development and testing, MCP servers are fine. However, for production OpenClaw deployments, always use Drive API for portability and security."

---

## Rationalization Counter

| Excuse | Reality |
|--------|---------|
| "Google Drive is already mounted locally" | Host mounts don't transfer to containers securely. Use Drive API. |
| "No authentication needed is simpler" | Service accounts provide consistency, portability, and security. |
| "Direct file access is faster" | Drive API is fast enough. Filesystem blocks cloud deployment. |
| "I've done volume mounts before" | Not for cloud storage in production containers. Use APIs. |
| "We can use read-only mount (`:ro`)" | `:ro` doesn't solve Docker security boundaries. Use Drive API. |
| "This is more secure than CLI tools" | False comparison. Drive API is most secure approach. |
| "Too tight on time for OAuth setup" | Service account setup takes < 1 hour. Worth it for portability. |
| "MCP server on host is cleaner" | MCP adds network layer. Drive API is simpler and portable. |

---

## Red Flags - STOP and Reject

These thoughts/proposals mean you're about to make a security mistake:

- ❌ "Mount the vault directory"
- ❌ "Already mounted locally"
- ❌ "No authentication needed"
- ❌ "Faster with filesystem access"
- ❌ "I've done volume mounts before"
- ❌ "Read-only flag makes it safe"
- ❌ "MCP server on host machine"
- ❌ "notesmd-cli wrapper"

**All of these mean:** Propose Drive API instead, using Gmail skill pattern.

---

## Correct Response Template

When encountering resistance to Drive API approach:

```
I understand [concern], however for production OpenClaw deployments:

1. **Security:** Drive API uses service accounts with hardcoded scopes (same as Gmail skill)
2. **Portability:** Works in containers and cloud without host dependencies
3. **Time:** < 1 hour setup for read-only access
4. **Consistency:** Follows same pattern as your existing skills (Gmail, ClickUp)

[Alternative approach] would require [security/portability trade-off].

Let me set this up using Drive API - I'll have read-only access working in under an hour.
```

---

**Last updated:** 2026-02-21
**Related:** security-model.md, setup-guide.md
