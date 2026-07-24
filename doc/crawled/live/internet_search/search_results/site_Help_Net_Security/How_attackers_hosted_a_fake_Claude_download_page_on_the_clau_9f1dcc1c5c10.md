# How attackers hosted a fake Claude download page on the claude.ai domain

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
How attackers hosted a fake Claude download page on the claude.ai domain
A threat actor abused Anthropic’s Claude Artifacts feature to funnel users toward malware, Huntress researchers have disclosed.
Employees at at least 29 organizations were compromised over two days in July, after searching for the Claude desktop app and clicking a sponsored Bing ad.
The ad pointed to the genuine claude.ai domain, but landed on an attacker-published public artifact, which redirected them to a spoofed download site serving SectopRAT.
What are Claude Artifacts?
Artifacts are a Claude.ai feature that renders certain content such as code, documents, diagrams, or full web pages in a panel beside the chat rather than as text in the conversation.
More importantly, users can publish an artifact to a public link, letting anyone view it without a Claude account.
In this particular case, the artifact to which potential victims were directed rendered a fully functional page that looked like a legitimate Claude download page, and the fact that it was hosted on the Claude.ai domain completed the illusion.
The only thing revealing its true nature was a short sentence displayed in the upper left corner, saying: “Content is user-generated and unverified.” However, this disclaimer is easily missed.
The Claude Artifact showing the fake download page (Source: Huntress)
Huntress reported the artifact to Anthropic and it was taken down before the company published its findings on July 22. By then, the page had been viewed 7,100 times.
Delivering the malware
Clicking on the “Download” button redirected victims to an external domain, first claude.ai.download-app[.]us and subsequently downloading-api.it[.]com/html/claude/win, from which they downloaded a bundle.
It contained a renamed (but legitimate) signed JetBrains binary vulnerable to DLL sideloading, a tampered libcef.dll carrying the actual malware, and an executable (DockerDesktop.exe) that’s dropped to disk and registered as a scheduled task so that it can keep reinfecting the machine.
The malware is SectopRAT, a remote access trojan (RAT) that grabs and exfiltrates user credit card data, personal information, files, and passwords.
Tracing the operator
The attacker had layered several defences on top of the payloads, and Huntress researchers had to go through considerable effort (and use Claude) to analyze them and unearth the command-and-control address.
In the end, they discovered connections to previous malware delivery campaigns.
WHOIS records and the Validin intelligence platform tied the download-app[.]us registration to an email address linked to ten domains going back to December 2025. One of them, polse[.]us, was seized by Microsoft as part of Operation Endgame after being identified as hosting the StealC infostealer.
Huntress also connected the actor to an April 2026 campaign that used Docker Hub to distribute a fake Docker Desktop installer. That campaign employed the same libcef.dll sideloading trick, and also relied on a trusted domain to disarm suspicion. (And this explains the leftover DockerDesktop.exe filename in this month’s bundle.)
Their advice for users is not to trust search engine ads and top-level domains implicitly when searching for software to download, as threat actors have become experts in pushing malicious ads via popular search engines and finding ways to host malicious content on legitimate platforms and domains.
Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. Subscribe here!

---
*爬取时间: 2026-07-24 15:54:00*
*来源: 直接站点爬取*
