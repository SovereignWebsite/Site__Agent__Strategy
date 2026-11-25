# cl-6.strategy: restart

A fresh session taking over:
1. Read CLAUDE.md, site/policy/abp.json, then role.md, now.md and agent.json in this folder.
2. Signing: the key in site/keys/cl-6.strategy.json is a session key; a new session makes its own with `bash tools/setup-signing.sh cl-6.strategy@dinis <session URL>`, publishes it alone in its own commit, and records the old key as ended in now.md.
3. Check opinions/ against cl-6.decisions's blocks: any block without an opinion here is the next job.
4. Update agent.json and now.md, then tell Dinis your fingerprint and this folder's link.
