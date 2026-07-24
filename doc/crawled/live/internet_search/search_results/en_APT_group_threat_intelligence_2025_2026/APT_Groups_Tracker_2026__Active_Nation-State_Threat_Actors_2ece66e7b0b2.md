# APT Groups Tracker 2026: Active Nation-State Threat Actors

### 来源信息
- **URL**: https://cybergeodigest.com/resources/apt-groups-tracker.html
- **域名**: cybergeodigest.com
- **检索关键词**: APT group threat intelligence 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Track every major APT group by country. Aliases, sponsor agencies, primary targets, notable campaigns, and MITRE ATT&CK techniques for all active nation-state hackers in 2026.

### 页面正文
Table of Contents
- What Are APT Groups and Why Tracking Them Matters
- 🇷🇺 Russia: APT28, APT29, Sandworm, Turla, Gamaredon
- 🇨🇳 China: APT41, APT40, Volt Typhoon, Salt Typhoon, HAFNIUM, Mustang Panda
- 🇮🇷 Iran: Charming Kitten, MuddyWater, OilRig
- 🇰🇵 North Korea: Lazarus Group, Kimsuky, Andariel
- Others: Scattered Spider, Lapsus$
- How to Use This Tracker for Threat Modeling
- Resources and Naming Conventions
What Are APT Groups and Why Tracking Them Matters
An advanced persistent threat (APT) group is a state-sponsored or state-tolerated hacking organization that conducts long-duration intrusion campaigns against strategic targets. The term "advanced" refers to their use of custom tooling, zero-day exploits, and sophisticated tradecraft. "Persistent" captures their defining characteristic: they do not give up after initial failure, and they maintain access to compromised networks for months or years. "Threat" acknowledges that their objectives, whether espionage, sabotage, or financial theft, cause real-world harm to national security, economic competitiveness, and human rights.
Tracking APT groups matters because attribution drives defense. When you know that a specific intrusion was conducted by APT29 rather than a ransomware gang, your incident response changes fundamentally. The attacker's objectives shift from extortion to long-term intelligence collection. Their persistence mechanisms will be different. Their willingness to re-compromise you after remediation is virtually guaranteed. Without understanding the adversary, defenders waste resources on the wrong countermeasures.
For security teams, an APT groups list is not an academic exercise. It is the foundation of threat-informed defense. By mapping your organization's industry, geography, and data assets against the known targeting patterns of active APT groups, you can prioritize which threats demand the most attention and allocate defensive resources accordingly. A defense contractor in the United States faces a fundamentally different APT landscape than a cryptocurrency exchange in Singapore or a human rights organization in Europe.
This tracker catalogs every major nation-state threat actor active in 2026, organized by sponsoring country, with the operational details security teams need for threat modeling and detection engineering. CyberGeoDigest tracks these groups daily, connecting their technical operations to the geopolitical events that drive them.
🇷🇺 Russia
Russia maintains the most destructive and operationally diverse state cyber capability in the world. Operations are split between the GRU (military intelligence), SVR (foreign intelligence), and FSB (domestic security), each running distinct APT groups with different mandates, tradecraft, and targeting patterns.
APT28 (Fancy Bear)
- Aliases: Fancy Bear, Forest Blizzard, Sofacy, Pawn Storm, Sednit, STRONTIUM
- Sponsor: GRU Unit 26165 (85th Main Special Service Center)
- Primary targets: NATO governments, defense organizations, political campaigns, media outlets, sporting bodies
- Notable campaigns: 2016 Democratic National Committee hack; 2015 German Bundestag breach; persistent targeting of European foreign ministries; 2018 World Anti-Doping Agency hack-and-leak; ongoing campaigns against Ukrainian government networks since 2022
- Key MITRE ATT&CK techniques: Spearphishing Attachment (T1566.001), Exploitation for Client Execution (T1203), OS Credential Dumping (T1003), Web Protocols for C2 (T1071.001), Data Staged for Exfiltration (T1074)
APT28 is the GRU's primary cyber espionage and information operations unit. They favor rapid exploitation of publicly disclosed vulnerabilities, aggressive credential harvesting, and hack-and-leak operations designed to influence political outcomes. Their targeting directly reflects Russian military and foreign policy priorities.
APT29 (Cozy Bear)
- Aliases: Cozy Bear, Midnight Blizzard, The Dukes, Nobelium, YTTRIUM
- Sponsor: SVR (Foreign Intelligence Service of Russia)
- Primary targets: Government ministries, technology companies, think tanks, diplomatic organizations, cloud service providers
- Notable campaigns: SolarWinds supply chain compromise (2020); Microsoft corporate email breach (2024); ongoing targeting of Microsoft 365 and Azure AD environments; COVID-19 vaccine research espionage
- Key MITRE ATT&CK techniques: Supply Chain Compromise (T1195.002), Trusted Relationship (T1199), Cloud Accounts (T1078.004), Application Access Token (T1550.001), Multi-hop Proxy (T1090.003)
APT29 is the SVR's elite cyber espionage group and among the most technically sophisticated threat actors in existence. They prioritize stealth over speed, often maintaining access for years before detection. Their targeting of cloud infrastructure and identity providers reflects a strategic shift toward compromising the technology supply chain rather than individual targets.
Sandworm (Voodoo Bear)
- Aliases: Voodoo Bear, Seashell Blizzard, IRIDIUM, Telebots, Iron Viking
- Sponsor: GRU Unit 74455 (Main Centre for Special Technologies)
- Primary targets: Critical infrastructure (energy, water, transportation), Ukrainian government and civilian infrastructure, global organizations (collateral damage)
- Notable campaigns: Ukraine power grid attacks (2015, 2016); NotPetya ($10B+ global damage, 2017); Olympic Destroyer (2018 Pyeongchang Games); Viasat KA-SAT satellite attack (2022); multiple wiper deployments against Ukraine (2022-present)
- Key MITRE ATT&CK techniques: Destructive Payload (T1485), Disk Wipe (T1561), Supply Chain Compromise (T1195), Exploitation of Remote Services (T1210), Impair Defenses (T1562)
Sandworm is the most destructive cyber actor on the planet. Unlike espionage-focused groups, Sandworm's mandate includes sabotage and disruption of critical infrastructure. NotPetya remains the costliest cyber attack in history. Their operations during Russia's invasion of Ukraine have demonstrated that cyber attacks are now a permanent feature of conventional warfare.
Turla
- Aliases: Secret Blizzard, Snake, Venomous Bear, Uroburos, Waterbug, KRYPTON
- Sponsor: FSB Center 16 (signals intelligence)
- Primary targets: Foreign government ministries, embassies, defense organizations, research institutions
- Notable campaigns: Agent.BTZ USB worm targeting U.S. military networks (2008); Snake implant infrastructure spanning 50+ countries (disrupted by FBI in 2023); hijacking of other APT groups' C2 infrastructure; satellite-based C2 communications
- Key MITRE ATT&CK techniques: Hijack Execution Flow (T1574), Ingress Tool Transfer (T1105), Encrypted Channel (T1573), Rootkit (T1014), Compromise Infrastructure (T1584)
Turla is one of the oldest and most technically sophisticated APT groups, active since at least 2004. They are known for innovative tradecraft, including using satellite internet connections to hide their C2 infrastructure and hijacking the infrastructure of other threat actors to conduct false-flag operations. The FBI's 2023 takedown of the Snake implant network revealed infrastructure embedded in government systems across more than 50 countries.
Gamaredon
- Aliases: Aqua Blizzard, Primitive Bear, Shuckworm, Armageddon, Actinium
- Sponsor: FSB (Crimea-based unit, 18th Center)
- Primary targets: Ukrainian government, military, law enforcement, diplomatic entities
- Notable campaigns: Persistent, high-volume campaigns against Ukrainian government networks (2014-present); rapid retooling of malware infrastructure; thousands of attacks per year against Ukrainian targets since the 2022 invasion
- Key MITRE ATT&CK techniques: Spearphishing Attachment (T1566.001), Template Injection (T1221), Obfuscated Files (T1027), Dynamic Resolution (T1568), Automated Collection (T1119)
Gamaredon is the most prolific Russian APT group in terms of sheer volume. While less technically sophisticated than APT29 or Turla, Gamaredon compensates with relentless tempo, launching thousands of spearphishing campaigns per year. Their nearly exclusive focus on Ukrainian targets and FSB attribution make them a key indicator of Russian intelligence priorities against Ukraine.
🇨🇳 China
China operates the largest and most prolific state-sponsored cyber espionage program in the world, coordinated primarily by the Ministry of State Security (MSS) and the People's Liberation Army (PLA). Chinese APT groups target every sector, but intellectual property theft, military intelligence, and pre-positioning in critical infrastructure are the strategic priorities.
APT41 (Double Dragon)
- Aliases: Double Dragon, Brass Typhoon, Wicked Panda, Winnti, Barium
- Sponsor: MSS (Chengdu-based contractors)
- Primary targets: Technology, telecommunications, healthcare, gaming, higher education, government
- Notable campaigns: Supply chain attacks targeting software vendors; simultaneous espionage and financially motivated intrusions (dual-hat operations); extensive use of rootkits and bootkit malware; indictments of five members by the U.S. DOJ in 2020
- Key MITRE ATT&CK techniques: Supply Chain Compromise (T1195), Rootkit (T1014), Valid Accounts (T1078), Exploitation of Public-Facing Applications (T1190), Boot or Logon Autostart Execution (T1547)
APT41 is unique among nation-state actors for conducting both state-directed espionage and financially motivated cybercrime, often simultaneously. Their dual-hat model reflects the MSS's use of private contractors who are permitted to pursue personal profit outside of sanctioned intelligence operations. This makes APT41 one of the most versatile and prolific threat actors globally.
APT40 (Leviathan)
- Aliases: Leviathan, Gingham Typhoon, TEMP.Periscope, TEMP.Jumper, Bronze Mohawk
- Sponsor: MSS Hainan State Security Department
- Primary targets: Maritime industries, naval defense contractors, governments in Southeast Asia, universities with oceanographic research
- Notable campaigns: Theft of naval technology and South China Sea policy intelligence; exploitation of edge devices and rapid weaponization of newly disclosed vulnerabilities; 2024 advisory from Five Eyes agencies detailing APT40's capability to exploit new CVEs within hours of public disclosure
- Key MITRE ATT&CK techniques: Exploit Public-Facing Application (T1190), Web Shell (T1505.003), Remote Services (T1021), Proxy (T1090), Archive Collected Data (T1560)
APT40's targeting patterns map precisely to China's maritime territorial claims and naval modernization efforts. The group is known for extremely rapid exploitation of newly disclosed vulnerabilities, often weaponizing public proof-of-concept code within hours. Five Eyes intelligence agencies issued a joint advisory in 2024 specifically warning about APT40's speed of exploitation.
Volt Typhoon
- Aliases: Volt Typhoon, Vanguard Panda, Bronze Silhouette, DEV-0391
- Sponsor: PLA and/or MSS (attribution debated, likely military)
- Primary targets: U.S. critical infrastructure: water, energy, telecommunications, transportation, maritime ports
- Notable campaigns: Multi-year pre-positioning campaign inside U.S. critical infrastructure networks discovered 2023; living-off-the-land techniques using legitimate tools (PowerShell, WMI, netsh) to evade detection; access maintained for 5+ years in some cases
- Key MITRE ATT&CK techniques: Living Off The Land (T1218), Valid Accounts (T1078), NTDS (T1003.003), Network Sniffing (T1040), Lateral Movement via Remote Services (T1021)
Volt Typhoon represents a strategic shift in Chinese cyber operations from espionage to pre-positioning for disruption. U.S. intelligence officials assess that Volt Typhoon's objective is not to steal data but to maintain persistent access to critical infrastructure that could be leveraged for destructive operations during a military conflict, most likely over Taiwan. The campaign's exclusive use of living-off-the-land techniques made detection extraordinarily difficult.
Salt Typhoon
- Aliases: Salt Typhoon, GhostEmperor, FamousSparrow
- Sponsor: MSS
- Primary targets: Telecommunications providers, lawful intercept systems, ISPs
- Notable campaigns: Deep compromise of AT&T, Verizon, and T-Mobile networks disclosed in late 2024; accessed law enforcement wiretap systems; intercepted communications of senior U.S. government officials and presidential campaign staff; one of the most significant intelligence compromises in U.S. history
- Key MITRE ATT&CK techniques: Exploit Public-Facing Application (T1190), Network Sniffing (T1040), Data from Network Shared Drive (T1039), Proxy (T1090), Account Manipulation (T1098)
Salt Typhoon's compromise of major U.S. telecommunications providers gave Chinese intelligence access to the communications metadata and content of millions of Americans, including the wiretap systems used by law enforcement. The campaign underscored the strategic value of targeting telecommunications infrastructure and prompted emergency cybersecurity reviews across the U.S. telecom sector.
HAFNIUM
- Aliases: HAFNIUM, Silk Typhoon
- Sponsor: MSS
- Primary targets: On-premises Microsoft Exchange servers, government entities, defense contractors, law firms, infectious disease researchers
- Notable campaigns: Mass exploitation of Microsoft Exchange ProxyLogon vulnerabilities (CVE-2021-26855) in early 2021, compromising an estimated 250,000+ servers globally before patches were available; rapid pivot to web shell deployment for persistent access
- Key MITRE ATT&CK techniques: Exploit Public-Facing Application (T1190), Web Shell (T1505.003), Server Software Component (T1505), OS Credential Dumping (T1003), Email Collection (T1114)
HAFNIUM's mass exploitation of Exchange servers in 2021 was among the most impactful cyber campaigns in recent years. The indiscriminate scale of the attack, affecting hundreds of thousands of organizations worldwide, demonstrated China's willingness to conduct broad opportunistic exploitation alongside targeted espionage operations.
Mustang Panda
- Aliases: Mustang Panda, Stately Taurus, Bronze President, RedDelta, TEMP.Hex
- Sponsor: MSS (likely Guangdong region)
- Primary targets: Southeast Asian governments, European diplomatic missions, NGOs, religious organizations, telecommunications
- Notable campaigns: Persistent campaigns against Myanmar, Vietnam, Philippines, and Mongolia government networks; targeting of European diplomatic entities involved in Asia-Pacific policy; use of USB propagation and PlugX malware variants
- Key MITRE ATT&CK techniques: Spearphishing Attachment (T1566.001), DLL Side-Loading (T1574.002), Replication Through Removable Media (T1091), Ingress Tool Transfer (T1105), Encrypted Channel (T1573)
Mustang Panda is one of China's most active espionage groups targeting Southeast Asian nations. Their operations align closely with China's Belt and Road Initiative interests and territorial disputes in the South China Sea. Mustang Panda is known for heavy reliance on the PlugX remote access trojan and creative use of USB-based propagation techniques.
🇮🇷 Iran
Iran's cyber operations are primarily run by the Islamic Revolutionary Guard Corps (IRGC) and the Ministry of Intelligence and Security (MOIS). Iranian APT groups focus on regional adversaries (Israel, Saudi Arabia, Gulf states), surveillance of dissidents, and retaliatory operations triggered by geopolitical tensions over sanctions and the nuclear program.
Charming Kitten (APT35)
- Aliases: APT35, Charming Kitten, Mint Sandstorm, Phosphorus, TA453, Yellow Garuda
- Sponsor: IRGC Intelligence Organization (IRGC-IO)
- Primary targets: Journalists, academics, diplomats, Middle East policy researchers, Iranian diaspora and dissidents, pharmaceutical companies
- Notable campaigns: Persistent credential harvesting campaigns targeting think tank researchers and journalists covering Iran; targeting of U.S. presidential campaigns (2020, 2024); COVID-19 vaccine research espionage; surveillance operations against domestic and diaspora dissidents
- Key MITRE ATT&CK techniques: Spearphishing Link (T1566.002), Multi-Factor Authentication Interception (T1111), Valid Accounts (T1078), Social Engineering via Impersonation (T1656), Exfiltration Over Web Service (T1567)
Charming Kitten is Iran's most prolific espionage group and one of the most persistent social engineering operators among all nation-state actors. They build elaborate fake personas, sometimes engaging targets in weeks-long email correspondence before delivering a payload. Their primary mission is intelligence collection on perceived threats to the Islamic Republic, with a particular emphasis on identifying and surveilling political opponents.
MuddyWater
- Aliases: MuddyWater, Mango Sandstorm, Mercury, TEMP.Zagros, Static Kitten
- Sponsor: MOIS (Ministry of Intelligence and Security)
- Primary targets: Government entities and telecommunications companies in the Middle East, Turkey, and South Asia; also targets in Europe and North America
- Notable campaigns: Persistent campaigns against Middle Eastern government ministries; exploitation of legitimate remote management tools (Atera, ScreenConnect) for persistence; targeting of Turkish and Israeli government entities
- Key MITRE ATT&CK techniques: Spearphishing Attachment (T1566.001), PowerShell (T1059.001), Signed Binary Proxy Execution (T1218), Remote Access Software (T1219), Ingress Tool Transfer (T1105)
MuddyWater is distinguished from other Iranian groups by its MOIS sponsorship rather than IRGC. The group is known for leveraging legitimate remote management tools as an evasion technique, blending malicious activity with normal administrative traffic. Their targeting of government networks across the Middle East reflects MOIS intelligence collection priorities.
OilRig (APT34)
- Aliases: APT34, OilRig, Hazel Sandstorm, Crambus, Helix Kitten, Cobalt Gypsy
- Sponsor: MOIS
- Primary targets: Energy sector, government agencies, financial institutions, and telecommunications in the Middle East; particular focus on Saudi Arabia, UAE, and Israel
- Notable campaigns: Long-running campaigns against Gulf state energy and government networks; DNS tunneling for data exfiltration; tools and operational details leaked online in 2019 (Lab Dookhtegan leaks), exposing victims and infrastructure
- Key MITRE ATT&CK techniques: DNS Tunneling (T1071.004), Web Shell (T1505.003), Credential Dumping (T1003), Scheduled Task (T1053.005), Account Discovery (T1087)
OilRig has been one of Iran's most technically capable espionage groups since at least 2014. Their targeting of energy sector organizations and Gulf state governments reflects Iran's focus on regional intelligence collection. The 2019 leak of their tools and victim data by a mysterious persona known as Lab Dookhtegan was an unprecedented exposure of a nation-state group's operational details.
🇰🇵 North Korea
North Korean cyber operations are unique among nation-states because revenue generation, not intelligence collection, is the primary objective. The Reconnaissance General Bureau (RGB) runs multiple cyber units that have collectively stolen billions of dollars to fund the regime's weapons programs, making North Korea's hackers the most financially successful state-sponsored threat actors in history.
Lazarus Group
- Aliases: Lazarus, Diamond Sleet, APT38, ZINC, Hidden Cobra, Labyrinth Chollima
- Sponsor: RGB (Reconnaissance General Bureau)
- Primary targets: Cryptocurrency exchanges and DeFi platforms, banks (SWIFT network), defense contractors, technology companies
- Notable campaigns: Sony Pictures hack (2014); Bangladesh Bank SWIFT heist ($81M, 2016); WannaCry ransomware (2017); Axie Infinity Ronin Bridge theft ($620M, 2022); Bybit exchange theft (~$1.5B, 2025); social engineering campaigns targeting developers via fake job offers
- Key MITRE ATT&CK techniques: Supply Chain Compromise (T1195), Social Engineering (T1566), Trojanized Software (T1195.002), Cryptocurrency Theft (T1657), Data Encrypted for Impact (T1486)
Lazarus is North Korea's flagship cyber unit and the most financially destructive APT group in the world. U.N. investigators estimate North Korean cyber actors have stolen over $3 billion in cryptocurrency since 2017. Lazarus operators increasingly target the software supply chain and cryptocurrency developers through elaborate social engineering, including fake job offers delivered via LinkedIn and other professional platforms.
Kimsuky
- Aliases: Kimsuky, Emerald Sleet, Velvet Chollima, Thallium, Black Banshee, APT43
- Sponsor: RGB
- Primary targets: South Korean government, think tanks, academics specializing in Korean Peninsula policy, defense and aerospace organizations in the U.S. and Japan
- Notable campaigns: Persistent spear-phishing against South Korean policy researchers and journalists; impersonation of real journalists and academics to build trust; credential theft campaigns targeting Google and Microsoft accounts; targeting of nuclear policy and denuclearization experts
- Key MITRE ATT&CK techniques: Spearphishing Link (T1566.002), Credential Harvesting (T1589.001), Impersonation (T1656), Browser Session Hijacking (T1185), Exfiltration Over Web Service (T1567)
Kimsuky is North Korea's dedicated intelligence collection unit, focused on gathering political and military intelligence related to the Korean Peninsula. Their social engineering is among the most patient of any APT group. Kimsuky operators routinely impersonate real journalists and researchers, sometimes exchanging weeks of benign emails before delivering a malicious payload or credential harvesting link.
Andariel
- Aliases: Andariel, Onyx Sleet, Silent Chollima, Plutonium, DarkSeoul
- Sponsor: RGB 3rd Bureau (Technical Reconnaissance Bureau)
- Primary targets: South Korean defense, aerospace, nuclear energy, and engineering organizations; U.S. defense contractors and healthcare organizations
- Notable campaigns: Theft of classified defense data from South Korean defense contractors; ransomware operations (Maui ransomware) against U.S. hospitals for revenue generation; espionage against nuclear energy and military satellite programs
- Key MITRE ATT&CK techniques: Exploit Public-Facing Application (T1190), Data Encrypted for Impact (T1486), Valid Accounts (T1078), Ingress Tool Transfer (T1105), Proxy (T1090)
Andariel blends espionage with revenue-generating ransomware operations, targeting defense and critical infrastructure organizations. The U.S. DOJ has indicted Andariel operatives for deploying Maui ransomware against American hospitals and healthcare providers, with the extorted cryptocurrency funneled back to fund further North Korean intelligence operations.
Others: Non-State and Ambiguously Attributed Groups
Not all significant threat actors fit neatly into the nation-state category. Several groups operating in 2025 and 2026 blur the line between criminal enterprise and state-tolerated operations.
Scattered Spider
- Aliases: Scattered Spider, Octo Tempest, UNC3944, 0ktapus, Star Fraud
- Sponsor: No state sponsor. English-speaking cybercriminal collective, predominantly young adults in the U.S. and UK
- Primary targets: Telecommunications, technology, hospitality, gaming, cryptocurrency, business process outsourcing (BPO)
- Notable campaigns: MGM Resorts and Caesars Entertainment attacks (2023); Okta support system compromise; persistent targeting of identity providers and help desks via social engineering and SIM swapping; affiliate operations with ALPHV/BlackCat ransomware
- Key MITRE ATT&CK techniques: Phishing for Credentials (T1598), SIM Swap (T1451), MFA Fatigue (T1621), Valid Accounts (T1078), Remote Access Software (T1219)
Scattered Spider is the most impactful English-speaking threat group to emerge in recent years. Their mastery of social engineering, particularly against help desks and identity providers, has made them effective against organizations with mature technical defenses. Their collaboration with ransomware-as-a-service operations amplifies their impact significantly.
Lapsus$
- Aliases: Lapsus$, DEV-0537, Strawberry Tempest
- Sponsor: No state sponsor. Loosely organized group, members primarily teenagers in the UK and Brazil
- Primary targets: Major technology companies (Microsoft, Nvidia, Samsung, Okta, Uber, Rockstar Games)
- Notable campaigns: Breach and source code theft from Microsoft, Nvidia, Samsung, and Uber in 2022; exploitation of contractor and third-party access; social engineering and insider recruitment for initial access
- Key MITRE ATT&CK techniques: Phishing (T1566), Insider Threat (T1199), Valid Accounts (T1078), Data from Information Repositories (T1213), Data Exfiltration (T1041)
Lapsus$ demonstrated that technically unsophisticated actors leveraging social engineering and insider recruitment can compromise even the most well-defended technology companies. While several members were arrested in 2022 and 2023, the group's tactics have been widely adopted by other threat actors, particularly Scattered Spider. Their legacy is a permanent reminder that identity and access management are the weakest points in most organizations' defenses.
How to Use This APT Tracker for Threat Modeling
A comprehensive APT groups list becomes actionable when you map it against your organization's specific risk profile. Here is a practical framework for using this tracker to inform your security program.
- Identify your threat surface: Determine which nation-state groups are most likely to target your industry, geography, and data assets. A U.S. defense contractor should prioritize Chinese (APT40, Volt Typhoon) and Russian (APT28, APT29) groups. A cryptocurrency company should focus on Lazarus Group and Andariel. A Middle Eastern energy company should watch OilRig and MuddyWater.
- Map adversary TTPs to your defenses: For each priority APT group, review their known MITRE ATT&CK techniques and evaluate whether your current security controls detect and prevent those specific behaviors. If Volt Typhoon is your primary threat, you need detection for living-off-the-land techniques, not just signature-based malware detection.
- Monitor geopolitical triggers: APT activity surges during geopolitical crises. Increased tension in the Taiwan Strait increases Volt Typhoon risk. Sanctions against Iran correlate with retaliatory cyber operations. Elections trigger APT28 information operations. Following these events through CyberGeoDigest's daily briefings helps you anticipate escalations before they hit your network.
- Build adversary-specific detection rules: Use the MITRE ATT&CK technique mappings for your priority threat actors to build and validate detection rules. Purple team exercises should simulate the specific tradecraft of the APT groups most likely to target your organization.
- Track naming conventions across vendors: The same APT group may have five or more names depending on which vendor is reporting. Use the aliases listed in this tracker to cross-reference reporting from different sources and ensure you are not missing critical intelligence because of naming inconsistencies.
Resources and Naming Conventions
The APT landscape is tracked by multiple organizations, each with their own naming conventions. Understanding these conventions is essential for cross-referencing intelligence.
- MITRE ATT&CK Groups: The authoritative reference for APT group profiles, techniques, and associated software. MITRE maintains detailed pages for each tracked group with sourced references. Visit attack.mitre.org/groups.
- Mandiant / Google Threat Intelligence: Uses the APT numbering system (APT28, APT29, APT41, etc.) and UNC designations for uncategorized groups. Mandiant's annual M-Trends report is essential reading for understanding year-over-year trends in nation-state activity.
- CrowdStrike: Uses animal-based naming tied to country of origin: Bear (Russia), Panda (China), Kitten (Iran), Chollima (North Korea), Spider (criminal). For example, Fancy Bear = APT28, Wicked Panda = APT41.
- Microsoft: Transitioned in 2023 from element-based names (STRONTIUM, HAFNIUM) to a weather-themed taxonomy. Country mappings: Blizzard (Russia), Typhoon (China), Sandstorm (Iran), Sleet (North Korea), Tempest (criminal). For example, Forest Blizzard = APT28, Volt Typhoon = Chinese critical infrastructure pre-positioning group.
- CyberGeoDigest: Our daily briefings reference multiple naming conventions and always provide geopolitical context for APT activity. We track new campaigns, attribution updates, and shifts in targeting as they happen, connecting technical intelligence to the state-level objectives driving each group's operations.
APT group tracking is not a static exercise. Groups evolve, retool, merge, and spawn new subunits. This tracker reflects the landscape as of early 2026 and is best used alongside daily intelligence sources that capture changes as they happen.
Frequently Asked Questions
What is an APT group?
An APT — advanced persistent threat — is a well-resourced attacker, usually state-sponsored, that gains unauthorized access and remains undetected for an extended period. "Advanced" refers to their capability and access to custom tooling; "persistent" to their long-term, objective-driven presence rather than a smash-and-grab.
How are APT groups named?
There is no single naming authority, which is why one group has many names. Vendors assign their own labels: Mandiant uses APT numbers (APT28, APT41), CrowdStrike uses animal themes tied to the sponsor country (Fancy Bear for Russia, Panda for China), and Microsoft uses weather themes (Forest Blizzard). Fancy Bear, APT28, and Forest Blizzard are all the same Russian GRU unit.
What is the difference between an APT and ordinary cybercrime?
APTs pursue strategic objectives — espionage, sabotage, positioning — with state backing and long timelines. Ordinary cybercrime is financially motivated, opportunistic, and moves fast to monetize access. The line blurs where states use criminal proxies or tolerate ransomware crews that serve national interests.
Which APT groups are the most active?
Consistently prominent groups include Russia's APT28 (Fancy Bear) and APT29 (Cozy Bear), China's APT41 and Salt/Volt Typhoon clusters, Iran's MuddyWater and APT35, and North Korea's Lazarus Group. Activity shifts with geopolitics, so a current tracker matters more than a static list.
Track APT groups in real time
Get a free daily briefing that connects APT campaigns to the geopolitical events driving them. Nation-state threats, attribution updates, and critical infrastructure risks in 5 minutes.
Subscribe free

---
*检索时间: 2026-07-24 15:16:30*
*搜索来源: DuckDuckGo*
