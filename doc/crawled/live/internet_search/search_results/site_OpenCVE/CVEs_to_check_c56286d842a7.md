# CVEs to check

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=userTag%3Atocheck
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | An issue in Code27 Companion Hub SQ3A.220705.003.A1 allows a physically proximate attacker to execute arbitrary code via the USB debugging (ADB) and Android Debug Bridge components | 
  
  
  
  | An OS command injection vulnerability exists in the start_bonjour() function of the "rc" binary in Cisco RV130/RV130W with firmware 1.0.3.55 and RV110W routers with firmware 1.2.2.5 / 1.2.2.8. The wan_hostname configuration parameter is not properly sanitized, which could allow an authenticated remote attacker to execute arbitrary OS commands with root privileges. | 
  
  
  
  | An OS command injection vulnerability exists in the save_syslog_to_file() function of the "httpd" binary in Cisco RV130/RV130W with firmware 1.0.3.55 and RV110W routers with firmware 1.2.2.5 / 1.2.2.8. The model_name configuration parameter is not properly sanitized, which could allow an authenticated remote attacker to execute arbitrary OS commands with root privileges. | 
  
  
  
  | An OS command injection vulnerability exists in the start_lltd() function of the "rc" binary in Cisco RV130/RV130W with firmware 1.0.3.55 and RV110W routers with firmware 1.2.2.5 / 1.2.2.8. The machine_name configuration parameter is not properly sanitized, which could allow an authenticated remote attacker to execute arbitrary OS commands with root privileges. | 
  
  
  
  | Incorrect authorization in the XML-RPC API of WebPros Plesk before 18.0.78.4 allows a low-privileged authenticated customer to look up domains they do not own, because ownership is enforced only for certain lookup filters and schema validation is bypassed for legacy protocol versions. This results in cross-tenant disclosure of other tenants' FTP credentials stored in cleartext, which can be leveraged to execute code as another tenant's system user. | 
  
  
  
  | Incorrect default permissions issue exists in Pupsman versions prior to 3.9.0. An attacker can place a malicious executable in the installation folder, which results in arbitrary code execution with SYSTEM privilege | 
  
  
  
  | Omnissa Workspace ONE® Tunnel for Windows addresses a  Local Privilege Escalation Vulnerability. | 
  
  
  
  | Dell PowerProtect Data Domain, versions 7.7.1.0 through 8.7, LTS2026 release version 8.6.1.0 through 8.6.1.10, LTS2025 release version 8.3.1.0 through 8.3.1.30, LTS2024 release versions 7.13.1.0 through 7.13.1.70 contain an Integer overflow or wraparound vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to denial of service. | 
  
  
  
  | Dell PowerProtect Data Domain, versions 7.7.1.0 through 8.7, LTS2026 release version 8.6.1.0 through 8.6.1.10, LTS2025 release version 8.3.1.0 through 8.3.1.30, LTS2024 release versions 7.13.1.0 through 7.13.1.70 contain an improper limitation of a pathname to a restricted directory ('path traversal') vulnerability. A high privileged attacker with remote access could potentially exploit this vulnerability, leading to unauthorized file modification. | 
  
  
  
  | Integer overflow in Extensions API in Google Chrome prior to 150.0.7871.115 allowed an attacker who convinced a user to install a malicious extension to perform an out of bounds memory read via a crafted Chrome Extension. (Chromium security severity: High) | 
  
  
  
  | Out of bounds read and write in Codecs in Google Chrome prior to 150.0.7871.115 allowed a remote attacker to potentially exploit heap corruption via a crafted video file. (Chromium security severity: High) | 
  
  
  
  | Use after free in Actor in Google Chrome prior to 150.0.7871.115 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High) | 
  
  
  
  | Inappropriate implementation in DOM in Google Chrome prior to 150.0.7871.115 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High) | 
  
  
  
  | The Brands for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'width' Shortcode Attribute in all versions up to, and including, 3.8.8 due to insufficient input sanitization and output escaping. This makes it possible for authenticated attackers, with contributor-level access and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. | 
  
  
  
  | Kernel software installed and running inside a Guest VM may post improper commands to the GPU Firmware to trigger a write of data outside the Guest's virtualised GPU memory.
Software installed and run under a Guest VM can send commands to the GPU which result in out of bounds memory accesses. These can be used to escalate privileges. | 
  
  
  
  | Kernel software installed and running inside a Guest VM may post improper commands to the GPU Firmware to trigger a write of data outside the Guest's virtualised GPU memory.
Out of bounds accesses triggered by malware introduced to a Guest KMD could allow privilege escalation which escapes virtualization boundaries. | 
  
  
  
  | Insufficient policy enforcement in Passwords in Google Chrome prior to 150.0.7871.115 allowed a remote attacker to bypass same origin policy via a crafted HTML page. (Chromium security severity: High) | 
  
  
  
  | decompress before 4.2.2 allows arbitrary hardlink creation during archive extraction, enabling file read disclosure and file corruption. When processing hardlink entries (type === 'link'), the x.linkname field from the archive is passed directly to fs.link() without validation (index.js line 113). An attacker can craft an archive with a hardlink entry whose linkname is an absolute path to any file on the same filesystem. This creates a hardlink inside the extraction directory that shares the same inode as the target file, enabling both reading and overwriting the original file's content. Hardlinks are limited to files on the same filesystem and cannot target directories. | 
  
  
  
  | Mercusys MW302R MW302R(EU)_V1_1.4.10 Build 231023 is vulnerable to Buffer Overflow in the administrative web interface. A stack buffer overflow vulnerability in the administrative web interface allows an authenticated attacker with administrative privileges to trigger a system crash by sending a specially crafted request. The vulnerability results in denial of service through control flow manipulation to an arbitrary instruction address. | 
  
  
  
  | Tenda CP3 V3.0 firmware V31.1.9.91 does not validate the Content-Length header field in RTSP requests (including DESCRIBE, SETUP, and PLAY methods). When a request carrying a Content-Length header is received without a corresponding message body, the RTSP parser enters a persistent body-awaiting state, causing the affected TCP connection to become permanently non-functional. The device does not actively close the connection, resulting in a TCP resource leak. This issue can be exploited by an unauthenticated remote attacker to cause a denial-of-service condition. |

---
*爬取时间: 2026-07-24 22:01:32*
*来源: 直接站点爬取*
