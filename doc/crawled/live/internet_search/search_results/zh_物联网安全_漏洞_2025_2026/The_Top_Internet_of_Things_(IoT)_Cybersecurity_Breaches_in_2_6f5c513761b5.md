# The Top Internet of Things (IoT) Cybersecurity Breaches in 2026

### 来源信息
- **URL**: https://asimily.com/blog/the-top-internet-of-things-iot-cybersecurity-breaches-in-2026/
- **域名**: asimily.com
- **检索关键词**: 物联网安全 漏洞 2025 2026
- **页面抓取**: 成功

### 搜索摘要
May 12, 2026 - In January 2026, Check Point Research identified an active, large-scale exploitation campaign targeting CVE-2025-37164, a critical unauthenticated remote code execution vulnerability in HPE OneView, a centralized infrastructure management platform ...

### 页面正文
The Top Internet of Things (IoT) Cybersecurity Breaches in 2026
oT devices are being compromised at a pace and scale that would have been difficult to imagine even two years ago. SonicWall recorded a 124% year-over-year increase in IoT attacks in 2024, and the trajectory has only steepened since. In March 2026, a coordinated law enforcement operation across the U.S., Germany, and Canada dismantled four IoT botnets that had collectively infected more than 3 million devices and were capable of generating DDoS attacks exceeding 31 Tbps. IoT malware incidents were up 124% by late 2025 compared to the prior year. The connected device population reached 21.1 billion globally at the end of 2025 and is projected to hit 39 billion by 2030. Every new device is a potential recruitment target for the next botnet, a potential entry point for ransomware, or a potential source of data exposure. This post covers the most significant IoT cybersecurity breaches of 2025 and 2026, what made each one possible, and what they mean for organizations managing connected devices.
On this page:
- Why IoT Devices Remain at Risk
- Major IoT Breaches and Incidents: 2026
- Major IoT Breaches and Incidents: 2025
- What the 2025-2026 IoT Breaches Have in Common
- How to Protect Your Organization
- How Asimily Helps
Why IoT Devices Remain at Risk
The number of connected devices keeps growing, and so does the attack surface. As of 2025, there are an estimated 21.1 billion IoT devices worldwide. While these devices provide operational value across every industry, they share a common set of security limitations: they lack the CPU and memory to run security agents, they ship with default credentials that often go unchanged, they receive firmware updates infrequently, and they communicate over protocols that many security tools do not parse.
The result is a vast population of devices that cannot protect themselves. Verizon’s 2025 DBIR recorded a 34% year-over-year rise in successful vulnerability exploits, with an eightfold jump in exploitation of edge devices and VPN concentrators. Forescout’s 2026 research found that routers and switches now average 32 vulnerabilities per device and account for 34% of the most critical vulnerabilities in enterprise networks. 40% of the riskiest device types in 2026 were not on the risk list a year ago.
The economics of IoT exploitation favor attackers. The average IoT security incident costs $330,000. Healthcare IoMT breaches average over $7 million. The cost of not securing connected devices is concrete and growing.
Major IoT Breaches and Incidents: 2026
DOJ Dismantles Four IoT Botnets (Aisuru, Kimwolf, JackSkid, Mossad): March 2026
In March 2026, the U.S. Department of Justice, working with authorities in Germany and Canada, disrupted the command-and-control infrastructure behind four IoT botnets: Aisuru, Kimwolf, JackSkid, and Mossad. Collectively, these botnets had infected more than 3 million devices worldwide, including routers, web cameras, digital video recorders, and smart TVs. The botnets were responsible for hundreds of thousands of DDoS attacks, some targeting U.S. Department of Defense systems.
The combined attack capacity was extraordinary. Cloudflare attributed a 31.4 Tbps DDoS attack in November 2025 to the Aisuru/Kimwolf network, and the DOJ characterized the attacks as record-breaking. Aisuru alone issued more than 200,000 attack commands. JackSkid launched at least 90,000 attacks. Kimwolf introduced a novel propagation method that allowed it to infect devices behind home routers, reaching systems on internal networks that are normally shielded from external threats.
Lumen’s Black Lotus Labs null-routed nearly 1,000 command-and-control servers. JackSkid was averaging over 150,000 daily victims in early March 2026, peaking at 250,000 on a single day. Nearly two dozen technology companies assisted in the operation.
Why it matters: The devices themselves remain infected after a takedown. Millions of insecure routers, cameras, and DVRs are still online, running outdated firmware with default credentials, ready to be conscripted by the next botnet builder. Law enforcement can disrupt infrastructure, but it cannot fix the underlying device security gap.
RondoDox Botnet Exploits HPE OneView Vulnerability: January 2026
In January 2026, Check Point Research identified an active, large-scale exploitation campaign targeting CVE-2025-37164, a critical unauthenticated remote code execution vulnerability in HPE OneView, a centralized infrastructure management platform used in enterprise data centers. The RondoDox botnet launched over 40,000 automated attack attempts in a four-hour window on January 7, targeting government, financial services, and industrial manufacturing organizations.
HPE OneView sits at the control plane for enterprise infrastructure, managing servers, firmware, and lifecycle operations. Successful exploitation gives an attacker centralized control over data center hardware at scale. CISA added the vulnerability to its Known Exploited Vulnerabilities catalog the same day Check Point reported it.
Why it matters: This incident demonstrates how IoT botnets are expanding beyond consumer devices. RondoDox targeted enterprise infrastructure management platforms, where compromise provides access far beyond a single device. The lag between vulnerability disclosure (December 2025) and mass automated exploitation (January 2026) was measured in weeks.
Microsoft Azure Absorbs 15.72 Tbps DDoS from Aisuru Botnet: Early 2026
Microsoft Azure blocked what it described as one of the largest DDoS attacks ever recorded: a multi-vector attack peaking at 15.72 Tbps and 3.64 billion packets per second, sourced from over 500,000 IP addresses across the globe. The attack targeted a single edge device in Australia and was attributed to the Aisuru IoT botnet, which recruits compromised home routers, surveillance cameras, and DVRs.
Why it matters: The sheer scale, 15.72 Tbps from half a million source IPs, illustrates the weaponization potential of unsecured IoT devices. Each source IP represents a compromised device somewhere in the world, silently participating in an attack while continuing to function normally for its owner.
Iranian Groups Target IP Cameras in the Middle East: February 2026
Check Point researchers reported a significant spike in attacks targeting internet-connected surveillance cameras across Israel, the UAE, Qatar, Bahrain, Kuwait, Lebanon, and Cyprus beginning February 28, 2026. The campaigns were attributed to multiple Iran-linked threat actors using commercial VPN services and virtual private servers as infrastructure.
Why it matters: This campaign shows nation-state actors targeting IoT devices for surveillance and intelligence purposes, not just for botnet recruitment. IP cameras in sensitive locations provide real-time visual intelligence that has geopolitical value.
Major IoT Breaches and Incidents: 2025
BadBox 2.0 Botnet Pre-Infects Over 10 Million Devices: July 2025
Google, in partnership with Human Security and Trend Micro, disclosed BadBox 2.0, the largest known botnet of internet-connected TVs. More than 10 million smart TVs, digital projectors, in-car infotainment systems, and digital picture frames were compromised. The malware was distributed in three ways: pre-installed on the device before purchase, retrieved from a command-and-control server on first boot, or downloaded from third-party app marketplaces.
Once infected, devices were enrolled into a global botnet used for click fraud, account hijacking, residential proxy services, and DDoS attacks. The operation evaded detection by blending with legitimate network traffic.
Why it matters: BadBox 2.0 demonstrated supply chain compromise at unprecedented scale. The malware was embedded in devices before they reached the buyer, making post-deployment security the only viable defense. Organizations cannot trust that a new device is clean simply because it comes in a sealed box.
Mars Hydro Exposes 2.7 Billion IoT Device Records: February 2025
A massive cloud misconfiguration at Mars Hydro, a grow-light and IoT device manufacturer, left 2.7 billion records exposed in an unprotected database. The exposed data included device telemetry, WiFi network names and passwords, IP addresses, and device identifiers. The database was publicly accessible without any authentication.
Why it matters: This was not a hack. No attacker exploited a vulnerability or cracked a password. The data was simply left open on the internet. It demonstrates that IoT security extends far beyond the device itself. The cloud infrastructure that collects, stores, and processes IoT data must be secured with the same rigor. WiFi credentials exposed in this breach could be used for secondary attacks against networks where Mars Hydro devices are deployed.
Aisuru/TurboMirai Achieves Record DDoS Capacity: Late 2025
The Aisuru botnet, first identified in late 2024, grew rapidly throughout 2025. By Q3 2025, it was launching DDoS attacks exceeding 29.7 Tbps and 14.1 billion packets per second, sourced from an estimated 300,000 to 700,000 compromised routers, DVRs, and IP cameras. Cloudflare mitigated the 29.7 Tbps attack in late 2025. The operators also began offering compromised devices as residential proxy services, expanding monetization beyond DDoS-for-hire.
Why it matters: Aisuru’s growth curve, from first identification in late 2024 to 29.7 Tbps capacity within a year, shows how quickly botnets scale when the supply of vulnerable devices is essentially unlimited.
Matrix Creates Global Botnet from Known Vulnerabilities: November 2024
A threat actor called “Matrix” built a global botnet by targeting IoT devices with known, unpatched vulnerabilities, deploying Mirai malware on infected machines and advertising DDoS-for-hire services. The campaign used publicly available tools to scan cloud provider IP ranges for vulnerable devices. China and Japan were the primary targets, likely due to their high concentration of connected devices.
Why it matters: Matrix was not a sophisticated actor. The campaign relied entirely on known vulnerabilities and default credentials. The barrier to entry for building an IoT botnet is now low enough that script-level operators can assemble attack infrastructure from publicly vulnerable devices.
Raptor Train Botnet Compromises 200,000+ Devices: September 2024
Security researchers uncovered a botnet of small office/home office and IoT devices likely operated by Flax Typhoon, a Chinese nation-state threat actor. Active since May 2020, the botnet compromised over 200,000 devices globally, peaking at 60,000 active nodes. It used a three-tiered architecture with compromised routers, IP cameras, and NAS devices at the bottom layer, controlled through a custom Mirai variant called Nosedive.
Why it matters: Raptor Train operated undetected for four years. The botnet’s three-tiered architecture made it resilient, and the volume of vulnerable devices available for reinfection meant that rebooting compromised devices provided only temporary relief. Nation-state actors are investing in IoT botnet capabilities for long-term persistent access, not just immediate disruption.
What the 2025-2026 IoT Breaches Have in Common
Several patterns emerge from the breaches of the past two years:
Botnets are growing faster and hitting harder. Attack capacity jumped from 5.6 Tbps (Mirai variant, October 2024) to 29.7 Tbps (Aisuru, Q3 2025) to 31.4 Tbps (Aisuru/Kimwolf, November 2025) in just over a year. The supply of vulnerable devices ensures that even when law enforcement disrupts one botnet, the next one can scale quickly from the same pool.
Supply chain compromise is a persistent threat. BadBox 2.0 (10 million devices pre-infected) and Mars Hydro (2.7 billion records exposed through cloud misconfiguration) both demonstrate that IoT security must extend beyond the device itself to the manufacturing supply chain and the cloud infrastructure that supports it.
Nation-state actors are heavily invested in IoT. Raptor Train (Flax Typhoon), Kimwolf’s novel internal-network propagation technique, and Iranian targeting of IP cameras all indicate that state-aligned groups view IoT devices as strategic assets for persistent access, intelligence collection, and pre-positioning for future operations.
Known vulnerabilities and default credentials are still the primary attack vectors. Matrix built an entire botnet from publicly known vulnerabilities. Aisuru recruits devices with default passwords. The RondoDox campaign automated exploitation of a vulnerability within weeks of disclosure. The overwhelming majority of IoT compromises exploit problems that are already understood and, in many cases, preventable.
Enterprise infrastructure is now a target, not just consumer devices. The RondoDox campaign against HPE OneView and the Kimwolf propagation technique that reaches devices behind home routers show that IoT attacks are reaching deeper into networks than ever before.
How to Protect Your Organization
The incidents above share a common thread: they exploited IoT devices that were unmonitored, unpatched, using default credentials, or sitting on unsegmented networks. The defenses are well understood:
- Maintain a continuous device inventory. Passive discovery is essential. You need to know every connected device on your network, including devices added by vendors, facilities teams, and operations staff.
- Segment IoT devices from critical systems. A compromised camera should not have a network path to your domain controller, EHR system, or financial applications. Targeted segmentation by exploit vector reduces the number of policies required while maximizing risk reduction.
- Prioritize and remediate vulnerabilities based on actual risk. The Matrix and RondoDox incidents both exploited known vulnerabilities with available patches. Contextual prioritization that considers network exposure, exploit availability, and business impact focuses effort where it matters.
- Eliminate default credentials. Multiple incidents in this list, including the Aisuru and Matrix botnets, relied on default passwords as their primary recruitment mechanism.
- Monitor for anomalous behavior. Raptor Train operated undetected for four years. Behavioral monitoring that baselines normal device communication and alerts on deviations catches compromised devices that signature-based tools miss.
- Evaluate device security before purchase. BadBox 2.0 proved that devices can arrive pre-infected. Pre-purchase assessment evaluates manufacturer security practices and identifies risks before devices enter your environment.
How Asimily Helps
The breaches documented in this post share a common denominator: organizations lacked visibility into the connected devices on their networks, could not prioritize which vulnerabilities mattered, and did not have segmentation controls in place to contain compromised devices.
Asimily addresses each of these gaps. The platform provides passive device discovery across IoT, IoMT, OT, and IT environments, contextual vulnerability prioritization using MITRE ATT&CK-based attack path analysis, automated segmentation policy generation with simulation, continuous behavioral monitoring, and forensic packet capture for incident response. Integration with existing network infrastructure, including Cisco ISE and other NAC platforms, means enforcement happens through the equipment already in place.
Asimily is the next-generation cyber asset and exposure management platform for IT, IoT, OT, and IoMT environments. Ranked 11th on the 2024 Deloitte Technology Fast 500 for fastest-growing cybersecurity companies in North America. Learn more.
Secure Every IoT Device.
Automatically. 
Cyber threats move fast — so should you. Asimily gives instant inventory and smart, prioritized risk mitigation insights for every IoT, OT, and IoMT device — so you can take action before threats strike.

---
*检索时间: 2026-07-24 21:11:36*
*搜索来源: DuckDuckGo*
