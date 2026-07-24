# Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 AttacksJul 24, 2026Cyber Espionage / Web SecurityThe Computer E

### 来源信息
- **URL**: https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
The Computer Emergency Response Team of Ukraine (CERT-UA) has warned of a new campaign that involves the use of a malicious program that's dressed up as a Notepad++ plugin to compromise Windows systems.
The activity has been attributed by the agency to a threat cluster it tracks as UAC-0099, a Russia-aligned group that has previously observed weaponizing security flaws in WinRAR software to deliver a malware strain called LONEPAGE. Other cyber attacks mounted by the adversary have employed phishing emails as an initial access method to deploy MATCHBOIL, MATCHWOK, and DRAGSTARE. It's known to be active since at least mid-2022.
The latest set of attacks begins, observed earlier this summer, with a phishing email containing an image attachment, which, when clicked, opens a URL that's concealed using a link shortener from where the request is sent to a file-sharing service like EasySend[.]co to retrieve a ZIP archive.
The ZIP file contains a Visual Basic Script (VBScript) that masquerades as a PDF document. Attempting to launch it will cause a decoy PDF to be downloaded and displayed to the victim as a distraction mechanism, while it silently downloads a second archive named "Evernote.zip." The archive includes multiple components -
- A complete copy of the legitimate editor Notepad++ version 8.8.3
- A malicious DLL plugin ("NppExport.dll")
- A password-protected archive ("updater.rar")
- Legitimate WinRAR executable ("winrar.exe")
The primary goal of the VBScript is to extract the contents of the archive and launch Notepad++, which, in turn, loads "NppExport.dll." Codenamed LUNCHPOKE, the DLL is designed to unpack the RAR archive, which contains "RemoteLibUpdater.exe" and "InitTest.dll," to a specific directory, set up persistence by means of a scheduled task to run "RemoteLibUpdater.exe" every three minutes.
The "RemoteLibUpdater.exe" binary is BURNYBEAR, which serves as a loader for "InitTest.dll," a modified version of MATCHBOIL, a C#-based loader capable of delivering secondary payloads. The new version has been codenamed MATCHBOIL.V2.
"At the same time, if 'RemoteLibUpdater.exe' is launched incorrectly, namely without specifying arguments, BURNYBEAR instead activates logic designed to exhaust computer resources (RAM and processor)," CERT-UA said.
CERT-UA is recommending that organizations update their WinRAR, 7-Zip, and Notepad++ software to the latest versions to prevent threat actors from exploiting any known vulnerabilities to facilitate follow-on attacks.
The disclosure comes as the U.S. government highlighted a phishing campaign orchestrated by the Russia-linked threat actor called Laundry Bear (aka CL-STA-1114, TA488, UNK_PitStop, and Void Blizzard) targeting Zimbra mail servers belonging to Western government and commercial organizations since at least July 2025.
The campaign employs a novel "half-click" exploit that abuses CVE-2025-66376 to deliver malicious JavaScript dubbed ZimReaper capable of harvesting email communications and other sensitive data.
"Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, Laundry Bear's latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service," the U.S. government said.
"The covert and persistent nature of this activity, along with the absence of any known financial extortion, almost certainly indicates this group's involvement in espionage activities with Russian government backing. Additionally, extensive Ukrainian targeting, prior to use against U.S. and other NATO allies, outlines an increasing trend within Russian cyber threat groups to target Ukrainian users first-both as a priority target and as a test bench for malicious cyber techniques before broader global deployment."
The disclosure also follows a report from Proofpoint about Russian threat actor's continued webmail targeting using half-click cross-site scripting (XSS) exploits to siphon valuable data as part of a campaign referred to as Operation RoundPress. The email security company is tracking the activity as TA458.
Since originally exposed by ESET in May 2025, the campaign has expanded in scope to target Kerio Webmail and SOGo Webmail, alongside Zimbra, mDaemon, and Roundcube. In March 2026, the hacking group is said to have exploited zero-day vulnerabilities in Kerio and the SOGo webmail platform (CVE-2026-8496). It was subsequently patched in version 5.12.8. In the case of Kerio, no CVE was issued as the webmail product was old and outdated.
It's worth noting that the campaign is different from Operation Roundish, which was disclosed by Hunt.io back in March and uses longstanding infrastructure that CERT-UA attributed to APT28 in 2024.
"Since at least July 2025, TA458 began removing stealing components, and swapping in interactive backdoor mechanisms to its Roundcube variant of SpyPress, to enable long-term access to the instance," Proofpoint researchers said. "SpyPress uses a second Roundcube exploit (CVE-2025-49113) that abuses Roundcube's file upload handler to trigger unsafe PHP deserialization."
The end goal is to trigger arbitrary code execution and install multiple backdoor or persistence mechanisms so as to ensure continued access in the face of disruption. TA458 has been described as likely a Russian military intelligence operation without any overlaps with APT28 (aka TA422).
"TA458 primarily targets Ukrainian government and Eastern European military and government entities across Albania, Greece, Moldova, and Türkiye, with occasional targeting of chemical, telecommunications, and technology firms," Proofpoint said. "TA458 continues to use SpyPress - an obfuscated JavaScript-based malware seen in Operation RoundPress - which the adversary modifies based on the targeted mail server."

---
*爬取时间: 2026-07-24 15:42:35*
*来源: 直接站点爬取*
