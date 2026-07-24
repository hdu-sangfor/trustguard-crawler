# The Ultimate SBOM Compliance Guide (2026) | Sbomify

### 来源信息
- **URL**: https://sbomify.com/compliance/
- **域名**: sbomify.com
- **检索关键词**: software supply chain security SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
In the US, Executive Order 14028 and NTIA minimum elements set the baseline; CISA's 2025 draft adds hash and license fields. In the EU, the Cyber Resilience Act legally requires SBOMs for digital products, while NIS2 mandates supply chain security.

### 页面正文
SBOM compliance requirements vary by jurisdiction and industry. In the US, Executive Order 14028 and NTIA minimum elements set the baseline; CISA's 2025 draft adds hash and license fields. In the EU, the Cyber Resilience Act legally requires SBOMs for digital products, while NIS2 mandates supply chain security. The UK's Software Security Code of Practice offers voluntary guidance. Use CycloneDX or SPDX format – both are widely accepted across all frameworks.
New to SBOMs? Start with What is an SBOM? to learn the basics, or explore our SBOM generation guides for language-specific tutorials.
Software Bill of Materials (SBOM) compliance requirements are rapidly evolving across the United States and European Union. Whether you’re navigating the NTIA minimum elements, preparing for the EU Cyber Resilience Act (CRA), meeting NIS2 Directive obligations, or submitting medical devices to the FDA, this guide provides a comprehensive reference for SBOM requirements across all major frameworks.
Feeling overwhelmed? If all these frameworks, acronyms, and requirements look like gibberish, you're not alone. SBOM compliance can be complex, but you don't have to figure it out on your own.
Get Help With ComplianceDisclaimer: This page represents our interpretation of the referenced frameworks and standards. While we strive for accuracy, we may have made errors or omissions. This content is provided for informational purposes only and does not constitute legal advice. For compliance decisions, consult the official source documents and seek qualified legal counsel.
Compliance Frameworks
US Frameworks
- Executive Order 14028 (2021) - The binding US directive that kicked off federal SBOM adoption. Updated: OMB Memorandum M-26-05 (January 2026) rescinded the mandatory attestation memos (M-22-18, M-23-16), shifting to an agency-led, risk-based approach. EO 14028 itself remains in effect. - Who it affects: US federal agencies and software vendors selling to the government
 
- NTIA Minimum Elements (2021) - The foundational US baseline for SBOM data fields - Who it affects: Software producers selling into federal or critical-infrastructure supply chains. Referenced by FDA, CISA, and other frameworks as the baseline.
 
- CISA Minimum Elements (2025 Draft) - Updated US guidance with new fields for hash, license, and generation context - Who it affects: Organizations in US public-sector and critical-infrastructure contexts
 
- FDA Medical Device Guidance (2025) - Healthcare sector SBOM requirements with lifecycle properties - Who it affects: Medical device manufacturers and their software suppliers
 
- NIST SP 800-53 Rev 5 - Federal security control catalog with supply chain risk management controls - Who it affects: US federal agencies and organizations subject to FISMA
 
- NIST SP 800-171 Rev 3 - CUI protection requirements for nonfederal systems - Who it affects: DoD contractors and organizations handling Controlled Unclassified Information (CUI)
 
EU Frameworks
- EU Cyber Resilience Act (CRA) - Binding EU law requiring SBOMs for products with digital elements - Who it affects: Manufacturers, importers, and distributors placing digital products on the EU market
 
- EU NIS2 Directive - EU cybersecurity law for essential and important entities - Who it affects: EU entities responsible for cybersecurity risk management and incident reporting
 
- BSI TR-03183-2 (v2.1.0) - German Federal Office for Information Security technical guideline defining concrete SBOM format and content requirements aligned with the EU CRA - Who it affects: Manufacturers placing products with digital elements on the EU market, and vendors selling into German federal procurement
 
UK Frameworks
- Software Security Code of Practice (UK, May 2025) - Voluntary UK government code setting baseline secure software development, supply chain resilience, and customer communication expectations- Who it affects: Organisations that develop and/or sell software to businesses or other organisations (especially B2B/proprietary software vendors and SaaS)
 
Industry Standards
- PCI DSS 4.0 - Payment card industry software component inventory requirements- Who it affects: Merchants and service providers handling cardholder data
 
Reference Documents
- CISA Framing Document (3rd Edition) - Baseline attribute definitions and format normalization - Who it affects: SBOM producers/consumers needing shared terminology and format crosswalk
 
- CISA SBOM Sharing Lifecycle Report - Operational guidance for SBOM distribution - Who it affects: Organizations distributing or retrieving SBOMs across supply chains
 
Technical Resources
- Schema Crosswalk: CycloneDX and SPDX - Complete field mappings for CycloneDX 1.7, SPDX 2.3, and SPDX 3.0 
- CLE: Common Lifecycle Enumeration - Standard for machine-readable component lifecycle events (EOL, EOS) 
Master Requirements Comparison
This table compares SBOM data field expectations across major frameworks. All frameworks assume machine-readable SBOMs in a commonly used format (e.g., CycloneDX, SPDX).
Framework context:
- EO 14028 is a binding US Executive Order for federal agencies and influences procurement expectations for software suppliers
- NTIA 2021 and CISA 2025 are US guidance documents (not law)
- NIST 800-53 is the federal security control catalog; NIST 800-171 applies to nonfederal organizations handling CUI
- CRA and NIS2 are binding EU legislation
- FDA 2025 is guidance for medical device premarket submissions
- PCI DSS 4.0 is an industry standard for payment card security
- UK SSCoP 2025 is voluntary UK government guidance for software vendors
| Property | EO 14028 | NTIA 2021 | CISA 2025 | CRA | NIS2 | FDA 2025 | PCI DSS 4.0 | UK SSCoP 2025 | 
|---|---|---|---|---|---|---|---|---|
| Document-Level Metadata | ||||||||
| SBOM Author | - | ✓ | ✓ | - | - | ✓ | - | - | 
| Timestamp | - | ✓ | ✓ | - | - | ✓ | - | - | 
| Tool Name/Version | - | - | ✓ | - | - | - | - | - | 
| Generation Context | - | - | ✓ | - | - | - | - | - | 
| Component Identification | ||||||||
| Supplier / Software Producer | - | ✓ | ✓ | - | - | ✓ | - | - | 
| Component Name | - | ✓ | ✓ | - | ● | ✓ | - | - | 
| Component Version | - | ✓ | ✓ | - | ● | ✓ | - | - | 
| Unique Identifiers (purl/CPE) | - | ✓ | ✓ | - | - | ✓ | - | - | 
| Component Hash | - | - | ✓ | - | - | - | - | - | 
| Relationships | ||||||||
| Dependency Relationship | ● | ✓ | ✓ | ✓* | - | ✓ | - | - | 
| Legal | ||||||||
| License | - | - | ✓ | - | - | - | - | - | 
| Lifecycle | ||||||||
| Support Level | - | - | - | - | - | ✓ | - | ✓‡ | 
| End-of-Support Date | - | - | - | - | - | ✓ | - | ✓‡ | 
| Process / Access | ||||||||
| SBOM provision to purchasers | ✓ | - | - | - | - | - | - | - | 
| SBOM production required | - | - | - | ✓ | - | - | ✓† | - | 
| Authority access on request | - | - | - | ● | - | - | - | - | 
| User access location disclosure | - | - | - | ● | - | - | - | - | 
| Supply chain security measures | ✓ | - | - | - | ✓ | - | ✓† | ✓‡ | 
| Vulnerability handling process | ✓ | - | - | - | ✓ | - | ✓† | ✓‡ | 
Legend:
- ✓ = Expected (NTIA/CISA minimum element, FDA recommended, EO 14028/NIS2 required)
- ✓* = CRA requires at least top-level (direct) dependencies
- ✓† = PCI DSS Req 6.3.2 (best practice until 31 Mar 2025, then required)
- ✓‡ = UK SSCoP voluntary guidance (not as SBOM fields, but as customer-facing expectations)
- ● = Conditional or implied (EO 14028: SBOM must include “supply chain relationships”; CRA: where applicable; NIS2: for in-scope entities per Regulation 2024/2690)
- - = Not specified by this framework
Important notes:
- EO 14028 requires SBOM provision in federal procurement but defers field-level requirements to NTIA minimum elements. Note: OMB M-26-05 (January 2026) rescinded the mandatory attestation memos (M-22-18, M-23-16), making vendor attestations optional and shifting to agency-led risk-based assurance. EO 14028’s core SBOM and supply chain provisions remain in effect
- NTIA 2021 and CISA 2025 define “minimum elements” as guidance, not legal requirements
- NTIA 2021 discusses license information as a key SBOM use case and useful content, but it is not listed among the minimum SBOM data fields
- CISA 2025 is a public comment draft and explicitly does not create new requirements
- FDA uses “should” language (recommendations for premarket submissions)
- CRA is binding law but does not specify individual data fields beyond dependency scope
- NIS2 does not mandate SBOMs by name, but the implementing regulation (2024/2690) requires “information describing the hardware and software components used” for in-scope entities
- PCI DSS 4.0 requires software component inventories for bespoke/custom software (Req 6.3.2) to facilitate vulnerability and patch management
- UK SSCoP 2025 is voluntary guidance; it does not mandate SBOMs by name but expects software composition awareness, vulnerability management, and customer lifecycle communication
Frequently Asked Questions
What is SBOM compliance?
SBOM compliance refers to meeting the requirements set by various government regulations and industry standards for creating, maintaining, and sharing Software Bills of Materials. Key frameworks include the US NTIA minimum elements, the EU Cyber Resilience Act, and sector-specific requirements like FDA medical device guidance.
Is an SBOM legally required?
It depends on your jurisdiction and industry. In the EU, the Cyber Resilience Act legally requires SBOMs for products with digital elements. In the US, SBOMs are required for software sold to the federal government (per Executive Order 14028) and recommended for FDA medical device submissions. The NIS2 Directive requires supply chain security measures that SBOMs help evidence.
What format should my SBOM be in?
Both CycloneDX and SPDX are widely accepted. The EU CRA requires a “commonly used and machine-readable format,” and both formats qualify. See our schema crosswalk for field mappings between formats.
What are the minimum SBOM fields required?
The NTIA minimum elements define seven baseline fields: Supplier Name, Component Name, Version, Unique Identifiers, Dependency Relationship, SBOM Author, and Timestamp. The CISA 2025 draft adds Component Hash, License, Tool Name, and Generation Context.
How do I generate an SBOM?
See our comprehensive SBOM generation guides covering Python, JavaScript, Java, Go, Rust, and 10+ other languages and platforms. For a list of tools, visit our SBOM resources page.
Additional Resources
Official Source Documents:
- Executive Order 14028 – Improving the Nation’s Cybersecurity (2021)
- NTIA Minimum Elements for a Software Bill of Materials (2021)
- CISA 2025 Minimum Elements (Public Comment Draft)
- CISA Framing Software Component Transparency (3rd Edition)
- CISA SBOM Sharing Lifecycle Report
- EU Cyber Resilience Act (Regulation 2024/2847)
- EU NIS2 Directive (Directive 2022/2555)
- PCI DSS v4.0.1 (June 2024)
- NIST SP 800-53 Rev 5 (September 2020, updated December 2024)
- NIST SP 800-171 Rev 3 (May 2024)
- Software Security Code of Practice (UK Government, May 2025)
- CLE Specification (ECMA-428)
Related sbomify Resources:
- What is an SBOM? - Introduction to Software Bills of Materials
- SBOM Generation Guides - Language and platform-specific tutorials
- SBOM Resources & Tools - Comprehensive tool directory

---
*检索时间: 2026-07-24 21:32:58*
*搜索来源: DuckDuckGo*
