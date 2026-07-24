# Critical (CVSS 4.0)

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=cvss40%3E%3D9
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | An unrestricted upload of file with dangerous type vulnerability in the e-paper draft upload function of SUNNET Corporate Training Management System through v10.3 allows remote authenticated users with administrator privileges to execute arbitrary commands by uploading a crafted ZIP archive containing a server-executable file. | 
  
  
  
  | A vulnerability has been identified in Opcenter X (All versions < V2604). Affected applications do not properly validate the algorithm specified in the JSON Web Token (JWT) header.
This could allow an unauthenticated remote attacker to forge arbitrary JWT, bypass authentication mechanisms and impersonate any user including administrative accounts, potentially gaining full unauthorized access to the application. | 
  
  
  
  | An authenticated non-admin user can exploit a SQL injection flaw in the ticketing REST API to access sensitive data stored in the appliance database. | 
  
  
  
  | The affected product is vulnerable to a heap-based buffer overflow via a crafted MMS Initiate request. Remote code execution (RCE) has been demonstrated when ASLR is disabled; memory corruption or denial of service may occur in configurations where ASLR is enabled. | 
  
  
  
  | Cal.com (calcom/cal.diy) before 5.9.9 is vulnerable to unauthenticated remote code execution because it bundles a version of Next.js whose React Server Components (RSC) request handling deserializes attacker-controlled input. A remote attacker can send a crafted RSC request to the server and cause arbitrary code to be executed during server-side processing, without authentication or user interaction. The flaw derives from the upstream Next.js vulnerability CVE-2025-55182 and is resolved in 5.9.9 by updating the affected dependency. | 
  
  
  
  | 9router 0.4.59 (fixed in 0.4.60) contains a chain of vulnerabilities: a hardcoded default password (123456) that authenticates any fresh installation, a bypass of the LOCAL_ONLY network gate via a spoofed Host header, and unvalidated arguments passed to child_process.spawn() when registering MCP plugins. A remote, unauthenticated attacker can log in with the default credential, spoof the Host header to reach local-only routes, and register a malicious MCP plugin (e.g. node -e <payload>) to achieve arbitrary code execution on the host operating system when the plugin's SSE endpoint is triggered. | 
  
  
  
  | DbGate is cross-platform database manager. Versions 7.1.8 and prior are vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`. Version 7.1.9 contains a patch. | 
  
  
  
  | DbGate is cross-platform database manager. In versions 7.1.8 and prior, the `unzipDirectory()` function in `packages/api/src/shell/unzipDirectory.js` (line 27) does not validate that extracted file paths stay within the output directory. A malicious ZIP with `../` entries writes files anywhere on the filesystem. In the default Docker deployment, DbGate runs as root and the `none` auth provider issues JWT tokens without credentials via `POST /auth/login`, so this is exploitable by any network-adjacent attacker. Version 7.1.9 fixes the issue. | 
  
  
  
  | Cal.com (repository calcom/cal.diy) in versions <= 4.7.15 is vulnerable to cross-site scripting (XSS) on the publicly accessible single booking view (e.g., /booking/<id>). Booking question (form field) labels are rendered via React's dangerouslySetInnerHTML without proper input sanitization or CSP, so an attacker who can create an event type with a malicious booking question label can inject arbitrary HTML/JavaScript that executes when a victim visits the booking view URL. Self-hosted instances with open registration are particularly at risk. The issue is fixed in version 4.7.16. | 
  
  
  
  | Cal.com (calcom/cal.diy) versions through 4.7.15 contain a stored cross-site scripting vulnerability. The single booking view (e.g., https://app.cal.com/booking/<id>) renders booking-question field labels via React's dangerouslySetInnerHTML without sanitizing or escaping user input. An attacker who can create an event type with a malicious booking-question label can inject arbitrary HTML/JavaScript that executes when a victim opens the crafted booking URL. The issue is fixed in v4.7.16. | 
  
  
  
  | The SAP Cloud Application Programming Model is a tool for building enterprise-grade cloud applications, and cap-js/cds-dbs is the monorepo for SQL database services for that tool. On April 29, 2026, compromised versions of `@cap-js/sqlite@2.2.2`, `@cap-js/postgres@2.2.2`, and `@cap-js/db-service@2.10.1` were published. The malicious packages harvested credentials and attempted self-propagation. If a compromised version was installed, all credentials accessible on that machine (npm tokens, cloud provider credentials, SSH keys, GitHub PATs) should be considered compromised. User should upgrade to `@cap-js/sqlite` >= 2.4.0, `@cap-js/postgres` >= 2.3.0, `@cap-js/db-service` >= 2.11.0. If a compromised version was ever installed, rotate all affected credentials. No known workarounds are available. | 
  
  
  
  | stoatchat before 0.13.5 contains an unauthenticated server-side request forgery vulnerability in the /proxy and /embed endpoints that accept arbitrary URLs without DNS resolution filtering or private IP range validation. Attackers can enumerate internal services, fingerprint applications, and reach instance metadata endpoints by supplying malicious URLs or leveraging redirect chains to access internal infrastructure. | 
  
  
  
  | The Microsoft 365 and Microsoft Entra ID Plugins for Moodle provide Office 365 and Azure Active Directory integration for Moodle. Prior to 4.5.6, 5.0.5, and 5.1.1, the Microsoft Office 365 Integration plugin local_o365 Teams SSO endpoint sso_login.php base64-decodes a JWT payload and authenticates users from the upn claim without verifying the JWT signature, allowing an unauthenticated attacker to forge a token and obtain a Moodle session as an O365-authenticated user. This issue is fixed in versions 4.5.6, 5.0.5, and 5.1.1. | 
  
  
  
  | Grafana OnCall through 1.16.11 contains an unauthenticated access vulnerability that allows remote attackers to obtain a valid PluginAuthToken by sending a POST request to the internal plugin install endpoint using hardcoded default stack_id and org_id values present in the public source tree. Attackers can leverage the acquired token to authenticate against all internal API endpoints, create arbitrary Admin users via the user-context header bootstrap path, revoke the legitimate plugin token, and redirect OnCall-to-Grafana API calls to an attacker-controlled host by overwriting the organization's grafana_url and api_token. | 
  
  
  
  | Frogman provides headless PBX control through MCP and HTTP API. Prior to 1.6.3, PERM_READ access was sufficient to call fm_list_managers, fm_list_pinsets, fm_show_context, fm_get_mcp_config, fm_backup_status, fm_whos_calling, fm_run_saved_query, and fm_diagnose_trunk, exposing AMI manager secrets, outbound dial PINs, full Asterisk dialplan context, root SSH connection commands, backup artifact paths, CDR history, arbitrary saved GraphQL query execution, and raw AMI endpoint dumps containing SIP fields such as password, md5_cred, and oauth_secret. This issue is fixed in version 1.6.3. | 
  
  
  
  | Jupyter Enterprise Gateway launches remote Jupyter Notebook kernels across distributed clusters like Apache Spark, Kubernetes, and Docker Swarm. In versions 2.0.0rc2 and above, prior to 3.3.0, the environment variables (KERNEL_XXX) used during the rendering of the Kubernetes manifest are vulnerable to Server Side Template Injection (SSTI). By including Jinja2 template expressions it is possible to execution Python code and OS Commands in the Enterprise Gateway service. The code can use or steal the Kubernetes service account token, which can steal Kubernetes secrets and be used to fully compromise the Kubernetes cluster by scheduling a privileged pod or a pod with a hostPath volume mount. This issue has been fixed in version 3.3.0. | 
  
  
  
  | Jupyter Enterprise Gateway launches remote Jupyter Notebook kernels across distributed clusters like Apache Spark, Kubernetes, and Docker Swarm. In versions prior to 3.3.0, the server interpolates untrusted environment variables (e.g., KERNEL_XXX) into Kubernetes manifests without YAML-aware escaping, enabling YAML injection attacks. Attackers can inject new fields, overwrite critical fields (e.g., duplicate securityContext keys, where the last one prevails), and inject document boundaries (--- for new documents, ... for end-of-document) to generate multiple resources, potentially creating arbitrary types, such as privileged pods. The Jinja2 template for the Kubernetes manifest contains several kernel_xxx variables, such as kernel_working_dir that are used when rendering the manifest and are all vectors for YAML injection. This issue has been fixed in version 3.3.0. | 
  
  
  
  | clawvet self-hosted API server (apps/api) before 0.7.5 hard-codes a fallback JWT secret ('clawvet-dev-secret-change-me') in auth.ts and ships it as the default in .env.example. Because GET /api/v1/scans returns scan records containing userId values without authentication, a remote unauthenticated attacker can harvest a victim's userId, forge a valid HS256 cg_session cookie offline using the known secret, and call GET /api/v1/auth/me to obtain the victim's email address, subscription plan, and secret apiKey. The published clawvet npm package (CLI only) is not affected. | 
  
  
  
  | Pronetiqs IntraVUE versions 3.2.1a14 and prior have an unintended proxy or intermediary vulnerability which could allow an attacker to use an active proxy, which would bypass OT segmentation. | 
  
  
  
  | Pronetiqs IntraVUE versions 3.2.1a14 and prior have an exposure of sensitive system information to an unauthorized control sphere vulnerability which could expose the underlying host/share filesystem. |

---
*爬取时间: 2026-07-24 22:01:32*
*来源: 直接站点爬取*
