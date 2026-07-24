# China-Nexus JadeProx Uses New TriBack Loader in Government and Healthcare AttacksJul 23, 2026Malware / Threat Intellige

### 来源信息
- **URL**: https://thehackernews.com/2026/07/china-nexus-jadeprox-uses-new-triback.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
An exposed Alibaba Cloud server has revealed a China-nexus operation that Group-IB tracks as JadeProx. The cluster has targeted government, healthcare, and education organizations across Asia and Latin America with a previously undocumented Windows loader called TriBack Loader.
Group-IB found the server in mid-April 2026 in Alibaba Cloud's Singapore region; it was offline by the time the report published on July 23, 2026.
Its bash history, phishing packages, post-exploitation tools, and webshell paths laid the operation out: active intrusions against a Vietnamese public hospital's medical imaging system and Malaysia's Ministry of Foreign Affairs, scanning and exploitation follow-up against Hong Kong education infrastructure, and a spear-phishing package addressed to the National Congress of Honduras.
The operators reached the hospital's imaging server through webshells planted on an exposed Java management interface.
One Loader, Four Builds
TriBack Loader appears in four infection chains built around DLL sideloading. Most recovered builds pair a legitimate signed executable with a malicious DLL and an encrypted .dat or .log payload.
The DLL reverses the payload bytes, XORs them with a rolling key, and executes the shellcode through Win32 calls that EDR watches less closely than CreateThread.
The builds rotate that final call: InitOnceExecuteOnce and a TimerQueue callback in two variants, and EtwpCreateEtwThread, an undocumented thread-creation routine in ntdll, in a third. The signed host binary changed between variants too. The repeated API sequence suggests a custom loader builder, the researchers say.
Two variants delivered AdaptixC2, an open-source post-exploitation framework. A Claude-themed variant used DonutLoader to run Beagle, a backdoor Sophos was first to document. The fourth variant's payload is unknown; its encrypted companion file was never recovered.
One spear-phishing archive carried a fake beverage-company account statement as the decoy. Another campaign impersonated Anthropic's Claude software from claude-pro[.]com, registered on March 28, 2026, serving a malicious MSI installer that, past a UAC prompt, placed the sideloading chain in the Windows Startup folder for persistence. The Beagle backdoor it delivered reported to license[.]claude-pro[.]com.
Sophos, working from the fake site, its hosting infrastructure, and malware samples, found the same reused XOR key in builds going back to February but said a shared key was not enough to conclude one actor.
Group-IB, working from the exposed server's contents, groups those builds with the Asian intrusions. It still stops short of naming an established group: tooling moves freely in the China-nexus ecosystem, Group-IB notes, so a match on tools is not a match on operators.
The operators also ran Nuclei with critical-severity templates only against a list of 14,653 Hong Kong education-related URLs, surfacing 13 unique vulnerabilities. Those 14,653 URLs are a scan list, and the report does not say how many of the follow-ups succeeded.
The report names four CVEs the operators attempted against individual hosts, and The Hacker News confirmed all four against NVD on July 23, 2026: CVE-2018-11511 in ASUSTOR ADM, CVE-2021-24139 in the 10Web Photo Gallery WordPress plugin, CVE-2021-31755 in Tenda AC11 routers, and CVE-2021-32305 in WebSVN. Each carries a CVSS base score of 9.8. The Tenda bug has been on CISA's Known Exploited Vulnerabilities catalog since November 3, 2021, with a federal remediation deadline that expired two weeks later.
Detection Starts With the Sideloading Chain
Sophos assessed that the fake Claude site was likely part of an active malvertising campaign. If so, the exposure runs well past the ministries and hospitals, out to users searching for a Claude download.
Detection works off the file layout, because the filenames and signed hosts change per build.
- Flag signed vendor binaries running from user-writable, temporary, or Startup directories, especially when an encrypted .dat or .log file sits in the same folder.
- Look for unexpected copies of hostfxr.dll, avk.dll, or MpClient.dll, plus nested _CL_###### folders and ~del.vbs.bat.
- Block or investigate the cluster's domains: claude-pro[.]com, license[.]claude-pro[.]com, sylverixstrategy[.]com, gouvvbo[.]top, vertextrust-advisors[.]com, and three security-vendor lookalikes sharing one IP, update-trellix[.]com, update-crowdstrike[.]com and update-sentinelone[.]com. The staging server was 43.106.71[.]28 on port 8000. Both lists come from Group-IB's July 23 report.
- Group-IB puts internet-facing Java applications first, then any public-facing system carrying an unpatched 9.8-rated flaw, these four included.
For all the loader engineering, the scanning half of this operation ran on flaws disclosed in 2018 and 2021. The custom work all sits downstream of the break-in.

---
*爬取时间: 2026-07-24 15:42:35*
*来源: 直接站点爬取*
