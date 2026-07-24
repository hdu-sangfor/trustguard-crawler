# High (CVSS 3.1)

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=cvss31%3E%3D7+AND+cvss31%3C9
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | Rapid7 InsightVM, Nexpose, and the Insight Agent execute discovered executables during authenticated assessment without validating file ownership, allowing a local low-privileged user to run code as the scan credential (Scan Engine) or as root/SYSTEM (Insight Agent). Fixed in Scan Engine content 1.1.3935 and Insight Agent content component 0.0.245.0. | 
  
  
  
  | Path traversal in Ivanti  Xtraction before version 2026.2.1 allows a remote authenticated attacker to read arbitrary files outside the web root. | 
  
  
  
  | In Roundcube Webmail before 1.6.17 and 1.7.x before 1.7.2, there is Stored Cross-Site Scripting (XSS) via a crafted plain-text email message. The attacker-controlled JavaScript executes within the victim's authenticated session simply by opening or previewing the message (zero-click). | 
  
  
  
  | A
DLL hijacking vulnerability exists in the GeoVision GV-IP Device Utility
desktop application. The application loads one or more dynamic-link libraries
(DLLs) from an unsafe search path, allowing a local attacker to place a
malicious DLL in a location searched before the legitimate library
location. | 
  
  
  
  | Dell ThinOS 10, versions prior to 2605_10.2100, contain an Obsolete Feature in UI vulnerability. A low privileged attacker with local access could potentially exploit this vulnerability, leading to Unauthorized access. | 
  
  
  
  | An issue was discovered in router/upnp/src/ssdp.c in DD-WRT before 45724. An unsafe strcpy in the UPnP handling functionality allows an unauthenticated remote attacker to send a request that would overflow an internal fixed buffer. Exploitation requires the DD-WRT user to enable UPnP (which is off by default, and only listens on internal interfaces by default). This occurs in ssdp_msearch (reachable by an M-SEARCH request). | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
ipv4: account for fraggap on the paged allocation path
In __ip_append_data(), when the paged-allocation branch is taken,
alloclen and pagedlen are computed as
	alloclen = fragheaderlen + transhdrlen;
	pagedlen = datalen - transhdrlen;
datalen already includes fraggap, but the fraggap bytes carried over
from the previous skb are copied into the new skb's linear area at
offset transhdrlen by the subsequent skb_copy_and_csum_bits(). The
linear area is therefore undersized by fraggap bytes while pagedlen is
overstated by the same amount.
The non-paged branch sets alloclen to fraglen, which already accounts
for fraggap because datalen does. Bring the paged branch in line by
adding fraggap to alloclen and subtracting it from pagedlen.
After this adjustment, copy no longer collapses to -fraggap on the
paged path, so remove the stale comment describing that old arithmetic. | 
  
  
  
  | AhnLab EPP Management v1.0.14.32-6249 was discovered to contain a NoSQL injection vulnerability via the eventlog/agentEvent/list endpoint. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
xfs: resample the data fork mapping after cycling ILOCK
xfs_reflink_fill_{cow_hole,delalloc} are both presented with an inode,
a data fork mapping, and a cow fork mapping.  Unfortunately, these two
helpers cycle the ILOCK to grab a transaction, which means that the
mappings are stale as soon as we reacquire the ILOCK.  Currently we
refresh the cow fork mapping by re-calling xfs_find_trim_cow_extent, but
we don't refresh the data fork mapping beforehand, which means that the
xfs_bmap_trim_cow in that function queries the refcount btree about the
wrong physical blocks and returns an inaccurate value in *shared.
If *shared is now false, the directio write proceeds with a stale data
fork mapping.  Fix this by querying the data fork mapping if the
sequence counter changes across the ILOCK cycle. | 
  
  
  
  | In OpenStack Ironic Python Agent through 11.6.0, a project-scoped user with the manager role can achieve arbitrary code execution on a running Ironic-Python-Agent via a maliciously constructed configuration, because the value of ntp_server is passed to a shell. | 
  
  
  
  | FlareSolverr before version 3.4.7 contains a server-side request forgery (SSRF) vulnerability in the /v1 API endpoint. This allows a remote attacker to obtain sensitive information | 
  
  
  
  | Use after free in Ozone in Google Chrome on Linux prior to 150.0.7871.128 allowed a remote attacker who convinced a user to engage in specific UI gestures to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High) | 
  
  
  
  | Use after free in Aura in Google Chrome prior to 150.0.7871.128 allowed a local attacker to potentially exploit heap corruption via a malicious file. (Chromium security severity: High) | 
  
  
  
  | Directory traversal vulnerability in knowns-dev/knowns 0.11.4 via crafted folder name value to the create_doc tool. | 
  
  
  
  | An issue in DayuanJiang next-ai-draw-io 0.4.13 allows a remote attacker to obtain sensitive information via the x-ai-provider component | 
  
  
  
  | Cross Site Scripting vulnerability in DayuanJiang next-ai-draw-io 0.4.13 allows a remote attacker to execute arbitrary code via the mcp parameter | 
  
  
  
  | An issue in exo-explore exo 1.0.69 allows a remote attacker to escalate privileges via the GET /state and DELETE /instance/{instance_id} endpoints with no authentication. | 
  
  
  
  | Multiple security vulnerabilities in Snowflake libsnowflakeclient versions prior to 2.9.2 could allow remote code execution and credential exfiltration. A stack-based buffer overflow in the file download path could allow remote code execution on a victim host. An attacker could exploit this by uploading a file with a crafted encryption metadata field to a shared internal stage that a victim process later downloads, and impact would be limited to deployments where principals with different privilege levels share the same internal stage. A related out-of-bounds write in the same download path could allow memory corruption with attacker-controlled write primitives. An attacker may exploit this through a crafted initialization vector metadata field on a shared stage, and impact would be limited by the same stage-write precondition. Improper validation of connection parameters could allow an attacker-controlled input to redirect outbound authentication requests — including credentials and tokens — to an attacker-controlled endpoint. Impact is limited to embedding deployments where a lower-privileged principal can influence connection configuration while higher-privileged service credentials are in use. The fix is available in Snowflake libsnowflakeclient version 2.9.2. Users must manually upgrade. | 
  
  
  
  | Exim before 4.99.5 allows .forward privilege escalation because force_command for a pipe transport is mishandled. | 
  
  
  
  | Exim before 4.99.5 allows directory traversal to access files outside of the spool area, and consequently gain privileges, because arguments related to queue-name are mishandled. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
