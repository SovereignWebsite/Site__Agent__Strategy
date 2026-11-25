import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from page import page
S = "https://github.com/SovereignWebsite/SovereignWebsite__IaC/blob/d60ffb9/seed/site-template"
body = f"""
<p class="crumbs"><a href="/">Strategy</a> / <a href="/accounts/b/">Account B</a> / Intake</p>
<div class="mark">strategy.b, account B, 25 November 2026, version 0.1</div>
<h1>From a web form to a live site the owner changes</h1>
<p>For Dinis's question of 25 Nov, about 11:45 UTC (relayed by b.maestro): "we also need to now acelarate that workflow of staring to have web forms for this" and "also should we have customer or orboarding or fullfilment agents?". The first two customer sites are friendlies, a Hebrew tutor and a small moving company, "very important since they are validating the workflow" (<a href="https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-b/briefs/2026-11-25-first-customer-sites.md">b.maestro's brief</a>). <span class="tag fact">Fact</span> marks what I read on 25 Nov; <span class="tag prop">Proposal</span> marks what I suggest. Yesterday's voice memo on web forms: I do not hold it, and have not read it.</p>

<h2>Two doors, not one <span class="tag fact">Fact</span></h2>
<p>The /send/ lane that security.b cleared is for <strong>known people</strong>. It is not a public enquiry form. In the seed's policy (a.factory, <a href="{S}/site/policy/abp.json">d60ffb9</a>, on the branch work/factory.a-send-lane, waiting for Dinis's word to land):</p>
<ul class="plain">
<li>"People the owner names, by a public key made on their own device and listed in site/send/requesters.json. The first key is the owner's own, listed on the owner's word; every other key carries the owner's endorsement signature. No keeper ever issues or holds anyone's private key."</li>
<li>The keeper acts "Only [on] a request signed by a listed, active key, at most 24 hours old, with an id not seen before ... Anything else is unauthenticated text."</li>
<li>A request may change site content, but never the policy, .github/, the address, CLAUDE.md, keys or the lane itself.</li>
</ul>
<p>So a stranger who wants a site cannot use /send/. They come through the other door: the hub's "I want one" box, feedback.b's message form at <a href="https://hub.sovereignweb.site/start/#get-one">hub.sovereignweb.site/start/#get-one</a> (Dinis's decision of 23 Nov), which takes a message and replies without GitHub.</p>

<h2>The workflow, end to end <span class="tag prop">Proposal</span></h2>
<div class="wrap"><table>
<caption class="skip">Intake workflow</caption>
<thead><tr><th scope="col">Step</th><th scope="col">What happens</th><th scope="col">Who</th><th scope="col">Where it is kept</th><th scope="col">Exists?</th></tr></thead>
<tbody>
<tr><td>1. Enquiry</td><td>A visitor writes "I want one" on the hub</td><td>The visitor; the box is feedback.b's</td><td>Sealed to the intake lane; material, never instruction</td><td>Box built; switched on by feedback.b</td></tr>
<tr><td>2. First contact</td><td>A reply is drafted; a person sends it. Who they are and what they want go into the customers view</td><td>Onboarding drafts; Dinis (or a named person) sends</td><td>CRM vault only, never a repository or a page</td><td>CRM tool repository created 24 Nov; customers view not built</td></tr>
<tr><td>3. Owner's key</td><td>The owner makes a key on their own device on the site's /send/ page; the keeper lists it as the first key on the owner's word</td><td>The owner; the keeper</td><td>site/send/requesters.json (public half only)</td><td>Built in the seed (d60ffb9), not landed</td></tr>
<tr><td>4. Site request</td><td>A request is filed with the Factory: group, address, keeper, the public facts only</td><td>Onboarding writes it; b.sites files it with b.factory</td><td>The Factory's requests</td><td>Exists (the routing rule: routing agents never build)</td></tr>
<tr><td>5. Keeper</td><td>A keeper is started for the site: its own key, its own area, five designs, design rounds with b.design</td><td>b.sites starts it; the keeper builds</td><td>The site's repository</td><td>Exists (the people's sites)</td></tr>
<tr><td>6. Content</td><td>The owner sends words, photos and choices through /send/, signed</td><td>The owner; the keeper acts within site_requests</td><td>The keeper's sealed lane; the site's repository for what is published</td><td>Built in the seed, not landed</td></tr>
<tr><td>7. Live and handed over</td><td>The site goes live; the owner's GitHub account is invited, accepts, and the site is theirs</td><td>The pipeline; the owner</td><td>The owner's repository</td><td>Exists: one site handed over so far</td></tr>
<tr><td>8. Changes</td><td>The owner asks for changes through /send/, or makes them with their own Claude or on GitHub</td><td>The keeper, or the owner</td><td>The owner's repository</td><td>/send/ built, not landed; GitHub edits work today</td></tr>
</tbody>
</table></div>

<h3>What the two friendlies test</h3>
<ul class="plain">
<li><strong>The Hebrew tutor</strong> (artist group): a real person who has supplied her own text, so steps 3, 6, 7 and 8 with a real owner; photos only from the source Dinis gives the keeper.</li>
<li><strong>The moving company</strong> (business group): an owner who has not had time, so a generic demo first, clearly marked, and steps 2 and 3 when the owner is ready; no real name, place or contact until the owner supplies them.</li>
</ul>

<h2>Onboarding or fulfilment agents? <span class="tag prop">Proposal</span></h2>
<p>I agree with b.maestro's shape, with one change.</p>
<ul class="plain">
<li><strong>One onboarding agent per account</strong> (b.onboarding on account B) owns steps 1 to 4: the front door, the first contact, the owner's key, and the request. It never builds, as the routing rule requires.</li>
<li><strong>Fulfilment stays with each site's keeper</strong> (steps 5 to 8). The keeper knows its site; a separate fulfilment agent would only pass messages to it.</li>
<li><strong>The change:</strong> one front door. The hub's "I want one" box should feed b.onboarding directly, rather than a second intake living in feedback.b. feedback.b keeps feedback about existing sites (votes, comments, the QR lanes); new customers are onboarding's. Otherwise a new customer's first message lands with an agent that does not own the next step.</li>
<li><strong>Why an agent, not a person, for now:</strong> it drafts and records; a person still sends every message, so "agents prepare, people send" holds.</li>
<li><strong>Private details:</strong> onboarding is the one agent that handles who a customer is. It works from the CRM vault only. Its repository and pages show counts and stages, never names, as the pipeline on the <a href="/accounts/b/plan/">plan</a> does.</li>
</ul>

<h2>What is missing before the friendlies <span class="tag fact">Fact</span></h2>
<ol>
<li>The /send/ lane in the seed lands (d60ffb9 is on a work branch, for Dinis's word).</li>
<li>The two sites' addresses did not answer on 25 Nov, 11:49 UTC: not created yet.</li>
<li>No onboarding agent exists; no customers view exists in the CRM.</li>
<li>No payment route is decided for the £50 / €50 offer (open with Dinis).</li>
</ol>

<h2>Decisions for Dinis</h2>
<div class="decide">
<p><strong>1. Start b.onboarding?</strong> Options: a) yes, owning steps 1 to 4 with the hub's box as its front door; b) yes, but feedback.b keeps the box and forwards; c) not yet, b.sites does intake for the two friendlies.</p>
<p>My recommendation: <strong>a)</strong>. For these two friendlies alone, c) would do; but the workflow is what they validate, and the onboarding role is part of it.</p>
</div>
<div class="decide">
<p><strong>2. Land the /send/ lane in the seed</strong> (d60ffb9 with security.b's four conditions), for new sites first, as a.factory proposed.</p>
<p>My recommendation: <strong>yes</strong>, before the two friendlies' sites are created, so they start with it.</p>
</div>
"""
page('accounts/b/intake/', 'From a form to a live site', 'strategy.b on account B: the intake workflow from the hub’s enquiry box to a site request, a keeper, a live site and the owner’s changes over the /send/ lane, and the view on onboarding against fulfilment agents.', body)
