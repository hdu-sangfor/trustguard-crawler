# Microsoft tightens Windows enterprise activation security

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/24/microsoft-kms-tpm-security-update/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
Microsoft tightens Windows enterprise activation security
Microsoft is making Trusted Platform Module (TPM)-backed attestation a requirement for Windows Key Management Service (KMS), the on-premises service used for Windows volume activation, replacing the software-only trust model with hardware-backed verification to strengthen enterprise activation security.
Attestation will become mandatory with the next Windows Server Long-Term Servicing Channel (LTSC) release.
How TPM-backed KMS attestation works
The KMS server uses its TPM to generate an attestation report proving its identity and integrity before activation is completed. The process creates a cryptographic chain of trust between Windows clients and the KMS host, reducing the risk of a KMS server being copied or impersonated.
Preparing KMS for hardware-backed trust
Microsoft is advising organizations to prepare their KMS environments for the transition to hardware-backed trust. Administrators should identify all KMS servers, verify that physical hosts support TPM and are certified for Windows Server, and confirm that TPM attestation is available. Guidance for virtual KMS hosts will be published later.
A successful “Key Attestation” response confirms TPM attestation support (Source: Microsoft)
Organizations should determine whether hardware upgrades are required to support the new security model, share migration plans with IT teams, and monitor Microsoft’s rollout schedule.
“Starting August 2026, Windows Server 2025 will provide readiness messaging to help administrators assess whether a KMS host is ready for hardware-based security, giving teams time to plan upgrades before enforcement begins,” Monika Kumar, Senior Program Manager at Microsoft, explained.

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
