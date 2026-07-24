# 弱点编号: CWE-863
## 弱点名称: Incorrect Authorization

###  Top 25 排名
- **排名**: #20
- **综合评分**: 7.53


### 状态
Incomplete

### 基本描述
The product performs an authorization check when an actor attempts to access a resource or perform an action, but it does not correctly perform the check.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Web Server (Often)
- **Technology**: Database Server (Often)
- **Technology**: Not Technology-Specific (Undetermined)

### 常见后果
- **范围**: Confidentiality
  **影响**: Read Application Data, Read Files or Directories
  **说明**: An attacker could bypass intended access restrictions to read sensitive data, either by reading the data directly from a data store that is not correctly restricted, or by accessing insufficiently-protected, privileged functionality to read the data.
- **范围**: Integrity
  **影响**: Modify Application Data, Modify Files or Directories
  **说明**: An attacker could bypass intended access restrictions to modify sensitive data, either by writing the data directly to a data store that is not correctly restricted, or by accessing insufficiently-protected, privileged functionality to write the data.
- **范围**: Access Control
  **影响**: Gain Privileges or Assume Identity, Bypass Protection Mechanism
  **说明**: An attacker could bypass intended access restrictions to gain privileges by modifying or reading critical data directly, or by accessing privileged functionality.
- **范围**: Confidentiality, Integrity, Availability
  **影响**: Execute Unauthorized Code or Commands
  **说明**: An attacker could use elevated privileges to execute unauthorized commands or code.
- **范围**: Availability
  **影响**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)
  **说明**: An attacker could gain unauthorized access to resources on the system and excessively consume those resources, leading to a denial of service.

### 缓解措施
- **阶段**: Architecture and Design
  **措施**: Divide the product into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully mapping roles with data and functionality. Use role-based access control (RBAC) [REF-229] to enforce the roles at the appropriate boundaries. Note that this approach may not protect against horizontal authorization, i.e., it will not protect a user from attacking others with the same role.
- **阶段**: Architecture and Design
  **措施**: Ensure that access control checks are performed related to the business logic. These checks may be different than the access control checks that are applied to more generic resources such as files, connections, processes, memory, and database records. For example, a database may restrict access for medical records to a specific database user, but each record might only be intended to be accessible to the patient and the patient's doctor [REF-7].
- **阶段**: Architecture and Design
  **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using authorization frameworks such as the JAAS Authorization Framework [REF-233] and the OWASP ESAPI Access Control feature [REF-45].
- **阶段**: Architecture and Design
  **措施**: For web applications, make sure that the access control mechanism is enforced correctly at the server side on every page. Users should not be able to access any unauthorized functionality or information by simply requesting direct access to that page. One way to do this is to ensure that all pages containing sensitive information are not cached, and that all such pages restrict access to requests that are accompanied by an active and authenticated session token associated with a user who has the required permissions to access that page.
- **阶段**: System Configuration, Installation
  **措施**: Use the access control capabilities of your operating system and server environment and define your access control lists accordingly. Use a "default deny" policy when defining these ACLs.

### 检测方法
- **方法**: Automated Static Analysis
  **说明**: Automated static analysis is useful for detecting commonly-used idioms for authorization. A tool may be able to analyze related configuration files, such as .htaccess in Apache web servers, or detect the usage of commonly-used authorization libraries. Generally, automated static analysis tools have difficulty detecting custom authorization schemes. Even if they can be customized to recognize these schemes, they might not be able to tell whether the scheme correctly performs the authorization in a way that cannot be bypassed or subverted by an attacker.
- **方法**: Automated Dynamic Analysis
  **说明**: Automated dynamic analysis may not be able to find interfaces that are protected by authorization checks, even if those checks contain weaknesses.
- **方法**: Manual Analysis
  **说明**: This weakness can be detected using tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. Specifically, manual static analysis is useful for evaluating the correctness of custom authorization mechanisms.
- **方法**: Manual Static Analysis - Binary or Bytecode
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Host Application Interface Scanner Fuzz Tester Framework-based Fuzzer Forced Path Execution Monitored Virtual Environment - run potentially malicious code in sandbox / wrapper / virtual machine, see if it does anything suspicious
- **方法**: Manual Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-24 12:08:25*
