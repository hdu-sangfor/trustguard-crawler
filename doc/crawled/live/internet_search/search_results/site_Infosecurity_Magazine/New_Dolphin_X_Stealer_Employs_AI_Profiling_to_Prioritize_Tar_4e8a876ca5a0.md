# New Dolphin X Stealer Employs AI Profiling to Prioritize Targets

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/new-dolphin-x-stealer-ai-targets/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
A newly discovered Windows infostealer and remote access trojan (RAT), dubbed Dolphin X, is using an AI-powered profiling system to help cybercriminals identify their most valuable victims, according to researchers at Varonis Threat Labs.
Advertised on a cybercrime forum, the malware is designed to target more than 300 applications and steal a wide range of sensitive data, including cryptocurrency wallets, .env files, SSH keys, cloud tokens and DevOps credentials.
However, researchers said Dolphin X's standout feature is an “AI Profiler” that automatically ranks infected users based on factors such as application usage, browsing activity and installed software.
Varonis obtained and analyzed the malware's operator panel in an isolated lab environment and found the tool assigns scores to victims, allowing attackers to quickly identify those most likely to provide valuable access or data.
This tool is useful because a cybercriminal could control thousands of infected machines, which Varonis noted is far more than they could review manually.
Attackers are sent a daily summary of rankings which Varonis said helps them identify high-value users.
Overall, the panel lists 329 features across ten categories and researchers noted that the most important figure is the collection scope: more than 300 application targets appear under the credential-looter category.
“These targets range from browser logins and cryptocurrency wallets to SSH keys and cloud tokens, with the collected data staged in a single archive,” Varonis researchers wrote.
In terms of defender recommendations, Varonis said security team responses should prioritize two items:
- Keep long-lived credentials off disk wherever possible, especially out of project directories and local credential stores. Infostealers are designed to grab everything in one pass, so anything stored locally should be treated as potentially exposed
- Focus detection on behavior rather than file signatures. For example, explorer.exe running under a non-default desktop is a strong indicator of an HVNC session, regardless of how the malware binary is packed or what hash it uses

---
*爬取时间: 2026-07-24 15:48:24*
*来源: 直接站点爬取*
