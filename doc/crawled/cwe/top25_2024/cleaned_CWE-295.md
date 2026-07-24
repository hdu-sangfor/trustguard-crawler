# 弱点编号: CWE-295
## 弱点名称: Improper Certificate Validation

###  Top 25 排名
- **排名**: #25
- **综合评分**: 5.85


### 状态
Draft

### 基本描述
The product does not validate, or incorrectly validates, a certificate.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)
- **Technology**: Mobile (Undetermined)

### 常见后果
- **范围**: Integrity, Authentication
  **影响**: Bypass Protection Mechanism, Gain Privileges or Assume Identity
  **说明**: When a certificate is invalid or malicious, it might allow an attacker to spoof a trusted entity by interfering in the communication path between the host and client. The product might connect to a malicious host while believing it is a trusted host, or the product might be deceived into accepting spoofed data that appears to originate from a trusted host.

### 缓解措施
- **阶段**: Architecture and Design, Implementation
  **措施**: Certificates should be carefully managed and checked to assure that data are encrypted with the intended owner's public key.
- **阶段**: Implementation
  **措施**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

### 检测方法
- **方法**: Automated Static Analysis - Binary or Bytecode
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner
- **方法**: Dynamic Analysis with Manual Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Man-in-the-middle attack tool
- **方法**: Manual Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-459
- CAPEC-475

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-24 12:09:03*
