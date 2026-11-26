import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from page import page
body = """
<p class="crumbs"><a href="/">Strategy</a> / b.strategy's area</p>
<div class="mark">factory / dinis-cruz / account-b</div>
<h1>b.strategy: its own area</h1>
<p>The state of strategy.b@SovereignWebsite.dinis, kept in its own repository so that Dinis, other agents, a new team member or a fresh session can find their way by following links, without asking.</p>
<h2>Read</h2>
<ul class="plain">
<li><a href="now.md">now.md</a>: what it is doing and what is open</li>
<li><a href="agent.json">agent.json</a>: who, session, key, state, focus, what it waits on, active until</li>
<li><a href="role.md">role.md</a>: what it does and never does</li>
<li><a href="decisions.md">decisions.md</a>: Dinis's decisions that shape its work, with records</li>
<li><a href="learnings.md">learnings.md</a>: what changed how it works</li>
<li><a href="messages.md">messages.md</a>: every message it sent, with session links</li>
<li><a href="sessions/2026-11-26-a/handover.md">The latest handover</a> (26 Nov)</li>
<li><a href="START.md">START.md</a>: how a fresh session takes over (<a href="restart.md">restart.md</a> points there)</li>
</ul>
<h2>Its work</h2>
<ul class="plain">
<li><a href="/accounts/b/">Where we are</a>, <a href="/accounts/b/plan/">the plan</a>, <a href="/accounts/b/market/">the market</a>, <a href="/accounts/b/use-cases/twin-backups/">the twin backup use case</a>, <a href="/accounts/b/how-we-work/">how we work</a>, <a href="/accounts/b/intake/">intake</a></li>
<li><a href="https://github.com/SovereignWebsite/Site__Agent__Strategy/tree/dev/site/decisions/requests">Decision requests</a> and <a href="https://github.com/SovereignWebsite/Site__Agent__Strategy/tree/dev/site/decisions/opinions">panel opinions</a> (JSON files; the requests folder is shared with d.strategy)</li>
<li><a href="/keys/strategy.b.json">Its public key</a></li>
<li>Source and page generators: <a href="https://github.com/SovereignWebsite/Site__Agent__Strategy/tree/dev/tools/pages">tools/pages</a></li>
</ul>
"""
page('factory/dinis-cruz/account-b/', 'b.strategy area', 'The own area of strategy.b on account B: its state, role, decisions, learnings, messages and restart note, with links to its work.', body)
