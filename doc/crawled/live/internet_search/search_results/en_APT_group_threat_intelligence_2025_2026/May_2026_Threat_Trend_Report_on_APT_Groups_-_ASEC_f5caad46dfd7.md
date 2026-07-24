# May 2026 Threat Trend Report on APT Groups - ASEC

### 来源信息
- **URL**: https://asec.ahnlab.com/en/94145/
- **域名**: asec.ahnlab.com
- **检索关键词**: APT group threat intelligence 2025 2026
- **页面抓取**: 成功

### 搜索摘要
4 weeks ago - The May 2026 APT Trends report identified supply chain attacks, developer environment attacks, automated Initial Breach, and exploitation of runtime environments as key developments.

### 页面正文
Purpose and Scope
The May 2026 APT Trends report identified supply chain attacks, developer environment attacks, automated Initial Breach, and exploitation of runtime environments as key developments. Lazarus, Famous Chollima, Gamaredon, MuddyWater, and Nimbus Manticore are of particular concern.
Status of Major APT Groups by Region
North Korea
- The Lazarus group exploited Git Hooks (Git features that automatically execute upon commit or branch changes) and Jenkins CI/CD (Continuous Integration and Continuous Deployment environments) to use the development workflow itself as a infection vector. It used pre-commit and post-checkout hooks to infect InvisibleFerret, BeaverTail, and FCCCall, increasing the risk of cryptocurrency wallet and developer credential theft.
- Famous Chollima contaminated npm and Packagist development branches and delivered payloads via Cloudflare Workers and blockchain RPC. It attempted to evade detection by tampering only with the development branches of legitimate packages or by using blockchain infrastructure as a dead drop.
- Kimsuky used LNK phishing, GitHub, Dropbox, GitLab, VSCode tunneling, and Microsoft CDNs to distribute multi-stage loaders, AsyncRAT variants, PebbleDash-based tools, MoonPeak, and HttpSpy. They broadly targeted entities in South Korea and Afghanistan, as well as those in the Education, defense, diplomacy, and cryptocurrency sectors.
- TA-RedAnt compromised a gaming platform in the Yanbian region and the Windows update chain to distribute BirdCall, RoKRAT, and a trojanized mono.dll. It also targeted the defense, police, and North Korea-related sectors through spear phishing, Python Embed, and .cat-disguised backdoors.
China
- Famous Sparrow exploited CVE-2021-34473, CVE-2021-34523, and CVE-2021-31207 in Microsoft Exchange, CVE-2022-41040, and CVE-2022-41082 to compromise an Azerbaijani oil and gas company. They used web shells, DLL sideloading, Deed RAT, and Terndoor to maintain persistent access and perform lateral movement.
- Red Lamassu executed JFMBackdoor in memory via public directory-based DLL sideloading and targeted telecommunications companies in Afghanistan and government agencies in the Asia-Pacific region.
- UAT-8302 utilized the MS Graph API, OneDrive, proxy chains, NetDraft, CloudSorcerer v3, VShell, SNOWLIGHT, SNOWRUST, DeedRAT, and ZingDoor to conduct information gathering, credential theft, and lateral movement.
- UNC5174 modified installation files from the official websites of Chinese-language encrypted instant messaging apps and used SNOWLIGHT and nps tunnels on Windows and Linux to perform infiltration and tunneling.
- Webworm leveraged Discord, the Microsoft Graph API, GitHub, and compromised Amazon S3 buckets to deploy EchoCreep, GraphWorm, WormFrp, ChainWorm, SmuxProxy, and WormSocket.
- OceanLotus hid ZiChatBot within the PyPI packages uuid32-utils, colorinal, and termncolor, and used the Zulip REST API as its C2.
Russia
- Gamaredon (UAC-0010) exploited the WinRAR vulnerability CVE-2025-8088 to attack Ukrainian government agencies, judicial agencies, and security agencies, and used NTFS ADS and the Startup folder to automatically install GammaDrop and GammaLoad.
- GREYVIBE distributed PhantomRelay, LegionRelay, and FallSpy (Android) using custom phishing, fake CAPTCHAs, and fake adult club websites. They utilized generative AI tools such as Ideogram AI, ChatGPT, and Gemini for both bait content and malware development.
- Cloud Atlas targeted Russia and Belarusian government agencies and diplomatic institutions using phishing LNK files, PowerShell, VBCloud, PowerShower, Reverse SSH, RevSocks, and Tor.
- Paper Werewolf distributed EchoGather RAT, PaperGrabber, and Mythic implants using PDF phishing, Inno Setup Installers, and JS, Python, C++, and .NET loaders.
- Silent Lynx conducted persistent remote control via compressed file delivery through Telegram, to disguise the service, and TLS/TCP reverse shells.
Iran
- MuddyWater combined Microsoft Teams-based social engineering, Quick Assist phishing, AnyDesk, DWAgent, and the Game.exe RAT to carry out data exfiltration and extortion.
- In another MuddyWater operation, the group used DLL sideloading, Node.js, PowerShell, and public file transfer services to conduct reconnaissance, privilege escalation, tunneling, and credential theft.
- Nimbus Manticore used a Trojanized Zoom installer and a fake SQL Developer download site, and deployed MiniJunk and MiniFast via .NET AppDomain hijacking.
- Screening Serpens distributed MiniUpdate and MiniJunk V2 via DLL sideloading and AppDomainManager hijacking to evade detection.
Pakistan
- Transparent Tribe (SideCopy) targeted the Afghan financial sector, distributing XenoRAT using ZIP files, malicious LNK files, mshta.exe, HTA, JavaScript, and .NET memory execution chains.
Others
- FrostyNeighbor targeted Ukrainian government agencies using server-side victim verification in PDF phishing, along with JavaScript PicassoLoader and Cobalt Strike Beacon.
Conclusion
This month, the trend of exploiting the developer ecosystem, open-source packages, legitimate updates, cloud services, and legitimate remote management tools became even more pronounced. In particular, the cryptocurrency, government, defense, diplomacy, energy, Education, and telecommunications sectors were repeatedly targeted, with the common objectives being credential theft, wallet keys, session information, documents, and browser data, as well as remote control.

---
*检索时间: 2026-07-24 21:30:38*
*搜索来源: DuckDuckGo*
