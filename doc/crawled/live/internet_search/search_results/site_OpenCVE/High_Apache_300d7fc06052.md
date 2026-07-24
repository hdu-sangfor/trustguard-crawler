# High Apache

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=vendor:apache+AND+cvss31%3E%3D7
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | Use After Free vulnerability in the Rust deserialization logic of Apache Fory. This issue affects Apache Fory from 0.13.0 through 1.3.0.
 A crafted Fory payload could cause undefined behavior, process crash, or potential memory disclosure.
Users are recommended to upgrade to version 1.4.0, which fixes the issue. | 
  
  
  
  | Path traversal on Windows in Apache MINA SSHD component sshd-git. Apache MINA SSHD is a Java library for client-side and server-side SSH.
A git server implemented with Apache MINA SSHD component sshd-git and running on Windows could allow an authenticated remote user access to git repositories outside of the configured server-side root directory. The path validation applied for CVE-2026-48827 in Apache MINA SSHD 2.18.0 and 3.0.0-M4 was partly ineffective for Servers running on Windows.
Applications are affected if they use org.apache.sshd:sshd-git to implement a git server and run on Windows. Applications not using sshd-git or not running on Windows are not affected.
Users are advised to upgrade affected applications to Apache MINA SSHD 2.19.0, which fixes the issue.
The issue also is present in the pre-release milestones 3.0.0-M1 to 3.0.0-M4 for a new upcoming new major version 3.0.0. Again, applications are affected only if they use sshd-git and run on Windows. Upgrade affected applications to 3.0.0-M5. | 
  
  
  
  | Out-of-bounds read via sun.misc.Unsafe in Apache Fory. When out-of-band zero-copy deserialization is used, readAlignedVarUint() can read beyond the bounds of the underlying buffer. Out-of-band zero-copy deserialization is an opt-in feature; applications that do not use it are not affected.
This issue affects Apache Fory (formerly Apache Fury): from 0.5.0 before 1.4.0. Versions before 0.11.0 were published under the Maven coordinates org.apache.fury:fury-core.
Users are recommended to upgrade to version 1.4.0, which fixes the issue. | 
  
  
  
  | Deserialization of untrusted data vulnerability that may allow class-registration checks to be bypassed during Java lambda deserialization. Only lambda capture class is affected
This issue affects Apache Fory: from before 1.4.0.
Users are recommended to upgrade to version 1.4.0, which fixes the issue. | 
  
  
  
  | Path traversal in the sshd-scp component of Apache MINA SSHD. Apache MINA SSHD is a Java library for client-side and server-side SSH.
The implementation of receiving files or directories via SCP did not validate filenames in SCP "C" or "D" commands. A malicious sender could send filenames containing paths, resulting in files to be written in attacker-controlled places.
The issue affects only
  *  applications that use no longer supported Apache MINA SSHD versions < 2.0.0 and use the SCP functions to receive files,
  *  or applications using sshd-scp in Apache MINA SSHD >= 2.0.0 to receive files.
Applications using Apache MINA SSHD >= 2.0.0 not using sshd-scp are not affected.
The issue is fixed in Apache MINA 2.19.0 and 3.0.0-M5. Affected applications are advised to upgrade to these versions. | 
  
  
  
  | Improper Isolation or Compartmentalization vulnerability in Apache Syncope.
An administrator with adequate entitlements can import arbitrary BPMN process definitions via the REST API and then start the process. When a BPMN process containing a Groovy scriptTask is imported and started, the Groovy script is executed directly on the server, with no sandbox.
This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.
Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue by wrapping Flowable's Groovy scriptTasks with security sandbox. | 
  
  
  
  | Improper Isolation or Compartmentalization vulnerability in Apache Syncope.
An administrator with adequate entitlements can achieve remote code execution through the connector subsystem by relying on scripted connectors' (REST and SQL) capability to run Groovy scripts.
This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.
Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue by hardening the Groovy security sandbox. | 
  
  
  
  | Low-privileged authenticated Server-Side Request Forgery (SSRF) 
vulnerability in Apache Syncope via Connectors and Resources check.
This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.
Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue. | 
  
  
  
  | Uncontrolled Resource Consumption vulnerability in Apache Traffic Server.
This issue affects Apache Traffic Server: from 9.0.0 through 9.1.13, from 10.0.0 through 10.1.2.
Users are recommended to upgrade to version 9.1.14 or 10.1.3, which fixes the issue. | 
  
  
  
  | A SQL Injection vulnerability exists in Apache Fineract's Report Execution API (runreports endpoint) in versions up to and including 1.14.0. Report parameter values are incorporated into the generated SQL query without sufficient validation, allowing an authenticated user with permission to run reports to inject arbitrary SQL via crafted parameter values. This can be leveraged to perform unauthorized access to data beyond what the report was designed to expose. Users are recommended to upgrade to a version containing the fix. | 
  
  
  
  | A SQL Injection vulnerability exists in Apache Fineract's Office Search API (GET /api/v1/offices) in versions up to and including 1.14.0. The orderBy request parameter is concatenated into a SQL query without sufficient validation, allowing an authenticated user with permission to view offices to inject arbitrary SQL via a crafted orderBy value. This is a bypass of the ColumnValidator fix introduced for CVE-2024-32838, which does not detect bare subqueries in the ORDER BY position. This can be leveraged to perform time-based blind SQL injection for data exfiltration. Because the injected query blocks the database connection for its full duration, concurrent exploitation can exhaust the application's database connection pool, resulting in denial of service for other users. Users are recommended to upgrade to a version containing the fix. | 
  
  
  
  | A boolean-based SQL Injection vulnerability exists in Apache Fineract's Client Search API (GET /api/v1/clients) in versions up to and including 1.14.0. The orderBy and sortOrder request parameters are concatenated into a SQL query without sufficient validation, allowing an authenticated user with permission to view clients to inject arbitrary SQL via a crafted orderBy value. This can be leveraged to perform blind boolean-based data extraction and, on MySQL/MariaDB, to disclose arbitrary files readable by the database process via the LOAD_FILE() function. Users are recommended to upgrade to a version containing the fix | 
  
  
  
  | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Kylin. A backend API may bring job config parameters to OS command line.
This issue affects Apache Kylin: from 4 through 5.0.3.
Users are recommended to upgrade to version 5.0.4, which fixes the issue. | 
  
  
  
  | Insufficient Technical Documentation vulnerability in Apache Tomcat since the requirements to securely configure the EncryptInterceptor were not clearly documented.
This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.23, from 10.1.0-M1 through 10.1.56, from 9.0.13 through 9.0.119, from 8.5.38 through 8.5.100, from 7.0.100 through 7.0.109. Other versions that have reached end of support may also be affected.
Users are recommended to upgrade to version 11.0.24, 10.1.57 or 9.0.120 which fix the issue. | 
  
  
  
  | In the Apache Airflow FAB auth manager, a DAG whose `dag_id` is `DAGs` collided with the global all-DAGs permission resource name produced by `resource_name()`, so a user granted per-DAG `access_control` on that one DAG was silently granted the global all-DAGs permission (privilege escalation). The escalation triggers when a DAG named `DAGs` exists and a lower-privileged user is given per-DAG access to it, granting that user read/edit access to every DAG. Users are advised to upgrade to `apache-airflow-providers-fab` 3.7.2 or later, which disambiguates the resource-name collision. | 
  
  
  
  | Improper Handling of URL Encoding (Hex Encoding) vulnerability in Apache Tomcat's rewrite valve allowed security constraint bypass for some configurations.
This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.23, from 10.1.0-M1 through 10.1.56, from 9.0.0.M1 through 9.0.119, from 8.5.0 through 8.5.100. Other versions that have reached end of support may also be affected.
Users are recommended to upgrade to version 11.0.24, 10.1.57 or 9.0.120, which fix the issue. | 
  
  
  
  | ** UNSUPPORTED WHEN ASSIGNED ** Incorrect Authorization vulnerability in Apache Submarine Server Core.
This issue affects Apache Submarine Server Core: from 0.8.0.
An attacker can bypass authentication by sending specially crafted REST requests.
As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.
NOTE: This vulnerability only affects products that are no longer supported by the maintainer. | 
  
  
  
  | URL path injection via unencoded user-supplied identifiers vulnerability in Apache Gravitino.
This issue affects Apache Gravitino: from 1.0.0 before 1.2.1.
Users are recommended to upgrade to version 1.2.1, which fixes the issue. | 
  
  
  
  | Apache Log4j's  JsonTemplateLayout https://logging.apache.org/log4j/2.x/manual/json-template-layout.html , in versions up to and including 2.25.3, produces invalid JSON output when log events contain non-finite floating-point values (NaN, Infinity, or -Infinity), which are prohibited by RFC 8259. This may cause downstream log processing systems to reject or fail to index affected records.
An attacker can exploit this issue only if both of the following conditions are met:
  *  The application uses JsonTemplateLayout.
  *  The application logs a MapMessage, or logs an object directly (e.g., via Logger.info(Object), which wraps it in an ObjectMessage), where the message contains an attacker-controlled floating-point value.
Users are advised to upgrade to Apache Log4j JSON Template Layout 2.25.4, which corrects this issue.
Note: The fix released in version 2.25.4 did not cover all affected code paths. CVE-2026-49844 was assigned to the remaining issue, which concerns the MapMessage.asJson() serialization in Apache Log4j API and is fixed in versions 2.25.5 and 2.26.1. | 
  
  
  
  | Incorrect Authorization, Improper Access Control vulnerability in Apache IoTDB.
Authorization bypass in /rest/v2/fastLastQuery exposes last-value data to unauthorized authenticated users.
This issue affects Apache IoTDB: from 1.3.5 before 1.3.8, from 2.0.5 before 2.0.10.
Users are recommended to upgrade to version 2.0.10, which fixes the issue. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
