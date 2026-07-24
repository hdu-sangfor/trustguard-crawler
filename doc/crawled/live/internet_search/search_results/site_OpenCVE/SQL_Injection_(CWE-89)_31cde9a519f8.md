# SQL Injection (CWE-89)

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=cwe:CWE-89
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | SQL injection vulnerability in Crocus v.1.3.44 allows a remote attacker to escalate privileges via the DeviceInfoMapper.xml file | 
  
  
  
  | SQL Injection vulnerability in aiflowy <= 2.1.2 allows a remote attacker to obtain sensitive information via the getPageData method in the DatacenterQuery.java file | 
  
  
  
  | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle).  Supported versions that are affected are 12.2.1.4.0 and  14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture.  While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change).  Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H). | 
  
  
  
  | The Advance Product Search- Voice & Ajax Search for WooCommerce plugin for WordPress is vulnerable to generic SQL Injection via the 's' and 'match' parameter in all versions up to, and including, 1.4.4 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query. This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database. | 
  
  
  
  | The MultiVendorX – WooCommerce Multivendor Marketplace AI Powered Solutions plugin for WordPress is vulnerable to generic SQL Injection via the 'order_by' parameter in all versions up to, and including, 5.0.9 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query. This makes it possible for authenticated attackers, with subscriber-level access and above, to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database. This vulnerability is exploitable by any authenticated subscriber-level user when the plugin's store approval setting is configured to automatically approve store owners (described as the default), as this allows any logged-in user to self-register as a store_owner via the public Stores REST endpoint, thereby obtaining the edit_stores capability required to reach the vulnerable transactions endpoint. | 
  
  
  
  | Joomla Extension - themexpert.com - Unauthenticated SQL injection in Quix Page Builder Pro < 6.2.1 - The Joomla extension Quix Page Builder Pro is vulnerable to an unauthenticated SQL injection. | 
  
  
  
  | A vulnerability was determined in CodeAstro Online Classroom 1.0. Affected by this issue is some unknown functionality of the file /OnlineClassroom/loginlinkadmin.php. Executing a manipulation of the argument aid can lead to sql injection. The attack can be executed remotely. The exploit has been publicly disclosed and may be utilized. | 
  
  
  
  | Vulnerability in the Oracle Time and Labor product of Oracle E-Business Suite (component: Internal Operations).  Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Time and Labor.  Successful attacks of this vulnerability can result in  unauthorized creation, deletion or modification access to critical data or all Oracle Time and Labor accessible data as well as  unauthorized access to critical data or complete access to all Oracle Time and Labor accessible data. CVSS 3.1 Base Score 8.1 (Confidentiality and Integrity impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N). | 
  
  
  
  | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Gis Informatics Engineering Consulting Laboratory R&D and Software Services Inc. GisLab Laboratory Management System allows SQL Injection.
This issue affects GisLab Laboratory Management System: from 1.4.03 through 08072026. | 
  
  
  
  | An unauthenticated SQL injection vulnerability exists in Sangoma Switchvox SMB Edition 8.3 (104997). The /pa endpoint processes XML content beginning with <PolycomIPPhone> and directly concatenates the user-controlled PhoneIP value into PostgreSQL queries without sanitization or parameterization. An unauthenticated remote attacker can execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution. | 
  
  
  
  | A Blind SQL injection vulnerability has been identified in Windu CMS. A remote unauthenticated attacker is able to inject SQL syntax into URL path in HTTP header resulting in Blind SQL Injection.
Because vendor contact attempts were unsuccessful, the vulnerability has only been confirmed in version 4.1 but may also affect other versions. | 
  
  
  
  | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Turkmesh Communication Services Inc. Turkhotspot 5651 Loglama allows SQL Injection.
This issue affects Turkhotspot 5651 Loglama: from 5.1.2 before 5.1.3. | 
  
  
  
  | A SQL injection (CWE-89) and security boundary bypass (CWE-863) vulnerability exists in the prebuilt BigQuery forecasting tool (bigquery-forecast) of googleapis/mcp-toolbox.
The tool accepts client-controlled parameters (data_col, timestamp_col, and id_cols) as plain strings and interpolates them unescaped via fmt.Sprintf directly into a generated AI.FORECAST table-valued SELECT statement. While MCP Toolbox utilizes an allowedDatasets mechanism to restrict queries, this defense only validates the history_data parameter; the final assembled query is executed without re-validation.
An attacker can break out of the string literal fields (such as timestamp_col) to inject a valid multi-statement or cross-dataset query block. This allows an unauthorized user to bypass the operator-configured allowedDatasets boundary and read arbitrary BigQuery tables. | 
  
  
  
  | DHIS2 is a flexible information system for data capture, management, validation, analytics and visualization. A SQL injection vulnerability was identified in the SqlView API endpoint of the DHIS2 application in the `filter` parameter used by the
`/api/sqlViews/{viewId}/data.json` endpoint. An authenticated user with access to a SqlView can inject arbitrary SQL queries inside the `filter` parameter by abusing an expression executed by PostgreSQL and its output is reflected inside the application error message. This behavior enables attackers to extract arbitrary database content using error-based SQL injection.
Affected versions include: 2.37, 2.38, 2.39, 2.40.x before 2.40.11.1/2.40.12, 2.41.x before 2.41.8.2, 2.42.x before 2.42.5.1, 2.43.0 before 2.43.0.1, 2.44 development branch before PR #24162
Patched versions include: 2.37-EOS (2026-06-09), 2.38-EOS (2026-06-09), 2.39-EOS (2026-06-09), 2.40.11.1, 2.40.12, 2.41.8.2, 2.42.5.1, 2.43.0.1, 2.44 development branch after PR #24162 | 
  
  
  
  | DHIS2 is a flexible information system for data capture, management, validation, analytics and visualization. DHIS2 SQL View data endpoints allowed authenticated users with SQL View access to provide crafted filter values that were interpolated into generated SQL. An authenticated user with access to SQL View execution could manipulate SQL generated for SQL View filters and potentially access data outside the intended SQL View result set.
This is distinct from CVE-2026-55084, which tracks the related SQL View filter column-name injection.
Known affected release lines for this advisory: DHIS2 2.37, 2.38, and 2.39 before the 2026-06-09 EOS security updates.
Patched by the 2026-06-09 EOS security updates for 2.37, 2.38, and 2.39. The same value-slot hardening was already present on later supported branches through DHIS2-20174 / PR #22253. | 
  
  
  
  | Linknat VOS3000 and VOS2009 through version 2.1.2.0 contain an unauthenticated SQL injection vulnerability that allows remote attackers to execute arbitrary SQL commands by manipulating the name parameter in a POST request to the login endpoint. Attackers can inject malicious SQL through the login form and retrieve injected query results from a subsequent session request, enabling extraction of plaintext credentials and other database content with DBA-level privileges. | 
  
  
  
  | Aptabase through commit 5a89368 contains a SQL injection vulnerability in the ClickHouse query backend that allows authenticated attackers to read event data across all tenants by injecting unsanitized filter parameters into Liquid SQL templates. Attackers can supply malicious values through EventName, CountryCode, OsName, DeviceModel, AppVersion, or SessionId parameters to inject a UNION ALL statement that bypasses the app_id tenant isolation filter across thirteen of the fifteen stats API endpoints. | 
  
  
  
  | Vulnerability in the Oracle Supply Chain Globalization product of Oracle E-Business Suite (component: Copy Inventory Organization).  Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Supply Chain Globalization.  Successful attacks of this vulnerability can result in  unauthorized update, insert or delete access to some of Oracle Supply Chain Globalization accessible data as well as  unauthorized read access to a subset of Oracle Supply Chain Globalization accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Supply Chain Globalization. CVSS 3.1 Base Score 6.3 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L). | 
  
  
  
  | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Xpoda Türkiye Informatics Technology Inc. No Code Platform allows SQL Injection.
This issue affects No Code Platform: from 4.3.1.0 through 20260722. NOTE: The vendor was contacted early about this disclosure but did not respond in any way. | 
  
  
  
  | The Lumise Product Designer for WooCommerce plugin for WordPress is vulnerable to SQL Injection via the 'id' and 'table' parameters in the uploaded cart JSON file processed by the checkout AJAX action in versions up to, and including, 2.1.1. This is due to insufficient escaping on the user-supplied parameters before they are appended directly to a raw SQL query in the find_resource() function — the 'id' field is interpolated without quotes into a WHERE clause (numeric context) and 'table' is interpolated into the FROM clause, neither of which is protected by wp_magic_quotes or passed through $wpdb->prepare(). This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
