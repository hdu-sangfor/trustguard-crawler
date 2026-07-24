# News AnalysisRansomware groups are hammering your vulnerable VPNsCampaigns against flaws in security systems from Palo A

### 来源信息
- **URL**: https://www.csoonline.com/article/4201019/ransomware-groups-are-hammering-your-vulnerable-vpns.html
- **来源站点**: CSO Online
- **页面抓取**: 成功

### 页面正文
Cybercriminals are actively exploiting a recently discovered vulnerability in Palo Alto Networks firewall and VPN appliances to deploy the Qilin ransomware strain.
A critical authentication bypass flaw (CVE-2026-0257) in Palo Alto GlobalProtect portal and gateway was the common link in a series of intrusions in June, Arctic Wolf Labs warns. Exploitation of the vulnerability came within days of disclosure.
“Post-exploitation tradecraft varied across intrusions, from rapid encryption-only operations to full double-extortion, possibly suggesting multiple affiliates operating under the Qilin ransomware-as-a-service (RaaS) umbrella,” Arctic Wolf’s researchers wrote in a post on the threat.
The campaign against Palo Alto’s VPN client is part of a rising trend that sees ransomware groups increasingly targeting vulnerabilities in network edge tools and devices.
Ransomware takes aim at the edge
Beyond GlobalProtect, Qilin — the most active threat group in Q2 2026, responsible for 14% of attacks, according to NCC Group’s latest Quarterly Cyber Threat Intelligence Report — has also targeted flaws in Fortinet’s FortiGate, Citrix NetScaler, and Check Point Remote Access VPN.
Check Point warned in June of ransomware attacks against VPNs that still use the deprecated Internet Key Exchange version 1 (IKEv1) protocol. Citrix issued patches in early July for a CitrixBleed-like flaw in its NetScalar devices that had come under attack.
Meanwhile, Fortibleed, a massive credential-compromise campaign, exposed 75,000 FortiGate firewalls in June.
Qilin is by no means alone in increasing its operations against VPNs and other network security tools.
The Gentlemen, No. 2 on NCC Group’s list with 238 victims in Q2 2026, is noted for breaking into organizations through firewalls, VPNs, and other internet-exposed systems — FortiGate and Cisco products in particular.
Akira, No. 4 on NCC Group’s list (127 victims), is also known for exploiting VPN vulnerabilities and abusing legitimate credentials, primarily versus products from Ivanti, Cisco, and Fortinet.
In the line of fire
Network edge security devices are becoming security liabilities for enterprise security professionals, with an alarming rise in zero-day exploits arising from what experts describe as basic and readily preventable vulnerabilities.
A range of attackers spanning opportunistic hackers to ransomware-as-a-service operators and nation-state sponsored APT (advanced persistent threat) groups are actively exploiting software vulnerabilities in edge devices to hack into corporate networks.
“Although there has not been a material rise in ransomware volume in the last quarter, the trajectory of attacks continues upwards, and VPNs remain an increasingly attractive target,” said Matt Hull, VP and head of cyber intelligence and response at NCC Group.
Unpatched vulnerabilities in edge devices are far from the only software bugs fueling ransomware attacks. For example, last year the Clop ransomware gang hacked hundreds of companies by exploiting zero-day vulnerabilities in Oracle’s E-Business Suite software.
Edge of darkness
VPNs and other internet-facing edge devices remain prime targets for ransomware operators because they provide a direct route into an organization’s network.
“Attackers may exploit an unpatched vulnerability, use stolen credentials, or target weak authentication controls,” said Alexander Leslie, a senior advisor at cyber threat intelligence firm Recorded Future. “In some cases, exploitation begins before organizations have had sufficient time to apply vendor guidance, leaving security teams with a very narrow window to respond.”
VPN exploitation sits alongside other initial access methods, such as phishing, compromised credentials, or software supply chain attacks. The preferred attacker infiltration method varies by campaign and sector but locating security in edge devices carry particular advantages from the perspective of attackers.
“Vulnerabilities in perimeter devices are particularly valuable to attackers because those systems are continuously exposed to the internet and can provide privileged access while bypassing some endpoint controls,” said Leslie.
Dray Agha, senior manager of security operations at managed detection and response firm Huntress, backed up this assessment that exploiting internet-facing VPNs and edge devices remains the “dominant, volume-driven tactic” for ransomware operators because these appliances offer a “direct, publicly accessible gateway straight into the heart of corporate networks.”
Rather than exploiting vulnerabilities in edge devices, attackers more commonly use internet-facing gateways as a means to abuse stolen credentials to break into corporate networks, according to Huntress.
“What we see at Huntress is that the VPN is the site of initial access some 70% of the time, for advanced threat actors,” said Agha. “Overwhelmingly, however, they are not exploiting for access; rather they are using stolen credentials to authenticate to non-MFA’d [multi-factor authentication] user accounts.”
Hardened perimeter
CSOs should treat their network perimeter as hostile territory by enforcing aggressive patch management, applying critical edge device updates within 24 to 48 hours, and mandating strict MFA for all access.
Implementing zero-trust network segmentation to trap attackers and prevent lateral movement if the initial gateway is compromised also helps in making enterprise networks more resilient against attacks, Huntress’ Agha advised.
Phishing-resistant multi-factor authentication, removal of unsupported systems, and close monitoring for unusual authentication or administrative activity also form key components in attack impact mitigation.
Internet-facing assets that are known to be actively exploited should be prioritized as a patching priority.
“Threat intelligence and evidence of active exploitation should help determine which vulnerabilities demand immediate action,” Recorded Future’s Leslie said.

---
*爬取时间: 2026-07-24 21:46:15*
*来源: 直接站点爬取*
