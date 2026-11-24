import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); G = HERE
from page import page
ev = open(G + '/market_evidence.html').read()
body = """
<p class="crumbs"><a href="/">Strategy</a> / <a href="/accounts/b/">Account B</a> / Market</p>
<div class="mark">strategy.b, account B, 23 November 2026, version 0.1</div>
<h1>The market: own it or rent it</h1>
<p>Public pages only, read on 23 November 2026, each with its link. No login, no contact, nothing copied. Prices are as each vendor's page showed them to a reader outside the UK, so most are in dollars; where a page did not say whether a price is monthly or annual billing, I say so. A page is not the product: what a page does not say may still exist. Builds on <a href="https://github.com/PrompTugal/PrompTugal__News__Website/tree/dev/board/team/landscape.d">landscape.d's</a> 31 players, read on 22 November.</p>

<h2>Own versus rent, for the hub <span class="tag fact">Fact</span></h2>
<div class="wrap"><table>
<caption class="skip">Own versus rent</caption>
<thead><tr><th scope="col">Product</th><th scope="col">Price as published</th><th scope="col">Can you take the site away?</th></tr></thead>
<tbody>
<tr><td>Wix</td><td>No UK price obtained: the page showed regional dollar prices only (Light $17.77 to Business Elite $159.77 a month, "includes GST")</td><td>No: "your site must run on Wix's servers" (<a href="https://support.wix.com/en/article/exporting-or-embedding-your-wix-site-elsewhere">Wix help</a>)</td></tr>
<tr><td><a href="https://www.squarespace.com/pricing">Squarespace</a></td><td>Basic $19 to $25, Core $29 to $39, Plus $49 to $65, Advanced $99 to $139 a month (lower figure appears to be annual billing)</td><td>In part: an XML file of some content; not store pages, custom CSS or style settings</td></tr>
<tr><td><a href="https://webflow.com/pricing">Webflow</a></td><td>Basic $15, Premium $25 a month, billed yearly</td><td>In part: HTML and CSS on paid Workspace plans; "Dynamic content (CMS items/pages) can't be exported"; forms stop working</td></tr>
<tr><td><a href="https://www.framer.com/pricing">Framer</a></td><td>Basic $10, Pro $30 a month</td><td>No: "Framer does not offer HTML export for self-hosting"</td></tr>
<tr><td><a href="https://www.hostinger.com/uk/website-builder">Hostinger</a></td><td>From £1.79 a month on 48 months paid upfront (£85.92), renewing at £10.99 a month</td><td>By hand: copy text, save images; an export of content to WordPress exists</td></tr>
<tr><td><a href="https://www.ionos.co.uk/websites/website-builder">IONOS (UK)</a></td><td>Starter £6 a month for 6 months (then £10 shown struck through), excluding VAT</td><td>No: builder projects "cannot be used outside the IONOS infrastructure"</td></tr>
<tr><td><a href="https://www.jimdo.com/pricing/">Jimdo</a></td><td>Start $11 to Unlimited $49.50 a month, billed yearly (from the page's data; the cards did not render)</td><td>The domain, yes; the site, page by page by hand</td></tr>
<tr><td><a href="https://wordpress.com/pricing/">WordPress.com</a></td><td>Personal $4 to Commerce $45 a month on yearly billing</td><td>Content yes (posts, pages, comments); theme and media not in the export; full backup on Business and above</td></tr>
<tr><td><a href="https://durable.com/pricing">Durable</a></td><td>Launch $22 to $25, Grow $41 to $49 a month</td><td>Not stated; the domain can be transferred out</td></tr>
<tr><td><a href="https://lovable.dev/pricing">Lovable</a></td><td>Pro $25, Business $50 a month</td><td>Yes, as code: "You own your code"; GitHub sync on all plans</td></tr>
<tr><td><a href="https://fliplet.com/pricing/">Fliplet</a></td><td>Free $0, Plus $25, Max from $50 a month (USD); Enterprise custom</td><td>No: "Fliplet does not offer a facility for You to transfer or copy any Content or Applications from Your Account to a third party service provider" (<a href="https://fliplet.com/terms/">terms</a>, 8.2)</td></tr>
<tr><td><a href="https://sovereignwebsite.ai/pricing.html">Sovereign Website</a></td><td>Launch offer £50, and €50 on European sites, paid once, "Decided by Dinis Cruz, 23 November 2026"; £500 anchor; nothing sold yet</td><td>Yes: plain files in a repository the owner holds, on any host</td></tr>
</tbody>
</table></div>

<h3>What we do better, in one line each</h3>
<ul class="plain">
<li>The whole site leaves with you, design included, not only the words. Of the eleven above, only Lovable says the same, and it is a tool for people who code.</li>
<li>Paid once, against monthly prices that rise: Squarespace raised its annual plans by up to 26% this year (below).</li>
<li>A team builds it from your words and photos, and your own AI edits it inside a written policy.</li>
</ul>
<h3>What we do not do yet</h3>
<ul class="plain">
<li>Nothing is sold yet. The launch offer was decided on 23 Nov; the way to take it up (the hub's message box) is being switched on.</li>
<li>Editing needs a Claude plan, or a partner, so "no technical skill" is not yet true.</li>
<li>No shop, no bookings, no forms of our own: the sites are static files.</li>
<li>No support desk, no service level, no certification.</li>
</ul>

<h2>What a person charges <span class="tag fact">Fact</span></h2>
<p>Third-party estimates, not survey data, and no named agency's price list was found:</p>
<ul class="plain">
<li>A five-page brochure site: freelancer £1,500 to £3,000, agency £3,000 to £5,000, excluding VAT; care plans £25 to £100 a month, agency retainers "typically £50 to £200" (<a href="https://whito.co.uk/research/website-design-costs-uk/">Whito</a>, page dated 18 Nov 2026, method not given).</li>
<li>Freelancer, three to five pages: £500 to £1,500; maintenance "£50-£300/month" (<a href="https://www.expertsure.com/uk/web-design/freelance-web-designer-costs/">ExpertSure</a>, "verified Oct 2026").</li>
</ul>
<p>So the recorded £500 anchor sits at the low end of a freelancer's build, and well below an agency's. That is a fact about the market, not a price recommendation.</p>
""" + ev + """
<h2>What this means <span class="tag prop">Proposal</span></h2>
<ol>
<li><strong>Lead with leaving, not with building.</strong> Every rented builder read either says you cannot leave or lets only part of the site go. "Your whole site, yours to move" is a claim we can prove and they cannot make.</li>
<li><strong>The managed services prove people pay a team monthly</strong> ($25 to $125 a month at UENI, with a $599 setup). None hands over the site. Our offer to A and C is that team, with the site handed over.</li>
<li><strong>Agencies are already a channel</strong> for white-label builders. Ours is the inverse: the client owns, the agency keeps the care fee.</li>
<li><strong>Still to read:</strong> UK prices for Wix, Squarespace and Webflow from a UK browser; Netlify's terms on commercial use; Durable's terms on export.</li>
</ol>
"""
page('accounts/b/market/', 'The market: own it or rent it', 'strategy.b on account B: website builders and managed services, their published prices and what they say about leaving, read 23 November 2026, with demand evidence.', body)
