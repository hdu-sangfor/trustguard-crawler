# GitHub - capetron/zero-trust-architecture-guide: Zero trust...

### 来源信息
- **URL**: https://github.com/capetron/zero-trust-architecture-guide
- **域名**: github.com
- **检索关键词**: zero trust architecture implementation guide
- **页面抓取**: 成功

### 搜索摘要
A practical guide to implementing zero trust architecture for IT teams and security leaders. This guide covers the core principles of zero trust, maps implementation to NIST SP 800-207, provides a phased rollout plan...

### 页面正文
A practical guide to implementing zero trust architecture for IT teams and security leaders. This guide covers the core principles of zero trust, maps implementation to NIST SP 800-207, provides a phased rollout plan, and includes a vendor evaluation framework and maturity model to measure your progress. Whether you are starting from a traditional perimeter network or evolving an existing zero trust initiative, this guide gives you a concrete path forward.
The traditional "castle and moat" security model assumed that everything inside the corporate network could be trusted. That assumption has been systematically dismantled by remote work, cloud migration, supply chain attacks, and increasingly sophisticated threat actors who move laterally once inside the perimeter.
Zero trust architecture (ZTA) operates on a fundamentally different principle: never trust, always verify. Every access request -- regardless of where it originates or what network it is on -- must be authenticated, authorized, and continuously validated before access is granted.
The federal government mandated zero trust for all agencies by the end of FY2024 (OMB M-22-09, EO 14028). Private sector adoption is accelerating as insurers, auditors, and compliance frameworks increasingly require zero trust controls. NIST SP 800-207 provides the authoritative reference architecture.
This is not about buying a single product. Zero trust is an architectural strategy implemented through a combination of identity, device, network, application, and data controls working together.
- Core Principles
- NIST SP 800-207 Alignment
- The Five Pillars of Zero Trust
- Phased Implementation Plan
- Technology Stack Comparison
- Zero Trust Maturity Model
- Network Segmentation Strategies
- Identity and Access Controls
- Device Trust and Compliance
- Data Protection in Zero Trust
- Vendor Evaluation Framework
- Common Mistakes
- Measuring Success
Zero trust is built on seven foundational principles, as defined in NIST SP 800-207:
| # | Principle | What It Means in Practice | 
|---|---|---|
| 1 | All data sources and computing services are considered resources | Not just servers -- SaaS apps, IoT devices, cloud workloads, and APIs are all resources requiring protection | 
| 2 | All communication is secured regardless of network location | Internal network traffic is encrypted and authenticated, not just traffic crossing the perimeter | 
| 3 | Access to individual resources is granted on a per-session basis | No persistent "trusted" sessions. Each request is evaluated independently | 
| 4 | Access is determined by dynamic policy | Policies consider user identity, device health, location, behavior, and data sensitivity -- not just username/password | 
| 5 | The enterprise monitors and measures security posture of all assets | Continuous monitoring, not point-in-time checks. Devices that fall out of compliance lose access | 
| 6 | All resource authentication and authorization are dynamic and strictly enforced | Real-time policy evaluation before access is granted. Step-up authentication for sensitive operations | 
| 7 | The enterprise collects information and uses it to improve security posture | Telemetry from all components feeds analytics for threat detection and policy refinement | 
- Not a product you can buy. No single vendor delivers "zero trust in a box."
- Not just VPN replacement. ZTNA is one component, not the whole architecture.
- Not binary. You do not flip a switch. Zero trust is a journey measured in maturity.
- Not a network-only concept. Identity, devices, applications, and data are equally important.
- Not about blocking everything. The goal is enabling secure access, not creating friction.
NIST SP 800-207 defines three core approaches to implementing zero trust:
Identity is the primary control plane. Every access decision starts with strong identity verification.
Best for: Organizations with strong IAM maturity, cloud-first environments Key technologies: SSO, MFA, PAM, identity governance (IGA), SCIM provisioning
Network segmentation is the primary control plane. Resources are isolated into fine-grained segments with enforcement at every boundary.
Best for: Organizations with significant on-premises infrastructure, OT/ICS environments Key technologies: Next-gen firewalls, SDN, microsegmentation platforms, east-west traffic inspection
Network access is abstracted through a broker that makes resources invisible to unauthorized users. Users connect to applications, not networks.
Best for: Remote-first organizations, hybrid environments, replacing VPN Key technologies: ZTNA gateways, SDP controllers, SASE platforms
NIST SP 800-207 defines these logical components that every zero trust architecture requires:
| Component | Function | Examples | 
|---|---|---|
| Policy Engine (PE) | Makes access decisions based on policy | Identity provider + context engine | 
| Policy Administrator (PA) | Executes the PE's decisions | ZTNA gateway, reverse proxy, API gateway | 
| Policy Enforcement Point (PEP) | Enforces the PA's instructions at the resource | Firewall, endpoint agent, application proxy | 
| Continuous Diagnostics and Mitigation (CDM) | Provides real-time device and asset health | EDR, UEM/MDM, vulnerability scanner | 
| Industry Compliance | Feeds regulatory requirements into policy | GRC platform, compliance policies | 
| Threat Intelligence | Informs dynamic risk assessment | TI feeds, SIEM correlation, user behavior analytics | 
| Activity Logs | Provides audit trail and analytics input | SIEM, centralized logging, UEBA | 
| Data Access Policy | Defines who can access what data under what conditions | DLP, data classification, ABAC policies | 
The CISA Zero Trust Maturity Model organizes zero trust into five pillars. Progress on each pillar can be tracked independently.
Goal: Strong identity verification for every access request.
| Maturity Level | Controls | 
|---|---|
| Traditional | Passwords only, limited MFA, manual provisioning | 
| Initial | MFA for remote access and admins, centralized SSO | 
| Advanced | MFA everywhere, risk-based authentication, automated provisioning/deprovisioning | 
| Optimal | Passwordless authentication, continuous identity verification, real-time risk scoring | 
Key technologies: Identity Provider (IdP), MFA, SSO, PAM, IGA, SCIM
Goal: Every device is identified, inventoried, and meets security requirements before access.
| Maturity Level | Controls | 
|---|---|
| Traditional | No device inventory, no compliance checks | 
| Initial | Device inventory, basic endpoint protection | 
| Advanced | EDR on all devices, compliance-based access (no patch = no access), BYOD management | 
| Optimal | Real-time device risk scoring, automated remediation, hardware attestation | 
Key technologies: EDR/XDR, UEM/MDM, device certificates, compliance engines
Goal: Network segmentation limits lateral movement. All traffic is encrypted and inspected.
| Maturity Level | Controls | 
|---|---|
| Traditional | Flat network, perimeter firewall only | 
| Initial | Basic VLANs, internal firewalls for critical segments | 
| Advanced | Microsegmentation, east-west traffic inspection, encrypted internal traffic | 
| Optimal | Software-defined segmentation, dynamic policy-based access, full traffic encryption | 
Key technologies: Next-gen firewalls, microsegmentation, SDN, ZTNA, encrypted DNS
Goal: Applications are secured, monitored, and accessible only through authorized channels.
| Maturity Level | Controls | 
|---|---|
| Traditional | Direct application access, no WAF, no API security | 
| Initial | WAF for web apps, basic API authentication | 
| Advanced | Application-level segmentation, API gateway with auth, runtime protection | 
| Optimal | Software-defined access to all apps (apps invisible without authorization), CI/CD security, SBOM tracking | 
Key technologies: ZTNA, WAF, API gateway, RASP, CASB, container security
Goal: Data is classified, protected, and access is controlled based on sensitivity and context.
| Maturity Level | Controls | 
|---|---|
| Traditional | No data classification, broad access | 
| Initial | Manual data classification, DLP for email | 
| Advanced | Automated data classification, DLP at endpoints and cloud, encryption at rest and in transit | 
| Optimal | Data-centric security (protection travels with the data), real-time access decisions based on data sensitivity and user context | 
Key technologies: DLP, data classification, encryption (FIPS 140-3), CASB, rights management
Zero trust implementation is a multi-year journey. This phased plan provides a realistic 18-24 month roadmap.
Focus: Visibility and identity
| Task | Deliverable | Effort | 
|---|---|---|
| Asset inventory (users, devices, applications, data) | Complete asset register | 2-4 weeks | 
| Data flow mapping (where does sensitive data live and move?) | Data flow diagrams | 2-3 weeks | 
| Identity consolidation (single IdP, eliminate duplicate accounts) | Centralized identity | 3-6 weeks | 
| Deploy MFA on all externally facing services | MFA coverage report | 2-4 weeks | 
| Deploy MFA on all privileged accounts | Admin MFA complete | 1-2 weeks | 
| Define zero trust policy framework (who accesses what, from where, under what conditions) | Policy document | 2-3 weeks | 
| Baseline current maturity level across all 5 pillars | Maturity assessment | 1-2 weeks | 
Focus: Identity hardening and initial segmentation
| Task | Deliverable | Effort | 
|---|---|---|
| Implement SSO for all SaaS applications | SSO integration complete | 4-8 weeks | 
| Deploy ZTNA for remote access (replace or augment VPN) | ZTNA pilot for 1-2 apps | 4-6 weeks | 
| Segment critical systems (DC, backup, management) from general network | Network segments configured | 3-4 weeks | 
| Deploy EDR on all endpoints and servers | EDR coverage 100% | 2-4 weeks | 
| Implement automated account provisioning/deprovisioning | SCIM integration | 3-4 weeks | 
| Enable conditional access policies (device compliance, location, risk) | Conditional access active | 2-3 weeks | 
Focus: Application-level controls and microsegmentation
| Task | Deliverable | Effort | 
|---|---|---|
| Expand ZTNA to all applications (no more direct network access to apps) | Full ZTNA rollout | 8-12 weeks | 
| Implement microsegmentation for server workloads | Microsegmentation deployed | 6-10 weeks | 
| Deploy data classification and DLP | Data protection active | 6-8 weeks | 
| Implement PAM for all privileged access | PAM operational | 4-6 weeks | 
| Enable risk-based authentication (step-up MFA for sensitive operations) | Risk engine active | 3-4 weeks | 
| Integrate SIEM with identity, device, and network telemetry | Unified monitoring | 4-6 weeks | 
Focus: Automation, analytics, and continuous improvement
| Task | Deliverable | Effort | 
|---|---|---|
| Implement user and entity behavior analytics (UEBA) | Behavior baselines established | 6-8 weeks | 
| Automate device compliance enforcement (non-compliant = quarantine) | Automated remediation | 4-6 weeks | 
| Evaluate passwordless authentication | Passwordless pilot | 4-8 weeks | 
| Implement data-centric security (encryption, rights management) | Data protection at rest and in transit | 6-8 weeks | 
| Continuous maturity assessment and gap closure | Quarterly maturity reports | Ongoing | 
| Zero trust tabletop exercises (test policies under attack scenarios) | Exercise reports | Quarterly | 
| Vendor | Strengths | Considerations | Best For | 
|---|---|---|---|
| Zscaler (ZIA + ZPA) | Largest global cloud, strong proxy architecture, mature DLP | Complex deployment, can be expensive | Large enterprises, cloud-first | 
| Palo Alto (Prisma Access) | Strong firewall heritage, integrated CASB, good for hybrid | Agent-heavy, licensing complexity | Hybrid environments, Palo Alto shops | 
| Cloudflare (Access + Gateway) | Developer-friendly, fast global network, transparent pricing | Newer to enterprise features | SMBs, developer-centric orgs | 
| Microsoft (Entra + Defender) | Deep M365 integration, conditional access, included in E5 | Microsoft-centric, less effective for non-MS apps | Microsoft-heavy environments | 
| CrowdStrike (Falcon) | Best-in-class EDR, identity threat detection | Primarily endpoint/identity, less network | EDR-first zero trust | 
| Fortinet (FortiSASE) | Affordable, strong SD-WAN integration | Smaller cloud footprint | Cost-sensitive, FortiGate shops | 
| Netskope | Strong CASB and DLP, good cloud visibility | Less known brand, smaller partner ecosystem | Data protection-focused | 
| Vendor | Approach | Best For | 
|---|---|---|
| Illumio | Agent-based workload segmentation | Data center, hybrid cloud | 
| Akamai Guardicore | Agent-based with network visibility | Large enterprise, complex environments | 
| VMware NSX | Hypervisor-level segmentation | VMware environments | 
| Cisco ACI | Network fabric-based | Cisco network shops | 
| ColorTokens | Agent + agentless hybrid | Mixed environments | 
| Vendor | Category | Best For | 
|---|---|---|
| Microsoft Entra ID (Azure AD) | IdP, MFA, Conditional Access | M365 environments | 
| Okta | IdP, SSO, lifecycle management | Multi-cloud, SaaS-heavy | 
| CyberArk | PAM, secrets management | Privileged access control | 
| BeyondTrust | PAM, endpoint privilege management | Windows-heavy environments | 
| Ping Identity | Federation, API security | Complex identity federation | 
Use this model to assess your current state and plan your roadmap. Score each pillar from 1 (Traditional) to 4 (Optimal).
| Pillar | Traditional (1) | Initial (2) | Advanced (3) | Optimal (4) | Current Score | 
|---|---|---|---|---|---|
| Identity | Passwords only | MFA for remote + admins | MFA everywhere, risk-based auth | Passwordless, continuous verification | |
| Devices | No inventory or compliance | Inventory + basic AV | EDR everywhere, compliance gates | Real-time risk scoring, auto-remediation | |
| Networks | Flat network, perimeter only | Basic VLANs | Microsegmentation, east-west inspection | Dynamic policy-based, fully encrypted | |
| Applications | Direct access, no controls | WAF, basic auth | ZTNA for all apps, API security | Apps invisible without auth, SBOM tracking | |
| Data | No classification | Manual classification, basic DLP | Automated classification, DLP everywhere | Data-centric security, real-time contextual access | 
| Total Score | Maturity Level | Description | 
|---|---|---|
| 5-8 | Traditional | Perimeter-based security. Significant zero trust gaps. | 
| 9-12 | Initial | Some zero trust controls in place. Identity is partially hardened. | 
| 13-16 | Advanced | Strong zero trust posture across most pillars. Continuous monitoring active. | 
| 17-20 | Optimal | Comprehensive zero trust architecture. Dynamic, automated, and continuously improving. | 
| Approach | How It Works | Complexity | Best For | 
|---|---|---|---|
| VLAN-based | Separate broadcast domains using 802.1Q tags | Low | Initial segmentation, small environments | 
| Firewall-based | Internal firewalls between segments | Medium | Traditional data centers | 
| Software-defined | SDN controller manages micro-perimeters | High | Cloud and hybrid environments | 
| Agent-based microsegmentation | Host-level firewall policy managed centrally | Medium-High | Workload protection across environments | 
| Identity-based | Access determined by user/device identity, not IP | High | ZTNA, cloud-native environments | 
| Zone | Contents | Access Policy | 
|---|---|---|
| Management | Domain controllers, SIEM, backup, PAM | Admin access only, MFA required, session recording | 
| User | Workstations, BYOD | Internet access via proxy, application access via ZTNA | 
| Server - Production | Business applications, databases | Application-specific access only, no direct user access | 
| Server - Development | Dev/test environments | Developer access only, isolated from production | 
| DMZ | Web servers, email gateway, VPN | Limited inbound, no direct internal access | 
| IoT/OT | Printers, cameras, building systems | Severely restricted, monitored, no internet | 
| Guest | Visitor Wi-Fi | Internet only, completely isolated from internal | 
| Backup | Backup servers, storage | Backup service accounts only, air-gapped or immutable | 
In a zero trust network, east-west (lateral) traffic between segments is explicitly controlled:
- Default deny -- No segment-to-segment traffic unless explicitly permitted
- Application-aware rules -- Allow only the specific ports and protocols needed
- Log everything -- All inter-segment traffic is logged for analytics
- Encrypt -- TLS/mTLS for all inter-segment communication
- Identity-aware -- Rules tied to service accounts or workload identity, not just IP addresses
From weakest to strongest, implement the highest level feasible:
| Level | Method | Zero Trust Suitability | 
|---|---|---|
| 1 | Password only | Unacceptable for zero trust | 
| 2 | Password + SMS OTP | Minimum (SMS is phishable, use only as fallback) | 
| 3 | Password + authenticator app (TOTP) | Acceptable for standard users | 
| 4 | Password + push notification (with number matching) | Good for standard users | 
| 5 | Password + FIDO2 hardware key | Strong for privileged users | 
| 6 | Passwordless (FIDO2 / passkey only) | Optimal -- eliminates credential phishing entirely | 
| Condition | Low Risk Response | Medium Risk Response | High Risk Response | 
|---|---|---|---|
| Known device + known location | Allow access | Allow access | MFA required | 
| Known device + unknown location | Allow access | MFA required | MFA + device compliance check | 
| Unknown device + known location | MFA required | MFA + limited session | Block or MFA + limited access | 
| Unknown device + unknown location | MFA required | Block or MFA + limited session | Block | 
| Impossible travel detected | MFA required | Block + alert | Block + alert + investigate | 
| Compromised credential detected | Block + force reset | Block + force reset | Block + force reset + investigate | 
- Separate admin accounts -- Admins use a dedicated account for admin tasks, never their daily account
- Just-in-time (JIT) access -- Privileges are granted for a limited time window, then automatically revoked
- Just-enough-access (JEA) -- Admin accounts have the minimum privileges required for the specific task
- Session recording -- All privileged sessions are recorded and available for audit
- Break-glass accounts -- Emergency accounts with full access, stored securely, and monitored for use
- No standing privileges -- In the optimal state, no one has permanent admin access. All admin access is requested and time-bound
Define minimum requirements that a device must meet to access resources:
| Requirement | Standard Users | Privileged Users | 
|---|---|---|
| OS version | Within 2 major versions | Current major version | 
| OS patches | Applied within 30 days | Applied within 14 days | 
| EDR agent | Installed and reporting | Installed, reporting, and no active threats | 
| Disk encryption | Enabled (BitLocker/FileVault) | Enabled with recovery key escrowed | 
| Firewall | Enabled | Enabled with restricted rules | 
| Screen lock | 15 minutes | 5 minutes | 
| Jailbreak/root | Not permitted | Not permitted | 
| Corporate certificate | Required | Required | 
Device requests access
  |
Is device enrolled in UEM/MDM?
  /  \
  YES  NO
  |  |
Is device  Is resource
compliant?  low-sensitivity?
  / \  / \
  Y  N  Y  N
  |  |  |  |
Grant  Quarantine  Allow  Block +
access  + remediate  limited  require
  auto  access  enrollment
| Level | Label | Examples | Controls | 
|---|---|---|---|
| Public | Unrestricted | Marketing materials, public website content | No special controls | 
| Internal | Internal Use Only | Internal memos, non-sensitive business data | Encryption in transit, access logging | 
| Confidential | Confidential | Financial data, HR records, customer PII | Encryption at rest + transit, DLP, access control, audit logging | 
| Restricted | Highly Restricted | CUI, PHI, PCI data, trade secrets, legal holds | Encryption everywhere, strict access control, DLP, monitoring, retention policies | 
| Control | Internal | Confidential | Restricted | 
|---|---|---|---|
| Encryption at rest | Recommended | Required | Required (FIPS 140-3) | 
| Encryption in transit | Required | Required | Required (FIPS 140-3) | 
| DLP monitoring | Optional | Required | Required | 
| Access logging | Required | Required | Required + alerted | 
| Data masking | Optional | Recommended | Required for non-prod | 
| Backup encryption | Required | Required | Required + separate keys | 
| Retention policy | Defined | Enforced | Enforced + legal hold | 
| Sharing restrictions | No external sharing without approval | Named individuals only | No external sharing | 
Use this scorecard when evaluating zero trust technology vendors. Score each criterion 1-5.
| Category | Criterion | Weight | Vendor A | Vendor B | Vendor C | 
|---|---|---|---|---|---|
| Architecture | Cloud-native (not bolted-on) | 10% | |||
| Architecture | API-first design | 5% | |||
| Architecture | Supports hybrid (cloud + on-prem) | 10% | |||
| Identity | Integration with your IdP | 10% | |||
| Identity | Supports FIDO2/passwordless | 5% | |||
| Policy | Granular, context-aware policies | 10% | |||
| Policy | Dynamic policy evaluation (not static) | 5% | |||
| Visibility | Comprehensive logging and analytics | 10% | |||
| Visibility | SIEM/SOAR integration | 5% | |||
| Scale | Performance at your scale | 10% | |||
| Scale | Global PoP coverage (if remote users) | 5% | |||
| Operations | Deployment complexity | 5% | |||
| Operations | Ongoing management overhead | 5% | |||
| Cost | Total cost of ownership (3-year) | 5% | |||
| Weighted Total | 100% | 
- How does your solution handle access decisions when connectivity to the cloud control plane is lost?
- What is the user experience impact (latency, extra steps) in typical workflows?
- How do you handle unmanaged devices (contractors, BYOD)?
- Can policies be applied consistently across on-premises, cloud, and SaaS resources?
- What does migration from our current solution look like? Can we run in parallel?
- How are policies versioned, tested, and rolled back?
- What certifications do you hold (SOC 2, FedRAMP, ISO 27001)?
Zero trust is a strategy, not a SKU. Organizations that buy a "zero trust" product without addressing identity, segmentation, and data protection end up with a fancy VPN replacement and little else.
Trying to implement all five pillars simultaneously leads to stalled projects. Start with identity (highest ROI) and expand methodically.
If zero trust makes users' lives significantly harder, they will find workarounds (shadow IT, shared credentials). Design for minimal friction.
Organizations implement MFA for all human users but leave service accounts with static passwords and excessive privileges. Service accounts need zero trust too -- workload identity, certificate-based auth, and just-in-time access.
You cannot enforce policies on resources you do not know exist. Asset discovery, data flow mapping, and traffic baselining must happen before policy enforcement.
Moving to the cloud does not automatically give you zero trust. Cloud environments still need identity controls, segmentation, data protection, and monitoring.
Many zero trust initiatives stop at the IT boundary. If you have OT/ICS systems (manufacturing, building management, medical devices), they need segmentation and monitoring too.
| KPI | How to Measure | Target | 
|---|---|---|
| MFA coverage | % of accounts with MFA enabled | 100% | 
| Mean time to detect (MTTD) | Average time from compromise to detection | < 24 hours | 
| Mean time to contain (MTTC) | Average time from detection to containment | < 4 hours | 
| Lateral movement success rate | Red team/pen test metric | 0% (attackers cannot move between segments) | 
| Phishing click rate | Simulated phishing exercises | < 3% | 
| Unmanaged device access | % of access from non-enrolled devices | < 5% | 
| Patch compliance | % of systems patched within SLA | > 95% | 
| Privileged access sessions recorded | % of admin sessions with recording | 100% | 
| Data classification coverage | % of data stores classified | > 90% | 
| Policy exceptions | Number of standing exceptions to zero trust policies | Trending down | 
- Update maturity scores across all 5 pillars
- Review and reduce policy exceptions
- Verify MFA coverage (new apps, new users)
- Test conditional access policies with tabletop scenarios
- Review access logs for anomalies
- Update asset inventory
- Validate segmentation rules with network scan
- Test break-glass account procedures
- Review vendor roadmaps for new capabilities
Need expert help implementing zero trust architecture? Petronella Technology Group provides:
- Managed IT Services - 24/7 monitoring and management
- Cybersecurity Assessments - Comprehensive security audits
- Network Security - Firewall, IDS/IPS, segmentation
- AI-Powered Security - Next-gen threat detection
Petronella Technology Group is a CMMC-RP certified cybersecurity firm in Raleigh, NC. Contact us or call (919) 348-4912.
Created by Petronella Technology Group, a cybersecurity and managed IT services firm based in Raleigh, NC. We design and implement zero trust architectures for businesses of all sizes, from initial assessment through full deployment.
CMMC-RP Certified | BBB A+ Since 2003 | 23+ Years of Cybersecurity Experience
Contact us: (919) 348-4912 | petronellatech.com/contact-us
- CMMC Compliance Guide
- Cybersecurity Services
- Virtual CISO
- Emergency IT Support
- Free Security Assessment
MIT License -- see LICENSE for details.

---
*检索时间: 2026-07-24 13:48:41*
*搜索来源: DuckDuckGo*
