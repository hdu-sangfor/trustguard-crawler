# What Is a SBOM? Software Supply Chain Security Explained

### 来源信息
- **URL**: https://www.encryptionconsulting.com/education-center/what-is-a-sbom/
- **域名**: www.encryptionconsulting.com
- **检索关键词**: software supply chain security SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
A SBOM is a machine-readable inventory of software components used to secure the supply chain. Learn what it is, the 2026 rules, formats, and the CBOM bridge.

### 页面正文
- Key Takeaways
- Why Software Supply Chain Security Matters
- What Goes Into an SBOM
- SBOM Formats: CycloneDX and SPDX
- The SBOM Regulatory Landscape in 2026
- The Direction of Travel
- How SBOMs Are Used in Practice
- From SBOM to CBOM: The Cryptography Connection
- How Encryption Consulting Helps
- Frequently Asked Questions
- Extend Supply Chain Security to Your Cryptography
A Software Bill of Materials (SBOM) is a formal, machine-readable inventory of all the components, libraries, and dependencies that make up a piece of software, along with the supply chain relationships between them.
A SBOM lists what a piece of software is actually made of: its first-party code, third-party libraries, open-source packages, and their versions and relationships. Security teams use it to find vulnerable components fast when a new flaw is disclosed, to meet procurement and regulatory requirements, and to manage risk across the software supply chain. The two dominant SBOM formats are CycloneDX and SPDX.
Key Takeaways
- A SBOM is a machine-readable inventory of every component in a piece of software, used to find vulnerabilities, meet compliance requirements, and manage supply chain risk.
- The two dominant, widely accepted SBOM formats are CycloneDX (OWASP, standardized as ECMA-424) and SPDX (an ISO/IEC standard). Most tools can produce both.
- US federal SBOM policy shifted in 2025 and 2026: EO 14306 (June 2025) amended earlier orders and OMB M-26-05 (January 2026) moved to an agency-led, risk-based approach. SBOMs are no longer uniformly mandated by attestation, but agencies may still require them.
- The EU Cyber Resilience Act, in force since December 2024, introduces SBOM-related obligations for products with digital elements, with key application dates in 2026 and 2027.
- A Cryptography Bill of Materials (CBOM) extends the SBOM idea to cryptographic assets, making it the bridge between software supply chain security and post-quantum readiness.
Why Software Supply Chain Security Matters
Modern software is assembled, not written from scratch. A typical application pulls in hundreds of open-source and third-party components, each of which may pull in its own dependencies. That dependency tree is the software supply chain, and every component in it is a potential entry point for an attacker.
Two incidents made this concrete for the whole industry. The 2020 SolarWinds attack inserted malicious code into a legitimate, signed software update that was then distributed to thousands of organizations. The 2021 Log4Shell vulnerability in the widely used Log4j logging library left countless applications exposed, and many organizations could not answer a basic question quickly: do we even use Log4j, and where? An SBOM is what lets an organization answer that question in minutes instead of weeks.
What Goes Into an SBOM
The US NTIA published a baseline set of minimum elements for an SBOM in 2021, which most frameworks still reference. At minimum, a SBOM records:
- Component name and supplier: What each component is and who produced it.
- Version. The specific version of each component, so known-vulnerable versions can be identified.
- Unique identifiers: Machine-readable identifiers such as Package URL (purl) or CPE.
- Dependency relationships: How components relate to one another, including transitive dependencies.
- Author and timestamp: Who generated the SBOM and when.
In 2025, CISA published a draft update to the minimum elements that adds fields such as component hash, license, and generation context. As of July 2026 the CISA 2025 minimum elements remain a public comment draft and do not create new legal requirements, so the NTIA 2021 baseline is still the safe floor to build to.
SBOM Formats: CycloneDX and SPDX
Two formats dominate, and both are accepted across essentially all current frameworks. The practical advice is to pick tools that can emit either, since different customers and regulators may ask for different formats.
| Attribute | CycloneDX | SPDX | 
|---|---|---|
| Steward | OWASP; standardized as Ecma ECMA-424 | Linux Foundation; standardized as ISO/IEC 5962 | 
| Original focus | Security and risk | Open-source license compliance | 
| BOM types | SBOM, CBOM, HBOM, SaaSBOM, OBOM, AI/ML-BOM | Primarily SBOM, with growing security fields | 
| Formats | JSON, XML, Protocol Buffers | JSON, YAML, RDF, tag-value, spreadsheet | 
| Cryptography support | Native CBOM (since v1.6) | Emerging | 
For a deeper side-by-side, see EC’s article on CBOM vs SBOM, and the explainer on what CycloneDX is.
The SBOM Regulatory Landscape in 2026
SBOM regulation is real but evolving, and the US federal picture changed significantly in 2025 and 2026. It is worth stating accurately rather than repeating older claims that a single executive order mandates SBOMs everywhere.
United States
Executive Order 14028 (May 2021) began modern federal SBOM adoption and directed NTIA to publish minimum elements. Executive Order 14306 (June 6, 2025) amended the intervening EO 14144, removing several enhanced attestation mandates while keeping software supply chain security, post-quantum cryptography, and secure development as priorities. OMB Memorandum M-26-05 (January 23, 2026) then rescinded the earlier attestation memos M-22-18 and M-23-16, moving federal agencies to an agency-led, risk-based approach.
The practical effect: federal agencies are no longer uniformly required to collect a standardized attestation form, but they may still require SBOMs contractually based on their own risk assessment. M-26-05 specifically notes that agencies requiring an SBOM from a cloud service provider should ask for one covering the runtime production environment. Sector and agency mandates also continue, including a US Army policy issued in early 2025 and the FDA’s medical device SBOM requirement in effect since March 2023.
European Union
The EU Cyber Resilience Act (CRA) entered into force in December 2024 and applies to manufacturers, importers, and distributors of products with digital elements sold in the EU market. It introduces vulnerability handling and SBOM-related transparency obligations, with a staged application timeline. Vulnerability and incident reporting obligations apply from September 11, 2026, and the broader set of requirements applies from December 11, 2027. Organizations selling digital products into the EU should plan against those dates now.
The Direction of Travel
Even where specific attestation mandates have been relaxed, the underlying expectation has not gone away: buyers, regulators, and large enterprises increasingly expect software producers to be able to produce a machine-readable SBOM on request. The safest posture is to treat SBOM generation as a standing capability, not a one-time compliance exercise.
How SBOMs Are Used in Practice
- Vulnerability response: When a new CVE lands, query your SBOMs to find every product that ships the affected component and version.
- Procurement and vendor risk: Request SBOMs from suppliers to understand what you are actually deploying before you buy.
- License compliance: Track open-source licenses across the dependency tree to avoid legal exposure.
- Incident response: During an incident, a SBOM shortens the time to determine blast radius.
- Continuous monitoring: Generate a SBOM on every build so the inventory stays current as code changes.
From SBOM to CBOM: The Cryptography Connection
A SBOM tells you what software components you run. It does not, on its own, tell you what cryptography those components use. That gap matters now because the migration to post-quantum cryptography (PQC) depends on knowing exactly which algorithms, key sizes, certificates, and protocols are in use across an environment.
A Cryptography Bill of Materials (CBOM) extends the SBOM concept to cryptographic assets. It inventories algorithms, keys, certificates, and the protocols that use them, and their relationships to software components. CycloneDX added native CBOM support in version 1.6 (April 2024) and expanded it in version 1.7 (October 2025). Because a CBOM can be expressed in the same CycloneDX document as an SBOM, an organization already generating SBOMs has a natural on-ramp to cryptographic inventory.
This is the bridge between software supply chain security and quantum readiness. NIST standardized its first post-quantum algorithms in August 2024 (ML-KEM as FIPS 203 and ML-DSA as FIPS 204), and you cannot plan a migration for cryptography you have not inventoried. The CBOM is how the inventory gets built and kept current.
How Encryption Consulting Helps
Encryption Consulting’s CBOM Secure service extends software supply chain visibility into cryptography. It scans your environment for algorithms, keys, certificates, and protocols and produces a CycloneDX-format Cryptography Bill of Materials that sits alongside your existing SBOMs, so cryptographic risk becomes as visible as component risk. For the software you build and ship, CodeSign Secure protects the integrity end of the supply chain by centralizing code signing behind a FIPS 140-2 Level 2 HSM, so the artifacts your SBOM describes are also verifiably authentic and tamper-evident. Backed by ISO/IEC 27001:2022 and SOC 2 certified practices.
Frequently Asked Questions
What is a SBOM in simple terms?
A SBOM, or Software Bill of Materials, is a list of everything that goes into a piece of software: its own code plus all the third-party and open-source components it depends on, with versions and relationships. Think of it like an ingredients label for software. When a vulnerability is found in one ingredient, a SBOM lets an organization quickly see which of its products contain that ingredient and need attention.
What is the difference between a SBOM and a CBOM?
A SBOM inventories software components: libraries, packages, and their versions. A CBOM (Cryptography Bill of Materials) inventories cryptographic assets: algorithms, keys, certificates, and protocols. A CBOM extends the SBOM idea to answer a different question, which is not just what software you run but what cryptography it uses. CycloneDX can express both in the same document, and the CBOM is a foundational step toward post-quantum cryptography readiness.
Are SBOMs legally required?
It depends on jurisdiction and sector. In the US, federal SBOM policy shifted in 2025 and 2026: EO 14306 and OMB Memorandum M-26-05 moved agencies to a risk-based approach, so SBOMs are no longer uniformly mandated by a standard attestation form, though agencies may still require them contractually. In the EU, the Cyber Resilience Act introduces SBOM-related obligations for products with digital elements, phasing in through 2026 and 2027. The FDA requires SBOMs for certain medical device submissions.
What are the main SBOM formats?
The two dominant formats are CycloneDX and SPDX. CycloneDX, an OWASP project standardized as Ecma ECMA-424, originated with a security focus and supports multiple BOM types including cryptography (CBOM). SPDX, standardized as ISO/IEC 5962, originated with a license-compliance focus. Both are widely accepted, and most SBOM tooling can produce either format, so the practical choice often comes down to what a specific customer or regulator asks for.
How does a SBOM help with the SolarWinds or Log4Shell type of attack?
In both the 2020 SolarWinds attack and the 2021 Log4Shell vulnerability, the hardest early question for many organizations was simply whether they were affected and where. With SBOMs on file for their software, organizations can query for a specific component and version and immediately list every affected product. This turns a multi-week investigation into a fast lookup, which is the difference between contained and widespread impact during an active incident.
What is the connection between SBOMs and post-quantum cryptography?
Post-quantum migration requires knowing which cryptographic algorithms and key sizes are in use across your systems, because algorithms like RSA and ECDSA will need to be replaced with quantum-resistant standards such as ML-KEM (FIPS 203) and ML-DSA (FIPS 204). A Cryptography Bill of Materials (CBOM), which extends the SBOM concept to cryptographic assets, is how that inventory is built. Organizations already producing SBOMs can extend the same CycloneDX tooling to produce a CBOM.
Extend Supply Chain Security to Your Cryptography
A SBOM secures your software components. A CBOM secures the cryptography inside them, and it is the first step toward post-quantum readiness. See how CBOM Secure builds your cryptographic inventory, or explore CodeSign Secure to protect the integrity of the software you ship.
- Key Takeaways
- Why Software Supply Chain Security Matters
- What Goes Into an SBOM
- SBOM Formats: CycloneDX and SPDX
- The SBOM Regulatory Landscape in 2026
- The Direction of Travel
- How SBOMs Are Used in Practice
- From SBOM to CBOM: The Cryptography Connection
- How Encryption Consulting Helps
- Frequently Asked Questions
- Extend Supply Chain Security to Your Cryptography

---
*检索时间: 2026-07-24 15:24:20*
*搜索来源: DuckDuckGo*
