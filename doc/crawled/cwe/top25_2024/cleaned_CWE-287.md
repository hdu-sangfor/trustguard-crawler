# 弱点编号: CWE-287
## 弱点名称: Improper Authentication

###  Top 25 排名
- **排名**: #13
- **综合评分**: 11.14


### 状态
Draft

### 基本描述
When an actor claims to have a given identity, the product does not prove or insufficiently proves that the claim is correct.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Operating_System**: Not OS-Specific (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)
- **Technology**: ICS/OT (Often)

### 常见后果
- **范围**: Integrity, Confidentiality, Availability, Access Control
  **影响**: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands
  **说明**: This weakness can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with sensitive information or even execute arbitrary code.

### 缓解措施
- **阶段**: Architecture and Design
  **措施**: Use an authentication framework or library such as the OWASP ESAPI Authentication feature.

### 检测方法
- **方法**: Automated Static Analysis
  **说明**: Automated static analysis is useful for detecting certain types of authentication. A tool may be able to analyze related configuration files, such as .htaccess in Apache web servers, or detect the usage of commonly-used authentication libraries. Generally, automated static analysis tools have difficulty detecting custom authentication schemes. In addition, the software's design may include some functionality that is accessible to any user and does not require an established identity; an automated technique that detects the absence of authentication may report false positives.
- **方法**: Manual Static Analysis
  **说明**: This weakness can be detected using tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. Manual static analysis is useful for evaluating the correctness of custom authentication mechanisms.
- **方法**: Manual Static Analysis - Binary or Bytecode
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Automated Static Analysis
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Configuration Checker
- **方法**: Architecture or Design Review
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction

### 相关攻击模式 (CAPEC)
- CAPEC-114
- CAPEC-115
- CAPEC-151
- CAPEC-194
- CAPEC-22
- CAPEC-57
- CAPEC-593
- CAPEC-633
- CAPEC-650
- CAPEC-94

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:33*
