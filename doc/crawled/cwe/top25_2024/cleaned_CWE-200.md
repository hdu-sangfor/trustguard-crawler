# 弱点编号: CWE-200
## 弱点名称: Exposure of Sensitive Information to an Unauthorized Actor

###  Top 25 排名
- **排名**: #18
- **综合评分**: 8.35


### 状态
Draft

### 基本描述
The product exposes sensitive information to an actor that is not explicitly authorized to have access to that information.

### 详细描述
There are many different kinds of mistakes that introduce information exposures. The severity of the error can range widely, depending on the context in which the product operates, the type of sensitive information that is revealed, and the benefits it may provide to an attacker. Some kinds of sensitive information include: - private, personal information, such as personal messages, financial data, health records, geographic location, or contact details - system status and environment, such as the operating system and installed packages - business secrets and intellectual property - network status and configuration - the product's own code or internal state - metadata, e.g. logging of connections or message headers - indirect information, such as a discrepancy between two internal operations that can be observed by an outsider Information might be sensitive to different parties, each of which may have their own expectations for whether the information should be protected. These parties include: - the product's own users - people or organizations whose information is created or used by the product, even if they are not direct product users - the product's administrators, including the admins of the system(s) and/or networks on which the product operates - the developer Information exposures can occur in different ways: - the code **explicitly inserts** sensitive information into resources or messages that are intentionally made accessible to unauthorized actors, but should not contain the information - i.e., the information should have been "scrubbed" or "sanitized" - a different weakness or mistake **indirectly inserts** the sensitive information into resources, such as a web script error revealing the full system path of the program. - the code manages resources that intentionally contain sensitive information, but the resources are **unintentionally made accessible** to unauthorized actors. In this case, the information exposure is resultant - i.e., a different weakness enabled the access to the information in the first place. It is common practice to describe any loss of confidentiality as an "information exposure," but this can lead to overuse of CWE-200 in CWE mapping. From the CWE perspective, loss of confidentiality is a technical impact that can arise from dozens of different weaknesses, such as insecure file permissions or out-of-bounds read. CWE-200 and its lower-level descendants are intended to cover the mistakes that occur in behaviors that explicitly manage, store, transfer, or cleanse sensitive information.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)
- **Technology**: Mobile (Undetermined)

### 常见后果
- **范围**: Confidentiality
  **影响**: Read Application Data

### 缓解措施
- **阶段**: Architecture and Design
  **措施**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

### 检测方法
- **方法**: Automated Static Analysis - Binary or Bytecode
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Inter-application Flow Analysis
- **方法**: Dynamic Analysis with Automated Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer Automated Monitored Execution Monitored Virtual Environment - run potentially malicious code in sandbox / wrapper / virtual machine, see if it does anything suspicious
- **方法**: Manual Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Context-configured Source Code Weakness Analyzer ``` Cost effective for partial coverage: ``` Source code Weakness Analyzer
- **方法**: Architecture or Design Review
  **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Attack Modeling Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-116
- CAPEC-13
- CAPEC-169
- CAPEC-22
- CAPEC-224
- CAPEC-285
- CAPEC-287
- CAPEC-290
- CAPEC-291
- CAPEC-292
- CAPEC-293
- CAPEC-294
- CAPEC-295
- CAPEC-296
- CAPEC-297
- CAPEC-298
- CAPEC-299
- CAPEC-300
- CAPEC-301
- CAPEC-302
- CAPEC-303
- CAPEC-304
- CAPEC-305
- CAPEC-306
- CAPEC-307
- CAPEC-308
- CAPEC-309
- CAPEC-310
- CAPEC-312
- CAPEC-313
- CAPEC-317
- CAPEC-318
- CAPEC-319
- CAPEC-320
- CAPEC-321
- CAPEC-322
- CAPEC-323
- CAPEC-324
- CAPEC-325
- CAPEC-326
- CAPEC-327
- CAPEC-328
- CAPEC-329
- CAPEC-330
- CAPEC-472
- CAPEC-497
- CAPEC-508
- CAPEC-573
- CAPEC-574
- CAPEC-575
- CAPEC-576
- CAPEC-577
- CAPEC-59
- CAPEC-60
- CAPEC-616
- CAPEC-643
- CAPEC-646
- CAPEC-651
- CAPEC-79

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-24 12:08:12*
