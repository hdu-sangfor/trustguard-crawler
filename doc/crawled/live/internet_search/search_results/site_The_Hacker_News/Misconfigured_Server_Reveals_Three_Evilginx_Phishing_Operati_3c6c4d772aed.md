# Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365

### 来源信息
- **URL**: https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
An attacker running a live Microsoft 365 phishing operation left a Python web server listening on a public port with directory listing switched on. The command that did it: python3 -m http.server 8080, was still sitting in the readable .bash_history.
From that one lapse, French security firm Lexfo lifted the operator's entire toolkit and pivoted through it to two more phishing operators, three campaigns in all. Each ran a custom fork of the open-source Evilginx proxy, cloned from public GitHub.
The largest of the three had been running for more than a year, its victims overwhelmingly corporate mailboxes.
The three got past MFA in two mechanically different ways, one by proxying the live login, one by abusing a legitimate Microsoft sign-in flow. The two need different defenses, which is the part that matters most if you run Microsoft 365.
Directory listing on a working attack server is close to a full confession. The listing exposed phishing configs, credential-harvesting logs, RMM installers, combolists, backup archives, and the operator's own Telegram session files.
Behind it ran an Evilginx adversary-in-the-middle proxy and a SimpleHelp remote console on the same host, at 185.163.204[.]7 in Budapest, cataloged in late April 2026 during a routine internet scan.
The bash history and a set of public repos pointed straight at the operator: an Egyptian actor the firm tracks as codemado, active in VoIP and hacking forums since 2018, now running a Microsoft 365 AiTM platform on picis[.]net and monetizing access through a bulk mailer he wrote called MaDoO Blaster.
His campaign went live on April 20 and kept running past the day the directory was found on April 30, with fresh subdomains and a renewed wildcard certificate turning up weeks later. His own bot logged captures against two corporate M365 accounts, one French, one North American.
The repeated captures of the same accounts from different IPs are consistent, the firm says, with the operator refreshing stolen tokens as they aged out.
Where the kits came from
codemado did not build the framework he runs. He cloned it, and his bash history shows him comparing kits side by side. The server held four Evilginx variants pulled from two other GitHub developers, and both turned out to be active operators in their own right.
The first, red-queen, comes from a Nigerian operator the report calls mail-argenta, and it shows how much polish gets bolted onto a public framework. His fork renames the crossorigin and integrity HTML attributes to defeat Subresource Integrity checks and adds a URL-rewriting engine to http_proxy.go to dodge path-based detection. It pre-fills the victim's email address to cut abandonment.
It also sets a one-year TTL, 31,536,000 seconds, on the captured Microsoft session cookies. The report says an intercepted login can then outlast a password reset and, without a CAE-capable Conditional Access policy, stay usable for months.
A pre-compiled evilginx2.exe is committed to the repo, so a buyer never has to build anything. One captured M365 cookie sitting in the repo carried an expiration date of June 30, 2027.
mail-argenta got caught the way his own victims do. The firm found his email and a password in infostealer logs, the kind of harvested-credential data his phishing panels exist to produce. That leaked password matched the one hardcoded as the MySQL password in his Kraken panel and reused across his accounts.
The quiet one
The third fork, black-queen, logged far more captures than the other two, and it never touches a password. Its author, whom the researchers could not identify past the handle saroula01, built it around Microsoft's OAuth device code flow, a legitimate sign-in path meant for input-constrained devices.
The attack generates a real device code, wraps it in an Authenticator-themed lure page, and tells the target to enter it at the genuine microsoft.com/devicelogin. The victim signs in on a real Microsoft page and clears MFA themselves. saroula01's backend polls the token endpoint and takes the token the moment they do.
Calling this "MFA bypass" misses how it works: nothing gets bypassed. The lure page is Authenticator-themed and attacker-built, but the device code and the Microsoft page where the victim finishes are genuine, so the MFA prompt the victim satisfies is real.
A passkey or FIDO2 key does not help either, because the victim clears it on genuine Microsoft infrastructure while authorizing the attacker's session; the origin binding that stops Evilginx passes cleanly when the origin really is Microsoft.
Microsoft documented the technique in February 2025, in a campaign it assessed with medium confidence as Russia-aligned. It has since spread well past state-backed use, into campaigns hitting hundreds of Microsoft 365 organizations.
saroula01's version ran quietly for over a year. The firm counted 218 distinct captured accounts in the campaign's Telegram bot logs across a dozen countries between June 2025 and July 2026, around 94 percent of them corporate mailboxes. Those are logged captures, not scan targets.
A token file briefly committed to the repo and then deleted, still readable in the git history, held 97 live Microsoft tokens tied to three of those victims, every one set to autoRefresh and some refreshed as many as 25 times. The framework was keeping the sessions alive on its own.
Both phishing domains, picis[.]net and romnor[.]ca, were offline when The Hacker News checked ahead of publication, though the report's timeline shows picis[.]net still provisioning new subdomains as late as May 2026. The Lexfo CTI team told THN that the domains had already gone offline before it took any action, and reads that as the operators rotating infrastructure or pulling back rather than a coordinated takedown, though it cannot confirm which.
The three connect, loosely, to something larger. In June 2026, SOCRadar documented a phishing-as-a-service ecosystem it named The Quarry, run by a developer it calls RockyBelling and, by its count, sold to close to 200 operators.
MaDoO Blaster shows up promoted inside The Quarry's Telegram channel as a third-party tool, flagged independently in both writeups, which the report frames as a supplier relationship, not membership in it. Whether mail-argenta or saroula01 has any direct tie cannot be shown from the artifacts. Their kits sat on public GitHub, and anyone could have taken them.
Built with help
The report found signs of AI-assisted development across all three operations, though they vary in strength. saroula01 left two git commits co-authored by Claude models. mail-argenta committed an instructions.txt that is a verbatim save of an AI coding session, references to earlier prompts and all, documenting how the URL-rewriting feature got built.
codemado's is thinner: one of his scripts credits CyberNeurova, a paid "uncensored" code-generation API, the report says, which advertises itself with the prompt "Build me a keylogger in Python." Two of the three put a model directly in the code; the third is a credit line, and none of them shows how much of each build the model did.
It is not confined to these three either. Microsoft has separately documented device-code phishing built on AI-driven backend automation and generative-AI lures.
The Hacker News asked the report's authors how much of the tooling AI actually produced across the three operations. The Lexfo CTI team said the Evilginx forks carried only minor changes to the core, and that the clearer signs of AI use sat in the glue code around them, the scripts and phishlets, several of which read as direct model output. It was less the framework itself, the team said, than the code built around it.
What defenders can actually do
The two techniques do not share a fix. Phishing-resistant MFA, FIDO2, or passkeys still shut down the Evilginx side by binding the sign-in to the real domain. It does not stop device code abuse. For that, the lever is Conditional Access.
Microsoft's own line is to block device code flow wherever possible. A handful of setups genuinely need it, mostly input-constrained hardware like Teams room devices and some command-line tools. Inventory that uses the sign-in logs, blocks the flow everywhere else, and tests the policy in report-only mode before enforcing.
Layer IP-based Conditional Access location policies and Continuous Access Evaluation on top, so that on supported Microsoft 365 workloads, a stolen token seen from outside your allowed ranges gets reevaluated instead of riding out its lifetime.
For detection, the report flags refresh-token grants from the Microsoft Office client ID d3590ed6-52b3-4102-aeff-aad2292ab01c in Entra sign-in logs as worth watching, where that desktop client is not in normal use; cross-check them against unfamiliar source IPs.
The same Microsoft guidance flags a catch: a session that started with device code flow stays tagged on later refreshes even when the current event no longer shows it, so hunt on the sign-in's Original transfer method field, not just the live authentication protocol.
On endpoints, hunt for the RMM tooling these operators drop for persistence; codemado's kit reaches for XEOX, so start with the agent at C:\Program Files (x86)\XEOX\xeox-agent_x64.exe and scheduled tasks matching *XEOX*Agent*Watchdog*. The domains and IPs are in the report, but that infrastructure rotates, so treat it as containment, not a fix.
The Hacker News also asked Microsoft about the abuse of its device code flow, and had received no response by the time of publication. This story will be updated with any reply.
None of this took much: three operators, none of whom built the frameworks they ran, stood up working campaigns off public repositories, kits that sell for a few hundred dollars, and a model helping with the custom parts.
The report reads that the barrier to a working campaign has fallen to near zero, and the Lexfo CTI team expects this class of attack to become significantly more common over the coming months.
One cheap ecosystem now supplies two ways around MFA, and that is the part that outlasts any single campaign here: a shop hardened against reverse-proxy phishing is still open to device-code abuse. Blocking that second path is one Conditional Access policy, no passkey rollout adds for you, and it exists only once someone writes it.
Update (July 16, 2026)
Lexfo has issued an erratum to the report. Three entries it originally listed as malicious indicators, agent01.xeox.com, ws01.xeox.com, and 80.80.250.0/24, are legitimate XEOX vendor infrastructure, shared across all XEOX customers. Anyone who blocked them off that list should reverse that.
The corrected guidance is to alert and audit XEOX activity only where XEOX is not an authorized tool, and the same qualifier applies to the endpoint artifacts above: XEOX is a product some environments run on purpose.

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
