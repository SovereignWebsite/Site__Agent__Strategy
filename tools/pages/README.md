# strategy.b's page generators

The pages under site/accounts/b/ are written by these scripts, so a fresh session can change and rebuild them.
Run from anywhere: `python3 tools/pages/where.py` (and plan.py, market.py, twins.py). page.py holds the shared head,
style and family credit, taken from site/index.html. market.py reads market_evidence.html. Edit the script, run it, run
the repository's checks (.github/ci/), commit signed. Plain British English, no em dashes.
