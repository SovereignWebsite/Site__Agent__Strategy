# Restart: how a new b.strategy session takes over

Read this, then START.md (same folder) for the detailed key and check commands.

## Repositories
- **Own (agent and work):** SovereignWebsite/Site__Agent__Strategy, dev branch only; served at https://strategy.agents.sovereignweb.site/. Shared with d.strategy (account D), which keeps site/factory/dinis-cruz/account-d/ and its own pages; change only b.strategy's paths: site/accounts/b/**, site/factory/dinis-cruz/account-b/**, site/keys/strategy.b.json, site/decisions/requests/<b.strategy's ids>, site/decisions/opinions/**, tools/pages/**, and the account-b lines of site/index.html, site/llms.txt, site/data/agents.json, site/factory/index.json.
- **Read only:** SovereignWebsite__IaC (the Factory; agents do not push there, Dinis 23 Nov 23:14 UTC), Site__Agent__Decisions (decisions.agents.sovereignweb.site), Site__Agent__Maestro, PrompTugal__News__Website (material).

## Wakes
- None. Dinis re-enables wakes himself. Work starts when Dinis or a peer writes to the session.

## Keys (by id only)
- Current: strategy.b@SovereignWebsite.dinis, signing sha256:7da14030e6234c36, at site/keys/strategy.b.json. Its private half lived only in the old session and is gone with it.
- A new session makes its own key (START.md step 2) and replaces site/keys/strategy.b.json in a commit that changes only that file, signed by the new key (key rotation, block 06).

## First steps
1. Read CLAUDE.md, now.md, agent.json, the latest sessions/*/handover.md, decisions.md, learnings.md.
2. Read https://decisions.agents.sovereignweb.site/how-it-works/ and check the open request's receipt: https://decisions.agents.sovereignweb.site/requests/strategy.b/2026-11-24__twin-copy-oauth-client.json
3. Make and publish the key; set the git config (START.md steps 2 to 4).
4. Rebuild the pages to confirm the generators work: python3 tools/pages/<name>.py; run the checks; push.
5. Update agent.json (session, updated, active_until) and now.md; log messages in messages.md.
6. Send b.decisions and b.maestro one line each: the link to this area, and that you have taken over.
