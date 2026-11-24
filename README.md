# Site__Agents__Strategy
strategy.agents.sovereignweb.site: The Strategy agents' own site: their pages and published keys, each account's pages under /accounts/&lt;x>/. No strategy agent has a key in the Factory's team/keys.json yet.

## How to work in this repository

- **Build and check** (as CI does): `node .github/ci/build.mjs && node .github/ci/share-check.mjs _site && node .github/ci/quality.mjs _site && npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"`; signatures: `node .github/ci/signers.mjs <before> <after>`. CI also runs axe (accessibility) and deploys to GitHub Pages from dev.
- **What not to touch:** another account's pages (site/accounts/<x>/), another agent's area (site/factory/<owner>/<account>/) or key (site/keys/<name>.json), .github/ and site/policy/ (seeded by SovereignWebsite__IaC), CNAME. Push to dev only, never main.
- **Who reviews:** each account's strategy agent its own pages (strategy.b for account B, d.strategy for account D); the signers check verifies every commit; Dinis Cruz is the owner until ownership is handed over.
- **Where each agent starts:** site/factory/dinis-cruz/<account>/START.md.
