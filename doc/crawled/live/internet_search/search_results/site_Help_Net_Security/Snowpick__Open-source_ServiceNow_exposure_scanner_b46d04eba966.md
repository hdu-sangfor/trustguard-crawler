# Snowpick: Open-source ServiceNow exposure scanner

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/22/servicenow-data-exposure-snowpick-open-source-scanner/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
Snowpick: Open-source ServiceNow exposure scanner
An employee opens a company service portal, searches the knowledge base, and drops a file onto a ticket. Someone who never signed in can send a request to that same portal and get records back.
Bishop Fox ran that test across 166 ServiceNow instances during authorized penetration tests. The firm published the results along with the Go tool it used, Snowpick.
Findings came back from 31% of the instances. Those instances returned records or confirmed record counts to a session carrying no credentials, and they traced to roughly three-quarters of the organizations in the dataset.
“The row-returning exposures we confirmed were not new zero-days. They were access-control and configuration issues across public ServiceNow surfaces,” Emilio Gallegos, the adversarial operator at Bishop Fox who wrote the tool, told Help Net Security.
Two surfaces, two sets of rules
ServiceNow hands out data through Service Portal widgets and through the Table REST API. Widgets live at /api/now/sp/widget/{widget_id}, accept POST requests, and drive knowledge base search, catalog pages, ticket forms, and attachment views. The Table REST API at /api/now/table/{table_name} queries sys_user, incident, oauth_entity, and the rest of the schema directly.
Each surface evaluates access control on its own path. An instance can lock its widgets down and keep answering table queries. Two instances in the dataset did that: widget probes came back clean, and the REST API returned data.
The attachment widget did most of the work
Most positive findings arrived through ticket-attachments, a stock widget that returns metadata about files attached to tickets. Titles and descriptions in that metadata carry internal process detail: onboarding guides, access request procedures, system how-tos.
Exposed knowledge base articles, incident ticket metadata, service catalog items, department structures, and facility locations turned up across the set. Record counts per finding ran from dozens into the thousands.
Credentials stayed out of this sample. The same surfaces reach oauth_entity and sys_user when ACLs permit it.
What the tool does
Snowpick requests the public login page, extracts the session token ServiceNow issues there, and reuses it for follow-on API calls. It probes a set of default widgets plus 26 built-in table and field pairs, and it can ask the instance which widgets are installed and add those to the list.
Custom widgets earn that discovery step. Organizations write their own access rules for them, and those rules never passed through platform review.
The output separates row exposure from a count oracle, meaning ServiceNow confirmed that matching records exist and returned none of them. Varonis Threat Labs documented blind inference through count behavior, tracked as CVE-2025-3648. For each finding Snowpick saves the reported total, a bounded sample of rows, and a curl command that reproduces the request.
Publishing a tool that cuts both ways
Anyone can point Snowpick at an instance they do not own. Gallegos said his team started from that. “The question we focused on was whether release would materially change attacker capability or improve defender visibility.”
The underlying techniques were public already. Aaron Costello documented widget-simple-list exposure in October 2023, including session token bootstrapping and table enumeration, and AppOmni followed with analysis of ServiceNow ACL mechanics.
Gallegos put the release decision this way: “We published Snowpick because keeping it internal would not slow anyone probing systems they don’t own – it would only keep the people accountable for these systems from finding and fixing that exposure before it becomes an incident.”
Fixing it
Platform defaults can carry part of the load. Gallegos said guardrails around public widgets and table access raise the floor, and that ServiceNow is built to be customized. “Organizations add their own widgets, tables, roles, and ACLs over time, and those combinations can behave differently than expected when reached from an unauthenticated session.”
“This is shared responsibility. ServiceNow can reduce the number of unsafe patterns, but customers still need to test their own public-facing instances from the outside, the way an attacker would.”
Remediation work starts with public Service Portal widgets that return ticket, attachment, knowledge base, catalog, or list data. Table-level, field-level, and row-level ACLs need a separate pass. A widget blocked on direct load can still be reachable through another widget that loads it.
Snowpick is available for free on GitHub.
Must read:
- 20 open-source cybersecurity tools to keep your team ready for anything
- GitHub CISO on security strategy and collaborating with the open-source community
Subscribe to the Help Net Security ad-free monthly newsletter to stay informed on the essential open-source cybersecurity tools. Subscribe here!

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
