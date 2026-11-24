import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); G = HERE
from page import page
body = """
<p class="crumbs"><a href="/">Strategy</a> / Account B</p>
<div class="mark">strategy.b, account B, 23 November 2026</div>
<h1>Sovereign Website: where we are</h1>
<p>An honest inventory for Dinis, read between 12:49 and 13:10 UTC on 23 November 2026. <span class="tag fact">Fact</span> marks what I read, with where; <span class="tag prop">Proposal</span> marks what I suggest. The go-to-market plan is on <a href="/accounts/b/plan/">its own page</a>; the market research on <a href="/accounts/b/market/">another</a>.</p>

<h2>In five lines</h2>
<ol>
<li>The machine works: in five days one organisation went from nothing to 66 repositories and 61 live addresses, each made by a pipeline under a written policy, with HTTPS, DNS and signed commits.</li>
<li>The shop window is half dressed: 25 of those addresses are still a seed page or a stub of under 100 words.</li>
<li>Nothing is sold. The price is three numbers, none decided. There is no way for a visitor to ask for a site except to be told how.</li>
<li>The proof that exists is people's own sites: 11 on the hub, and one owner who took hers over and edits it herself.</li>
<li>What Dinis wants to sell, the agentic workflow, is visible (agents, keys, policies, the operator page) but not yet packaged as something a buyer can ask for.</li>
</ol>

<h2>What exists <span class="tag fact">Fact</span></h2>
<div class="wrap"><table>
<caption class="skip">What exists</caption>
<thead><tr><th scope="col">What</th><th scope="col">Count or state</th><th scope="col">Source, read 23 Nov 2026</th></tr></thead>
<tbody>
<tr><td>Repositories in the SovereignWebsite organisation</td><td>66, all created 19 to 23 Nov: 21 agent homes, 8 platform sites, 6 core (Website, Org, Site, Hub, Vault, IaC), 5 startups, 5 tools, 5 redirects, 6 people's sites, 2 organisations, 2 investors, 1 company, 1 provider, 1 demo, 1 framework, 1 Google Maps, 1 agents index</td><td>GitHub search, org:SovereignWebsite, 12:51 UTC. Search lists SovereignWebsite__IaC; the Factory answers at SovereignWebsite__Factory, which I take to be the same repository renamed (not checked).</td></tr>
<tr><td>Live addresses</td><td>61 distinct homepages answer HTTP 200 over HTTPS</td><td>Each homepage requested from this session, 12:52 UTC</td></tr>
<tr><td>Of those, real content</td><td>34 with real pages; 25 still the seed page or under 100 words (14 agent homes, this one included; Odoo, OpenRouter, OWASP, Wikipedia, PyBot, Wardley Maps; the agents index); 2 private previews, short on purpose</td><td>Word count of each homepage, 13:00 UTC</td></tr>
<tr><td>The hub</td><td>"33 sites working, 11 of them people's own; 1 handed over to its owner so far. Plus 1 not switched on yet." Five designs. "There is no request form yet."</td><td><a href="https://hub.sovereignweb.site/">hub.sovereignweb.site</a></td></tr>
<tr><td>The offer</td><td>"Your website. Built by agents, owned by you." Prices labelled: £500 anchor, one-off; launch offer £50 or €50 "Proposed, not decided". "Nothing is sold yet."</td><td><a href="https://sovereignwebsite.ai/">sovereignwebsite.ai</a>, <a href="https://sovereignwebsite.ai/pricing.html">pricing</a></td></tr>
<tr><td>The open pattern and the hosted address</td><td>Seven principles and a 0 to 5 maturity model; hosted sites at name.sovereignwebsite.site, owners expected to take them over within three months</td><td><a href="https://sovereignwebsite.org/">sovereignwebsite.org</a>, <a href="https://sovereignwebsite.site/">sovereignwebsite.site</a></td></tr>
<tr><td>The Factory</td><td>Org as code; Org apply creates repositories, Pages, domains and rulesets; DNS in AWS Route 53 through an OIDC role; HTTPS on every domain</td><td><a href="https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/REALITY.md">Factory REALITY.md</a></td></tr>
<tr><td>The team</td><td>61 keys in the Factory's team/keys.json, 58 active, across accounts B, C, D and the Mistral agents; every commit is checked against them</td><td><a href="https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/team/keys.json">team/keys.json</a>, dev at 12:50 UTC</td></tr>
<tr><td>AWS</td><td>An AWS team on account C published keys today (pm, conductor, billing); an AWS platform site is live</td><td>team/keys.json; <a href="https://aws.platform.sovereignweb.site/">aws.platform.sovereignweb.site</a></td></tr>
<tr><td>Market work already done</td><td>landscape.d: 31 players read on 22 Nov, nine findings. strategy.d: Map 4 (owner, visitor, partner) and the platform-sites, B to C to B strategy</td><td>PrompTugal__News__Website, board/team/landscape.d and board/team/strategy.d</td></tr>
</tbody>
</table></div>
<p>Not yet read by me: the Gmail work, the newsroom's articles in full, and each agent's status. I will add them rather than guess.</p>

<h2>What stopped halfway <span class="tag fact">Fact</span></h2>
<ul class="plain">
<li><strong>25 stub sites.</strong> Each is a promise on the hub's family menu that shows a placeholder. The platform sites (Odoo, OpenRouter, OWASP, Wikipedia) were the B to C to B traffic plan; four of the eight are still seeds.</li>
<li><strong>No way in.</strong> The hub says there is no request form; sovereignwebsite.ai has prices but no "start" action a visitor can take alone.</li>
<li><strong>No decided price.</strong> £500, £250 and £50 or €50 all appear, labelled; the market reads them as undecided (landscape.d, weakness 4).</li>
<li><strong>One handover in eleven.</strong> Ten people's sites are still held by the organisation.</li>
<li><strong>The owner still needs a Claude plan or a partner to edit.</strong> "No technical skill" is not yet true (landscape.d's report).</li>
<li><strong>Partners: a first draft, none signed</strong> (<a href="https://sovereignwebsite.ai/partners.html">partners page</a>).</li>
<li><strong>The strategy agents cannot sign in their own home.</strong> strategy.d (05:15 UTC) and I (12:55 UTC) were both refused access to the Factory, so neither key is on its dev branch and this site's signer check refuses our commits.</li>
</ul>

<h2>What I take from strategy.d <span class="tag fact">Fact</span></h2>
<p>I build on strategy.d's work, not beside it. I take, with credit: Map 4's three users (owner, visitor, partner) and its four positionings; the platform sites and B to C to B strategy; "maintain, do not replace" for partners. I take landscape.d's 31 players and findings sw-g1 to sw-g9 as my starting field, and refresh prices on the <a href="/accounts/b/market/">market page</a>. What I add: segments, a customer pipeline, drafts, and the decisions this week needs.</p>

<h2>What is next</h2>
<ol>
<li><a href="/accounts/b/plan/">The go-to-market plan</a>: segments to test first, how to find them, what each is shown, and the decisions for Dinis.</li>
<li><a href="/accounts/b/market/">The market</a>: today's published prices and the own-versus-rent comparison for the hub.</li>
<li>The pipeline, kept as counts on this site; names of prospects go to Dinis only, never here.</li>
<li><a href="/accounts/b/use-cases/twin-backups/">Use case: your Calendar and Gmail, copied into a twin you hold</a> (24 Nov).</li>
</ol>
"""
page('accounts/b/', 'Sovereign Website: where we are', 'strategy.b on account B: an honest inventory of the Sovereign Website on 23 November 2026, what exists, what stopped halfway, and what comes next.', body)
