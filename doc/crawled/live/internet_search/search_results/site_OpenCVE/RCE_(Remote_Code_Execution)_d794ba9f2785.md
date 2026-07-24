# RCE (Remote Code Execution)

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=description%3A%27remote+code+execution%27
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | In Eclipse BaSyx Java Server SDK versions 2.0.0-milestone-05 to 2.0.0-milestone-12, deployments using the MongoDB backend are vulnerable to an unauthenticated arbitrary file write through the AAS thumbnail API.
The AAS thumbnail upload path accepted a client-controlled fileName request parameter and passed it through repository file handling as both a repository key and, during thumbnail retrieval, a local filesystem path. With the MongoDB file repository, the supplied filename was treated as an opaque GridFS key and was not normalized or restricted as a filesystem path. A remote attacker could upload thumbnail content using an absolute or traversal-style filename, then trigger thumbnail retrieval so that the uploaded bytes were written to the attacker-chosen path on the server filesystem.
This could allow writing files anywhere the Java process has permission to write and may lead to remote code execution. The default InMemory backend is not affected by this specific path because it normalizes and restricts file paths to its temporary directory.
The issue is fixed in Eclipse BaSyx Java Server SDK 2.0.0-milestone-13. | 
  
  
  
  | Multiple security vulnerabilities in Snowflake libsnowflakeclient versions prior to 2.9.2 could allow remote code execution and credential exfiltration. A stack-based buffer overflow in the file download path could allow remote code execution on a victim host. An attacker could exploit this by uploading a file with a crafted encryption metadata field to a shared internal stage that a victim process later downloads, and impact would be limited to deployments where principals with different privilege levels share the same internal stage. A related out-of-bounds write in the same download path could allow memory corruption with attacker-controlled write primitives. An attacker may exploit this through a crafted initialization vector metadata field on a shared stage, and impact would be limited by the same stage-write precondition. Improper validation of connection parameters could allow an attacker-controlled input to redirect outbound authentication requests — including credentials and tokens — to an attacker-controlled endpoint. Impact is limited to embedding deployments where a lower-privileged principal can influence connection configuration while higher-privileged service credentials are in use. The fix is available in Snowflake libsnowflakeclient version 2.9.2. Users must manually upgrade. | 
  
  
  
  | An authenticated path traversal vulnerability exists in AOS-CX. Successful exploitation of this vulnerability allows an attacker to copy arbitrary files to a user readable location from the command line interface of the underlying operating system, which could lead to remote code execution. | 
  
  
  
  | The affected product is vulnerable to a heap-based buffer overflow via a crafted MMS Initiate request. Remote code execution (RCE) has been demonstrated when ASLR is disabled; memory corruption or denial of service may occur in configurations where ASLR is enabled. | 
  
  
  
  | Cal.com (calcom/cal.diy) before 5.9.9 is vulnerable to unauthenticated remote code execution because it bundles a version of Next.js whose React Server Components (RSC) request handling deserializes attacker-controlled input. A remote attacker can send a crafted RSC request to the server and cause arbitrary code to be executed during server-side processing, without authentication or user interaction. The flaw derives from the upstream Next.js vulnerability CVE-2025-55182 and is resolved in 5.9.9 by updating the affected dependency. | 
  
  
  
  | DbGate is cross-platform database manager. In versions 7.1.8 and prior, DbGate's JSON script runner (`POST /runners/start`) allows remote code execution via code injection in the `functionName` parameter of JSON script `assign` commands. The `functionName` value is interpolated directly into dynamically generated JavaScript source code via string concatenation. The generated code is then executed in a forked Node.js child process. Version 7.1.9 contains a patch. | 
  
  
  
  | DbGate is cross-platform database manager. Versions 7.1.8 and prior are vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`. Version 7.1.9 contains a patch. | 
  
  
  
  | An unauthenticated SQL injection vulnerability exists in Sangoma Switchvox SMB Edition 8.3 (104997). The /pa endpoint processes XML content beginning with <PolycomIPPhone> and directly concatenates the user-controlled PhoneIP value into PostgreSQL queries without sanitization or parameterization. An unauthenticated remote attacker can execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution. | 
  
  
  
  | Windu CMS does not validate types of uploaded files. An authenticated attacker can upload arbitrary files, including PHP. This can lead to Remote Code Execution.
Because vendor contact attempts were unsuccessful, the vulnerability has only been confirmed in version 4.1 but may also affect other versions. | 
  
  
  
  | The MapSVG plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation in the SVGFile constructor in all versions up to, and including, 8.14.0 This is due to an incorrect conditional check that prevents file validation from taking place. This makes it possible for authenticated attackers, with Administrator-level access and above, to upload arbitrary files on the affected site's server which may make remote code execution possible. | 
  
  
  
  | The WP Foodbakery plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the 'delete_locations_backup_file_callback' function in all versions up to, and including, 4.9. This makes it possible for authenticated attackers, with subscriber-level access and above, to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). | 
  
  
  
  | The GoDAM – Organize WordPress Media Library & File Manager with Unlimited Folders for Images, Videos & more plugin for WordPress is vulnerable to arbitrary file uploads in versions up to, and including, 1.12.2. This is due to insufficient file type validation in the save_video_file() function hooked into WPForms' public wpforms_process_before_filter, which trusts the attacker-supplied multipart Content-Type header, preserves the original filename via wp_unique_filename(), and moves the raw upload with $wp_filesystem->move() into a web-served directory — bypassing wp_handle_upload()'s MIME/extension allowlist. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible. | 
  
  
  
  | Subscriber Remote Code Execution (RCE) in Advanced Views <= 3.8.11 versions. | 
  
  
  
  | Zohocorp ManageEngine ADAudit Plus versions before 8606 are affected by Unauthenticated Remote code execution due to the vulnerable agent API. | 
  
  
  
  | Grav versions >= 1.7.0 and before 2.0.9 contain a remote code execution vulnerability. FlexDirectory::dynamicDataField() resolves blueprint data-*@: directives by calling call_user_func_array() on attacker-influenced input, validating only that the target is callable (is_callable()) without restricting dangerous functions such as exec, system, passthru, or shell_exec. Because FlexDirectory registers this handler for every Flex directory, it bypasses the validation added to Blueprint::dynamicData() in 2.0.7 (GHSA-fj2p-qj2f-74v5). Any authenticated user with create or update permission on any Flex-based directory (Flex Users, Flex Pages, Flex Objects, or custom Flex types) can execute arbitrary shell commands on the server. | 
  
  
  
  | h2oGPT through 0.2.1 contains a path traversal vulnerability in the OpenAI-compatible files API that allows unauthenticated remote attackers to read, write, and delete arbitrary files accessible to the server process by supplying traversal sequences in the bearer token. The get_user_dir function in openai_server/backend_utils.py uses the bearer token string unsanitized as a path component via os.path.join, and because the default API key is EMPTY authentication is bypassed, enabling attackers to traverse outside the intended user directory through the file content, delete, and upload endpoints to achieve remote code execution by writing to startup hooks or application-loaded files. | 
  
  
  
  | The FileOrganizer  WordPress plugin before 1.2.0 does not validate the file type on several of its file-management operations, allowing authenticated users who have been granted file-manager access — which its premium add-on can extend to sub-administrator roles — to upload arbitrary PHP files and achieve remote code execution. This is an incomplete fix of CVE-2024-7985, which only added file-type validation to the upload operation. | 
  
  
  
  | FUXA is a web-based Process Visualization (SCADA/HMI/Dashboard) software. Version 1.3.0 has an unauthenticated Remote Code Execution vulnerability when `secureEnabled` is set to `true`. The `POST /api/runscript` endpoint checks authorization against the stored script's permission by ID, but when `test: true` is set in the request, it compiles and executes attacker-supplied code instead of the stored script's code. An unauthenticated attacker who knows a valid script ID and name may execute arbitrary code via test mode if at least one server-side script exists and is accessible without restrictive permissions. Script IDs and names can be obtained through the unauthenticated information disclosure in `GET /api/project` (reported separately). The only prerequisite is that at least one server-side script exists in the project. Version 1.3.1 fixes the issue. | 
  
  
  
  | A remote code execution (RCE) vulnerability exists in fastjson 1.2.68 through 1.2.83. This vulnerability is exploitable under fastjson's stock default configuration — no AutoType enablement required, no classpath gadget required. | 
  
  
  
  | n8n before 2.30.1 and 2.29.8 assigns all Public API key scopes to JWTs issued through the Token Exchange module regardless of the acting user's role. On instances where the Token Exchange feature and Public API are enabled, a low-privileged user who can obtain a valid external JWT trusted by a configured issuer can use the resulting access token to invoke administrator-only Public API operations such as role escalation, user creation, and user deletion (role escalation requires an Advanced Permissions license), and, when unverified Community Package installation is enabled, achieve remote code execution. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
