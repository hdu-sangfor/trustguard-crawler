# Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity

### 来源信息
- **URL**: https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
Attackers whose methods line up with the data-extortion group ShinyHunters have spent the past year walking into corporate Salesforce environments without exploiting a single flaw in the platform.
The way in has been the trust the organization had already extended, usually through the OAuth connections that tie Salesforce to the apps and third-party vendors around it.
In research published July 13, Microsoft mapped the campaigns, which ran from mid-2025 into mid-2026, to three distinct techniques. It also worked with Salesforce to roll out new detection and governance tooling aimed at addressing the activity authentication logs miss.
That is what makes this hard to catch. When the access comes from a real user who approved a connected app, or from an integration the company already trusts, the traffic reads as ordinary use, and sign-in and authentication monitoring barely registers it.
What matters is what the app or account does once it is in, and that is exactly what most Salesforce logging was not built to show.
Microsoft groups the activity into three intrusion paths:
- vishing calls that trick employees into approving a malicious connected app,
- stolen OAuth tokens from compromised software vendors, and
- misconfigured guest access to Salesforce sites.
Each maps onto a Salesforce incident from the past year, and Microsoft says it saw the activity across tenants in industries including retail, education, and manufacturing.
The phone call
The first path is the one that kicked off the whole run. Starting in mid-2025, the actors placed voice-phishing (vishing) calls posing as IT support and talked employees through Salesforce's OAuth consent screen, getting them to authorize an attacker-controlled connected app dressed up as Salesforce's own Data Loader tool.
Once consent was granted, the app could make API calls as that user, letting the attackers enumerate the org's Salesforce data, hold persistent access to CRM records, and hunt for credentials that might open the door to other SaaS platforms.
No malware, no stolen password replay. Just a phone call and a consent click.
This is the campaign Google's Threat Intelligence Group (GTIG) and Mandiant documented in mid-2025, tracking the initial access as UNC6040 and the follow-on extortion as UNC6240, both of which kept claiming to be ShinyHunters to lean harder on victims.
Google confirmed one of its own corporate Salesforce instances was hit in June 2025, with the attackers taking largely public business contact data before Google cut them off. The same wave was publicly linked to breaches at Chanel and Pandora, with Adidas, Qantas, Allianz Life, and several LVMH brands also named as targets.
Mandiant's advice to defenders was blunt: these calls exploit a help desk's instinct to be helpful, standard identity checks often do not apply, and the safe move is to hang up and call back on a known-good channel.
Stolen tokens from trusted vendors
The second path skips the employee entirely. Instead of phishing a user, the attackers compromise a third-party vendor whose app already holds OAuth access to its customers' Salesforce orgs, steal the connection secrets or tokens, and use them to query and export data across many downstream instances at once.
Because the traffic comes from an approved integration, it does not trigger sign-in alarms and blends into normal automation.
Microsoft points to three incidents here. The August 2025 Salesloft Drift compromise is the biggest and the clearest: attackers stole OAuth and refresh tokens tied to the Drift AI chat integration and turned them against Salesforce customer environments.
Google estimated that the Drift token theft potentially exposed more than 700 organizations, among them Cloudflare, Zscaler, Palo Alto Networks, Proofpoint, PagerDuty, and Tanium. Google tracks the cluster as UNC6395; Cloudflare's Cloudforce One calls it GRUB1.
Salesloft later traced the root cause to the attacker's access to its GitHub account as early as March 2025, which was used to reach Drift's AWS environment and harvest the tokens. The operators were there for secrets, running SOQL queries to sift through support cases and other objects for AWS keys, Snowflake tokens, and passwords, then deleting their query jobs to slow down anyone investigating.
The November 2025 Gainsight incident ran the same play against a different vendor. Salesforce pulled Gainsight-published apps after spotting unusual API activity, and GTIG tied the campaign to ShinyHunters affiliates across more than 200 affected Salesforce instances.
The people behind the ShinyHunters name claimed the Salesloft and Gainsight waves together reached close to 1,000 organizations, a figure that has not been independently confirmed.
The most recent case, from June 2026, is the Klue compromise. Attackers got into the competitive-intelligence platform through a long-disused but still-active legacy credential left over from a test integration that was never deployed, pushed a code update that harvested customers' OAuth tokens, and used those to reach Salesforce and Gong data belonging to Klue customers, including Huntress and Recorded Future.
Microsoft tracks the Klue actor as Storm-3138. One naming wrinkle for anyone cross-referencing reports: most of the industry, Huntress and Datadog included, ties the Klue extortion to a group calling itself Icarus, and a Telegram account claiming to be ShinyHunters also took credit.
The labels blur because these identities overlap and get claimed opportunistically, which holds across this whole set of campaigns.
Guest access left open
The third path needs no credentials at all. Microsoft saw a rise in suspicious guest-user activity against Salesforce Aura endpoints, the framework behind Experience Cloud sites. Where guest-user permissions were misconfigured, the actors reached Aura functionality without authenticating.
Calling the GraphQL Aura controller, they used cursor-based pagination to pull records past the standard 2,000-record query limit, walking off with far more than the guest role was meant to expose.
Microsoft's related detection points to the AuraInspector tooling used to probe these endpoints. No exploit was involved. The org had left the guest role able to see more than it should, and the actors read it for everything it was worth.
What Microsoft and Salesforce shipped to catch it
The signal that does exist lives in what happens after access: which connected app made a call, what OAuth scopes it holds, how much it is querying, and whether any of that is normal for the tenant.
Microsoft worked with Salesforce to surface exactly that in Defender for Cloud Apps. For customers running Salesforce Shield Event Monitoring, the upgraded Salesforce connector onboards the Real-Time Event Monitoring framework for near-real-time detection and adds connected-app attribution, tying activity to a specific app identity and its granted OAuth scopes, along with more session and API context.
Alongside detection, Microsoft added posture and governance features for connected OAuth apps: a view of highly privileged apps holding elevated scopes, a way to surface unused apps that have sat inactive for 90 days or more while keeping live permissions, and a 0 to 100 risk score per app that teams can wire to alerts and policies.
The aim is to find the over-permissioned and forgotten integrations before someone else does.
Shrinking the OAuth attack surface
Microsoft's guidance is practical and matches what the vendors said after each incident: connect Salesforce instances to Defender for Cloud Apps for the extra telemetry, turn on and actually watch Salesforce event logs, and lock down Experience Cloud guest-user access.
Beyond the product-specific steps, the durable fixes are the familiar ones. Inventory the connected apps, cut the ones nobody uses, scope the rest to least privilege, and be ready to revoke and rotate tokens the moment an integration starts behaving oddly.
The pattern under all three paths is the same. The identity controls most companies spent the last decade building were made for human logins: MFA, conditional access, and session policies. The OAuth apps, integration accounts, and service credentials that do the actual work in a modern Salesforce stack mostly sit outside all of it, unwatched and over-permissioned.
The attackers who figured this out ran it for a year, and more than once, the way in was nothing more exotic than a credential someone forgot to switch off.
The Hacker News has reached out to Microsoft for further details on its attribution of the actors behind these campaigns and will update this story with any response.

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
