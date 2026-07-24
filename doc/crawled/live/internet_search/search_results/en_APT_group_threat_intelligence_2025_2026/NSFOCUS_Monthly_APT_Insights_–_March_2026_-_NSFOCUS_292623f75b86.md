# NSFOCUS Monthly APT Insights – March 2026 - NSFOCUS

### 来源信息
- **URL**: https://nsfocusglobal.com/nsfocus-monthly-apt-insights-march-2026/
- **域名**: nsfocusglobal.com
- **检索关键词**: APT group threat intelligence 2025 2026
- **页面抓取**: 成功

### 搜索摘要
May 28, 2026 - As the APT group with the highest attack frequency and the broadest impact, Lazarus has evolved into a massive criminal conglomerate comprising multiple sub-groups. The timeline of known Lazarus supply chain operations is provided in the table below: Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights. A vulnerability in F5 BIG-IP products, CVE-2025-53521, has been escalated to a Remote Code Execution (RCE) severity and is currently being exploited in the wild

### 页面正文
Regional APT Threat Situation
In March 2026, the global threat hunting system of Fuying Lab detected a total of 31 APT attack activities. These activities were primarily concentrated in regions including South Asia, Eastern Europe, and the Middle East, as shown in the figure below.
Regarding the activity levels of different groups, the most active APT group this month was TransparentTribe, operating out of South Asia, and APT28, based in Eastern Europe. Other notably active groups included MuddyWater from the Middle East and SideWinder from South Asia.
The most prevalent intrusion method in this month’s incidents was spear-phishing email attacks, accounting for 87% of all attack events. A small number of threat actors also utilized vulnerability exploitations (10%) and watering hole attacks for infiltration (3%).
In March 2026, the primary target industries for APT groups were military institutions, accounting for 33%, followed by government agencies, accounting for 30%. Other attack targets included organizations and individuals, research institutions and financial institutions.
South Asia
This month, APT activity in South Asia was primarily driven by known APT groups. Victims included Indian military institutions and government agencies, Pakistani government agencies and military institutions, Sri Lankan military institutions and government agencies, and Afghan military institutions. In terms of attack tactics, spear-phishing emails constituted the primary method employed in South Asian APT operations this month. A typical decoy targeted Indian defense-related military entities: the attacking group utilized its customary spear-phishing approach, delivering a PowerPoint file as the payload.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
Eastern Europe
This month, APT activities in Eastern Europe were primarily conducted by known APT groups. Victims included Ukrainian government agencies, Ukrainian military institutions, Ukrainian organizations or individuals, and Romanian government agencies. In terms of attack tactics, spear-phishing emails remained the predominant method employed in Eastern European APT operations this month, complemented by some incidents where threat actors exploited vulnerabilities to gain initial access. Regarding spear-phishing campaigns, a typical decoy involved a forged government document purportedly issued by the Romanian Border Police.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
Middle East
This month, APT activities in the Middle East were primarily carried out by known APT groups. Victims included Israeli government agencies, Israeli organizations or individuals, Iraqi government departments, U.S. infrastructure entities, as well as various organizations and individuals across the Middle East. In terms of attack tactics, spear-phishing via email remained the predominant method employed in Middle Eastern APT operations this month. Regarding spear-phishing campaigns, a notable example involved phishing SMS messages targeted at the Israeli public.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
East Asia
This month, APT activities in East Asia were primarily conducted by known APT groups, with victims predominantly located in South Korea. Affected entities included South Korean research institutions, the financial sector, as well as various organizations and individuals. In terms of attack tactics, the majority of APT operations in East Asia this month relied on spear-phishing emails, while a minority utilized waterhole attacks. Regarding spear-phishing campaigns, a typical decoy involved a forged government announcement purportedly issued by the Republic of Korea Army.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
Global Key APT Events
| Event Name | Related Groups | 
|---|---|
| The APT group UNC1069 orchestrated the Axios supply chain poisoning campaign | UNC1069 | 
| A vulnerability in F5 BIG-IP products, CVE-2025-53521, has been escalated to a Remote Code Execution (RCE) severity and is currently being exploited in the wild | Unconfirmed | 
| The Threat Actor Leverages OpenClaw-Related GitHub Repositories to Distribute Malware | TroyDen | 
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
Interpretation of Key APT Events
The APT group UNC1069 orchestrated the Axios supply chain poisoning campaign
Earlier this year, the North Korean APT group UNC1069 compromised the account of Jason Saayman, a key administrator of the popular JavaScript project Axios. The group leveraged this access to publish malicious versions of the Axios package, executing a supply chain poisoning attack.
UNC1069 initially gained control of Saayman’s npm account through unspecified social engineering tactics. This compromise granted them the authority to push new versions of the Axios project via the npm JavaScript package manager, establishing the foundation for their supply chain assault.
UNC1069 is considered a subordinate entity of the North Korean APT group Lazarus. Security researchers have widely attributed the Axios supply chain incident to this group, as the macOS-based RAT malware deployed in the attack bears a striking resemblance to the WAVESHAPER backdoor previously associated with them. As the APT group with the highest attack frequency and the broadest impact, Lazarus has evolved into a massive criminal conglomerate comprising multiple sub-groups.
The timeline of known Lazarus supply chain operations is provided in the table below:
| Date | Victim / Target | Incident Overview | 
|---|---|---|
| 2021 | Several South Korean Software Companies | Lazarus leveraged the supply chain of domestic South Korean security software to conduct infiltration. The attackers tampered with the update mechanisms of trusted software, implanting malicious code to target government agencies and financial institutions. | 
| 2022 | Trading Technologies | Lazarus compromised X_TRADER, a financial trading software from this company that had ceased maintenance but remained in use. This incident served as the root cause of the subsequent widespread 3CX infection. | 
| …… | …… | …… | 
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
A vulnerability in F5 BIG-IP products, CVE-2025-53521, has been escalated to a Remote Code Execution (RCE) severity and is currently being exploited in the wild
In a March announcement, networking equipment vendor F5 stated that the vulnerability type of a known flaw in its BIG-IP products, CVE-2025-53521, has been reclassified. Originally identified as a Denial of Service (DoS) vulnerability, it has been upgraded to a Remote Code Execution (RCE) vulnerability. Consequently, its severity score has increased from 7.5 (CVSS v3.1) / 8.7 (CVSS v4.0) to 9.8 (CVSS v3.1) / 9.3 (CVSS v4.0). Furthermore, active exploitation of this vulnerability in the wild has been confirmed.
CVE-2025-53521 was initially disclosed in F5’s quarterly security bulletin on October 15, 2025. At that time, it was characterized as a DoS vulnerability affecting the F5 BIG-IP Access Policy Manager (APM) system. It was believed that attackers could craft specific malicious network traffic to cause the Traffic Management Microkernel (TMM) to crash, leading to device reboots or service interruptions. The understanding of this vulnerability evolved following the F5 source code leak in October 2025.
A national-level APT group infiltrated F5 Networks’ internal systems prior to August 9, 2025, stealing the majority of the BIG-IP source code along with information on undisclosed vulnerabilities. F5 publicly disclosed this breach and several of the previously unknown vulnerabilities, including CVE-2025-53521, in its quarterly security bulletin on October 15, 2025. Since the October disclosure, new intelligence regarding the F5 source code leak has emerged.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.
The threat actor leverages OpenClaw-related GitHub repositories to distribute malware
An unconfirmed threat actor (temporarily designated as TroyDen) launched a campaign in early 2026 exploiting the popularity of “OpenClaw.”
The group utilized AI tools to generate a large volume of GitHub repositories encompassing popular open-source projects, game cheats, and development tools. Malicious Lua scripts were injected into these projects to deliver malware. To enhance credibility, the group employed Search Engine Optimization (SEO) techniques to boost the search ranking of these repositories and used fake accounts to artificially inflate their Star and Fork counts. A typical example is the AAAbiola/openclaw-docker project created by TroyDen.
In our February 2026 monthly report, we discussed security concerns surrounding emerging AI Agent tools, outlining eight potential exploitation scenarios: credential leakage, access control flaws, malicious skill injection, data exfiltration, task chain pollution, network exposure, lack of auditing, and sandbox evasion. However, the recent TroyDen incident has outpaced all theoretical predictions: the immense popularity of OpenClaw itself has become an exploitable vector. Attackers can conceal their payloads within OpenClaw deployment tools.
Subscribe NSFOCUS Threat Intelligence for full details of APT incident insights.

---
*检索时间: 2026-07-24 21:30:29*
*搜索来源: DuckDuckGo*
