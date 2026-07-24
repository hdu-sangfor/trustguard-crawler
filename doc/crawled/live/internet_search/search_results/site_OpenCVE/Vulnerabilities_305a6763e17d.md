# Vulnerabilities

### 来源信息
- **URL**: https://www.opencve.io/cve/
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | The SCORM lab launch endpoint in Skillable (scorm.skillable.com) through 2026-07-13 does not validate the client-supplied userId parameter against the authenticated SCORM session token. An authenticated user can substitute arbitrary userId values to bypass per-user lab launch rate limits and consume other users' lab allocations, resulting in denial of service against targeted users' lab and exam access. Skillable was formerly named Learn on Demand Systems. | 
  
  
  
  | The SureForms  WordPress plugin before 2.11.1 does not properly validate the payment amount on forms that use a dynamically-sourced (variable/hidden) payment amount, allowing unauthenticated users to underpay for the configured product or subscription. Forms using a fixed configured price are not affected. | 
  
  
  
  | In Eclipse BaSyx Java Server SDK versions 2.0.0-milestone-05 to 2.0.0-milestone-12, deployments using the MongoDB backend are vulnerable to an unauthenticated arbitrary file write through the AAS thumbnail API.
The AAS thumbnail upload path accepted a client-controlled fileName request parameter and passed it through repository file handling as both a repository key and, during thumbnail retrieval, a local filesystem path. With the MongoDB file repository, the supplied filename was treated as an opaque GridFS key and was not normalized or restricted as a filesystem path. A remote attacker could upload thumbnail content using an absolute or traversal-style filename, then trigger thumbnail retrieval so that the uploaded bytes were written to the attacker-chosen path on the server filesystem.
This could allow writing files anywhere the Java process has permission to write and may lead to remote code execution. The default InMemory backend is not affected by this specific path because it normalizes and restricts file paths to its temporary directory.
The issue is fixed in Eclipse BaSyx Java Server SDK 2.0.0-milestone-13. | 
  
  
  
  | Eclipse Grizzly in versions before 5.0.2, cannot properly parse the trailer section in malformed trailer header's line, which can be leveraged to perform HTTP request smuggling. | 
  
  
  
  | In Eclipse Jetty, for HTTP/1, HTTP/2 and HTTP/3 requests, there is no strict check that the request authority (host and port) matches what provided in the Host header (if present).
This was not enforced in earlier HTTP RFC (for example, in RFC 2616), but it is in the latest RFC (9110 and 9112).
This mismatch can cause a number of problems that may be classified as vulnerabilities such as:
  *  
  
  URI constructions (for example, for redirects -- this is typical for login pages)
  *  
  
  Virtual host selection
  *  
  
  Reverse proxying
  *  
  
  Misleading logs
  *  
  
  Etc.
Given that the latest RFCs require that request authority and Host header must match, Jetty should enforce this invariant. | 
  
  
  
  | A vulnerability has been identified in Opcenter X (All versions < V2604). Affected applications do not properly validate the algorithm specified in the JSON Web Token (JWT) header.
This could allow an unauthenticated remote attacker to forge arbitrary JWT, bypass authentication mechanisms and impersonate any user including administrative accounts, potentially gaining full unauthorized access to the application. | 
  
  
  
  | An attacker with access to an HX 10.0.0  and previous versions, may send specially-crafted data to the HX console. The malicious detection would then trigger decompression of a large file that consumes an excessive amount of system resources thus causing a Denial of Service. | 
  
  
  
  | Rapid7 InsightVM, Nexpose, and the Insight Agent execute discovered executables during authenticated assessment without validating file ownership, allowing a local low-privileged user to run code as the scan credential (Scan Engine) or as root/SYSTEM (Insight Agent). Fixed in Scan Engine content 1.1.3935 and Insight Agent content component 0.0.245.0. | 
  
  
  
  | The ProfileGrid  WordPress plugin before 5.9.9.7 does not verify PayPal IPN notifications before granting paid group membership, allowing unauthenticated attackers to forge a payment notification and mark any user as a paid member of any group without any payment being made. | 
  
  
  
  | The ProfileGrid  WordPress plugin before 5.9.9.7 does not perform any authorization or ownership check on some of its private-message thread actions, allowing authenticated users with Subscriber-level access and above to soft-delete, tamper with the metadata of, and mark as read other users' private message threads. | 
  
  
  
  | The ProfileGrid  WordPress plugin before 5.9.9.7 does not perform a capability check on its license management actions, relying only on a nonce that is exposed to any logged-in user, allowing authenticated users with Subscriber-level access and above to overwrite the site's premium license settings. | 
  
  
  
  | Joomla Extension - phoca.cz - Reflected XSS vulnerability in Phoca Guestbook 5.0.0-6.1.0 - Improper validation of user inputs lead to a reflective XSS vulnerability. | 
  
  
  
  | Joomla Extension - phoca.cz - Reflected XSS vulnerability in Phoca Maps 5.0.0-6.0.4 - Improper validation of user inputs lead to a reflective XSS vulnerability. | 
  
  
  
  | Path traversal in Ivanti  Xtraction before version 2026.2.1 allows a remote authenticated attacker to read arbitrary files outside the web root. | 
  
  
  
  | A improper certificate validation vulnerability in Fortinet FortiClientEMS 7.4.3 through 7.4.5, FortiClientEMS 7.4.0 through 7.4.1, FortiClientEMS 7.2 all versions may allow attacker to information disclosure via <insert attack vector here> | 
  
  
  
  | An Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting') vulnerability [CWE-113] vulnerability in Fortinet FortiOS 7.6.0 through 7.6.4, FortiOS 7.4 all versions, FortiOS 7.2 all versions, FortiProxy 7.6.0 through 7.6.4, FortiProxy 7.4 all versions, FortiProxy 7.2 all versions may allow an attacker able to intercept and modify a user's captive portal authentication request to inject arbitrary headers via crafted HTTP requests. | 
  
  
  
  | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiOS 7.6.0 through 7.6.6, FortiOS 7.4.0 through 7.4.9, FortiOS 7.2 all versions, FortiOS 7.0 all versions, FortiOS 6.4 all versions, FortiPAM 1.8.0, FortiPAM 1.7.0 through 1.7.2, FortiPAM 1.6 all versions, FortiPAM 1.5 all versions, FortiPAM 1.4 all versions, FortiPAM 1.3 all versions, FortiPAM 1.2 all versions, FortiPAM 1.1 all versions, FortiPAM 1.0 all versions, FortiProxy 7.6.0 through 7.6.5, FortiProxy 7.4 through 7.4.13, FortiProxy 7.2 all versions, FortiProxy 7.0 all versions may allow attacker to execute unauthorized code or commands via <insert attack vector here> | 
  
  
  
  | A buffer over-read vulnerability in Fortinet FortiOS 7.6.0 through 7.6.3, FortiOS 7.4.0 through 7.4.8, FortiOS 7.2 all versions, FortiOS 7.0 all versions, FortiOS 6.4 all versions may allow an authenticated remote attacker to return a portion of device memory in the redirect response via submitting a specially crafted request. | 
  
  
  
  | A buffer over-read vulnerability in Fortinet FortiOS 7.6.0 through 7.6.3, FortiOS 7.4.0 through 7.4.8, FortiOS 7.2 all versions, FortiOS 7.0 all versions, FortiOS 6.4 all versions, FortiProxy 7.6.0 through 7.6.5, FortiProxy 7.4.0 through 7.4.13, FortiProxy 7.2 all versions, FortiProxy 7.0 all versions may allow attacker to information disclosure via <insert attack vector here> | 
  
  
  
  | In Roundcube Webmail before 1.6.17 and 1.7.x before 1.7.2, the TNEF decoder was subject to denial of service via a crafted compressed-RTF size. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
