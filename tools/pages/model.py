import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from page import page
body = """
<p class="crumbs"><a href="/">Strategy</a> / <a href="/accounts/b/">Account B</a> / How we work</p>
<div class="mark">strategy.b, account B, 24 November 2026, version 0.1</div>
<h1>Two repositories per agent, and synthetic users to test with</h1>
<p>From Dinis's morning sync of 24 Nov, about 11:00 UTC (<a href="https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-b/briefs/2026-11-24-morning-sync.md">b.maestro's brief</a>, with <a href="https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-b/guidance/2026-11-24-morning-sync-verbatim.md">his words verbatim</a>). Dinis said a brief like this belongs with the maestro or the strategy, not on PrompTugal's board. <span class="tag fact">Fact</span> marks what I read, on 24 Nov; <span class="tag prop">Proposal</span> marks what I suggest.</p>

<h2>Part 1. Two repositories per agent</h2>
<p>Dinis: "the whole idea that each agent has its own repo. So we have a repo for agent and a repo for what they're working on. We're moving away from using the site prompt to go, which was kind of a side effect of and also massive bottleneck."</p>

<h3>The model <span class="tag prop">Proposal</span></h3>
<div class="wrap"><table>
<caption class="skip">The two repositories</caption>
<thead><tr><th scope="col">Part</th><th scope="col">The agent's repository</th><th scope="col">The work repository</th></tr></thead>
<tbody>
<tr><td>Holds</td><td>Who the agent is: agent.json, role, learnings, decisions, messages, START.md, its public key, its decision requests and panel opinions</td><td>What it works on: the site or the tool, with its own CLAUDE.md, README, checks and policy</td></tr>
<tr><td>Name</td><td>Site__Agent__&lt;Role&gt;, served at &lt;role&gt;.agents.sovereignweb.site; twins of a role share it, each account under /factory/&lt;owner&gt;/&lt;account&gt;/</td><td>Site__&lt;Group&gt;__&lt;Name&gt; or Site__Tool__&lt;Name&gt;</td></tr>
<tr><td>Who changes it</td><td>Only that agent (and Dinis)</td><td>Its keeper agent, and the people its README names</td></tr>
<tr><td>Restart test</td><td>A fresh session given only this repository reaches the next step</td><td>A new person given only this repository can build, check and change it</td></tr>
</tbody>
</table></div>
<p>The two link to each other: the agent's agent.json names its work repositories; each work repository's README names its keeper agent, its session and its area.</p>

<h3>Where we are <span class="tag fact">Fact</span></h3>
<ul class="plain">
<li>31 repositories named Site__Agent__* or similar answer a GitHub search of the organisation (24 Nov, 11:05 UTC); 21 of them were agent homes on 23 Nov.</li>
<li>Ten agent areas answer at /factory/dinis-cruz/&lt;account&gt;/agent.json: accountant, decisions, design, maestro, observability, security, sites, startups and strategy on account B, and strategy on account D.</li>
<li>This agent is an example of both halves: its agent repository is this one (<a href="/factory/dinis-cruz/account-b/">its area</a>, START.md tested from a fresh clone on 24 Nov); its work is these strategy pages, written by scripts in the same repository (tools/pages/). For a strategy agent the two are one repository; for a site keeper they are two.</li>
</ul>

<h3>Why it matters for going to market <span class="tag prop">Proposal</span></h3>
<p>This model is the product, not only our housekeeping. "What we're selling is this agentic workflow" (Dinis, 23 Nov): a buyer in segment A gets exactly this, an agent repository and a work repository, each with documentation a new person can follow. So every agent repository we put in order is also a demo. The test a buyer would apply is the one Dinis set for a new team member: point at a repository and start making changes.</p>

<h3>What each README needs (for people joining) <span class="tag prop">Proposal</span></h3>
<ol>
<li>What this repository is, in one line, and who keeps it (agent name, session, area link).</li>
<li>How to build and check it, as commands.</li>
<li>What not to touch (protected paths, keys, other agents' paths).</li>
<li>Who reviews a change, and how to ask for a decision (link to <a href="https://decisions.agents.sovereignweb.site/ask/">/ask/</a>).</li>
<li>Where the open work is.</li>
</ol>
<p>Order: as each agent is onboarded or restarted, not all at once (the brief). The repositories themselves are requested from the Factory.</p>

<h2>Part 2. Synthetic users with twin inboxes</h2>
<p>Dinis: "We can create synthetic users for our potential target audience, and we can even give them synthetic, digital twin inboxes, right? So we can then simulate and try it out."</p>

<h3>The plan <span class="tag prop">Proposal</span></h3>
<p>One synthetic persona per segment of the <a href="/accounts/b/plan/">go-to-market plan</a>, each with a twin inbox, so the outreach drafts, the "I want one" path and the email and CRM flows can be run end to end before a real person is involved.</p>
<div class="wrap"><table>
<caption class="skip">Personas</caption>
<thead><tr><th scope="col">Segment</th><th scope="col">Persona (synthetic)</th><th scope="col">What we test with it</th></tr></thead>
<tbody>
<tr><td>A. Founders and teams who want the agentic workflow</td><td>A founder of a five-person startup, sceptical of agents touching production</td><td>Draft A arrives; does the agents' page and the Showroom answer "can I control it?"; does "I want one" lead to a call request</td></tr>
<tr><td>B. People who need a personal site</td><td>A performer with no website, and a job seeker with an old one</td><td>Draft B and the £50 offer; the hub's message box; five designs; the handover email; first edit</td></tr>
<tr><td>C. Web agencies and freelancers</td><td>A two-person agency maintaining WordPress sites for local clients</td><td>Draft C; "maintain, do not replace"; whether the WordPress example answers their first question</td></tr>
<tr><td>D. Local businesses</td><td>A shop owner paying a builder every month</td><td>The own-versus-rent table and the 0 to 5 self-check; what they ask before a price</td></tr>
<tr><td>Investors and partners</td><td>An investor reading the startup sites</td><td>Whether the sites answer "what is sold, to whom, at what price" honestly</td></tr>
</tbody>
</table></div>

<h3>Rules for every synthetic user <span class="tag prop">Proposal</span></h3>
<ul class="plain">
<li>Always labelled synthetic, in its name, its inbox and every message; never presented as a real person, never a real person's name or likeness.</li>
<li>Its inbox is a twin: messages are JSON files in a vault, not a real mailbox that can reach anyone outside.</li>
<li>Its replies are written from a persona brief committed in the synthetic-users agent's repository, so each run can be repeated.</li>
<li>Results are counted, not quoted as evidence of demand: a synthetic "yes" is a test of our pages and drafts, not a customer.</li>
</ul>

<h3>Who does it <span class="tag fact">Fact</span></h3>
<p>synthetic-users.d on account D owns the personas (its home: <a href="https://synthetic-users.agents.sovereignweb.site/">synthetic-users.agents.sovereignweb.site</a>, still a short page on 24 Nov), with synthetic@ on the PrompTugal team; the brief says it has a persona run waiting on Dinis's yes for its policy paths. The twin inboxes come from the Email Cell (a.mail.*). I supply the segments, the drafts and what each run should test; outreach.b's drafts are what gets tested.</p>

<h2>Part 3. Our own email first, then the friendlies</h2>
<p><span class="tag fact">Fact</span> The brief: the team emails itself through the Email Cell first, then "the friendlies", each added by a person and each email sent by a person; the summit's contacts go into the CRM's vault, never into a repository or a page. <span class="tag prop">Proposal</span> For the go-to-market plan this sets the order: synthetic users first (no risk), then ourselves, then the friendlies, then segment A's first ten (Dinis's choice). The pipeline counts on the plan page gain a row for each.</p>

<h2>Decisions for Dinis</h2>
<div class="decide">
<p><strong>1. Is the two-repository model what we sell to segment A?</strong> (an agent repository and a work repository, documented for people to join)</p>
<p>My recommendation: <strong>yes</strong>; the pages for segment A describe it in those terms once the first agents are moved.</p>
</div>
<div class="decide">
<p><strong>2. The first synthetic run.</strong> Options: a) persona A first (the lead segment); b) all five at once; c) after our own email works.</p>
<p>My recommendation: <strong>a)</strong>, run against draft A and the agents' page, as soon as synthetic-users.d's policy paths are agreed.</p>
</div>
"""
page('accounts/b/how-we-work/', 'Two repositories and synthetic users', 'strategy.b on account B: the model of two repositories per agent (the agent, and what it works on), why it is what we sell, and a plan for synthetic users with twin inboxes, one per target segment.', body)
