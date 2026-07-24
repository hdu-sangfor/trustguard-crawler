# 2026 Supply Chain Security Report: Attack Analysis & Compliance Guide | Bastion

### 来源信息
- **URL**: https://bastion.tech/blog/2026-supply-chain-security-report/
- **域名**: bastion.tech
- **检索关键词**: 供应链攻击 案例 分析 2025 2026
- **页面抓取**: 成功

### 搜索摘要
February 17, 2026 - This report analyzes the major supply chain attacks of 2025-2026, identifies common attack patterns, and provides practical guidance for strengthening your vendor risk management program.

### 页面正文
Software supply chain attacks more than doubled in 2025, with global losses reaching $60 billion. Over 70% of organizations reported experiencing at least one third-party or software supply chain-related security incident. For engineering teams managing vendor relationships, understanding these attacks and how compliance frameworks address them has never been more critical.
This report analyzes the major supply chain attacks of 2025-2026, identifies common attack patterns, and provides practical guidance for strengthening your vendor risk management program.
The 2025-2026 Supply Chain Attack Landscape
The Shai-Hulud Campaigns: Multi-Wave JavaScript Supply Chain Attacks
The most significant supply chain attacks of 2025 were the Shai-Hulud campaigns: coordinated, multi-wave attacks targeting the JavaScript ecosystem that evolved from opportunistic compromises to engineered, targeted attacks.
Wave 1: Shai-Hulud (September 2025)
The initial attack compromised 500+ npm packages through stolen maintainer credentials:
- Attackers gained initial access through compromised npm maintainer accounts
- They deployed malware that scanned environments for GitHub Personal Access Tokens (PATs) and cloud service API keys (AWS, GCP, Azure)
- Credentials were uploaded to a public repository named "Shai-Hulud" via the GitHub API
- An automated process spread the attack by authenticating to npm as compromised developers, injecting code into other packages
Wave 2: Shai-Hulud 2.0 "The Second Coming" (November 21-23, 2025)
A more aggressive follow-up campaign affected 25,000+ GitHub repositories, pushing trojanized versions of legitimate packages to millions of downstream users. This wave demonstrated the attackers' ability to scale rapidly using credentials harvested in the initial campaign.
The s1ngularity Attack: 2,349 Credentials from a Build Tool
Between August and November 2025, the s1ngularity campaign targeted Nx, a popular build system used by thousands of organizations. We covered this attack in detail in our Nx supply chain attack analysis. The attackers exploited a vulnerability in the pull_request_target trigger in GitHub Actions workflows, stealing an npm publishing token and using it to publish malicious versions.
Impact:
- 2,349 credentials harvested
- 1,079 developer systems compromised
- Malicious code distributed through a trusted build tool
- First documented attack to weaponize AI CLI tools (Claude, Gemini) for reconnaissance
GhostActions: PyPI to npm via GitHub Actions
On September 2, 2025, the GhostActions campaign leveraged a compromised PyPI maintainer account to insert a malicious GitHub Actions workflow. This single compromise exfiltrated over 3,000 secrets, including npm tokens that enabled subsequent attacks across ecosystems.
The September npm Hijacking: 18 Packages, 2 Billion Weekly Downloads
In September 2025, attackers hijacked 18 popular npm packages collectively downloaded over 2 billion times weekly. Using phishing campaigns to compromise maintainer accounts, they gained control over widely-used linting and formatting libraries, injecting info-stealer malware.
Beyond npm: High-Profile Enterprise Attacks
Supply chain attacks extended beyond package registries into enterprise systems:
Jaguar Land Rover (August 2025): A cyberattack that disrupted production for five weeks, affecting more than 5,000 businesses across JLR's global supply chain. Expected cost: Â£1.9 billion, widely regarded as the most economically damaging cyber incident in UK history.
Marks & Spencer (April 2025): A social engineering attack against employees at a third-party contractor over Easter weekend resulted in an estimated Â£300 million loss in operating profit.
F5 BIG-IP Source Code Theft: Nation-state actors maintained unauthorized access to F5's internal systems, exfiltrating portions of BIG-IP source code. This software is deployed across enterprise and government environments globally.
Common Attack Patterns
Analysis of 2025-2026 attacks reveals consistent patterns that organizations can defend against:
1. Credential-Adjacent Compromise
Attackers gain initial footholds via compromised credentials or OAuth tokens. The same pattern repeats across ecosystems: maintainers get phished, credentials get abused, and malicious code persists far too long.
Defense: Mandate phishing-resistant multi-factor authentication (MFA) on all developer accounts. CISA specifically recommends this in their September 2025 advisory.
2. Install-Time Execution with Obfuscation
Malicious post-install or lifecycle scripts are injected into packages, with payloads often conditionally activated and only revealing behavior at runtime.
Defense: Review postinstall scripts in dependencies. Use tools that can detect suspicious lifecycle script behavior.
3. Cross-Ecosystem Propagation
Attackers increasingly target multiple package ecosystems simultaneously. A compromised PyPI account can yield npm tokens, which compromise npm packages, which yield more credentials in a cascading effect.
Defense: Treat all package ecosystem credentials with equal criticality. Rotate credentials immediately upon any suspected compromise.
4. CI/CD Pipeline Exploitation
GitHub Actions workflows, particularly the pull_request_target trigger, have become a primary attack vector. This allows attackers to run code with write permissions on repositories.
Defense: Audit GitHub Actions workflows. Avoid pull_request_target unless necessary, and never checkout untrusted code in such workflows.
Supply Chain Attacks by the Numbers
| Metric | Value | Source | 
|---|---|---|
| YoY increase in supply chain attacks | >100% | Silobreaker | 
| Organizations experiencing third-party incidents | 70% | ReversingLabs | 
| Breaches linked to third-party access | 35.5% | SecurityScorecard | 
| Ransomware attacks involving third-party vectors | 41.4% | SecurityScorecard | 
| CISOs with full supply chain visibility | 15% | Panorays 2026 Survey | 
| Average breach cost (US) | $10.22M | DeepStrike | 
| CVEs reported in 2025 | 45,777 | Cisco | 
Mapping Supply Chain Security to Compliance Frameworks
SOC 2 Vendor Management Requirements
SOC 2's Trust Services Criteria address supply chain security through several controls:
CC9.2 - Vendor and Business Partner Risk Management
The AICPA criteria CC9.2 requires organizations to assess and manage risks associated with vendors and business partners. Implementation involves:
- Due diligence before onboarding: Request SOC 2 reports from vendors. If unavailable, require completion of a security questionnaire (NIST, SANS Top 20, ISACA frameworks)
- Contractual requirements: Define security expectations, data protection measures, and incident response procedures
- Ongoing monitoring: Continuously review vendor compliance and conduct periodic risk assessments
CC2.3 - External Party Communication
Requires communication with external parties regarding matters affecting internal control. This is critical during supply chain incidents.
CC3.2 and CC3.4 - Risk Identification and Change Management
These criteria require identifying risks across the organization and assessing changes that could impact internal controls. This is directly applicable to dependency updates and vendor changes.
Practical Implementation:
- Maintain an inventory of all critical vendors and their SOC 2 status
- Request Type 2 reports (which test controls over time) rather than Type 1 (point-in-time)
- For vendors without SOC 2, implement compensating controls and enhanced monitoring
- Include supply chain security requirements in vendor contracts
ISO 27001 Supplier Relationship Controls
ISO 27001 provides specific controls for supplier relationships through its Annex A controls:
A5.19 - Information Security in Supplier Relationships
Establishes security policies for supplier relationships, ensuring all third parties comply with internal and regulatory standards.
A5.20 - Addressing Information Security within Supplier Agreements
Requires supplier agreements to specify security expectations, including data protection, incident response, and compliance obligations.
A5.21 - Managing Information Security in the ICT Supply Chain
Extends security controls beyond direct suppliers to the broader ICT supply chain, ensuring subcontractors and service providers adhere to the same standards.
A5.22 - Monitoring, Review and Change Management of Supplier Services
Requires ongoing monitoring of supplier security and managing changes to prevent adverse effects on the ISMS.
A5.23 - Information Security for Use of Cloud Services
Specifically addresses security requirements when using cloud service providers.
Practical Implementation:
- Develop a documented supplier management policy covering the entire relationship lifecycle
- Require suppliers to hold ISO 27001 certification or equivalent
- Classify data shared with suppliers and apply appropriate controls
- Conduct periodic supplier security assessments
- Implement change management procedures for supplier service modifications
Practical Steps to Strengthen Supply Chain Security
1. Implement Dependency Version Pinning and Waiting Periods
Research from GitHub Security shows that waiting 7-14 days after a package release before accepting it prevents the majority of supply chain attacks. A seven-day cooldown would have prevented eight out of ten major 2025 supply chain attacks.
Action items:
- Pin dependencies to specific versions (avoid ^and~in package.json)
- Implement a policy to delay adoption of new package versions
- Use lock files (package-lock.json, yarn.lock, poetry.lock) and commit them to version control
2. Adopt Software Bill of Materials (SBOM)
SBOMs provide an exact inventory of every dependency in your software. During incidents like Log4j, organizations with SBOMs identified exposure in minutes instead of days.
Recommended tools:
| Tool | Type | Best For | 
|---|---|---|
| OWASP Dependency-Track | Open Source | Continuous SBOM analysis with vulnerability intelligence | 
| CycloneDX Generator (cdxgen) | Open Source | Multi-language SBOM generation | 
| Wiz | Commercial | Agentless cloud-native SBOM | 
| Snyk | Commercial | Developer-friendly dependency scanning | 
| Bastion SBOM | Commercial | SBOM generation with continuous supply chain monitoring and compliance integration | 
Action items:
- Generate SBOMs for all production applications
- Integrate SBOM generation into CI/CD pipelines
- Establish processes to query SBOMs during incident response
- Consider solutions with integrated supply chain monitoring for real-time vulnerability alerts
3. Strengthen CI/CD Pipeline Security
Given the prevalence of GitHub Actions as an attack vector:
Action items:
- Audit all GitHub Actions workflows for risky patterns
- Remove or restrict pull_request_targettriggers
- Use permissions:to limit token scope in workflows
- Require approval for workflow changes
- Enable GitHub's secret scanning
4. Implement Comprehensive Credential Management
Action items:
- Mandate phishing-resistant MFA for all developer accounts (npm, PyPI, GitHub)
- Rotate API keys and tokens regularly
- Use short-lived credentials where possible
- Monitor for credential exposure in public repositories
5. Establish Vendor Risk Tiering
Not all vendors carry equal risk. Implement tiering based on:
- Data access level
- System criticality
- Integration depth
- Compliance status
Tier 1 (Critical): Direct access to production data or systems
- Require SOC 2 Type 2 or ISO 27001 certification
- Annual security assessments
- Contractual security requirements
Tier 2 (Important): Limited data access or non-production systems
- Require SOC 2 Type 1 or security questionnaire
- Biennial security assessments
Tier 3 (Standard): No direct data access
- Self-attestation acceptable
- Periodic review
6. Build Incident Response Capabilities for Supply Chain Attacks
Action items:
- Include supply chain scenarios in incident response plans
- Establish communication channels with critical vendors
- Define escalation procedures for suspected dependency compromises
- Practice supply chain incident tabletop exercises
Looking Ahead: 2026 Predictions
Security researchers expect supply chain attacks to continue evolving:
- Expanded ecosystem targeting: Beyond npm and PyPI, expect attacks on Maven, RubyGems, and NuGet 
- AI-generated malicious code: As AI code generation becomes prevalent, attackers will leverage it to create more sophisticated, harder-to-detect malicious packages 
- Faster exploitation: Attacks will become faster, broader, and harder to contain once initial access is achieved 
- Regulatory pressure: SBOM requirements will expand beyond federal contractors. Gartner predicts 60% of organizations building critical infrastructure software will mandate SBOMs by 2025 (already exceeded in early 2026) 
- Infrastructure expansion: Expect attacks on smart transportation, vessels, public transit, smart buildings, and satellite communications 
Conclusion
The 2025-2026 supply chain attack landscape demonstrates that organizations can no longer treat dependency management as a purely technical concern. With 70% of organizations experiencing supply chain incidents and losses reaching $60 billion, vendor risk management has become a business-critical function.
The good news: compliance frameworks like SOC 2 and ISO 27001 provide structured approaches to managing these risks. By implementing the controls outlined in this report (version pinning, SBOM adoption, CI/CD hardening, credential management, and vendor tiering), organizations can significantly reduce their exposure to supply chain attacks.
The organizations that will weather 2026's inevitable supply chain storms are those building these capabilities today.
Key Takeaways
- Supply chain attacks doubled in 2025, with global losses reaching $60 billion
- Common attack patterns include credential compromise, install-time exploitation, and cross-ecosystem propagation
- SOC 2 CC9.2 and ISO 27001 A5.19-A5.23 provide frameworks for vendor risk management
- Seven-day waiting periods on new package versions would prevent most attacks
- SBOM adoption enables rapid incident response when vulnerabilities are discovered
- 2026 will bring expanded ecosystem targeting and faster attack propagation
This report is provided for educational purposes. Organizations should consult with qualified security and compliance professionals when implementing vendor risk management programs. Bastion provides compliance automation and security monitoring solutions to help organizations manage supply chain risks effectively.
Share this article
Related Articles
12 Best Practices to Prevent Software Supply Chain Attacks
Software supply chain attacks have surged, with tools like Axios, LiteLLM, and Trivy all compromised in early 2026 alone. This guide covers 12 actionable best practices every engineering team should implement, from dependency pinning and SBOMs to CI/CD hardening and compliance alignment.
HackerBot-Claw and the Rise of AI Agent Supply Chain Attacks on GitHub Actions
An autonomous AI bot systematically compromised seven major open-source repositories in one week. Here's what tech startups need to know about securing GitHub Actions against AI-powered supply chain attacks.
npm Supply Chain Attacks in 2026: What SaaS Engineering Teams Must Know
npm supply chain attacks are no longer theoretical. With Shai-Hulud compromising 796 packages and the September 2025 hijacking affecting 2 billion weekly downloads, SaaS teams need practical defenses beyond npm audit.
Learn More About Compliance
Explore our guides for deeper insights into compliance frameworks.
NIS 2 Supply Chain Security Requirements
Supply chain security is one of the most significant additions in NIS 2 compared to the original directive. Article 21(2)(d) specifically mandates that organizations address cybersecurity risks in their relationships with suppliers and service providers. This reflects the growing recognition that an organization's security is only as strong as its weakest link in the supply chain.
What is an Information Security Management System (ISMS)?
An Information Security Management System (ISMS) is at the heart of ISO 27001 certification. Understanding what an ISMS is and how to build one is essential for successful certification. This guide explains everything you need to know.
ISO 27017 and ISO 27018: Cloud Security Standards
ISO 27017 and ISO 27018 extend ISO 27001 with specific guidance for cloud computing environments. Understanding these standards helps cloud service providers and their customers address cloud-specific security and privacy requirements.

---
*检索时间: 2026-07-24 14:08:38*
*搜索来源: DuckDuckGo*
