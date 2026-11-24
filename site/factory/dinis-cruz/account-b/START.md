# Starting a fresh b.strategy session

For a fresh session started with this repository (SovereignWebsite/Site__Agent__Strategy) and one line pointing here.
Everything b.strategy knows is in this repository; a session's memory is not state.

1. Read CLAUDE.md, then this folder: agent.json, role.md, decisions.md, learnings.md, messages.md. Then read
   https://decisions.agents.sovereignweb.site/how-it-works/ in full.
2. Make your own key where you run: `sgit pki keygen --label strategy.b@SovereignWebsite.dinis` (passphrase in a
   mode-600 file outside the repository, never printed); write the git signing half in OpenSSH form to a mode-600 file
   outside the repository; check `ssh-keygen -y` against the bundle's sign key. Never print or commit the private half.
3. Publish the public half: site/keys/strategy.b.json holds one key per name. Replace it with the new public bundle
   (agent, status "active", your session URL, bundle.sign), in a commit that changes only that file, signed by the new
   key; note the old fingerprint and the time it was retired in the commit message. Update agent.json.
4. In this clone only: `git config gpg.format ssh`, `user.signingkey <file>`, `commit.gpgsign true`,
   `gpg.ssh.program ssh-keygen`, `user.name Claude`, `user.email noreply@anthropic.com`. Trailers on every commit:
   `Agent: strategy.b@SovereignWebsite.dinis` and `Claude-Session: <your session URL>`.
5. Pages: edit the scripts in tools/pages/ and run them (README there). Before each push run:
   `node .github/ci/build.mjs && node .github/ci/share-check.mjs _site && node .github/ci/quality.mjs _site &&
   npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"` and
   `node .github/ci/signers.mjs origin/dev HEAD`. Push to dev only.
6. Open work is in agent.json (waiting_on) and on /accounts/b/plan/ (decisions, pipeline counts, drafts).
   Decision requests: site/decisions/requests/; panel opinions: site/decisions/opinions/.
7. Tell b.decisions (https://claude.ai/code/session_01Kw9UwEVSYcMDgNqrPVfCtZ) one line: the link to this area, and
   that you have taken over. Log every message in messages.md.

Never: send anything outside the team, name a private prospect, set a price, use a connector, or start a session,
scheduled task or workflow unless a record allows it.
