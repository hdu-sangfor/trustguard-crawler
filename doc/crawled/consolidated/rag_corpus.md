# 网络安全与数据安全 RAG 语料库
## Unified Cybersecurity RAG Corpus

> **生成时间**: 2026-07-17 13:46:50
> **总条目数**: 114
> **总字符数**: 303,479

---

## 目录

- **攻击模式 (CAPEC)** (2 条)
  - [CAPEC_Mechanisms_of_Attack](#capec_mechanisms_of_attack) — CAPEC (Common Attack Pattern Enumeration and Classification)
  - [CAPEC_Top_Attack_Patterns](#capec_top_attack_patterns) — CAPEC Top 攻击模式
- **已知被利用漏洞 (CISA KEV)** (1 条)
  - [CISA_KEV_Recent_100](#cisa_kev_recent_100) — CISA Known Exploited Vulnerabilities (KEV)
- **法规与标准 (中国)** (6 条)
  - [AI_LLM_Security_Framework](#ai_llm_security_framework) — AI 与 LLM 安全框架
  - [China_CyberLaw_System](#china_cyberlaw_system) — 中国网络安全法律法规体系
  - [Cloud_Security_Matrix](#cloud_security_matrix) — 云安全责任共担模型与安全控制矩阵
  - [Data_Security_Lifecycle](#data_security_lifecycle) — 数据安全全生命周期管理
  - [Equal_Protection_2.0_Mapping](#equal_protection_2.0_mapping) — 等保2.0 与 NIST CSF / ISO 27001 对照表
  - [GB_Standards_Catalog](#gb_standards_catalog) — 中国网络安全国家标准体系 (GB/T)
- **安全框架 (NIST/ISO)** (4 条)
  - [CISA_KEV_Catalog](#cisa_kev_catalog) — CISA Known Exploited Vulnerabilities (KEV) 目录
  - [ISO27001_2022_Framework](#iso27001_2022_framework) — ISO/IEC 27001:2022
  - [NIST_CSF_2.0_Framework](#nist_csf_2.0_framework) — NIST Cybersecurity Framework (CSF) 2.0
  - [NIST_SP800-53_Rev5](#nist_sp800-53_rev5) — NIST SP 800-53 Rev. 5
- **安全标准 (OWASP)** (3 条)
  - [OWASP_ASVS_v4.0.3](#owasp_asvs_v4.0.3) — OWASP ASVS (Application Security Verification Standard) v4.0.3
  - [OWASP_WSTG_v4.2](#owasp_wstg_v4.2) — OWASP WSTG (Web Security Testing Guide) v4.2
  - [OWASP_Top10_2021_Detailed](#owasp_top10_2021_detailed) — OWASP Top 10:2021 - Web Application Security Risks
- **漏洞实例 (CVE)** (70 条)
  - [CVE-2026-12348](#cve-2026-12348) — 漏洞编号: CVE-2026-12348
  - [CVE-2026-35258](#cve-2026-35258) — 漏洞编号: CVE-2026-35258
  - [CVE-2026-35259](#cve-2026-35259) — 漏洞编号: CVE-2026-35259
  - [CVE-2026-35261](#cve-2026-35261) — 漏洞编号: CVE-2026-35261
  - [CVE-2026-35262](#cve-2026-35262) — 漏洞编号: CVE-2026-35262
  - [CVE-2026-35263](#cve-2026-35263) — 漏洞编号: CVE-2026-35263
  - [CVE-2026-35265](#cve-2026-35265) — 漏洞编号: CVE-2026-35265
  - [CVE-2026-35267](#cve-2026-35267) — 漏洞编号: CVE-2026-35267
  - [CVE-2026-35268](#cve-2026-35268) — 漏洞编号: CVE-2026-35268
  - [CVE-2026-35269](#cve-2026-35269) — 漏洞编号: CVE-2026-35269
  - [CVE-2026-35270](#cve-2026-35270) — 漏洞编号: CVE-2026-35270
  - [CVE-2026-35271](#cve-2026-35271) — 漏洞编号: CVE-2026-35271
  - [CVE-2026-35272](#cve-2026-35272) — 漏洞编号: CVE-2026-35272
  - [CVE-2026-35274](#cve-2026-35274) — 漏洞编号: CVE-2026-35274
  - [CVE-2026-35275](#cve-2026-35275) — 漏洞编号: CVE-2026-35275
  - [CVE-2026-35276](#cve-2026-35276) — 漏洞编号: CVE-2026-35276
  - [CVE-2026-35278](#cve-2026-35278) — 漏洞编号: CVE-2026-35278
  - [CVE-2026-35279](#cve-2026-35279) — 漏洞编号: CVE-2026-35279
  - [CVE-2026-35280](#cve-2026-35280) — 漏洞编号: CVE-2026-35280
  - [CVE-2026-35281](#cve-2026-35281) — 漏洞编号: CVE-2026-35281
  - [cleaned_CVE-2026-12348](#cleaned_cve-2026-12348) — CVE-2026-12348
  - [cleaned_CVE-2026-35258](#cleaned_cve-2026-35258) — CVE-2026-35258
  - [cleaned_CVE-2026-35259](#cleaned_cve-2026-35259) — CVE-2026-35259
  - [cleaned_CVE-2026-35261](#cleaned_cve-2026-35261) — CVE-2026-35261
  - [cleaned_CVE-2026-35262](#cleaned_cve-2026-35262) — CVE-2026-35262
  - [cleaned_CVE-2026-35263](#cleaned_cve-2026-35263) — CVE-2026-35263
  - [cleaned_CVE-2026-35265](#cleaned_cve-2026-35265) — CVE-2026-35265
  - [cleaned_CVE-2026-35267](#cleaned_cve-2026-35267) — CVE-2026-35267
  - [cleaned_CVE-2026-35268](#cleaned_cve-2026-35268) — CVE-2026-35268
  - [cleaned_CVE-2026-35269](#cleaned_cve-2026-35269) — CVE-2026-35269
  - [cleaned_CVE-2026-35270](#cleaned_cve-2026-35270) — CVE-2026-35270
  - [cleaned_CVE-2026-35271](#cleaned_cve-2026-35271) — CVE-2026-35271
  - [cleaned_CVE-2026-35272](#cleaned_cve-2026-35272) — CVE-2026-35272
  - [cleaned_CVE-2026-35274](#cleaned_cve-2026-35274) — CVE-2026-35274
  - [cleaned_CVE-2026-35275](#cleaned_cve-2026-35275) — CVE-2026-35275
  - [cleaned_CVE-2026-35276](#cleaned_cve-2026-35276) — CVE-2026-35276
  - [cleaned_CVE-2026-35278](#cleaned_cve-2026-35278) — CVE-2026-35278
  - [cleaned_CVE-2026-35279](#cleaned_cve-2026-35279) — CVE-2026-35279
  - [cleaned_CVE-2026-35280](#cleaned_cve-2026-35280) — CVE-2026-35280
  - [cleaned_CVE-2026-35281](#cleaned_cve-2026-35281) — CVE-2026-35281
  - [cleaned_CVE-2026-35282](#cleaned_cve-2026-35282) — CVE-2026-35282
  - [cleaned_CVE-2026-35283](#cleaned_cve-2026-35283) — CVE-2026-35283
  - [cleaned_CVE-2026-35284](#cleaned_cve-2026-35284) — CVE-2026-35284
  - [cleaned_CVE-2026-35285](#cleaned_cve-2026-35285) — CVE-2026-35285
  - [cleaned_CVE-2026-35286](#cleaned_cve-2026-35286) — CVE-2026-35286
  - [cleaned_CVE-2026-35288](#cleaned_cve-2026-35288) — CVE-2026-35288
  - [cleaned_CVE-2026-35289](#cleaned_cve-2026-35289) — CVE-2026-35289
  - [cleaned_CVE-2026-35291](#cleaned_cve-2026-35291) — CVE-2026-35291
  - [cleaned_CVE-2026-35292](#cleaned_cve-2026-35292) — CVE-2026-35292
  - [cleaned_CVE-2026-35293](#cleaned_cve-2026-35293) — CVE-2026-35293
  - [cleaned_CVE-2026-35294](#cleaned_cve-2026-35294) — CVE-2026-35294
  - [cleaned_CVE-2026-35295](#cleaned_cve-2026-35295) — CVE-2026-35295
  - [cleaned_CVE-2026-35296](#cleaned_cve-2026-35296) — CVE-2026-35296
  - [cleaned_CVE-2026-35298](#cleaned_cve-2026-35298) — CVE-2026-35298
  - [cleaned_CVE-2026-35299](#cleaned_cve-2026-35299) — CVE-2026-35299
  - [cleaned_CVE-2026-35300](#cleaned_cve-2026-35300) — CVE-2026-35300
  - [cleaned_CVE-2026-35301](#cleaned_cve-2026-35301) — CVE-2026-35301
  - [cleaned_CVE-2026-35302](#cleaned_cve-2026-35302) — CVE-2026-35302
  - [cleaned_CVE-2026-35303](#cleaned_cve-2026-35303) — CVE-2026-35303
  - [cleaned_CVE-2026-35304](#cleaned_cve-2026-35304) — CVE-2026-35304
  - [cleaned_CVE-2026-35305](#cleaned_cve-2026-35305) — CVE-2026-35305
  - [cleaned_CVE-2026-35306](#cleaned_cve-2026-35306) — CVE-2026-35306
  - [cleaned_CVE-2026-35307](#cleaned_cve-2026-35307) — CVE-2026-35307
  - [cleaned_CVE-2026-35308](#cleaned_cve-2026-35308) — CVE-2026-35308
  - [cleaned_CVE-2026-35309](#cleaned_cve-2026-35309) — CVE-2026-35309
  - [cleaned_CVE-2026-35310](#cleaned_cve-2026-35310) — CVE-2026-35310
  - [cleaned_CVE-2026-35311](#cleaned_cve-2026-35311) — CVE-2026-35311
  - [cleaned_CVE-2026-35312](#cleaned_cve-2026-35312) — CVE-2026-35312
  - [cleaned_CVE-2026-35313](#cleaned_cve-2026-35313) — CVE-2026-35313
  - [cleaned_CVE-2026-35314](#cleaned_cve-2026-35314) — CVE-2026-35314
- **软件弱点 (CWE)** (25 条)
  - [CWE-119](#cwe-119) — 弱点编号: CWE-119
  - [CWE-125](#cwe-125) — 弱点编号: CWE-125
  - [CWE-1321](#cwe-1321) — 弱点编号: CWE-1321
  - [CWE-20](#cwe-20) — 弱点编号: CWE-20
  - [CWE-200](#cwe-200) — 弱点编号: CWE-200
  - [CWE-22](#cwe-22) — 弱点编号: CWE-22
  - [CWE-287](#cwe-287) — 弱点编号: CWE-287
  - [CWE-295](#cwe-295) — 弱点编号: CWE-295
  - [CWE-352](#cwe-352) — 弱点编号: CWE-352
  - [CWE-401](#cwe-401) — 弱点编号: CWE-401
  - [CWE-416](#cwe-416) — 弱点编号: CWE-416
  - [CWE-434](#cwe-434) — 弱点编号: CWE-434
  - [CWE-476](#cwe-476) — 弱点编号: CWE-476
  - [CWE-502](#cwe-502) — 弱点编号: CWE-502
  - [CWE-611](#cwe-611) — 弱点编号: CWE-611
  - [CWE-77](#cwe-77) — 弱点编号: CWE-77
  - [CWE-78](#cwe-78) — 弱点编号: CWE-78
  - [CWE-787](#cwe-787) — 弱点编号: CWE-787
  - [CWE-79](#cwe-79) — 弱点编号: CWE-79
  - [CWE-798](#cwe-798) — 弱点编号: CWE-798
  - [CWE-862](#cwe-862) — 弱点编号: CWE-862
  - [CWE-863](#cwe-863) — 弱点编号: CWE-863
  - [CWE-89](#cwe-89) — 弱点编号: CWE-89
  - [CWE-918](#cwe-918) — 弱点编号: CWE-918
  - [CWE-94](#cwe-94) — 弱点编号: CWE-94
- **弱点分类视图 (CWE Views)** (3 条)
  - [CWE-View-1000](#cwe-view-1000) — CWE 视图: 1000
  - [CWE-View-1003](#cwe-view-1003) — CWE 视图: 1003
  - [CWE-View-699](#cwe-view-699) — CWE 视图: 699

---


============================================================
## CWE-119
### 弱点编号: CWE-119

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 9604

# 弱点编号: CWE-119
## 弱点名称: Improper Restriction of Operations within the Bounds of a Memory Buffer

### Top 25 排名
- **排名**: #17
- **综合评分**: 8.88


### 状态
Stable

### 基本描述
The product performs operations on a memory buffer, but it reads from or writes to a memory location outside the buffer's intended boundary. This may result in read or write operations on unexpected memory locations that could be linked to other variables, data structures, or internal program data.

### 适用平台
- **Language**: Memory-Unsafe (Often)
- **Language**: C (Often)
- **Language**: C++ (Often)
- **Language**: Assembly (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)

### 常见后果
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands, Modify Memory
 **说明**: If the memory accessible by the attacker can be effectively controlled, it may be possible to execute arbitrary code, as with a standard buffer overflow. If the attacker can overwrite a pointer's worth of memory (usually 32 or 64 bits), they can alter the intended control flow by redirecting a function pointer to their own malicious code. Even when the attacker can only modify a single byte arbitrary code execution can be possible. Sometimes this is because the same problem can be exploited repeatedly to the same effect. Other times it is because the attacker can overwrite security-critical application-specific data -- such as a flag indicating whether the user is an administrator.
- **范围**: Availability, Confidentiality
 **影响**: Read Memory, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
 **说明**: Out of bounds memory access will very likely result in the corruption of relevant memory, and perhaps instructions, possibly leading to a crash. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.
- **范围**: Confidentiality
 **影响**: Read Memory
 **说明**: In the case of an out-of-bounds read, the attacker may have access to sensitive information. If the sensitive information contains system details, such as the current buffer's position in memory, this knowledge can be used to craft further attacks, possibly with more severe consequences.

### 缓解措施
- **阶段**: Requirements
 **措施**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, many languages that perform their own memory management, such as Java and Perl, are not subject to buffer overflows. Other languages, such as Ada and C#, typically provide overflow protection, but the protection can be disabled by the programmer. Be wary that a language's interface to native code may still be subject to overflows, even if the language itself is theoretically safe.
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. Examples include the Safe C String Library (SafeStr) by Messier and Viega [REF-57], and the Strsafe.h library from Microsoft [REF-56]. These libraries provide safer versions of overflow-prone string-handling functions.
- **阶段**: Operation, Build and Compilation
 **措施**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **阶段**: Implementation
 **措施**: Consider adhering to the following rules when allocating and managing an application's memory: - Double check that the buffer is as large as specified. - When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string. - Check buffer boundaries if accessing the buffer in a loop and make sure there is no danger of writing past the allocated space. - If necessary, truncate all input strings to a reasonable length before passing them to the copy and concatenation functions.
- **阶段**: Operation, Build and Compilation
 **措施**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **阶段**: Operation
 **措施**: Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336].
- **阶段**: Implementation
 **措施**: Replace unbounded copy functions with analogous functions that support length arguments, such as strcpy with strncpy. Create these if they are not available.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives. Automated static analysis generally does not account for environmental considerations when reporting out-of-bounds memory operations. This can make it difficult for users to determine which warnings should be investigated first. For example, an analysis tool might report buffer overflows that originate from command line arguments in a program that is not expected to run with setuid or other special privileges.
- **方法**: Automated Dynamic Analysis
 **说明**: This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode Quality Analysis Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer ``` Cost effective for partial coverage: ``` Source Code Quality Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-10
- CAPEC-100
- CAPEC-123
- CAPEC-14
- CAPEC-24
- CAPEC-42
- CAPEC-44
- CAPEC-45
- CAPEC-46
- CAPEC-47
- CAPEC-8
- CAPEC-9

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:01*

---

============================================================
## CWE-125
### 弱点编号: CWE-125

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 4285

# 弱点编号: CWE-125
## 弱点名称: Out-of-bounds Read

### Top 25 排名
- **排名**: #6
- **综合评分**: 16.71


### 状态
Draft

### 基本描述
The product reads data past the end, or before the beginning, of the intended buffer.

### 适用平台
- **Language**: Memory-Unsafe (Undetermined)
- **Language**: C (Undetermined)
- **Language**: C++ (Undetermined)
- **Technology**: ICS/OT (Often)

### 常见后果
- **范围**: Confidentiality
 **影响**: Read Memory
 **说明**: An attacker could get secret values such as cryptographic keys, PII, memory addresses, or other information that could be used in additional attacks.
- **范围**: Confidentiality
 **影响**: Bypass Protection Mechanism
 **说明**: Out-of-bounds memory could contain memory addresses or other information that can be used to bypass ASLR and other protection mechanisms in order to improve the reliability of exploiting a separate weakness for code execution.
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: An attacker could cause a segmentation fault or crash by causing memory to be read outside of the bounds of the buffer. This is especially likely when the code reads a variable amount of data and assumes that a sentinel exists to stop the read operation, such as a NUL in a string.
- **范围**: Other
 **影响**: Varies by Context
 **说明**: The read operation could produce other undefined or unexpected results.

### 缓解措施
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. To reduce the likelihood of introducing an out-of-bounds read, ensure that you validate and ensure correct calculations for any length argument, buffer size calculation, or offset. Be especially careful of relying on a sentinel (i.e. special character such as NUL) in untrusted inputs.
- **阶段**: Architecture and Design
 **措施**: Use a language that provides appropriate memory abstractions.

### 检测方法
- **方法**: Fuzzing
 **说明**: Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

### 相关攻击模式 (CAPEC)
- CAPEC-540

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:47*

---

============================================================
## CWE-1321
### 弱点编号: CWE-1321

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 2959

# 弱点编号: CWE-1321
## 弱点名称: Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')

### Top 25 排名
- **排名**: #22
- **综合评分**: 6.78


### 状态
Incomplete

### 基本描述
The product receives input from an upstream component that specifies attributes that are to be initialized or updated in an object, but it does not properly control modifications of attributes of the object prototype.

### 适用平台
- **Language**: JavaScript (Undetermined)

### 常见后果
- **范围**: Confidentiality, Integrity, Availability
 **影响**: Read Application Data, Modify Application Data
 **说明**: This weakness is usually exploited by using a special attribute of objects called proto, constructor, or prototype. Such attributes give access to the object prototype. An attacker can inject attributes that are used in other components by adding or modifying attributes of an object prototype. This creates attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the product depends on existence or non-existence of certain attributes, or uses pre-defined attributes of the object prototype (such as hasOwnProperty, toString, or valueOf).
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: An attacker can override existing attributes with ones that have incompatible type, which may lead to a crash.

### 缓解措施
- **阶段**: Implementation
 **措施**: By freezing the object prototype first (for example, Object.freeze(Object.prototype)), modification of the prototype becomes impossible.
- **阶段**: Architecture and Design
 **措施**: By blocking modifications of attributes that resolve to object prototype, such as proto or prototype, this weakness can be mitigated.
- **阶段**: Implementation
 **措施**: When handling untrusted objects, validating using a schema can be used.
- **阶段**: Implementation
 **措施**: By using an object without prototypes (via Object.create(null) ), adding object prototype attributes by accessing the prototype via the special attributes becomes impossible, mitigating this weakness.
- **阶段**: Implementation
 **措施**: Map can be used instead of objects in most cases. If Map methods are used instead of object attributes, it is not possible to access the object prototype or modify it.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-1
- CAPEC-180
- CAPEC-77

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:38*

---

============================================================
## CWE-20
### 弱点编号: CWE-20

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 12934

# 弱点编号: CWE-20
## 弱点名称: Improper Input Validation

### Top 25 排名
- **排名**: #11
- **综合评分**: 12.78


### 状态
Stable

### 基本描述
The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly.

### 详细描述
Input validation is a frequently-used technique for checking potentially dangerous inputs in order to ensure that the inputs are safe for processing within the code, or when communicating with other components. Input can consist of: - raw data - strings, numbers, parameters, file contents, etc. - metadata - information about the raw data, such as headers or size Data can be simple or structured. Structured data can be composed of many nested layers, composed of combinations of metadata and raw data, with other simple or structured data. Many properties of raw data or metadata may need to be validated upon entry into the code, such as: - specified quantities such as size, length, frequency, price, rate, number of operations, time, etc. - implied or derived quantities, such as the actual size of a file instead of a specified size - indexes, offsets, or positions into more complex data structures - symbolic keys or other elements into hash tables, associative arrays, etc. - well-formedness, i.e. syntactic correctness - compliance with expected syntax - lexical token correctness - compliance with rules for what is treated as a token - specified or derived type - the actual type of the input (or what the input appears to be) - consistency - between individual data elements, between raw data and metadata, between references, etc. - conformance to domain-specific rules, e.g. business logic - equivalence - ensuring that equivalent inputs are treated the same - authenticity, ownership, or other attestations about the input, e.g. a cryptographic signature to prove the source of the data Implied or derived properties of data must often be calculated or inferred by the code itself. Errors in deriving properties may be considered a contributing factor to improper input validation.

### 适用平台
- **Language**: Not Language-Specific (Often)
- **Technology**: AI/ML (Often)

### 常见后果
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
 **说明**: An attacker could provide unexpected values and cause a program crash or arbitrary control of resource allocation, leading to excessive consumption of resources such as memory and CPU.
- **范围**: Confidentiality
 **影响**: Read Memory, Read Files or Directories
 **说明**: An attacker could read confidential data if they are able to control resource references.
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Modify Memory, Execute Unauthorized Code or Commands
 **说明**: An attacker could use malicious input to modify data or possibly alter control flow in unexpected ways, including arbitrary command execution.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Consider using language-theoretic security (LangSec) techniques that characterize inputs using a formal language and build "recognizers" for that language. This effectively requires parsing to be a distinct layer that effectively enforces a boundary between raw input and internal data representations, instead of allowing parser code to be scattered throughout the program, where it could be subject to errors or inconsistencies that create weaknesses. [REF-1109] [REF-1110] [REF-1111]
- **阶段**: Architecture and Design
 **措施**: Use an input validation framework such as Struts or the OWASP ESAPI Validation API. Note that using a framework does not automatically address all input validation problems; be mindful of weaknesses that could arise from misusing the framework itself (CWE-1173).
- **阶段**: Architecture and Design, Implementation
 **措施**: Understand all the potential areas where untrusted inputs can enter the product, including but not limited to: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, filenames, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server. Even though client-side checks provide minimal benefits with respect to server-side security, they are still useful. First, they can support intrusion detection. If the server receives input that should have been rejected by the client, then it may be an indication of an attack. Second, client-side error-checking can provide helpful feedback to the user about the expectations for valid input. Third, there may be a reduction in server-side processing time for accidental input errors, although this is typically a small savings.
- **阶段**: Implementation
 **措施**: When your application combines data from multiple sources, perform the validation after the sources have been combined. The individual data elements may pass the validation step but violate the intended restrictions after they have been combined.
- **阶段**: Implementation
 **措施**: Be especially careful to validate all input when invoking code that crosses language boundaries, such as from an interpreted language to native code. This could create an unexpected interaction between the language boundaries. Ensure that you are not violating any of the expectations of the language with which you are interfacing. For example, even though Java may not be susceptible to buffer overflows, providing a large argument in a call to native code might trigger an overflow.
- **阶段**: Implementation
 **措施**: Directly convert your input type into the expected data type, such as using a conversion function that translates a string into a number. After converting to the expected data type, ensure that the input's values fall within the expected range of allowable values and that multi-field consistencies are maintained.
- **阶段**: Implementation
 **措施**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180, CWE-181). Make sure that your application does not inadvertently decode the same input twice (CWE-174). Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked. Use libraries such as the OWASP ESAPI Canonicalization control. Consider performing repeated canonicalization until your input does not change any more. This will avoid double-decoding and similar scenarios, but it might inadvertently modify inputs that are allowed to contain properly-encoded dangerous content.
- **阶段**: Implementation
 **措施**: When exchanging data between components, ensure that both components are using the same character encoding. Ensure that the proper encoding is applied at each interface. Explicitly set the encoding you are using whenever the protocol allows you to do so.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Some instances of improper input validation can be detected using automated static analysis. A static analysis tool might allow the user to specify which application-specific methods or functions perform input validation; the tool might also have built-in knowledge of validation frameworks such as Struts. The tool may then suppress or de-prioritize any associated warnings. This allows the analyst to focus on areas of the software in which input validation does not appear to be present. Except in the cases described in the previous paragraph, automated static analysis might not be able to recognize when proper input validation is being performed, leading to false positives - i.e., warnings that do not have any security consequences or require any code changes.
- **方法**: Manual Static Analysis
 **说明**: When custom input validation is required, such as when enforcing business rules, manual analysis is necessary to ensure that the validation is properly implemented.
- **方法**: Fuzzing
 **说明**: Fuzzing techniques can be useful for detecting input validation errors. When unexpected inputs are provided to the software, the software should not crash or otherwise become unstable, and it should generate application-controlled error messages. If exceptions or interpreter-generated error messages occur, this indicates that the input was not detected and handled within the application logic itself.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Fuzz Tester Framework-based Fuzzer ``` Cost effective for partial coverage: ``` Host Application Interface Scanner Monitored Virtual Environment - run potentially malicious code in sandbox / wrapper / virtual machine, see if it does anything suspicious
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Attack Modeling

### 相关攻击模式 (CAPEC)
- CAPEC-10
- CAPEC-101
- CAPEC-104
- CAPEC-108
- CAPEC-109
- CAPEC-110
- CAPEC-120
- CAPEC-13
- CAPEC-135
- CAPEC-136
- CAPEC-14
- CAPEC-153
- CAPEC-182
- CAPEC-209
- CAPEC-22
- CAPEC-23
- CAPEC-230
- CAPEC-231
- CAPEC-24
- CAPEC-250
- CAPEC-261
- CAPEC-267
- CAPEC-28
- CAPEC-3
- CAPEC-31
- CAPEC-42
- CAPEC-43
- CAPEC-45
- CAPEC-46
- CAPEC-47
- CAPEC-473
- CAPEC-52
- CAPEC-53
- CAPEC-588
- CAPEC-63
- CAPEC-64
- CAPEC-664
- CAPEC-67
- CAPEC-7
- CAPEC-71
- CAPEC-72
- CAPEC-73
- CAPEC-78
- CAPEC-79
- CAPEC-8
- CAPEC-80
- CAPEC-81
- CAPEC-83
- CAPEC-85
- CAPEC-88
- CAPEC-9

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:19*

---

============================================================
## CWE-200
### 弱点编号: CWE-200

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 6403

# 弱点编号: CWE-200
## 弱点名称: Exposure of Sensitive Information to an Unauthorized Actor

### Top 25 排名
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
*采集时间: 2026-07-17 13:43:12*

---

============================================================
## CWE-22
### 弱点编号: CWE-22

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 13258

# 弱点编号: CWE-22
## 弱点名称: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

### Top 25 排名
- **排名**: #5
- **综合评分**: 18.68


### 状态
Stable

### 基本描述
The product uses external input to construct a pathname that is intended to identify a file or directory that is located underneath a restricted parent directory, but the product does not properly neutralize special elements within the pathname that can cause the pathname to resolve to a location that is outside of the restricted directory.

### 详细描述
Many file operations are intended to take place within a restricted directory. By using special elements such as ".." and "/" separators, attackers can escape outside of the restricted location to access files or directories that are elsewhere on the system. One of the most common special elements is the "../" sequence, which in most modern operating systems is interpreted as the parent directory of the current location. This is referred to as relative path traversal. Path traversal also covers the use of absolute pathnames such as "/usr/local/bin" to access unexpected files. This is referred to as absolute path traversal.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: AI/ML (Often)

### 常见后果
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.
- **范围**: Integrity
 **影响**: Modify Files or Directories
 **说明**: The attacker may be able to overwrite or create critical files, such as programs, libraries, or important data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, appending a new account at the end of a password file may allow an attacker to bypass authentication.
- **范围**: Confidentiality
 **影响**: Read Files or Directories
 **说明**: The attacker may be able read the contents of unexpected files and expose sensitive data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, by reading a password file, the attacker could conduct brute force password guessing attacks in order to break into an account on the system.
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: The attacker may be able to overwrite, delete, or corrupt unexpected critical files such as programs, libraries, or important data. This may prevent the product from working at all and in the case of protection mechanisms such as authentication, it has the potential to lock out product users.

### 缓解措施
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **阶段**: Implementation
 **措施**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked. Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links (CWE-23, CWE-59). This includes: - realpath() in C - getCanonicalPath() in Java - GetFullPath() in ASP.NET - realpath() or abs_path() in Perl - realpath() in PHP
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482].
- **阶段**: Operation
 **措施**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].
- **阶段**: Architecture and Design, Operation
 **措施**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **阶段**: Architecture and Design
 **措施**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs. For example, ID 1 could map to "inbox.txt" and ID 2 could map to "profile.txt". Features such as the ESAPI AccessReferenceMap [REF-185] provide this capability.
- **阶段**: Architecture and Design, Operation
 **措施**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **阶段**: Architecture and Design, Operation
 **措施**: Store library, include, and utility files outside of the web document root, if possible. Otherwise, store them in a separate directory and use the web server's access control capabilities to prevent attackers from directly requesting them. One common practice is to define a fixed constant in each calling program, then check for the existence of the constant in the library/include file; if the constant does not exist, then the file was directly requested, and it can exit immediately. This significantly reduces the chance of an attacker being able to bypass any protection mechanisms that are in the base program but not in the include files. It will also reduce the attack surface.
- **阶段**: Implementation
 **措施**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not. In the context of path traversal, error messages which disclose path information can help attackers craft the appropriate attack strings to move through the file system hierarchy.
- **阶段**: Operation, Implementation
 **措施**: When using PHP, configure the application so that it does not use register_globals. During implementation, develop the application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated techniques can find areas where path traversal weaknesses exist. However, tuning or customization may be required to remove or de-prioritize path-traversal problems that are only exploitable by the product's administrator - or other privileged users - and thus potentially valid behavior or, at worst, a bug instead of a vulnerability.
- **方法**: Manual Static Analysis
 **说明**: Manual white box techniques may be able to provide sufficient code coverage and reduction of false positives if all file access operations can be assessed within limited time constraints.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis ``` Cost effective for partial coverage: ``` Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Manual Source Code Review (not inspections) ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-126
- CAPEC-64
- CAPEC-76
- CAPEC-78
- CAPEC-79

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:37*

---

============================================================
## CWE-287
### 弱点编号: CWE-287

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 4005

# 弱点编号: CWE-287
## 弱点名称: Improper Authentication

### Top 25 排名
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

---

============================================================
## CWE-295
### 弱点编号: CWE-295

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3275

# 弱点编号: CWE-295
## 弱点名称: Improper Certificate Validation

### Top 25 排名
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
*采集时间: 2026-07-17 13:43:56*

---

============================================================
## CWE-352
### 弱点编号: CWE-352

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 7262

# 弱点编号: CWE-352
## 弱点名称: Cross-Site Request Forgery (CSRF)

### Top 25 排名
- **排名**: #4
- **综合评分**: 19.46


### 状态
Stable

### 基本描述
The web application does not, or cannot, sufficiently verify whether a request was intentionally provided by the user who sent the request, which could have originated from an unauthorized actor.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)
- **Technology**: Web Server (Undetermined)

### 常见后果
- **范围**: Confidentiality, Integrity, Availability, Non-Repudiation, Access Control
 **影响**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data, DoS: Crash, Exit, or Restart
 **说明**: The consequences will vary depending on the nature of the functionality that is vulnerable to CSRF. An attacker could trick a client into making an unintentional request to the web server via a URL, image load, XMLHttpRequest, etc., which would then be treated as an authentic request from the client - effectively performing any operations as the victim, leading to an exposure of data, unintended code execution, etc. If the victim is an administrator or privileged user, the consequences may include obtaining complete control over the web application - deleting or stealing data, uninstalling the product, or using it to launch other attacks against all of the product's users. Because the attacker has the identity of the victim, the scope of CSRF is limited only by the victim's privileges.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. For example, use anti-CSRF packages such as the OWASP CSRFGuard. [REF-330] Another example is the ESAPI Session Management control, which includes a component for CSRF. [REF-45]
- **阶段**: Implementation
 **措施**: Ensure that the application is free of cross-site scripting issues (CWE-79), because most CSRF defenses can be bypassed using attacker-controlled script.
- **阶段**: Architecture and Design
 **措施**: Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330). [REF-332]
- **阶段**: Architecture and Design
 **措施**: Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
- **阶段**: Architecture and Design
 **措施**: Use the "double-submitted cookie" method as described by Felten and Zeller: When a user visits a site, the site should generate a pseudorandom value and set it as a cookie on the user's machine. The site should require every form submission to include this value as a form value and also as a cookie value. When a POST request is sent to the site, the request should only be considered valid if the form value and the cookie value are the same. Because of the same-origin policy, an attacker cannot read or modify the value stored in the cookie. To successfully submit a form on behalf of the user, the attacker would have to correctly guess the pseudorandom value. If the pseudorandom value is cryptographically strong, this will be prohibitively difficult. This technique requires Javascript, so it may not work for browsers that have Javascript disabled. [REF-331]
- **阶段**: Architecture and Design
 **措施**: Do not use the GET method for any request that triggers a state change.
- **阶段**: Implementation
 **措施**: Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### 检测方法
- **方法**: Manual Analysis
 **说明**: This weakness can be detected using tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. Specifically, manual analysis can be useful for finding this weakness, and for minimizing false positives assuming an understanding of business logic. However, it might not achieve desired code coverage within limited time constraints. For black-box analysis, if credentials are not known for privileged accounts, then the most security-critical portions of the application may not receive sufficient attention. Consider using OWASP CSRFTester to identify potential issues and aid in manual analysis.
- **方法**: Automated Static Analysis
 **说明**: CSRF is currently difficult to detect reliably using automated techniques. This is because each application has its own implicit security policy that dictates which requests can be influenced by an outsider and automatically performed on behalf of a user, versus which requests require strong confidence that the user intends to make the request. For example, a keyword search of the public portion of a web site is typically expected to be encoded within a link that can be launched automatically when the user clicks on the link.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Web Application Scanner
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction

### 相关攻击模式 (CAPEC)
- CAPEC-111
- CAPEC-462
- CAPEC-467
- CAPEC-62

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:33*

---

============================================================
## CWE-401
### 弱点编号: CWE-401

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3317

# 弱点编号: CWE-401
## 弱点名称: Missing Release of Memory after Effective Lifetime

### Top 25 排名
- **排名**: #21
- **综合评分**: 7.12


### 状态
Draft

### 基本描述
The product does not sufficiently track and release allocated memory after it has been used, making the memory unavailable for reallocation and reuse.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Language**: C (Undetermined)
- **Language**: C++ (Undetermined)

### 常见后果
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart, DoS: Instability, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
 **说明**: Most memory leaks result in general product reliability problems, but if an attacker can intentionally trigger a memory leak, the attacker might be able to launch a denial of service attack (by crashing or hanging the program) or take advantage of other unexpected program behavior resulting from a low memory condition.
- **范围**: Other
 **影响**: Reduce Performance

### 缓解措施
- **阶段**: Implementation
 **措施**: Choose a language or tool that provides automatic memory management, or makes manual memory management less error-prone. For example, glibc in Linux provides protection against free of invalid pointers. When using Xcode to target OS X or iOS, enable automatic reference counting (ARC) [REF-391]. To help correctly and consistently manage memory when programming in C++, consider using a smart pointer class such as std::auto_ptr (defined by ISO/IEC ISO/IEC 14882:2003), std::shared_ptr and std::unique_ptr (specified by an upcoming revision of the C++ standard, informally referred to as C++ 1x), or equivalent solutions such as Boost.
- **阶段**: Architecture and Design
 **措施**: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **阶段**: Architecture and Design, Build and Compilation
 **措施**: Consider using the Boehm-Demers-Weiser garbage collector (bdwgc), which can help avoid leaks.

### 检测方法
- **方法**: Fuzzing
 **说明**: Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518] or valgrind [REF-480].
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:28*

---

============================================================
## CWE-416
### 弱点编号: CWE-416

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3395

# 弱点编号: CWE-416
## 弱点名称: Use After Free

### Top 25 排名
- **排名**: #8
- **综合评分**: 15.49


### 状态
Stable

### 基本描述
The product reuses or references memory after it has been freed. At some point afterward, the memory may be allocated again and saved in another pointer, while the original pointer references a location somewhere within the new allocation. Any operations using the original pointer are no longer valid because the memory "belongs" to the code that operates on the new pointer.

### 适用平台
- **Language**: Memory-Unsafe (Often)
- **Language**: C (Often)
- **Language**: C++ (Often)

### 常见后果
- **范围**: Integrity
 **影响**: Modify Memory
 **说明**: The use of previously freed memory may corrupt valid data, if the memory area in question has been allocated and used properly elsewhere.
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: If chunk consolidation occurs after the use of previously freed data, the process may crash when invalid data is used as chunk information.
- **范围**: Confidentiality
 **影响**: Read Memory
 **说明**: Read operations on freed memory can sometimes leak sensitive information instead of causing a crash
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: If malicious data is entered before chunk consolidation can take place, it may be possible to take advantage of a write-what-where primitive to execute arbitrary code. If the newly allocated data happens to hold a class, in C++ for example, various function pointers may be scattered within the heap data. If one of these function pointers is overwritten with an address to valid shellcode, execution of arbitrary code can be achieved.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Choose a language that provides automatic memory management.
- **阶段**: Implementation
 **措施**: When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

### 检测方法
- **方法**: Fuzzing
 **说明**: Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:02*

---

============================================================
## CWE-434
### 弱点编号: CWE-434

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 7550

# 弱点编号: CWE-434
## 弱点名称: Unrestricted Upload of File with Dangerous Type

### Top 25 排名
- **排名**: #10
- **综合评分**: 13.42


### 状态
Draft

### 基本描述
The product allows the upload or transfer of dangerous file types that are automatically processed within its environment.

### 适用平台
- **Language**: ASP.NET (Sometimes)
- **Language**: PHP (Often)
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Web Server (Sometimes)
- **Technology**: AI/ML (Undetermined)

### 常见后果
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: Arbitrary code execution is possible if an uploaded file is interpreted and executed as code by the recipient. This is especially true for web-server extensions such as .asp and .php because these file types are often treated as automatically executable, even when file system permissions do not specify execution. For example, in Unix environments, programs typically cannot run unless the execute bit is set, but PHP programs may be executed by the web server without directly invoking them on the operating system.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Generate a new, unique filename for an uploaded file instead of using the user-supplied filename, so that no external input is used at all.[REF-422] [REF-423]
- **阶段**: Architecture and Design
 **措施**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.
- **阶段**: Architecture and Design
 **措施**: Consider storing the uploaded files outside of the web document root entirely. Then, use other mechanisms to deliver the files dynamically. [REF-423]
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. For example, limiting filenames to alphanumeric characters can help to restrict the introduction of unintended file extensions.
- **阶段**: Architecture and Design
 **措施**: Define a very limited set of allowable extensions and only generate filenames that end in these extensions. Consider the possibility of XSS (CWE-79) before allowing .html or .htm file types.
- **阶段**: Implementation
 **措施**: Ensure that only one extension is used in the filename. Some web servers, including some versions of Apache, may process files based on inner extensions so that "filename.php.gif" is fed to the PHP interpreter.[REF-422] [REF-423]
- **阶段**: Implementation
 **措施**: When running on a web server that supports case-insensitive filenames, perform case-insensitive evaluations of the extensions that are provided.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **阶段**: Implementation
 **措施**: Do not rely exclusively on sanity checks of file contents to ensure that the file is of the expected type and size. It may be possible for an attacker to hide code in some file segments that will still be executed by the server. For example, GIF images may contain a free-form comments field.
- **阶段**: Implementation
 **措施**: Do not rely exclusively on the MIME content type or filename attribute when determining how to render a file. Validating the MIME content type and ensuring that it matches the extension is only a partial solution.
- **阶段**: Architecture and Design, Operation
 **措施**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **阶段**: Architecture and Design, Operation
 **措施**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

### 检测方法
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-1

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:16*

---

============================================================
## CWE-476
### 弱点编号: CWE-476

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3921

# 弱点编号: CWE-476
## 弱点名称: NULL Pointer Dereference

### Top 25 排名
- **排名**: #14
- **综合评分**: 10.41


### 状态
Stable

### 基本描述
The product dereferences a pointer that it expects to be valid but is NULL.

### 适用平台
- **Language**: C (Undetermined)
- **Language**: C++ (Undetermined)
- **Language**: Java (Undetermined)
- **Language**: C# (Undetermined)
- **Language**: Go (Undetermined)

### 常见后果
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: NULL pointer dereferences usually result in the failure of the process unless exception handling (on some platforms) is available and implemented. Even when exception handling is being used, it can still be very difficult to return the software to a safe state of operation.
- **范围**: Integrity, Confidentiality
 **影响**: Execute Unauthorized Code or Commands, Read Memory, Modify Memory
 **说明**: In rare circumstances, when NULL is equivalent to the 0x0 memory address and privileged code can access it, then writing or reading memory is possible, which may lead to code execution.

### 缓解措施
- **阶段**: Implementation
 **措施**: For any pointers that could have been modified or provided from a function that can return NULL, check the pointer for NULL before use. When working with a multithreaded or otherwise asynchronous environment, ensure that proper locking APIs are used to lock before the check, and unlock when it has finished [REF-1484].
- **阶段**: Requirements
 **措施**: Select a programming language that is not susceptible to these issues.
- **阶段**: Implementation
 **措施**: Check the results of all functions that return a value and verify that the value is non-null before acting upon it.
- **阶段**: Architecture and Design
 **措施**: Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.
- **阶段**: Implementation
 **措施**: Explicitly initialize all variables and other data stores, either during declaration or just before the first usage.

### 检测方法
- **方法**: Automated Dynamic Analysis
 **说明**: This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **方法**: Manual Dynamic Analysis
 **说明**: Identify error conditions that are not likely to occur during normal usage and trigger them. For example, run the program under low memory conditions, run with insufficient privileges or permissions, interrupt a transaction before it is completed, or disable connectivity to basic network services such as DNS. Monitor the software for any unexpected behavior. If you trigger an unhandled exception or similar error that was discovered and handled by the application's environment, it may still indicate unexpected conditions that were not handled by the application itself.
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:44*

---

============================================================
## CWE-502
### 弱点编号: CWE-502

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 4370

# 弱点编号: CWE-502
## 弱点名称: Deserialization of Untrusted Data

### Top 25 排名
- **排名**: #15
- **综合评分**: 9.87


### 状态
Draft

### 基本描述
The product deserializes untrusted data without sufficiently ensuring that the resulting data will be valid.

### 适用平台
- **Language**: Java (Undetermined)
- **Language**: Ruby (Undetermined)
- **Language**: PHP (Undetermined)
- **Language**: Python (Undetermined)
- **Language**: JavaScript (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: ICS/OT (Often)
- **Technology**: AI/ML (Often)

### 常见后果
- **范围**: Integrity
 **影响**: Modify Application Data, Unexpected State
 **说明**: Attackers can modify unexpected objects or data that was assumed to be safe from modification. Deserialized data or code could be modified without using the provided accessor functions, or unexpected functions could be invoked.
- **范围**: Availability
 **影响**: DoS: Resource Consumption (CPU)
 **说明**: If a function is making an assumption on when to terminate, based on a sentry in a string, it could easily never terminate.
- **范围**: Other
 **影响**: Varies by Context
 **说明**: The consequences can vary widely, because it depends on which objects or methods are being deserialized, and how they are used. Making an assumption that the code in the deserialized object is valid is dangerous and can enable exploitation. One example is attackers using gadget chains to perform unauthorized actions, such as generating a shell.

### 缓解措施
- **阶段**: Architecture and Design, Implementation
 **措施**: If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.
- **阶段**: Implementation
 **措施**: When deserializing data, populate a new object rather than just deserializing. The result is that the data flows through safe input validation and that the functions are safe.
- **阶段**: Implementation
 **措施**: Explicitly define a final object() to prevent deserialization.
- **阶段**: Architecture and Design, Implementation
 **措施**: Make fields transient to protect them from deserialization. An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.
- **阶段**: Implementation
 **措施**: Avoid having unnecessary types or gadgets (a sequence of instances and method invocations that can self-execute during the deserialization process, often found in libraries) available that can be leveraged for malicious ends. This limits the potential for unintended or unauthorized types and gadgets to be leveraged by the attacker. Add only acceptable classes to an allowlist. Note: new gadgets are constantly being discovered, so this alone is not a sufficient mitigation.
- **阶段**: Architecture and Design, Implementation
 **措施**: Employ cryptography of the data or code for protection. However, it's important to note that it would still be client-side security. This is risky because if the client is compromised then the security implemented on the client (the cryptography) can be bypassed.
- **阶段**: Operation
 **措施**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-586

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:47*

---

============================================================
## CWE-611
### 弱点编号: CWE-611

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3014

# 弱点编号: CWE-611
## 弱点名称: Improper Restriction of XML External Entity Reference

### Top 25 排名
- **排名**: #23
- **综合评分**: 6.41


### 状态
Draft

### 基本描述
The product processes an XML document that can contain XML entities with URIs that resolve to documents outside of the intended sphere of control, causing the product to embed incorrect documents into its output.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Language**: XML (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)

### 常见后果
- **范围**: Confidentiality
 **影响**: Read Application Data, Read Files or Directories
 **说明**: If the attacker is able to include a crafted DTD and a default entity resolver is enabled, the attacker may be able to access arbitrary files on the system. By submitting an XML file that defines an external entity with a file:// URI, an attacker can cause the processing application to read the contents of a local file. For example, a URI such as "file:///c:/winnt/win.ini" designates (in Windows) the file C:\Winnt\win.ini, or file:///etc/passwd designates the password file in Unix-based systems. Once the content of the URI is read, it is fed back into the application that is processing the XML. This application may echo back the data (e.g., in an error message), thereby exposing the file contents.
- **范围**: Integrity
 **影响**: Bypass Protection Mechanism
 **说明**: An attacker may supply a crafted DTD using URIs with schemes such as http://, forcing the application to make outgoing HTTP requests to servers that the attacker cannot reach directly, which can be used to bypass firewall restrictions; hide the source of attacks such as port scanning; or otherwise leverage the server's trust relationship with other entities.
- **范围**: Availability
 **影响**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
 **说明**: The product could consume excessive CPU cycles or memory using a URI that points to a large file, or a device that always returns data such as /dev/random. Alternately, the URI could reference a file that contains many nested or recursive entity references to further slow down parsing.

### 缓解措施
- **阶段**: Implementation, System Configuration
 **措施**: Many XML parsers and validators can be configured to disable external entity expansion.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-221

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:41*

---

============================================================
## CWE-77
### 弱点编号: CWE-77

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 3740

# 弱点编号: CWE-77
## 弱点名称: Improper Neutralization of Special Elements used in a Command ('Command Injection')

### Top 25 排名
- **排名**: #16
- **综合评分**: 9.32


### 状态
Draft

### 基本描述
The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.

### 详细描述
Many protocols and products have their own custom command language. While OS or shell command strings are frequently discovered and targeted, developers may not realize that these other command languages might also be vulnerable to attacks.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: AI/ML (Undetermined)

### 常见后果
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: If a malicious user injects a character (such as a semi-colon) that delimits the end of one command and the beginning of another, it may be possible to then insert an entirely new and unrelated command that was not intended to be executed. This gives an attacker a privilege or capability that they would not otherwise have.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: If at all possible, use library calls rather than external processes to recreate the desired functionality.
- **阶段**: Implementation
 **措施**: If possible, ensure that all external commands called from the program are statically created.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **阶段**: Operation
 **措施**: Run time: Run time policy enforcement may be used in an allowlist fashion to prevent use of any non-sanctioned commands.
- **阶段**: System Configuration
 **措施**: Assign permissions that prevent the user from accessing/opening privileged files.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-136
- CAPEC-15
- CAPEC-183
- CAPEC-248
- CAPEC-40
- CAPEC-43
- CAPEC-75
- CAPEC-76

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:58*

---

============================================================
## CWE-78
### 弱点编号: CWE-78

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 17438

# 弱点编号: CWE-78
## 弱点名称: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

### Top 25 排名
- **排名**: #7
- **综合评分**: 15.65


### 状态
Stable

### 基本描述
The product constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component.

### 详细描述
This weakness can lead to a vulnerability in environments in which the attacker does not have direct access to the operating system, such as in web applications. Alternately, if the weakness occurs in a privileged program, it could allow the attacker to specify commands that normally would not be accessible, or to call alternate commands with privileges that the attacker does not have. The problem is exacerbated if the compromised process does not follow the principle of least privilege, because the attacker-controlled commands may run with special system privileges that increases the amount of damage. There are at least two subtypes of OS command injection: - The application intends to execute a single, fixed program that is under its own control. It intends to use externally-supplied inputs as arguments to that program. For example, the program might use system("nslookup [HOSTNAME]") to run nslookup and allow the user to supply a HOSTNAME, which is used as an argument. Attackers cannot prevent nslookup from executing. However, if the program does not remove command separators from the HOSTNAME argument, attackers could place the separators into the arguments, which allows them to execute their own program after nslookup has finished executing. - The application accepts an input that it uses to fully select which program to run, as well as which commands to use. The application simply redirects this entire command to the operating system. For example, the program might use "exec([COMMAND])" to execute the [COMMAND] that was supplied by the user. If the COMMAND is under attacker control, then the attacker can execute arbitrary commands or programs. If the command is being executed using functions like exec() and CreateProcess(), the attacker might not be able to combine multiple commands together in the same line. From a weakness standpoint, these variants represent distinct programmer errors. In the first variant, the programmer clearly intends that input from untrusted parties will be part of the arguments in the command to be executed. In the second variant, the programmer does not intend for the command to be accessible to any untrusted party, but the programmer probably has not accounted for alternate ways in which malicious attackers can provide input.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Not Technology-Specific (Undetermined)
- **Technology**: AI/ML (Often)
- **Technology**: Web Server (Often)

### 常见后果
- **范围**: Confidentiality, Integrity, Availability, Non-Repudiation
 **影响**: Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart, Read Files or Directories, Modify Files or Directories, Read Application Data, Modify Application Data, Hide Activities
 **说明**: Attackers could execute unauthorized operating system commands, which could then be used to disable the product, or read and modify data for which the attacker does not have permissions to access directly. Since the targeted application is directly executing the commands instead of the attacker, any malicious activities may appear to come from the application or the application's owner.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: If at all possible, use library calls rather than external processes to recreate the desired functionality.
- **阶段**: Architecture and Design, Operation
 **措施**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **阶段**: Architecture and Design
 **措施**: For any data that will be used to generate a command to be executed, keep as much of that data out of external control as possible. For example, in web applications, this may require storing the data locally in the session's state instead of sending it out to the client in a hidden form field.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using the ESAPI Encoding control [REF-45] or a similar tool, library, or framework. These will help the programmer encode outputs in a manner less prone to error.
- **阶段**: Implementation
 **措施**: While it is risky to use dynamically-generated query strings, code, or commands that mix control and data together, sometimes it may be unavoidable. Properly quote arguments and escape any special characters within those arguments. The most conservative approach is to escape or filter all characters that do not pass an extremely strict allowlist (such as everything that is not alphanumeric or white space). If some special characters are still needed, such as white space, wrap each argument in quotes after the escaping/filtering step. Be careful of argument injection (CWE-88).
- **阶段**: Implementation
 **措施**: If the program to be executed allows arguments to be specified within an input file or from standard input, then consider using that mode to pass arguments instead of the command line.
- **阶段**: Architecture and Design
 **措施**: If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated. Some languages offer multiple functions that can be used to invoke commands. Where possible, identify any function that invokes a command shell using a single string, and replace it with a function that requires individual arguments. These functions typically perform appropriate quoting and filtering of arguments. For example, in C, the system() function accepts a string that contains the entire command to be executed, whereas execl(), execve(), and others require an array of strings, one for each argument. In Windows, CreateProcess() only accepts one command at a time. In Perl, if system() is provided with an array of arguments, then it will quote each of the arguments.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When constructing OS command strings, use stringent allowlists that limit the character set based on the expected value of the parameter in the request. This will indirectly limit the scope of an attack, but this technique is less important than proper output encoding and escaping. Note that proper output encoding, escaping, and quoting is the most effective solution for preventing OS command injection, although input validation may provide some defense-in-depth. This is because it effectively limits what will appear in output. Input validation will not always prevent OS command injection, especially if you are required to support free-form text fields that could contain arbitrary characters. For example, when invoking a mail program, you might need to allow the subject field to contain otherwise-dangerous inputs like ";" and ">" characters, which would need to be escaped or otherwise handled. In this case, stripping the character might reduce the risk of OS command injection, but it would produce incorrect behavior because the subject field would not be recorded as the user intended. This might seem to be a minor inconvenience, but it could be more important when the program relies on well-structured subject lines in order to pass messages to other components. Even if you make a mistake in your validation (such as forgetting one out of 100 input fields), appropriate encoding is still likely to protect you from injection-based attacks. As long as it is not done in isolation, input validation is still a useful technique, since it may significantly reduce your attack surface, allow you to detect some attacks, and provide other security benefits that proper encoding does not address.
- **阶段**: Architecture and Design
 **措施**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.
- **阶段**: Operation
 **措施**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **阶段**: Operation
 **措施**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **阶段**: Implementation
 **措施**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not. In the context of OS Command Injection, error information passed back to the user might reveal whether an OS command is being executed and possibly which command is being used.
- **阶段**: Operation
 **措施**: Use runtime policy enforcement to create an allowlist of allowable commands, then prevent use of any command that does not appear in the allowlist. Technologies such as AppArmor are available to do this.
- **阶段**: Operation
 **措施**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].
- **阶段**: Architecture and Design, Operation
 **措施**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **阶段**: Operation, Implementation
 **措施**: When using PHP, configure the application so that it does not use register_globals. During implementation, develop the application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives. Automated static analysis might not be able to recognize when proper input validation is being performed, leading to false positives - i.e., warnings that do not have any security consequences or require any code changes. Automated static analysis might not be able to detect the usage of custom API functions or third-party libraries that indirectly invoke OS commands, leading to false negatives - especially if the API/library code is not available for analysis.
- **方法**: Automated Dynamic Analysis
 **说明**: This weakness can be detected using dynamic tools and techniques that interact with the product using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The product's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **方法**: Manual Static Analysis
 **说明**: Since this weakness does not typically appear frequently within a single software package, manual white box techniques may be able to provide sufficient code coverage and reduction of false positives if all potentially-vulnerable operations can be assessed within limited time constraints.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Manual Source Code Review (not inspections) ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-108
- CAPEC-15
- CAPEC-43
- CAPEC-6
- CAPEC-88

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:51*

---

============================================================
## CWE-787
### 弱点编号: CWE-787

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 6020

# 弱点编号: CWE-787
## 弱点名称: Out-of-bounds Write

### Top 25 排名
- **排名**: #2
- **综合评分**: 45.69


### 状态
Draft

### 基本描述
The product writes data past the end, or before the beginning, of the intended buffer.

### 适用平台
- **Language**: Memory-Unsafe (Often)
- **Language**: C (Often)
- **Language**: C++ (Often)
- **Language**: Assembly (Undetermined)
- **Technology**: ICS/OT (Often)

### 常见后果
- **范围**: Integrity
 **影响**: Modify Memory, Execute Unauthorized Code or Commands
 **说明**: Write operations could cause memory corruption. In some cases, an adversary can modify control data such as return addresses in order to execute unexpected code.
- **范围**: Availability
 **影响**: DoS: Crash, Exit, or Restart
 **说明**: Attempting to access out-of-range, invalid, or unauthorized memory could cause the product to crash.
- **范围**: Other
 **影响**: Unexpected State
 **说明**: Subsequent write operations can produce undefined or unexpected results.

### 缓解措施
- **阶段**: Requirements
 **措施**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, many languages that perform their own memory management, such as Java and Perl, are not subject to buffer overflows. Other languages, such as Ada and C#, typically provide overflow protection, but the protection can be disabled by the programmer. Be wary that a language's interface to native code may still be subject to overflows, even if the language itself is theoretically safe.
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. Examples include the Safe C String Library (SafeStr) by Messier and Viega [REF-57], and the Strsafe.h library from Microsoft [REF-56]. These libraries provide safer versions of overflow-prone string-handling functions.
- **阶段**: Operation, Build and Compilation
 **措施**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **阶段**: Implementation
 **措施**: Consider adhering to the following rules when allocating and managing an application's memory: - Double check that the buffer is as large as specified. - When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string. - Check buffer boundaries if accessing the buffer in a loop and make sure there is no danger of writing past the allocated space. - If necessary, truncate all input strings to a reasonable length before passing them to the copy and concatenation functions.
- **阶段**: Operation, Build and Compilation
 **措施**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **阶段**: Operation
 **措施**: Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336].
- **阶段**: Implementation
 **措施**: Replace unbounded copy functions with analogous functions that support length arguments, such as strcpy with strncpy. Create these if they are not available.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives. Automated static analysis generally does not account for environmental considerations when reporting out-of-bounds memory operations. This can make it difficult for users to determine which warnings should be investigated first. For example, an analysis tool might report buffer overflows that originate from command line arguments in a program that is not expected to run with setuid or other special privileges.
- **方法**: Automated Dynamic Analysis
 **说明**: This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **方法**: Automated Dynamic Analysis
 **说明**: Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:19*

---

============================================================
## CWE-79
### 弱点编号: CWE-79

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 12823

# 弱点编号: CWE-79
## 弱点名称: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

### Top 25 排名
- **排名**: #1
- **综合评分**: 46.82


### 状态
Stable

### 基本描述
The product does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users.

### 详细描述
There are many variants of cross-site scripting, characterized by a variety of terms or involving different attack topologies. However, they all indicate the same fundamental weakness: improper neutralization of dangerous input between the adversary and a victim.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: AI/ML (Undetermined)
- **Technology**: Web Based (Often)
- **Technology**: Web Server (Undetermined)

### 常见后果
- **范围**: Access Control, Confidentiality
 **影响**: Bypass Protection Mechanism, Read Application Data
 **说明**: The most common attack performed with cross-site scripting involves the disclosure of private information stored in user cookies, such as session information. Typically, a malicious user will craft a client-side script, which -- when parsed by a web browser -- performs some activity on behalf of the victim to an attacker-controlled system (such as sending all site cookies to a given E-mail address). This could be especially dangerous to the site if the victim has administrator privileges to manage that site. This script will be loaded and run by each user visiting the web site. Since the site requesting to run the script has access to the cookies in question, the malicious script does also.
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: In some circumstances it may be possible to run arbitrary code on a victim's computer when cross-site scripting is combined with other flaws, for example, "drive-by hacking."
- **范围**: Confidentiality, Integrity, Availability, Access Control
 **影响**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Read Application Data
 **说明**: The consequence of an XSS attack is the same regardless of whether it is stored or reflected. The difference is in how the payload arrives at the server. XSS can cause a variety of problems for the end user that range in severity from an annoyance to complete account compromise. Some cross-site scripting vulnerabilities can be exploited to manipulate or steal cookies, create requests that can be mistaken for those of a valid user, compromise confidential information, or execute malicious code on the end user systems for a variety of nefarious purposes. Other damaging attacks include the disclosure of end user files, installation of Trojan horse programs, redirecting the user to some other page or site, running "Active X" controls (under Microsoft Internet Explorer) from sites that a user perceives as trustworthy, and modifying presentation of content.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.
- **阶段**: Implementation, Architecture and Design
 **措施**: Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies. For any data that will be output to another web page, especially any data that was received from external inputs, use the appropriate encoding on all non-alphanumeric characters. Parts of the same output document may require different encodings, which will vary depending on whether the output is in the: - HTML body - Element attributes (such as src="XYZ") - URIs - JavaScript sections - Cascading Style Sheets and style property etc. Note that HTML Entity Encoding is only appropriate for the HTML body. Consult the XSS Prevention Cheat Sheet [REF-724] for more details on the types of encoding and escaping that are needed.
- **阶段**: Architecture and Design, Implementation
 **措施**: Understand all the potential areas where untrusted inputs can enter your software: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, filenames, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **阶段**: Architecture and Design
 **措施**: If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated.
- **阶段**: Implementation
 **措施**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component. The problem of inconsistent output encodings often arises in web pages. If an encoding is not specified in an HTTP header, web browsers often guess about which encoding is being used. This can open up the browser to subtle XSS attacks.
- **阶段**: Implementation
 **措施**: With Struts, write all data from form beans with the bean's filter attribute set to true.
- **阶段**: Implementation
 **措施**: To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XmlHttpRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When dynamically constructing web pages, use stringent allowlists that limit the character set based on the expected value of the parameter in the request. All input should be validated and cleansed, not just parameters that the user is supposed to specify, but all data in the request, including hidden fields, cookies, headers, the URL itself, and so forth. A common mistake that leads to continuing XSS vulnerabilities is to validate only fields that are expected to be redisplayed by the site. It is common to see data from the request that is reflected by the application server or the application that the development team did not anticipate. Also, a field that is not currently reflected may be used by a future developer. Therefore, validating ALL parts of the HTTP request is recommended. Note that proper output encoding, escaping, and quoting is the most effective solution for preventing XSS, although input validation may provide some defense-in-depth. This is because it effectively limits what will appear in output. Input validation will not always prevent XSS, especially if you are required to support free-form text fields that could contain arbitrary characters. For example, in a chat application, the heart emoticon ("<3") would likely pass the validation step, since it is commonly used. However, it cannot be directly inserted into the web page because it contains the "<" character, which would need to be escaped or otherwise handled. In this case, stripping the "<" might reduce the risk of XSS, but it would produce incorrect behavior because the emoticon would not be recorded. This might seem to be a minor inconvenience, but it would be more important in a mathematical forum that wants to represent inequalities. Even if you make a mistake in your validation (such as forgetting one out of 100 input fields), appropriate encoding is still likely to protect you from injection-based attacks. As long as it is not done in isolation, input validation is still a useful technique, since it may significantly reduce your attack surface, allow you to detect some attacks, and provide other security benefits that proper encoding does not address. Ensure that you perform input validation at well-defined interfaces within the application. This will help protect the application even if a component is reused or moved elsewhere.
- **阶段**: Architecture and Design
 **措施**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.
- **阶段**: Operation
 **措施**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].
- **阶段**: Operation, Implementation
 **措施**: When using PHP, configure the application so that it does not use register_globals. During implementation, develop the application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Use automated static analysis tools that target this type of weakness. Many modern techniques use data flow analysis to minimize the number of false positives. This is not a perfect solution, since 100% accuracy and coverage are not feasible, especially when multiple components are involved.
- **方法**: Black Box
 **说明**: Use the XSS Cheat Sheet [REF-714] or automated test-generation tools to help launch a wide variety of attacks against your web application. The Cheat Sheet contains many subtle XSS variations that are specifically targeted against weak XSS defenses.

### 相关攻击模式 (CAPEC)
- CAPEC-209
- CAPEC-588
- CAPEC-591
- CAPEC-592
- CAPEC-63
- CAPEC-85

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:15*

---

============================================================
## CWE-798
### 弱点编号: CWE-798

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 8910

# 弱点编号: CWE-798
## 弱点名称: Use of Hard-coded Credentials

### Top 25 排名
- **排名**: #24
- **综合评分**: 6.12


### 状态
Draft

### 基本描述
The product contains hard-coded credentials, such as a password or cryptographic key.

### 详细描述
There are two main variations: - Inbound: the product contains an authentication mechanism that checks the input credentials against a hard-coded set of credentials. In this variant, a default administration account is created, and a simple password is hard-coded into the product and associated with that account. This hard-coded password is the same for each installation of the product, and it usually cannot be changed or disabled by system administrators without manually modifying the program, or otherwise patching the product. It can also be difficult for the administrator to detect. - Outbound: the product connects to another system or component, and it contains hard-coded credentials for connecting to that component. This variant applies to front-end systems that authenticate with a back-end service. The back-end service may require a fixed password that can be easily discovered. The programmer may simply hard-code those back-end credentials into the front-end product.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Mobile (Undetermined)
- **Technology**: ICS/OT (Often)

### 常见后果
- **范围**: Access Control
 **影响**: Bypass Protection Mechanism
 **说明**: If hard-coded passwords are used, it is almost certain that malicious users will gain access to the account in question. Any user of the product that hard-codes passwords may be able to extract the password. Client-side systems with hard-coded passwords pose even more of a threat, since the extraction of a password from a binary is usually very simple.
- **范围**: Integrity, Confidentiality, Availability, Access Control, Other
 **影响**: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands, Other
 **说明**: This weakness can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with sensitive information or even execute arbitrary code. If the password is ever discovered or published (a common occurrence on the Internet), then anybody with knowledge of this password can access the product. Finally, since all installations of the product will have the same password, even across different organizations, this enables massive attacks such as worms to take place.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: For outbound authentication: store passwords, keys, and other credentials outside of the code in a strongly-protected, encrypted configuration file or database that is protected from access by all outsiders, including other local users on the same system. Properly protect the key (CWE-320). If you cannot use encryption to protect the file, then make sure that the permissions are as restrictive as possible [REF-7]. In Windows environments, the Encrypted File System (EFS) may provide some protection.
- **阶段**: Architecture and Design
 **措施**: For inbound authentication: Rather than hard-code a default username and password, key, or other authentication credentials for first time logins, utilize a "first login" mode that requires the user to enter a unique strong password or key.
- **阶段**: Architecture and Design
 **措施**: If the product must contain hard-coded credentials or they cannot be removed, perform access control checks and limit which entities can access the feature that requires the hard-coded credentials. For example, a feature might only be enabled through the system console instead of through a network connection.
- **阶段**: Architecture and Design
 **措施**: For inbound authentication using passwords: apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control. That way, theft of the file/database still requires the attacker to try to crack the password. When handling an incoming password during authentication, take the hash of the password and compare it to the saved hash. Use randomly assigned salts for each separate hash that is generated. This increases the amount of computation that an attacker needs to conduct a brute-force attack, possibly limiting the effectiveness of the rainbow table method.
- **阶段**: Architecture and Design
 **措施**: For front-end to back-end connections: Three solutions are possible, although none are complete. - The first suggestion involves the use of generated passwords or keys that are changed automatically and must be entered at given time intervals by a system administrator. These passwords will be held in memory and only be valid for the time intervals. - Next, the passwords or keys should be limited at the back end to only performing actions valid for the front end, as opposed to having full access. - Finally, the messages sent should be tagged and checksummed with time sensitive values so as to prevent replay-style attacks.

### 检测方法
- **方法**: Black Box
 **说明**: Credential storage in configuration files is findable using black box methods, but the use of hard-coded credentials for an incoming authentication routine typically involves an account that is not visible outside of the code.
- **方法**: Automated Static Analysis
 **说明**: Automated white box techniques have been published for detecting hard-coded credentials for incoming authentication, but there is some expert disagreement regarding their effectiveness and applicability to a broad range of methods.
- **方法**: Manual Static Analysis
 **说明**: This weakness may be detectable using manual code analysis. Unless authentication is decentralized and applied throughout the product, there can be sufficient time for the analyst to find incoming authentication routines and examine the program logic looking for usage of hard-coded credentials. Configuration files could also be analyzed.
- **方法**: Manual Dynamic Analysis
 **说明**: For hard-coded credentials in incoming authentication: use monitoring tools that examine the product's process as it interacts with the operating system and the network. This technique is useful in cases when source code is unavailable, if the product was not developed by you, or if you want to verify that the build phase did not introduce any new weaknesses. Examples include debuggers that directly attach to the running process; system-call tracing utilities such as truss (Solaris) and strace (Linux); system activity monitors such as FileMon, RegMon, Process Monitor, and other Sysinternals utilities (Windows); and sniffers and protocol analyzers that monitor network traffic. Attach the monitor to the process and perform a login. Using call trees or similar artifacts from the output, examine the associated behaviors and see if any of them appear to be comparing the input to a fixed string or value.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Network Sniffer Forced Path Execution
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Automated Static Analysis
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Configuration Checker
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction

### 相关攻击模式 (CAPEC)
- CAPEC-191
- CAPEC-70

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:52*

---

============================================================
## CWE-862
### 弱点编号: CWE-862

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 6793

# 弱点编号: CWE-862
## 弱点名称: Missing Authorization

### Top 25 排名
- **排名**: #9
- **综合评分**: 14.09


### 状态
Incomplete

### 基本描述
The product does not perform an authorization check when an actor attempts to access a resource or perform an action.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: AI/ML (Often)
- **Technology**: Web Server (Often)
- **Technology**: Database Server (Often)
- **Technology**: Not Technology-Specific (Undetermined)

### 常见后果
- **范围**: Confidentiality
 **影响**: Read Application Data, Read Files or Directories
 **说明**: An attacker could read sensitive data, either by reading the data directly from a data store that is not restricted, or by accessing insufficiently-protected, privileged functionality to read the data.
- **范围**: Integrity
 **影响**: Modify Application Data, Modify Files or Directories
 **说明**: An attacker could modify sensitive data, either by writing the data directly to a data store that is not restricted, or by accessing insufficiently-protected, privileged functionality to write the data.
- **范围**: Access Control
 **影响**: Gain Privileges or Assume Identity, Bypass Protection Mechanism
 **说明**: An attacker could gain privileges by modifying or reading critical data directly, or by accessing privileged functionality.
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
 **说明**: Automated static analysis is useful for detecting commonly-used idioms for authorization. A tool may be able to analyze related configuration files, such as .htaccess in Apache web servers, or detect the usage of commonly-used authorization libraries. Generally, automated static analysis tools have difficulty detecting custom authorization schemes. In addition, the software's design may include some functionality that is accessible to any user and does not require an authorization check; an automated technique that detects the absence of authorization may report false positives.
- **方法**: Automated Dynamic Analysis
 **说明**: Automated dynamic analysis may find many or all possible interfaces that do not require authorization, but manual analysis is required to determine if the lack of authorization violates business logic.
- **方法**: Manual Analysis
 **说明**: This weakness can be detected using tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. Specifically, manual static analysis is useful for evaluating the correctness of custom authorization mechanisms.
- **方法**: Manual Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner Database Scanners
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Host Application Interface Scanner Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction

### 相关攻击模式 (CAPEC)
- CAPEC-665

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:05*

---

============================================================
## CWE-863
### 弱点编号: CWE-863

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 7189

# 弱点编号: CWE-863
## 弱点名称: Incorrect Authorization

### Top 25 排名
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
*采集时间: 2026-07-17 13:43:25*

---

============================================================
## CWE-89
### 弱点编号: CWE-89

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 13408

# 弱点编号: CWE-89
## 弱点名称: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

### Top 25 排名
- **排名**: #3
- **综合评分**: 36.47


### 状态
Stable

### 基本描述
The product constructs all or part of an SQL command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended SQL command when it is sent to a downstream component. Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Language**: SQL (Often)
- **Technology**: Database Server (Undetermined)

### 常见后果
- **范围**: Confidentiality, Integrity, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: Adversaries could execute system commands, typically by changing the SQL statement to redirect output to a file that can then be executed.
- **范围**: Confidentiality
 **影响**: Read Application Data
 **说明**: Since SQL databases generally hold sensitive data, loss of confidentiality is a frequent problem with SQL injection vulnerabilities.
- **范围**: Authentication
 **影响**: Gain Privileges or Assume Identity, Bypass Protection Mechanism
 **说明**: If poor SQL commands are used to check user names and passwords or perform other kinds of authentication, it may be possible to connect to the product as another user with no previous knowledge of the password.
- **范围**: Access Control
 **影响**: Bypass Protection Mechanism
 **说明**: If authorization information is held in a SQL database, it may be possible to change this information through the successful exploitation of a SQL injection vulnerability.
- **范围**: Integrity
 **影响**: Modify Application Data
 **说明**: Just as it may be possible to read sensitive information, it is also possible to modify or even delete this information with a SQL injection attack.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. For example, consider using persistence layers such as Hibernate or Enterprise Java Beans, which can provide significant protection against SQL injection if used properly.
- **阶段**: Architecture and Design
 **措施**: If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated. Process SQL queries using prepared statements, parameterized queries, or stored procedures. These features should accept parameters or variables and support strong typing. Do not dynamically construct and execute query strings within these features using "exec" or similar functionality, since this may re-introduce the possibility of SQL injection. [REF-867]
- **阶段**: Architecture and Design, Operation
 **措施**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations. Specifically, follow the principle of least privilege when creating user accounts to a SQL database. The database users should only have the minimum privileges necessary to use their account. If the requirements of the system indicate that a user can read and modify their own data, then limit their privileges so they cannot read/write others' data. Use the strictest permissions possible on all database objects, such as execute-only for stored procedures.
- **阶段**: Architecture and Design
 **措施**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **阶段**: Implementation
 **措施**: While it is risky to use dynamically-generated query strings, code, or commands that mix control and data together, sometimes it may be unavoidable. Properly quote arguments and escape any special characters within those arguments. The most conservative approach is to escape or filter all characters that do not pass an extremely strict allowlist (such as everything that is not alphanumeric or white space). If some special characters are still needed, such as white space, wrap each argument in quotes after the escaping/filtering step. Be careful of argument injection (CWE-88). Instead of building a new implementation, such features may be available in the database or programming language. For example, the Oracle DBMS_ASSERT package can check or enforce that parameters have certain properties that make them less vulnerable to SQL injection. For MySQL, the mysql_real_escape_string() API function is available in both C and PHP.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When constructing SQL query strings, use stringent allowlists that limit the character set based on the expected value of the parameter in the request. This will indirectly limit the scope of an attack, but this technique is less important than proper output encoding and escaping. Note that proper output encoding, escaping, and quoting is the most effective solution for preventing SQL injection, although input validation may provide some defense-in-depth. This is because it effectively limits what will appear in output. Input validation will not always prevent SQL injection, especially if you are required to support free-form text fields that could contain arbitrary characters. For example, the name "O'Reilly" would likely pass the validation step, since it is a common last name in the English language. However, it cannot be directly inserted into the database because it contains the "'" apostrophe character, which would need to be escaped or otherwise handled. In this case, stripping the apostrophe might reduce the risk of SQL injection, but it would produce incorrect behavior because the wrong name would be recorded. When feasible, it may be safest to disallow meta-characters entirely, instead of escaping them. This will provide some defense in depth. After the data is entered into the database, later processes may neglect to escape meta-characters before use, and you may not have control over those processes.
- **阶段**: Architecture and Design
 **措施**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.
- **阶段**: Implementation
 **措施**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not. In the context of SQL Injection, error messages revealing the structure of a SQL query can help attackers tailor successful attack strings.
- **阶段**: Operation
 **措施**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481.
- **阶段**: Operation, Implementation
 **措施**: When using PHP, configure the application so that it does not use register_globals. During implementation, develop the application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives. Automated static analysis might not be able to recognize when proper input validation is being performed, leading to false positives - i.e., warnings that do not have any security consequences or do not require any code changes. Automated static analysis might not be able to detect the usage of custom API functions or third-party libraries that indirectly invoke SQL commands, leading to false negatives - especially if the API/library code is not available for analysis.
- **方法**: Automated Dynamic Analysis
 **说明**: This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **方法**: Manual Analysis
 **说明**: Manual analysis can be useful for finding this weakness, but it might not achieve desired code coverage within limited time constraints. This becomes difficult for weaknesses that must be considered for all inputs, since the attack surface can be too large.
- **方法**: Automated Static Analysis - Binary or Bytecode
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- **方法**: Dynamic Analysis with Automated Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Database Scanners ``` Cost effective for partial coverage: ``` Web Application Scanner Web Services Scanner
- **方法**: Dynamic Analysis with Manual Results Interpretation
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Cost effective for partial coverage: ``` Fuzz Tester Framework-based Fuzzer
- **方法**: Manual Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Manual Source Code Review (not inspections) ``` Cost effective for partial coverage: ``` Focused Manual Spotcheck - Focused manual analysis of source
- **方法**: Automated Static Analysis - Source Code
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- **方法**: Architecture or Design Review
 **说明**: According to SOAR [REF-1479], the following detection techniques may be useful: ``` Highly cost effective: ``` Formal Methods / Correct-By-Construction ``` Cost effective for partial coverage: ``` Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-108
- CAPEC-109
- CAPEC-110
- CAPEC-470
- CAPEC-66
- CAPEC-7

### 可利用性评估
- **利用可能性**: High

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:41:22*

---

============================================================
## CWE-918
### 弱点编号: CWE-918

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 1920

# 弱点编号: CWE-918
## 弱点名称: Server-Side Request Forgery (SSRF)

### Top 25 排名
- **排名**: #19
- **综合评分**: 7.91


### 状态
Incomplete

### 基本描述
The web server receives a URL or similar request from an upstream component and retrieves the contents of this URL, but it does not sufficiently ensure that the request is being sent to the expected destination.

### 适用平台
- **Language**: Not Language-Specific (Undetermined)
- **Technology**: Web Based (Undetermined)
- **Technology**: AI/ML (Often)
- **Technology**: Web Server (Undetermined)

### 常见后果
- **范围**: Confidentiality
 **影响**: Read Application Data
- **范围**: Integrity
 **影响**: Execute Unauthorized Code or Commands
- **范围**: Access Control
 **影响**: Bypass Protection Mechanism
 **说明**: By providing URLs to unexpected hosts or ports, attackers can make it appear that the server is sending the request, possibly bypassing access controls such as firewalls that prevent the attackers from accessing the URLs directly. The server can be used as a proxy to conduct port scanning of hosts in internal networks, use other URLs such as that can access documents on the system (using file://), or use other protocols such as gopher:// or tftp://, which may provide greater control over the contents of requests.

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-664

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:15*

---

============================================================
## CWE-94
### 弱点编号: CWE-94

**来源**: MITRE CWE | **分类**: weakness | **字符数**: 6102

# 弱点编号: CWE-94
## 弱点名称: Improper Control of Generation of Code ('Code Injection')

### Top 25 排名
- **排名**: #12
- **综合评分**: 11.91


### 状态
Draft

### 基本描述
The product constructs all or part of a code segment using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the syntax or behavior of the intended code segment.

### 适用平台
- **Language**: Interpreted (Sometimes)
- **Technology**: AI/ML (Undetermined)

### 常见后果
- **范围**: Access Control
 **影响**: Bypass Protection Mechanism
 **说明**: In some cases, injectable code controls authentication; this may lead to a remote vulnerability.
- **范围**: Access Control
 **影响**: Gain Privileges or Assume Identity
 **说明**: Injected code can access resources that the attacker is directly prevented from accessing.
- **范围**: Integrity, Confidentiality, Availability
 **影响**: Execute Unauthorized Code or Commands
 **说明**: When a product allows a user's input to contain code syntax, it might be possible for an attacker to craft the code in such a way that it will alter the intended control flow of the product. As a result, code injection can often result in the execution of arbitrary code. Code injection attacks can also lead to loss of data integrity in nearly all cases, since the control-plane data injected is always incidental to data recall or writing.
- **范围**: Non-Repudiation
 **影响**: Hide Activities
 **说明**: Often the actions performed by injected control code are unlogged.

### 缓解措施
- **阶段**: Architecture and Design
 **措施**: Refactor your program so that you do not have to dynamically generate code.
- **阶段**: Architecture and Design
 **措施**: Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which code can be executed by your product. Examples include the Unix chroot jail and AppArmor. In general, managed code may provide some protection. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **阶段**: Implementation
 **措施**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. To reduce the likelihood of code injection, use stringent allowlists that limit which constructs are allowed. If you are dynamically constructing code that invokes a function, then verifying that the input is alphanumeric might be insufficient. An attacker might still be able to reference a dangerous function that you did not intend to allow, such as system(), exec(), or exit().
- **阶段**: Testing
 **措施**: Use dynamic tools and techniques that interact with the product using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The product's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **阶段**: Operation
 **措施**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **阶段**: Operation
 **措施**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **阶段**: Implementation
 **措施**: For Python programs, it is frequently encouraged to use the ast.literal_eval() function instead of eval, since it is intentionally designed to avoid executing code. However, an adversary could still cause excessive memory or stack consumption via deeply nested structures [REF-1372], so the python documentation discourages use of ast.literal_eval() on untrusted data [REF-1373].

### 检测方法
- **方法**: Automated Static Analysis
 **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-242
- CAPEC-35
- CAPEC-77

### 可利用性评估
- **利用可能性**: Medium

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:42:30*

---

============================================================
## CWE-View-1000
### CWE 视图: 1000

**来源**: MITRE CWE | **分类**: weakness_view | **字符数**: 559

# CWE 视图: 1000
## Research Concepts

### 类型
Graph

### 状态
Draft

### 目标
This view is intended to facilitate research into weaknesses, including their inter-dependencies, and can be leveraged to systematically identify theoretical gaps within CWE. It is mainly organized according to abstractions of behaviors instead of how they can be detected, where they appear in code, or when they are introduced in the development life cycle. By design, this view is expected to include every weakness within CWE.

---
*数据来源: MITRE CWE Views*
*采集时间: 2026-07-17 13:44:06*

---

============================================================
## CWE-View-1003
### CWE 视图: 1003

**来源**: MITRE CWE | **分类**: weakness_view | **字符数**: 648

# CWE 视图: 1003
## Weaknesses for Simplified Mapping of Published Vulnerabilities

### 类型
Graph

### 状态
Incomplete

### 目标
CWE entries in this view (graph) may be used to categorize potential weaknesses within sources that handle public, third-party vulnerability information, such as the National Vulnerability Database (NVD). By design, this view is incomplete. It is limited to a small number of the most commonly-seen weaknesses, so that it is easier for humans to use. This view uses a shallow hierarchy of two levels in order to simplify the complex navigation of the entire CWE corpus.

---
*数据来源: MITRE CWE Views*
*采集时间: 2026-07-17 13:44:09*

---

============================================================
## CWE-View-699
### CWE 视图: 699

**来源**: MITRE CWE | **分类**: weakness_view | **字符数**: 580

# CWE 视图: 699
## Software Development

### 类型
Graph

### 状态
Draft

### 目标
This view organizes weaknesses around concepts that are frequently used or encountered in software development. This includes all aspects of the software development lifecycle including both architecture and implementation. Accordingly, this view can align closely with the perspectives of architects, developers, educators, and assessment vendors. It provides a variety of categories that are intended to simplify navigation, browsing, and mapping.

---
*数据来源: MITRE CWE Views*
*采集时间: 2026-07-17 13:44:19*

---

============================================================
## CAPEC_Mechanisms_of_Attack
### CAPEC (Common Attack Pattern Enumeration and Classification)

**来源**: MITRE CAPEC | **分类**: attack_pattern | **字符数**: 555

# CAPEC (Common Attack Pattern Enumeration and Classification)
## 攻击机制分类

CAPEC 由 MITRE 维护，提供了攻击模式的分类和描述。

### 九大攻击机制

### 机制 1: Engage in Deceptive Interactions (欺骗性交互)

### 机制 2: Abuse Existing Functionality (滥用现有功能)

### 机制 3: Manipulate Data Structures (操纵数据结构)

### 机制 4: Manipulate System Resources (操纵系统资源)

### 机制 5: Inject Unexpected Items (注入非预期内容)

### 机制 6: Employ Probabilistic Techniques (使用概率技术)

### 机制 7: Manipulate Timing and State (操纵时序与状态)

### 机制 8: Collect and Analyze Information (收集与分析信息)

### 机制 9: Subvert Access Control (破坏访问控制)

---

============================================================
## CAPEC_Top_Attack_Patterns
### CAPEC Top 攻击模式

**来源**: MITRE CAPEC | **分类**: attack_pattern | **字符数**: 2655

# CAPEC Top 攻击模式
## 常见攻击模式分类

### 概述
以下列举了 CAPEC 中最常见和最具代表性的攻击模式，按攻击机制分类。

---

### CAPEC-66: SQL Injection
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-66

---

### CAPEC-1: Accessing Functionality Not Properly Constrained by ACLs
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-1

---

### CAPEC-7: Blind SQL Injection
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-7

---

### CAPEC-19: Embedding Scripts within Scripts (XSS)
- **攻击机制**: Engage in Deceptive Interactions (欺骗性交互)
- **CAPEC ID**: CAPEC-19

---

### CAPEC-12: Choosing a Message/Channel Identifier on a Public/Multicast Channel
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-12

---

### CAPEC-16: Dictionary-based Password Attack
- **攻击机制**: Employ Probabilistic Techniques (使用概率技术)
- **CAPEC ID**: CAPEC-16

---

### CAPEC-49: Password Brute Forcing
- **攻击机制**: Employ Probabilistic Techniques (使用概率技术)
- **CAPEC ID**: CAPEC-49

---

### CAPEC-59: Session Credential Falsification through Prediction
- **攻击机制**: Subvert Access Control (破坏访问控制)
- **CAPEC ID**: CAPEC-59

---

### CAPEC-60: Reusing Session IDs (Session Replay)
- **攻击机制**: Subvert Access Control (破坏访问控制)
- **CAPEC ID**: CAPEC-60

---

### CAPEC-63: Token Impersonation (Privilege Escalation)
- **攻击机制**: Subvert Access Control (破坏访问控制)
- **CAPEC ID**: CAPEC-63

---

### CAPEC-86: XSS via Log Files
- **攻击机制**: Engage in Deceptive Interactions (欺骗性交互)
- **CAPEC ID**: CAPEC-86

---

### CAPEC-242: Code Injection
- **攻击机制**: Inject Unexpected Items (注入非预期内容)
- **CAPEC ID**: CAPEC-242

---

### CAPEC-88: OS Command Injection
- **攻击机制**: Inject Unexpected Items (注入非预期内容)
- **CAPEC ID**: CAPEC-88

---

### CAPEC-108: Command Line Execution through SQL Injection
- **攻击机制**: Inject Unexpected Items (注入非预期内容)
- **CAPEC ID**: CAPEC-108

---

### CAPEC-101: Server Side Request Forgery (SSRF)
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-101

---

### CAPEC-220: Client-Server Protocol Manipulation
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-220

---

### CAPEC-233: Privilege Escalation
- **攻击机制**: Subvert Access Control (破坏访问控制)
- **CAPEC ID**: CAPEC-233

---

### CAPEC-272: Protocol Manipulation
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-272

---

### CAPEC-466: Cross Site Request Forgery (CSRF)
- **攻击机制**: Engage in Deceptive Interactions (欺骗性交互)
- **CAPEC ID**: CAPEC-466

---

### CAPEC-664: Server Side Request Forgery (SSRF) via DNS Rebinding
- **攻击机制**: Abuse Existing Functionality (滥用现有功能)
- **CAPEC ID**: CAPEC-664

---

---

============================================================
## OWASP_ASVS_v4.0.3
### OWASP ASVS (Application Security Verification Standard) v4.0.3

**来源**: OWASP | **分类**: security_standard | **字符数**: 1835

# OWASP ASVS (Application Security Verification Standard) v4.0.3
## 应用安全验证标准

### 概述
OWASP ASVS 是用于应用程序安全验证的开放标准，提供了安全需求和控制的框架。

---

## V1: Architecture, Design and Threat Modeling

### 安全验证目标
确保应用系统在Design and Threat Modeling方面满足安全要求。

---

## V2: Authentication Verification Requirements

### 安全验证目标
确保应用系统在Verification Requirements方面满足安全要求。

---

## V3: Session Management Verification Requirements

### 安全验证目标
确保应用系统在Management Verification Requirements方面满足安全要求。

---

## V4: Access Control Verification Requirements

### 安全验证目标
确保应用系统在Control Verification Requirements方面满足安全要求。

---

## V5: Validation, Sanitization and Encoding Verification Requirements

### 安全验证目标
确保应用系统在Sanitization and Encoding Verification Requirements方面满足安全要求。

---

## V6: Stored Cryptography Verification Requirements

### 安全验证目标
确保应用系统在Cryptography Verification Requirements方面满足安全要求。

---

## V7: Error Handling and Logging Verification Requirements

### 安全验证目标
确保应用系统在Handling and Logging Verification Requirements方面满足安全要求。

---

## V8: Data Protection Verification Requirements

### 安全验证目标
确保应用系统在Protection Verification Requirements方面满足安全要求。

---

## V9: Communications Verification Requirements

### 安全验证目标
确保应用系统在Verification Requirements方面满足安全要求。

---

## V10: Malicious Code Verification Requirements

### 安全验证目标
确保应用系统在Code Verification Requirements方面满足安全要求。

---

## V11: Business Logic Verification Requirements

### 安全验证目标
确保应用系统在Logic Verification Requirements方面满足安全要求。

---

## V12: Files and Resources Verification Requirements

### 安全验证目标
确保应用系统在and Resources Verification Requirements方面满足安全要求。

---

## V13: API and Web Service Verification Requirements

### 安全验证目标
确保应用系统在and Web Service Verification Requirements方面满足安全要求。

---

## V14: Configuration Verification Requirements

### 安全验证目标
确保应用系统在Verification Requirements方面满足安全要求。

---

---

============================================================
## OWASP_WSTG_v4.2
### OWASP WSTG (Web Security Testing Guide) v4.2

**来源**: OWASP | **分类**: security_standard | **字符数**: 1318

# OWASP WSTG (Web Security Testing Guide) v4.2
## Web安全测试指南

### 概述
OWASP Web Security Testing Guide 是全面的 Web 应用安全测试指南，涵盖了从信息收集到客户端测试的完整测试流程。

---

## WSTG-INFO: Information Gathering (信息收集)

### 测试目标
针对Information Gathering进行系统性的安全测试。

---

## WSTG-CONF: Configuration and Deployment Management Testing (配置与部署管理测试)

### 测试目标
针对Configuration and Deployment Management Testing进行系统性的安全测试。

---

## WSTG-IDNT: Identity Management Testing (身份管理测试)

### 测试目标
针对Identity Management Testing进行系统性的安全测试。

---

## WSTG-ATHN: Authentication Testing (认证测试)

### 测试目标
针对Authentication Testing进行系统性的安全测试。

---

## WSTG-ATHZ: Authorization Testing (授权测试)

### 测试目标
针对Authorization Testing进行系统性的安全测试。

---

## WSTG-SESS: Session Management Testing (会话管理测试)

### 测试目标
针对Session Management Testing进行系统性的安全测试。

---

## WSTG-INPV: Input Validation Testing (输入验证测试)

### 测试目标
针对Input Validation Testing进行系统性的安全测试。

---

## WSTG-ERRH: Error Handling (错误处理)

### 测试目标
针对Error Handling进行系统性的安全测试。

---

## WSTG-CRYP: Cryptography (密码学)

### 测试目标
针对Cryptography进行系统性的安全测试。

---

## WSTG-BUSL: Business Logic Testing (业务逻辑测试)

### 测试目标
针对Business Logic Testing进行系统性的安全测试。

---

## WSTG-CLIENT: Client-side Testing (客户端测试)

### 测试目标
针对Client-side Testing进行系统性的安全测试。

---

## WSTG-APIT: API Testing (API测试)

### 测试目标
针对API Testing进行系统性的安全测试。

---

---

============================================================
## CISA_KEV_Catalog
### CISA Known Exploited Vulnerabilities (KEV) 目录

**来源**: NIST | **分类**: security_framework | **字符数**: 1053

# CISA Known Exploited Vulnerabilities (KEV) 目录
## 已知被利用的漏洞目录

### 概述
CISA（美国网络安全和基础设施安全局）维护的已知被利用漏洞目录，
收录了在实际攻击中被证实有活跃利用的漏洞。这是漏洞优先级管理的重要参考。

### 关键特征
- 收录的漏洞均有证据表明在野外被活跃利用
- 联邦机构必须在指定时间内修复
- 可作为漏洞管理优先级排序的重要依据

### 主要漏洞类别

#### 1. 远程代码执行 (RCE)
- 允许攻击者通过网络远程执行任意代码
- 通常影响最大，修复优先级最高
- 示例：Log4Shell (CVE-2021-44228)、ProxyShell (CVE-2021-34473)

#### 2. 权限提升 (Privilege Escalation)
- 允许低权限用户获取更高权限
- 常与RCE漏洞组合使用
- 示例：Windows Print Spooler (CVE-2021-34527)

#### 3. 认证绕过 (Authentication Bypass)
- 绕过身份验证机制获取未授权访问
- 可导致数据泄露或系统控制
- 示例：CVE-2021-40539

#### 4. 信息泄露 (Information Disclosure)
- 导致敏感信息未经授权地暴露
- 可能成为进一步攻击的跳板
- 示例：ProxyLogon (CVE-2021-26855)

### 漏洞管理建议
1. **建立资产清单**: 了解环境中运行的所有软件和硬件
2. **自动化扫描**: 持续扫描KEV中的漏洞
3. **优先级排序**: 根据CVSS评分和利用活跃度确定修复顺序
4. **补丁管理**: 建立及时部署安全补丁的流程
5. **缓解措施**: 对无法立即修补的漏洞实施补偿控制

### 参考链接
- CISA KEV 目录: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA BOD 22-01: https://www.cisa.gov/binding-operational-directive-22-01

---
*数据来源: CISA Known Exploited Vulnerabilities Catalog*
*生成时间: 2026-07-17 13:41:07*

---

============================================================
## ISO27001_2022_Framework
### ISO/IEC 27001:2022

**来源**: NIST | **分类**: security_framework | **字符数**: 1696

# ISO/IEC 27001:2022
## 信息安全、网络安全和隐私保护 — 信息安全管理体系 — 要求

### 概述
ISO/IEC 27001 是国际标准化组织发布的信息安全管理体系 (ISMS) 标准。
它提供了建立、实施、维护和持续改进信息安全管理体系的框架。

### 标准控制域 (Annex A)

---

## A.5: 信息安全策略 (Information Security Policies)

### 控制目标
确保在信息安全策略方面建立有效的信息安全管理措施。

---


## A.6: 信息安全组织 (Organization of Information Security)

### 控制目标
确保在信息安全组织方面建立有效的信息安全管理措施。

---


## A.7: 人力资源安全 (Human Resource Security)

### 控制目标
确保在人力资源安全方面建立有效的信息安全管理措施。

---


## A.8: 资产管理 (Asset Management)

### 控制目标
确保在资产管理方面建立有效的信息安全管理措施。

---


## A.9: 访问控制 (Access Control)

### 控制目标
确保在访问控制方面建立有效的信息安全管理措施。

---


## A.10: 密码学 (Cryptography)

### 控制目标
确保在密码学方面建立有效的信息安全管理措施。

---


## A.11: 物理和环境安全 (Physical and Environmental Security)

### 控制目标
确保在物理和环境安全方面建立有效的信息安全管理措施。

---


## A.12: 操作安全 (Operations Security)

### 控制目标
确保在操作安全方面建立有效的信息安全管理措施。

---


## A.13: 通信安全 (Communications Security)

### 控制目标
确保在通信安全方面建立有效的信息安全管理措施。

---


## A.14: 系统获取、开发和维护 (System Acquisition, Development and Maintenance)

### 控制目标
确保在系统获取、开发和维护方面建立有效的信息安全管理措施。

---


## A.15: 供应商关系 (Supplier Relationships)

### 控制目标
确保在供应商关系方面建立有效的信息安全管理措施。

---


## A.16: 信息安全事件管理 (Information Security Incident Management)

### 控制目标
确保在信息安全事件管理方面建立有效的信息安全管理措施。

---


## A.17: 业务连续性管理 (Business Continuity Management)

### 控制目标
确保在业务连续性管理方面建立有效的信息安全管理措施。

---


## A.18: 符合性 (Compliance)

### 控制目标
确保在符合性方面建立有效的信息安全管理措施。

---


### 与 NIST CSF 的互补关系
| ISO 27001 | NIST CSF | 说明 |
|-----------|----------|------|
| A.5 安全策略 | Govern | 政策治理 |
| A.8 资产管理 | Identify | 资产识别 |
| A.9 访问控制 | Protect | 保护控制 |
| A.12 操作安全 | Protect | 运营保护 |
| A.16 事件管理 | Respond | 事件响应 |
| A.17 业务连续性 | Recover | 恢复策略 |

---
*标准版本: ISO/IEC 27001:2022*
*生成时间: 2026-07-17 13:41:11*

---

============================================================
## NIST_CSF_2.0_Framework
### NIST Cybersecurity Framework (CSF) 2.0

**来源**: NIST | **分类**: security_framework | **字符数**: 2778

# NIST Cybersecurity Framework (CSF) 2.0
## NIST 网络安全框架 v2.0

### 基本信息
- **发布机构**: National Institute of Standards and Technology (NIST)
- **发布版本**: v2.0
- **发布日期**: 2024-02-26
- **框架类型**: 网络安全风险管理框架

### 概述
NIST 网络安全框架 (CSF) 2.0 是理解和降低网络安全风险的标准化指南框架。
它由六个核心功能 (Functions) 组成：治理 (Govern)、识别 (Identify)、保护 (Protect)、
检测 (Detect)、响应 (Respond) 和恢复 (Recover)，涵盖了网络安全风险管理的完整生命周期。

---

## GOVERN (治理) (GV)

### 功能概述
建立和监控组织的网络安全风险管理策略、期望和政策。治理为安全活动提供方向，确保与组织使命和利益相关者需求一致。

### 分类 (Categories)

#### GV.OC: Organizational Context (组织环境)
理解组织的使命、利益相关者期望、法律监管要求和风险偏好，以指导网络安全风险管理。

#### GV.RM: Risk Management Strategy (风险管理策略)
建立、沟通和监控组织的网络安全风险管理策略，包括角色、职责和问责制度。

#### GV.SC: Cybersecurity Supply Chain Risk Management (供应链风险管理)
识别、评估和管理与第三方供应商、服务提供商和合作伙伴相关的网络安全风险。

#### GV.RR: Roles, Responsibilities, and Authorities (角色职责与权限)
明确网络安全相关的角色、职责和权限，确保问责制和有效的决策。

#### GV.PO: Policies, Processes, and Procedures (政策流程与程序)
建立、维护和传达网络安全政策、流程和程序，以支持风险管理策略的执行。

#### GV.OV: Oversight (监督)
定期审查和评估网络安全风险管理活动，确保持续改进和与组织目标的协调。

---

## IDENTIFY (识别) (ID)

### 功能概述
识别和记录组织当前的网络安全风险，包括资产、业务流程、供应商和相关威胁。

### 分类 (Categories)

#### ID.AM: Asset Management (资产管理)
识别和管理支持业务目标的数据、人员、设备、系统和设施，使其与网络安全风险重要性一致。

#### ID.RA: Risk Assessment (风险评估)
理解组织运营、资产和个人的网络安全风险，包括威胁、漏洞、影响和可能性评估。

#### ID.IM: Improvement (改进)
识别组织网络安全风险管理活动和结果的改进机会，推动持续优化。

---

## PROTECT (保护) (PR)

### 功能概述
实施防护措施以防止潜在的网络安全事件，确保关键服务的韧性。

### 分类 (Categories)

#### PR.AA: Identity Management, Authentication and Access Control (身份管理与访问控制)
限制对物理和逻辑资产的访问，确保只有授权用户、服务、系统和设备可以访问。

#### PR.AT: Awareness and Training (意识与培训)
为人员提供必要的网络安全意识和技能培训，使其能够履行职责并应对威胁。

#### PR.DS: Data Security (数据安全)
确保信息在存储、传输和处理过程中的机密性、完整性和可用性 (CIA)。

#### PR.PS: Platform Security (平台安全)
确保硬件、软件（固件、操作系统、应用）和服务的安全配置和管理。

#### PR.IR: Technology Infrastructure Resilience (技术基础设施韧性)
设计和维护具有弹性的技术架构，确保系统能够承受和从攻击中恢复。

---

## DETECT (检测) (DE)

### 功能概述
及时发现潜在的网络安全事件，通过持续监控和分析识别异常和攻击。

### 分类 (Categories)

#### DE.CM: Continuous Monitoring (持续监控)
持续监控网络、系统、应用和服务，发现异常的网络安全事件和其他潜在威胁。

#### DE.AE: Adverse Event Analysis (异常事件分析)
分析检测到的异常和警报警示，识别潜在的网络安全事件，区分真实威胁和误报。

---

## RESPOND (响应) (RS)

### 功能概述
对检测到的网络安全事件采取行动，控制和减轻事件影响。

### 分类 (Categories)

#### RS.MA: Incident Management (事件管理)
实施事件响应计划，协调响应活动，与内外利益相关者沟通，确保有效的事件处理。

#### RS.AN: Incident Analysis (事件分析)
调查和取证，确定事件的范围、影响和根本原因，指导后续恢复和预防措施。

#### RS.MI: Incident Response, Reporting, and Communication (事件报告与沟通)
按照法规和组织政策要求，及时报告网络安全事件并保持透明沟通。

---

## RECOVER (恢复) (RC)

### 功能概述
从网络安全事件中恢复，恢复正常运营，并从中吸取经验教训。

### 分类 (Categories)

#### RC.RP: Incident Recovery Plan Execution (事件恢复计划执行)
执行恢复计划，确保系统、数据和服务的及时恢复，最小化停机时间。

#### RC.CO: Incident Recovery Communication (事件恢复沟通)
与内部和外部利益相关者沟通恢复进度，协调恢复活动。

---

---
*数据来源: NIST Cybersecurity Framework 2.0*
*发布日期: 2024-02-26*
*处理时间: 2026-07-17 13:41:07*

---

============================================================
## NIST_SP800-53_Rev5
### NIST SP 800-53 Rev. 5

**来源**: NIST | **分类**: security_framework | **字符数**: 2148

# NIST SP 800-53 Rev. 5
## 信息系统和组织的安全与隐私控制

### 概述
NIST Special Publication 800-53 Rev. 5 提供了全面的安全和隐私控制目录，
用于保护信息系统和组织运营，是美国联邦信息系统安全的基础标准。

### 控制家族总览
SP 800-53 包含 20 个控制家族，涵盖从访问控制到供应链风险管理的完整安全控制体系。

---


## AC: Access Control (访问控制)

### 控制目标
限制信息系统对授权用户、代表授权用户的进程或设备的访问，以及这些授权用户被允许执行的操作类型。

---


## AT: Awareness and Training (意识与培训)

### 控制目标
确保管理人员和用户了解与他们的活动相关的安全风险，以及适用的政策、标准和程序。

---


## AU: Audit and Accountability (审计与问责)

### 控制目标
创建、保护并保留信息系统审计记录，使其能够监控、分析、调查和报告非法的或非授权的系统活动。

---


## CA: Assessment, Authorization, and Monitoring (评估、授权与监控)

### 控制目标
定期评估安全控制措施的有效性，并对信息系统进行授权。

---


## CM: Configuration Management (配置管理)

### 控制目标
建立和维护信息系统和产品的基线配置，控制变更，并记录配置变更。

---


## CP: Contingency Planning (应急计划)

### 控制目标
通过计划、程序和技术措施，确保信息系统在紧急情况下的持续运行。

---


## IA: Identification and Authentication (标识与认证)

### 控制目标
识别用户、进程或设备，并验证其身份，然后才允许访问信息系统。

---


## IR: Incident Response (事件响应)

### 控制目标
建立对信息安全事件的运营层面的响应能力，包括准备、检测、分析、遏制、恢复和用户响应活动。

---


## MA: Maintenance (维护)

### 控制目标
对组织信息系统进行例行维护和修复，确保安全控制措施持续有效运行。

---


## MP: Media Protection (介质保护)

### 控制目标
保护信息系统介质（纸质和数字），限制仅授权用户访问介质上的信息，并对介质进行安全销毁或净化。

---


## PE: Physical and Environmental Protection (物理与环境安全)

### 控制目标
限制对信息系统、设备和相应操作环境的物理访问，保护免受物理和环境威胁。

---


## PL: Planning (规划)

### 控制目标
制定、记录、更新和实施安全计划，描述系统安全需求和运维环境。

---


## PM: Program Management (项目管理)

### 控制目标
在整个组织层面管理信息安全项目，为信息系统安全控制提供全组织视角。

---


## PS: Personnel Security (人员安全)

### 控制目标
确保人员（包括第三方服务提供商）可靠可信，满足既定的安全标准和政策。

---


## PT: PII Processing and Transparency (个人信息处理与透明度)

### 控制目标
确保组织以透明的方式处理 PII，并向个人提供有关 PII 处理活动的信息。

---


## RA: Risk Assessment (风险评估)

### 控制目标
评估组织运营和资产的风险，包括威胁、漏洞、可能性和影响。

---


## SA: System and Services Acquisition (系统与服务获取)

### 控制目标
在获取信息系统和服务时，确保安全需求被考虑并纳入合同和开发流程。

---


## SC: System and Communications Protection (系统与通信保护)

### 控制目标
监控、控制和保护在信息系统内部和外部传输的通信。

---


## SI: System and Information Integrity (系统与信息完整性)

### 控制目标
识别、报告并纠正信息和信息系统的缺陷，保护其免受恶意代码的攻击和未经授权的修改。

---


## SR: Supply Chain Risk Management (供应链风险管理)

### 控制目标
管理信息系统、组件和服务的供应链风险，防止供应过程中的篡改、仿冒和恶意插入。

---


---
*数据来源: NIST Special Publication 800-53 Rev. 5*
*处理时间: 2026-07-17 13:41:07*

---

============================================================
## CVE-2026-12348
### 漏洞编号: CVE-2026-12348

**来源**: NVD | **分类**: vulnerability | **字符数**: 367

# 漏洞编号: CVE-2026-12348

### 漏洞描述
Address bar spoofing in Arc Search for Android allows a remote attacker to display a trusted domain in the address bar while rendering attacker-controlled content, enabling phishing.

### 风险评估
- **CVSS 评分**: 7.4
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-1021

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35258
### 漏洞编号: CVE-2026-35258

**来源**: NVD | **分类**: vulnerability | **字符数**: 1073

# 漏洞编号: CVE-2026-35258

### 漏洞描述
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTPS to compromise WebLogic Server. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all WebLogic Server accessible data as well as unauthorized access to critical data or complete access to all WebLogic Server accessible data. CVSS 3.1 Base Score 8.7 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N).

### 风险评估
- **CVSS 评分**: 8.7
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-601

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35259
### 漏洞编号: CVE-2026-35259

**来源**: NVD | **分类**: vulnerability | **字符数**: 780

# 漏洞编号: CVE-2026-35259

### 漏洞描述
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise WebLogic Server. Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.8
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-601

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35261
### 漏洞编号: CVE-2026-35261

**来源**: NVD | **分类**: vulnerability | **字符数**: 864

# 漏洞编号: CVE-2026-35261

### 漏洞描述
Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in unauthorized update, insert or delete access to some of Oracle Access Manager accessible data as well as unauthorized read access to a subset of Oracle Access Manager accessible data. CVSS 3.1 Base Score 6.5 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N).

### 风险评估
- **CVSS 评分**: 6.5
- **严重等级**: MEDIUM

### 关联弱点类型 (CWE)
CWE-287

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35262
### 漏洞编号: CVE-2026-35262

**来源**: NVD | **分类**: vulnerability | **字符数**: 1018

# 漏洞编号: CVE-2026-35262

### 漏洞描述
Vulnerability in the Oracle Data Integrator product of Oracle Fusion Middleware (component: Market Place). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Data Integrator. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Data Integrator accessible data as well as unauthorized access to critical data or complete access to all Oracle Data Integrator accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Data Integrator. CVSS 3.1 Base Score 8.3 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L).

### 风险评估
- **CVSS 评分**: 8.3
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35263
### 漏洞编号: CVE-2026-35263

**来源**: NVD | **分类**: vulnerability | **字符数**: 811

# 漏洞编号: CVE-2026-35263

### 漏洞描述
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise WebLogic Server. While the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.9
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35265
### 漏洞编号: CVE-2026-35265

**来源**: NVD | **分类**: vulnerability | **字符数**: 698

# 漏洞编号: CVE-2026-35265

### 漏洞描述
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: Security). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.8
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35267
### 漏洞编号: CVE-2026-35267

**来源**: NVD | **分类**: vulnerability | **字符数**: 706

# 漏洞编号: CVE-2026-35267

### 漏洞描述
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: REST WebServices). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.8
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35268
### 漏洞编号: CVE-2026-35268

**来源**: NVD | **分类**: vulnerability | **字符数**: 819

# 漏洞编号: CVE-2026-35268

### 漏洞描述
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Identity Manager. While the vulnerability is in Identity Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.9
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35269
### 漏洞编号: CVE-2026-35269

**来源**: NVD | **分类**: vulnerability | **字符数**: 756

# 漏洞编号: CVE-2026-35269

### 漏洞描述
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: REST WebServices). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Identity Manager accessible data. CVSS 3.1 Base Score 7.5 (Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N).

### 风险评估
- **CVSS 评分**: 7.5
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35270
### 漏洞编号: CVE-2026-35270

**来源**: NVD | **分类**: vulnerability | **字符数**: 858

# 漏洞编号: CVE-2026-35270

### 漏洞描述
Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle WebCenter Content. While the vulnerability is in Oracle WebCenter Content, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Content. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.1
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35271
### 漏洞编号: CVE-2026-35271

**来源**: NVD | **分类**: vulnerability | **字符数**: 1075

# 漏洞编号: CVE-2026-35271

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Weblogic). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. While the vulnerability is in PeopleSoft Enterprise PT PeopleTools, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all PeopleSoft Enterprise PT PeopleTools accessible data as well as unauthorized access to critical data or complete access to all PeopleSoft Enterprise PT PeopleTools accessible data. CVSS 3.1 Base Score 8.7 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N).

### 风险评估
- **CVSS 评分**: 8.7
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35272
### 漏洞编号: CVE-2026-35272

**来源**: NVD | **分类**: vulnerability | **字符数**: 806

# 漏洞编号: CVE-2026-35272

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with logon to the infrastructure where PeopleSoft Enterprise PT PeopleTools executes to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.4 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.4
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-269

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35274
### 漏洞编号: CVE-2026-35274

**来源**: NVD | **分类**: vulnerability | **字符数**: 923

# 漏洞编号: CVE-2026-35274

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all PeopleSoft Enterprise PT PeopleTools accessible data as well as unauthorized update, insert or delete access to some of PeopleSoft Enterprise PT PeopleTools accessible data. CVSS 3.1 Base Score 8.2 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N).

### 风险评估
- **CVSS 评分**: 8.2
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35275
### 漏洞编号: CVE-2026-35275

**来源**: NVD | **分类**: vulnerability | **字符数**: 1037

# 漏洞编号: CVE-2026-35275

### 漏洞描述
Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Shared Folders). The supported version that is affected is 7.2.8. Difficult to exploit vulnerability allows low privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox. While the vulnerability is in Oracle VM VirtualBox, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle VM VirtualBox accessible data as well as unauthorized access to critical data or complete access to all Oracle VM VirtualBox accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N).

### 风险评估
- **CVSS 评分**: 7.5
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35276
### 漏洞编号: CVE-2026-35276

**来源**: NVD | **分类**: vulnerability | **字符数**: 752

# 漏洞编号: CVE-2026-35276

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Application Server). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.1
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35278
### 漏洞编号: CVE-2026-35278

**来源**: NVD | **分类**: vulnerability | **字符数**: 755

# 漏洞编号: CVE-2026-35278

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Performance Monitor). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.8
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35279
### 漏洞编号: CVE-2026-35279

**来源**: NVD | **分类**: vulnerability | **字符数**: 753

# 漏洞编号: CVE-2026-35279

### 漏洞描述
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Performance Monitor). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 8.1
- **严重等级**: HIGH

### 关联弱点类型 (CWE)
CWE-306

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35280
### 漏洞编号: CVE-2026-35280

**来源**: NVD | **分类**: vulnerability | **字符数**: 904

# 漏洞编号: CVE-2026-35280

### 漏洞描述
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.9
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## CVE-2026-35281
### 漏洞编号: CVE-2026-35281

**来源**: NVD | **分类**: vulnerability | **字符数**: 904

# 漏洞编号: CVE-2026-35281

### 漏洞描述
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 风险评估
- **CVSS 评分**: 9.9
- **严重等级**: CRITICAL

### 关联弱点类型 (CWE)
CWE-284

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: 2026-07-17 13:41:11*

---

============================================================
## AI_LLM_Security_Framework
### AI 与 LLM 安全框架

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 1763

# AI 与 LLM 安全框架
## 生成式人工智能安全风险与缓解措施

### 概述
随着大语言模型 (LLM) 和生成式 AI 的快速普及，AI 安全已成为网络安全的重要组成部分。
本框架综合了 OWASP Top 10 for LLM Applications、中国《生成式人工智能服务管理暂行办法》
以及 NIST AI RMF 的核心内容。

---

### OWASP Top 10 for LLM Applications (2025)

#### LLM01: Prompt Injection (提示注入)
- **风险**: 攻击者通过精心构造的提示词绕过安全限制，操控 LLM 输出
- **影响**: 数据泄露、权限绕过、恶意行为触发
- **缓解**: 输入过滤、输出验证、权限最小化、沙箱隔离

#### LLM02: Sensitive Information Disclosure (敏感信息泄露)
- **风险**: LLM 在训练数据中学习了敏感信息后可能在输出中泄露
- **影响**: 个人隐私泄露、商业机密曝光
- **缓解**: 数据脱敏训练、输出过滤、差分隐私

#### LLM03: Supply Chain (供应链风险)
- **风险**: 第三方模型、数据集或插件的安全漏洞
- **影响**: 模型后门、恶意行为注入
- **缓解**: 供应链审查、模型签名验证、来源追踪

#### LLM04: Data and Model Poisoning (数据与模型投毒)
- **风险**: 训练数据或模型参数被恶意篡改
- **影响**: 模型行为异常、后门植入
- **缓解**: 数据来源验证、训练过程监控、模型完整性校验

#### LLM05: Improper Output Handling (输出处理不当)
- **风险**: LLM 输出直接被用于下游操作而未经验证
- **影响**: XSS、SQL注入、代码执行
- **缓解**: 输出验证、编码转义、沙箱执行

#### LLM06: Excessive Agency (过度自主权)
- **风险**: LLM 被授予过多自主执行能力
- **影响**: 非授权操作、系统破坏
- **缓解**: 功能权限最小化、人类审核环节、操作日志

#### LLM07: System Prompt Leakage (系统提示词泄露)
- **风险**: 攻击者诱导 LLM 泄露系统级别的提示词设置
- **影响**: 安全机制暴露、越狱攻击
- **缓解**: 提示词分层设计、监控泄露尝试

#### LLM08: Vector and Embedding Weaknesses (向量与嵌入弱点)
- **风险**: RAG 知识库的向量数据库安全漏洞
- **影响**: 数据污染、检索操控
- **缓解**: 向量数据访问控制、完整性校验

#### LLM09: Misinformation and Hallucination (错误信息与幻觉)
- **风险**: LLM 生成看似合理但事实错误的内容
- **影响**: 决策误导、声誉损害
- **缓解**: 事实核查、来源引用、置信度标注

#### LLM10: Unbounded Consumption (无界资源消耗)
- **风险**: LLM 被滥用以消耗大量计算资源
- **影响**: DoS、成本爆炸
- **缓解**: 速率限制、资源配额、输入长度限制

---

### 中国 AIGC 监管框架

| 法规要求 | 核心要点 | 对应风险 |
|---------|---------|---------|
| 训练数据合规 | 数据来源合法、不侵犯知识产权 | LLM03, LLM04 |
| 内容标识 | AIGC 内容必须标识 | LLM09 |
| 安全评估 | 上线前进行安全评估 | 全部 |
| 算法备案 | 算法需向监管部门备案 | LLM06 |
| 个人信息保护 | 训练数据中的个人信息保护 | LLM02 |

---
*编制时间: 2026-07-17 13:41:06*

---

============================================================
## China_CyberLaw_System
### 中国网络安全法律法规体系

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 1159

# 中国网络安全法律法规体系
## 法律 — 行政法规 — 部门规章 三级体系

### 概述
中国已初步形成了以《网络安全法》《数据安全法》《个人信息保护法》三部基础法律为核心，
配套行政法规和部门规章的网络安全法律体系。

---

## 法律层面


### 《网络安全法》
- **生效日期**: 2017-06-01
- **修订日期**: 2025-10-28

**核心内容**:
- 网络安全等级保护制度
- 关键信息基础设施安全保护
- 个人信息保护义务
- 网络安全审查制度
- 网络运营者安全义务
- 监测预警与应急处置


### 《数据安全法》
- **生效日期**: 2021-09-01

**核心内容**:
- 数据分类分级保护
- 数据安全审查
- 数据出口管制
- 重要数据保护目录
- 数据安全风险评估
- 数据交易安全


### 《个人信息保护法》
- **生效日期**: 2021-11-01

**核心内容**:
- 个人信息处理原则（合法、正当、必要、诚信）
- 告知-同意规则
- 敏感个人信息保护
- 个人信息跨境提供规则
- 个人在信息处理活动中的权利
- 大型互联网平台义务

---

## 行政法规层面


### 《关键信息基础设施安全保护条例》
- **生效日期**: 2021-09-01

**核心内容**:
- 关键信息基础设施认定规则
- 安全保护责任与措施
- 安全检测评估
- 网络安全信息共享


### 《网络安全审查办法》
- **生效日期**: 2022-02-15

**核心内容**:
- 网络平台运营者赴国外上市审查
- 关键信息基础设施运营者采购审查
- 国家安全风险评估


### 《数据出境安全评估办法》
- **生效日期**: 2022-09-01

**核心内容**:
- 数据出境安全评估触发条件
- 评估流程与时限
- 自评估与安全评估报告

---

## 部门规章与规范性文件


### 《网络数据安全管理条例》
- **生效日期**: 2025-01-01

**核心内容**:
- 数据分类分级
- 重要数据处理
- 个人信息保护
- 数据安全评估与审查


### 《汽车数据安全管理若干规定(试行)》
- **生效日期**: 2021-10-01

**核心内容**:
- 汽车数据处理原则
- 车内座舱数据保护
- 车外数据采集规范


### 《生成式人工智能服务管理暂行办法》
- **生效日期**: 2023-08-15

**核心内容**:
- 训练数据合规要求
- AIGC内容标识
- 安全评估与算法备案

---

---
*数据整理时间: 2026-07-17 13:41:06*

---

============================================================
## Cloud_Security_Matrix
### 云安全责任共担模型与安全控制矩阵

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 1321

# 云安全责任共担模型与安全控制矩阵
## CSA (Cloud Security Alliance) 指导框架

### 概述
云安全采用责任共担模型 (Shared Responsibility Model)，云服务提供商 (CSP) 和云上用户分别承担不同层面的安全责任。

---

### 云安全责任共担模型

| 服务模型 | CSP 责任 | 用户责任 |
|---------|---------|---------|
| IaaS | 物理设施、网络、虚拟化层安全 | OS、中间件、应用、数据、IAM |
| PaaS | 物理设施、网络、虚拟化、OS、运行时 | 应用、数据、IAM、API安全 |
| SaaS | 物理设施到应用层的全栈安全 | 数据、IAM、安全配置 |

---

### CSA 云计算关键领域安全指南 v4.0

#### 领域1: 治理和企业风险管理
- 云治理框架、风险评估、合规映射
- 云服务提供商尽职调查

#### 领域2: 法律问题：合同与电子发现
- 云合同条款审查
- 数据主权与跨境数据传输
- 电子发现 (e-Discovery) 能力

#### 领域3: 合规和审计管理
- 合规框架映射 (等保/ISO/SOC)
- 持续合规监控
- 审计权力与透明度

#### 领域4: 信息治理
- 数据分类分级
- 数据生命周期管理
- 数据所有权和管理权

#### 领域5: 管理平面与业务连续性
- 云管理控制台安全
- 业务连续性和灾难恢复计划

#### 领域6: 基础设施安全
- 网络虚拟化和微分段
- 安全基线配置 (CIS Benchmarks)
- 容器和 Serverless 安全

#### 领域7: 虚拟化和容器安全
- 虚拟机逃逸防护
- 容器镜像安全扫描
- Kubernetes 安全配置

#### 领域8: 事件响应、通知和补救
- 云环境事件响应计划
- CSP 通知义务
- 取证数据获取

#### 领域9: 应用安全
- 安全软件开发生命周期 (SSDLC)
- WAAP (Web Application and API Protection)
- DevSecOps 实践

#### 领域10: 数据安全和加密
- BYOK (Bring Your Own Key)
- 传输和存储加密策略
- 数据防泄漏 (DLP)

#### 领域11: IAM (身份、权限与访问管理)
- 联合身份 (Federated Identity)
- 多因素认证 (MFA)
- 特权访问管理 (PAM)

#### 领域12: 安全即服务 (Security as a Service)
- SECaaS 分类 (SIEM、WAF、IDS等)
- 第三方安全工具的云部署

#### 领域13: 新兴技术安全
- AI/ML 安全
- IoT 安全
- 量子计算安全

---
*参考: CSA Security Guidance v4.0, NIST SP 800-144*
*编制时间: 2026-07-17 13:41:06*

---

============================================================
## Data_Security_Lifecycle
### 数据安全全生命周期管理

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 1201

# 数据安全全生命周期管理
## DSG (Data Security Governance) 框架

### 概述
数据安全是网络安全的核心组成部分。本框架综合 Gartner DSG、微软 DGPC 和中国 DSMM 的最佳实践，
覆盖数据从创建到销毁的全生命周期安全管控。

---

### 数据安全生命周期六阶段

#### 1. 数据采集 (Data Collection)
- **安全要求**:
 - 采集目的明确、合法、必要
 - 数据主体知情同意（符合个保法要求）
 - 数据分类分级标识
 - 数据源验证和完整性校验
- **关键控制**: 采集声明、同意管理、最少够用原则

#### 2. 数据传输 (Data Transmission)
- **安全要求**:
 - 传输通道加密 (TLS 1.2+)
 - 数据完整性验证
 - 跨境传输合规审查
 - 传输日志和审计
- **关键控制**: TLS/SSL、VPN、数据脱敏传输

#### 3. 数据存储 (Data Storage)
- **安全要求**:
 - 存储加密（文件级/数据库级）
 - 密钥生命周期管理
 - 介质安全与防泄漏
 - 备份与容灾
- **关键控制**: AES-256、HSM、DLP、冗余备份

#### 4. 数据处理 (Data Processing)
- **安全要求**:
 - 数据脱敏与匿名化
 - 最小权限访问控制
 - 处理环境隔离
 - 处理日志记录
- **关键控制**: 数据脱敏、RBAC、安全沙箱

#### 5. 数据交换 (Data Exchange)
- **安全要求**:
 - 数据共享审批流程
 - 数据水印与溯源
 - API 安全控制
 - 第三方安全评估
- **关键控制**: 数据水印、API 网关、审批工作流

#### 6. 数据销毁 (Data Destruction)
- **安全要求**:
 - 安全擦除标准 (DoD 5220.22-M)
 - 销毁证明和记录
 - 云端数据安全删除
 - 介质物理销毁
- **关键控制**: 安全擦除工具、销毁审计

---

### 数据分类分级模型

| 级别 | 标签 | 示例数据 | 保护要求 |
|-----|------|---------|---------|
| 1级 | 公开 | 产品文档、公开年报 | 基础保护 |
| 2级 | 内部 | 内部邮件、项目文档 | 访问控制 |
| 3级 | 机密 | 商业机密、核心算法 | 加密+审计 |
| 4级 | 绝密/重要数据 | 国家安全相关、重要民生数据 | 最高级保护 |

---
*参考框架: Gartner DSG、DSMM、DAMA-DMBOK*
*编制时间: 2026-07-17 13:41:06*

---

============================================================
## Equal_Protection_2.0_Mapping
### 等保2.0 与 NIST CSF / ISO 27001 对照表

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 1169

# 等保2.0 与 NIST CSF / ISO 27001 对照表
## 国际网络安全框架映射

### 概述
中国等保2.0 (GB/T 22239-2019) 是强制性的网络安全合规框架。以下将其与国际主流框架进行对照映射，
便于跨国组织和研究人员理解和协调合规工作。

---

### 等保2.0 安全层面与 NIST CSF 映射

| 等保2.0 安全层面 | NIST CSF 功能 | ISO 27001 控制域 |
|----------------|--------------|-----------------|
| 安全物理环境 | Protect | A.11 物理和安全环境 |
| 安全通信网络 | Protect (PR.PS) | A.13 通信安全 |
| 安全区域边界 | Detect / Protect | A.12 操作安全 |
| 安全计算环境 | Protect | A.12 / A.14 |
| 安全管理中心 | Govern / Detect | A.5 / A.6 |
| 安全管理制度 | Govern | A.5 安全策略 |
| 安全管理人员 | Govern (GV.RR) | A.7 人力资源安全 |
| 安全建设管理 | Identify | A.14 系统获取开发 |
| 安全运维管理 | Detect / Respond | A.12 / A.16 |

### 等保2.0 等级与保护要求

| 等级 | 侵害客体 | 侵害程度 | 监管强度 | 对应保护要求 |
|-----|---------|---------|---------|------------|
| 第一级 | 公民、法人和其他组织 | 一般损害 | 自主保护 | 基本防护措施 |
| 第二级 | 公民、法人和其他组织 | 严重损害 | 指导保护 | 安全审计+身份鉴别 |
| 第三级 | 社会秩序和公共利益 | 特别严重损害 | 监督保护 | 强制访问控制+双因子认证 |
| 第四级 | 国家安全 | 特别严重损害 | 强制保护 | 结构化保护 |
| 第五级 | 国家安全 | 特别严重损害 | 专控保护 | 形式化验证保护 |

### 与 CMMI / DSMM 的成熟度关联

| 等保等级 | DSMM 等级 | 说明 |
|---------|----------|------|
| 第一级 | 1-2级 | 基础数据安全能力 |
| 第二级 | 2-3级 | 规范化数据安全管理 |
| 第三级 | 3-4级 | 充分定义且量化可控 |
| 第四级以上 | 4-5级 | 量化优化，持续改进 |

---
*编制时间: 2026-07-17 13:41:06*

---

============================================================
## GB_Standards_Catalog
### 中国网络安全国家标准体系 (GB/T)

**来源**: China Standards | **分类**: regulation_and_standard | **字符数**: 2692

# 中国网络安全国家标准体系 (GB/T)
## 信息安全技术标准族

### 概述
中国网络安全国家标准体系以《网络安全法》《数据安全法》《个人信息保护法》为上位法律依据，
由全国信息安全标准化技术委员会 (TC260) 组织制定，涵盖了从等保合规到数据安全治理的完整标准框架。

---

## 等级保护 (等保2.0)


### GB/T 22239-2019: 信息安全技术 网络安全等级保护基本要求
- **英文名称**: Information Security Technology - Baseline for Classified Protection of Cybersecurity
- **标准级别**: 国家标准

**内容概述**: 规定了网络安全等级保护的基本安全要求，包括安全通用要求和安全扩展要求（云计算、移动互联、物联网、工业控制、大数据）。

**关键安全域**:
- 安全物理环境
- 安全通信网络
- 安全区域边界
- 安全计算环境
- 安全管理中心
- 安全管理制度


### GB/T 28448-2019: 信息安全技术 网络安全等级保护测评要求
- **英文名称**: Information Security Technology - Evaluation Requirements for Classified Protection of Cybersecurity
- **标准级别**: 国家标准

**内容概述**: 规定了网络安全等级保护测评的总体要求、测评指标和测评方法。


### GB/T 25070-2019: 信息安全技术 网络安全等级保护安全设计技术要求
- **英文名称**: Information Security Technology - Technical Requirements of Security Design for Classified Protection of Cybersecurity
- **标准级别**: 国家标准

**内容概述**: 规定了网络安全等级保护安全设计的技术要求。

---

## 数据安全


### GB/T 37988-2019: 信息安全技术 数据安全能力成熟度模型
- **英文名称**: DSMM - Data Security Maturity Model
- **标准级别**: 国家标准

**内容概述**: 提供了组织数据安全能力成熟度模型的框架，涵盖数据采集、传输、存储、处理、交换和销毁全生命周期。

**成熟度等级**:
- 1级: 非正式执行
- 2级: 计划跟踪
- 3级: 充分定义
- 4级: 量化控制
- 5级: 持续优化


### GB/T 35273-2020: 信息安全技术 个人信息安全规范
- **英文名称**: Information Security Technology - Personal Information Security Specification
- **标准级别**: 国家标准

**内容概述**: 规定了个人信息收集、存储、使用、共享、转让和公开披露的安全要求和保护措施。


### GB/T 39335-2020: 信息安全技术 个人信息安全影响评估指南
- **英文名称**: Information Security Technology - Personal Information Security Impact Assessment Guidelines
- **标准级别**: 国家标准

**内容概述**: 提供了个人信息安全影响评估的框架、流程和方法。

---

## 关键信息基础设施


### GB/T 39204-2020: 信息安全技术 关键信息基础设施安全保护要求
- **英文名称**: Information Security Technology - Security Protection Requirements for Critical Information Infrastructure
- **标准级别**: 国家标准

**内容概述**: 规定了关键信息基础设施安全保护的要求和措施。


### GB/T 41400-2022: 信息安全技术 关键信息基础设施安全保护指标体系
- **英文名称**: Information Security Technology - Indicator System for Critical Information Infrastructure Security
- **标准级别**: 国家标准

**内容概述**: 建立了关键信息基础设施安全保护的指标体系。

---

## 云计算安全


### GB/T 31167-2023: 信息安全技术 云计算服务安全指南
- **英文名称**: Information Security Technology - Security Guide for Cloud Computing Services
- **标准级别**: 国家标准

**内容概述**: 提供了云计算服务安全能力的分类、评估和使用指南。


### GB/T 31168-2023: 信息安全技术 云计算服务安全能力要求
- **英文名称**: Information Security Technology - Security Capability Requirements for Cloud Computing Services
- **标准级别**: 国家标准

**内容概述**: 规定了云计算服务提供商应具备的安全能力。

---

## 密码安全


### GB/T 39786-2021: 信息安全技术 信息系统密码应用基本要求
- **英文名称**: Information Security Technology - Basic Requirements for Cryptographic Application in Information Systems
- **标准级别**: 国家标准

**内容概述**: 规定了信息系统密码应用的基本要求，包括密码算法、密钥管理、密码产品和服务。

---

---
*数据整理时间: 2026-07-17 13:41:06*
*标准来源: 全国信息安全标准化技术委员会 (TC260)*

---

============================================================
## CISA_KEV_Recent_100
### CISA Known Exploited Vulnerabilities (KEV)

**来源**: CISA | **分类**: known_exploited_vulnerability | **字符数**: 46443

# CISA Known Exploited Vulnerabilities (KEV)
## 最近100个已知被利用漏洞

*更新时间: 2026-07-17 13:46:40*

## Top 10 受影响厂商

- **Microsoft**: 19 个漏洞
- **Cisco**: 8 个漏洞
- **Fortinet**: 4 个漏洞
- **Adobe**: 4 个漏洞
- **Oracle**: 3 个漏洞
- **Langflow**: 3 个漏洞
- **SimpleHelp **: 3 个漏洞
- **Ubiquiti**: 3 个漏洞
- **Ivanti**: 3 个漏洞
- **SonicWall**: 2 个漏洞

## 全部 100 条记录

### CVE-2026-58644
- **名称**: Microsoft SharePoint Deserialization of Untrusted Data Vulnerability
- **厂商**: Microsoft
- **产品**: SharePoint
- **添加日期**: 2026-07-16
- **修复截止**: 2026-07-19
- **备注**: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-58644 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-58644

---

### CVE-2026-25089
- **名称**: Fortinet FortiSandbox OS Command Injection Vulnerability
- **厂商**: Fortinet
- **产品**: FortiSandbox
- **添加日期**: 2026-07-16
- **修复截止**: 2026-07-19
- **备注**: https://fortiguard.fortinet.com/psirt/FG-IR-26-141 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-25089

---

### CVE-2026-39808
- **名称**: Fortinet FortiSandbox OS Command Injection Vulnerability
- **厂商**: Fortinet
- **产品**: FortiSandbox
- **添加日期**: 2026-07-16
- **修复截止**: 2026-07-19
- **备注**: https://fortiguard.fortinet.com/psirt/FG-IR-26-100 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-39808

---

### CVE-2026-46817
- **名称**: Oracle E-Business Suite Improper Privilege Management Vulnerability
- **厂商**: Oracle
- **产品**: E-Business Suite
- **添加日期**: 2026-07-15
- **修复截止**: 2026-07-18
- **备注**: https://www.oracle.com/security-alerts/cspumay2026.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-46817

---

### CVE-2023-4346
- **名称**: KNX Association KNX Protocol Connection Authorization Option 1 Overly Restrictive Account Lockout Mechanism Vulnerability
- **厂商**: KNX Association
- **产品**: KNX Protocol Connection Authorization Option 1
- **添加日期**: 2026-07-15
- **修复截止**: 2026-07-29
- **备注**: https://www.cisa.gov/news-events/ics-advisories/icsa-23-236-01 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2023-4346

---

### CVE-2026-56155
- **名称**: Microsoft Active Directory Federation Services Insufficient Granularity of Access Control Vulnerability 
- **厂商**: Microsoft
- **产品**: Active Directory Federation Services
- **添加日期**: 2026-07-14
- **修复截止**: 2026-07-28
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-56155 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-56155; https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/decommission/adfs-decommission-guide

---

### CVE-2026-56164
- **名称**: Microsoft SharePoint Server Missing Authentication for Critical Function Vulnerability
- **厂商**: Microsoft
- **产品**: SharePoint Server
- **添加日期**: 2026-07-14
- **修复截止**: 2026-07-17
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-56164 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-56164

---

### CVE-2026-15409
- **名称**: SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability
- **厂商**: SonicWall
- **产品**: SMA1000 Appliances
- **添加日期**: 2026-07-14
- **修复截止**: 2026-07-17
- **备注**: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-15409

---

### CVE-2026-15410
- **名称**: SonicWall SMA1000 Appliances Code Injection Vulnerability
- **厂商**: SonicWall
- **产品**: SMA1000 Appliances
- **添加日期**: 2026-07-14
- **修复截止**: 2026-07-17
- **备注**: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-15410

---

### CVE-2008-4128
- **名称**: Cisco IOS Cross-Site Request Forgery Vulnerability
- **厂商**: Cisco
- **产品**: IOS
- **添加日期**: 2026-07-13
- **修复截止**: 2026-07-16
- **备注**: https://www.cisco.com/c/en/us/obsolete/ios-nx-os-software/cisco-ios-software-releases-12-4-mainline.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2008-4128

---

### CVE-2026-56291
- **名称**: Balbooa Forms Unrestricted Upload of File with Dangerous Type Vulnerability
- **厂商**: Balbooa
- **产品**: Forms
- **添加日期**: 2026-07-10
- **修复截止**: 2026-07-13
- **备注**: https://www.balbooa.com/joomla-forms ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-56291

---

### CVE-2026-48939
- **名称**: iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability
- **厂商**: iCagenda
- **产品**: iCagenda
- **添加日期**: 2026-07-10
- **修复截止**: 2026-07-13
- **备注**: https://www.icagenda.com/#download ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-48939

---

### CVE-2026-48908
- **名称**: JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability
- **厂商**: JoomShaper
- **产品**: SP Page Builder
- **添加日期**: 2026-07-07
- **修复截止**: 2026-07-10
- **备注**: https://extensions.joomla.org/extension/sp-page-builder/ ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-48908

---

### CVE-2026-55255
- **名称**: Langflow Authorization Bypass Through User-Controlled Key Vulnerability
- **厂商**: Langflow
- **产品**: Langflow
- **添加日期**: 2026-07-07
- **修复截止**: 2026-07-10
- **备注**: https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-55255

---

### CVE-2026-56290
- **名称**: Joomlack Page Builder Improper Access Control Vulnerability
- **厂商**: Joomlack
- **产品**: Page Builder
- **添加日期**: 2026-07-07
- **修复截止**: 2026-07-10
- **备注**: https://www.joomlack.fr/en/joomla-extensions/page-builder-ck ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-56290

---

### CVE-2026-48282
- **名称**: Adobe ColdFusion Path Traversal Vulnerability
- **厂商**: Adobe
- **产品**: ColdFusion
- **添加日期**: 2026-07-07
- **修复截止**: 2026-07-10
- **备注**: https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-48282

---

### CVE-2026-45659
- **名称**: Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability
- **厂商**: Microsoft
- **产品**: SharePoint Server
- **添加日期**: 2026-07-01
- **修复截止**: 2026-07-04
- **备注**: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-45659

---

### CVE-2026-48558
- **名称**: SimpleHelp Authentication Bypass Vulnerability
- **厂商**: SimpleHelp 
- **产品**: SimpleHelp
- **添加日期**: 2026-06-29
- **修复截止**: 2026-07-02
- **备注**: https://simple-help.com/security/simplehelp-security-update-2026-05 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-48558

---

### CVE-2026-12569
- **名称**: PTC Windchill and FlexPLM Improper Input Validation Vulnerability
- **厂商**: PTC
- **产品**: Windchill and FlexPLM
- **添加日期**: 2026-06-25
- **修复截止**: 2026-06-28
- **备注**: https://www.ptc.com/en/support/article/CS473270 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-12569

---

### CVE-2026-20230
- **名称**: Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability
- **厂商**: Cisco
- **产品**: Unified Communications Manager
- **添加日期**: 2026-06-25
- **修复截止**: 2026-06-28
- **备注**: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssrf-cXPnHcW.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-20230

---

### CVE-2025-67038
- **名称**: Lantronix EDS5000 Code Injection Vulnerability
- **厂商**: Lantronix
- **产品**: EDS5000
- **添加日期**: 2026-06-23
- **修复截止**: 2026-06-26
- **备注**: https://ltrxdev.atlassian.net/wiki/spaces/LTRXTS/pages/2538438657/Latest+Firmware+for+the+EDS5000+series+EDS5008+EDS5016+EDS5032 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2025-67038

---

### CVE-2026-34910
- **名称**: Ubiquiti UniFi OS Improper Input Validation Vulnerability
- **厂商**: Ubiquiti
- **产品**: UniFi OS
- **添加日期**: 2026-06-23
- **修复截止**: 2026-06-26
- **备注**: https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-34910

---

### CVE-2026-34909
- **名称**: Ubiquiti UniFi OS Path Traversal Vulnerability
- **厂商**: Ubiquiti
- **产品**: UniFi OS
- **添加日期**: 2026-06-23
- **修复截止**: 2026-06-26
- **备注**: https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-34909

---

### CVE-2026-34908
- **名称**: Ubiquiti UniFi OS Improper Access Control Vulnerability
- **厂商**: Ubiquiti
- **产品**: UniFi OS
- **添加日期**: 2026-06-23
- **修复截止**: 2026-06-26
- **备注**: https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-34908

---

### CVE-2026-20253
- **名称**: Splunk Enterprise Missing Authentication for Critical Function Vulnerability
- **厂商**: Splunk
- **产品**: Enterprise
- **添加日期**: 2026-06-18
- **修复截止**: 2026-06-21
- **备注**: https://advisory.splunk.com/advisories/SVD-2026-0603 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-20253

---

### CVE-2026-48907
- **名称**: Widget Factory Joomla Content Editor Improper Access Control Vulnerability
- **厂商**: Widget Factory
- **产品**: Joomla Content Editor 
- **添加日期**: 2026-06-16
- **修复截止**: 2026-06-19
- **备注**: https://www.joomlacontenteditor.net/news/jce-security-update-and-a-free-patch-for-older-sites ; https://www.joomlacontenteditor.net/support/changelog/editor ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-48907

---

### CVE-2026-54420
- **名称**: LiteSpeed cPanel Plugin UNIX Symbolic Link (Symlink) Following Vulnerability
- **厂商**: LiteSpeed
- **产品**: cPanel Plugin
- **添加日期**: 2026-06-15
- **修复截止**: 2026-06-18
- **备注**: https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/ ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-54420

---

### CVE-2026-20262
- **名称**: Cisco Catalyst SD-WAN Manager Directory or Path Traversal Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN Manager
- **添加日期**: 2026-06-15
- **修复截止**: 2026-06-29
- **备注**: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-20262

---

### CVE-2026-35273
- **名称**: Oracle PeopleSoft Enterprise PeopleTools Missing Authentication for Critical Function Vulnerability
- **厂商**: Oracle
- **产品**: PeopleSoft Enterprise PeopleTools
- **添加日期**: 2026-06-12
- **修复截止**: 2026-06-15
- **备注**: https://www.oracle.com/security-alerts/alert-cve-2026-35273.html ; https://support.oracle.com/signin/ ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-35273

---

### CVE-2026-10520
- **名称**: Ivanti Sentry OS Command Injection Vulnerability
- **厂商**: Ivanti
- **产品**: Sentry
- **添加日期**: 2026-06-11
- **修复截止**: 2026-06-14
- **备注**: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-10520

---

### CVE-2026-11645
- **名称**: Google Chromium V8 Out-of-Bounds Read and Write Vulnerability
- **厂商**: Google
- **产品**: Chromium V8
- **添加日期**: 2026-06-09
- **修复截止**: 2026-06-23
- **备注**: https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0153744567.html ; https://issues.chromium.org/issues/506689381 ; https://nvd.nist.gov/vuln/detail/CVE-2026-11645

---

### CVE-2026-7473
- **名称**: Arista Extensible Operating System Incomplete Comparison with Missing Factors Vulnerability
- **厂商**: Arista
- **产品**: Extensible Operating System
- **添加日期**: 2026-06-09
- **修复截止**: 2026-06-23
- **备注**: https://www.arista.com/en/support/advisories-notices/security-advisory/24005-security-advisory-0137 ; https://nvd.nist.gov/vuln/detail/CVE-2026-7473

---

### CVE-2026-20245
- **名称**: Cisco Catalyst SD-WAN Manager Improper Encoding or Escaping of Output Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN Manager
- **添加日期**: 2026-06-09
- **修复截止**: 2026-06-23
- **备注**: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx ; https://nvd.nist.gov/vuln/detail/CVE-2026-20245

---

### CVE-2026-42271
- **名称**: BerriAI LiteLLM Command Injection Vulnerability
- **厂商**: BerriAI
- **产品**: LiteLLM
- **添加日期**: 2026-06-08
- **修复截止**: 2026-06-22
- **备注**: This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see: https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g ; https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable ; https://nvd.nist.gov/vuln/detail/CVE-2026-42271

---

### CVE-2026-50751
- **名称**: Check Point Security Gateway Improper Authentication Vulnerability
- **厂商**: Check Point
- **产品**: Security Gateway
- **添加日期**: 2026-06-08
- **修复截止**: 2026-06-11
- **备注**: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/ ; https://support.checkpoint.com/results/sk/sk185033?_gl=1*1wqeqhc*_gcl_au*MTI1MzE5MjI2LjE3ODA5MzQ1NTM. ; https://nvd.nist.gov/vuln/detail/CVE-2026-50751

---

### CVE-2026-28318
- **名称**: SolarWinds Serv-U Uncontrolled Resource Consumption Vulnerability
- **厂商**: SolarWinds
- **产品**: Serv-U
- **添加日期**: 2026-06-05
- **修复截止**: 2026-06-19
- **备注**: https://www.solarwinds.com/trust-center/security-advisories/cve-2026-28318 ; https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_15-5-4-hotfix-1_release_notes.htm#link7 ; https://nvd.nist.gov/vuln/detail/CVE-2026-28318

---

### CVE-2026-45247
- **名称**: Mirasvit Full Page Cache Warmer Deserialization of Untrusted Data Vulnerability
- **厂商**: Mirasvit
- **产品**: Mirasvit Full Page Cache Warmer
- **添加日期**: 2026-06-03
- **修复截止**: 2026-06-06
- **备注**: https://mirasvit.com/package/changelog/?package=mirasvit/module-cache-warmer ; https://nvd.nist.gov/vuln/detail/CVE-2026-45247

---

### CVE-2022-0492
- **名称**: Linux Kernel Improper Authentication Vulnerability
- **厂商**: Linux
- **产品**: Kernel
- **添加日期**: 2026-06-02
- **修复截止**: 2026-06-05
- **备注**: This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=24f6008564183aa120d07c03d9289519c2fe02af ; https://www.kernel.org/ ; https://nvd.nist.gov/vuln/detail/CVE-2022-0492

---

### CVE-2025-48595
- **名称**: Android Framework Integer Overflow Vulnerability
- **厂商**: Android
- **产品**: Framework
- **添加日期**: 2026-06-02
- **修复截止**: 2026-06-05
- **备注**: https://source.android.com/docs/security/bulletin/2026/2026-06-01 ; https://nvd.nist.gov/vuln/detail/CVE-2025-48595

---

### CVE-2024-21182
- **名称**: Oracle WebLogic Server Unspecified Vulnerability
- **厂商**: Oracle
- **产品**: WebLogic Server
- **添加日期**: 2026-06-01
- **修复截止**: 2026-06-04
- **备注**: https://www.oracle.com/security-alerts/cpujul2024.html ; https://nvd.nist.gov/vuln/detail/CVE-2024-21182

---

### CVE-2026-0257
- **名称**: Palo Alto Networks PAN-OS Authentication Bypass Vulnerability
- **厂商**: Palo Alto Networks
- **产品**: PAN-OS
- **添加日期**: 2026-05-29
- **修复截止**: 2026-06-01
- **备注**: https://security.paloaltonetworks.com/CVE-2026-0257 ; https://nvd.nist.gov/vuln/detail/CVE-2026-0257

---

### CVE-2026-48027
- **名称**: Nx Console Embedded Malicious Code Vulnerability
- **厂商**: Nx
- **产品**: Nx Console
- **添加日期**: 2026-05-27
- **修复截止**: 2026-06-10
- **备注**: This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w ; https://nvd.nist.gov/vuln/detail/CVE-2026-48027

---

### CVE-2026-45321
- **名称**: TanStack Unspecified Vulnerability
- **厂商**: TanStack
- **产品**: TanStack
- **添加日期**: 2026-05-27
- **修复截止**: 2026-06-10
- **备注**: This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx ; https://nvd.nist.gov/vuln/detail/CVE-2026-45321

---

### CVE-2026-8398
- **名称**: Daemon Tools Lite Embedded Malicious Code Vulnerability
- **厂商**: Daemon
- **产品**: Daemon Tools Lite
- **添加日期**: 2026-05-27
- **修复截止**: 2026-05-30
- **备注**: https://blog.daemon-tools.cc/post/security-incident ; https://nvd.nist.gov/vuln/detail/CVE-2026-8398

---

### CVE-2026-48172
- **名称**: LiteSpeed cPanel Plugin Privilege Escalation Vulnerability
- **厂商**: LiteSpeed
- **产品**: cPanel Plugin
- **添加日期**: 2026-05-26
- **修复截止**: 2026-05-29
- **备注**: https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/ ; https://nvd.nist.gov/vuln/detail/CVE-2026-48172

---

### CVE-2026-9082
- **名称**: Drupal Core SQL Injection Vulnerability
- **厂商**: Drupal
- **产品**: Core
- **添加日期**: 2026-05-22
- **修复截止**: 2026-05-27
- **备注**: https://www.drupal.org/sa-core-2026-004 ; https://nvd.nist.gov/vuln/detail/CVE-2026-9082

---

### CVE-2025-34291
- **名称**: Langflow Origin Validation Error Vulnerability
- **厂商**: Langflow
- **产品**: Langflow
- **添加日期**: 2026-05-21
- **修复截止**: 2026-06-04
- **备注**: This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/langflow-ai/langflow ; https://github.com/langflow-ai/langflow/releases/tag/v1.9.3; https://github.com/langflow-ai/langflow/issues/11465#event-25774545848 ; https://nvd.nist.gov/vuln/detail/CVE-2025-34291

---

### CVE-2026-34926
- **名称**: Trend Micro Apex One (On-Premise) Directory Traversal Vulnerability
- **厂商**: Trend Micro
- **产品**: Apex One
- **添加日期**: 2026-05-21
- **修复截止**: 2026-06-04
- **备注**: https://success.trendmicro.com/en-US/solution/KA-0023430 ; https://nvd.nist.gov/vuln/detail/CVE-2026-34926

---

### CVE-2008-4250
- **名称**: Microsoft Windows Buffer Overflow Vulnerability
- **厂商**: Microsoft
- **产品**: Windows
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067 ; https://nvd.nist.gov/vuln/detail/CVE-2008-4250

---

### CVE-2009-1537
- **名称**: Microsoft DirectX NULL Byte Overwrite Vulnerability
- **厂商**: Microsoft
- **产品**: DirectX
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2009/ms09-028 ; https://nvd.nist.gov/vuln/detail/CVE-2009-1537

---

### CVE-2009-3459
- **名称**: Adobe Acrobat and Reader Heap-Based Buffer Overflow Vulnerability
- **厂商**: Adobe
- **产品**: Acrobat and Reader
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://www.cisa.gov/news-events/alerts/2009/10/13/adobe-reader-and-acrobat-vulnerabilities ; https://web.archive.org/web/20120324170253/http://www.adobe.com/support/security/bulletins/apsb09-15.html#:~:text=CVE%2D2009%2D3459).-,NOTE%3A,-There%20are%20reports ; https://nvd.nist.gov/vuln/detail/CVE-2009-3459

---

### CVE-2010-0249
- **名称**: Microsoft Internet Explorer Use-After-Free Vulnerability
- **厂商**: Microsoft
- **产品**: Internet Explorer
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://learn.microsoft.com/en-us/security-updates/SecurityAdvisories/2010/979352 ; https://nvd.nist.gov/vuln/detail/CVE-2010-0249

---

### CVE-2010-0806
- **名称**: Microsoft Internet Explorer Use-After-Free Vulnerability
- **厂商**: Microsoft
- **产品**: Internet Explorer
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://learn.microsoft.com/en-us/security-updates/securityadvisories/2010/981374 ; https://nvd.nist.gov/vuln/detail/CVE-2010-0806

---

### CVE-2026-41091
- **名称**: Microsoft Defender Link Following Vulnerability
- **厂商**: Microsoft
- **产品**: Defender
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41091 ; https://nvd.nist.gov/vuln/detail/CVE-2026-41091

---

### CVE-2026-45498
- **名称**: Microsoft Defender Denial of Service Vulnerability
- **厂商**: Microsoft
- **产品**: Defender
- **添加日期**: 2026-05-20
- **修复截止**: 2026-06-03
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45498 ; https://nvd.nist.gov/vuln/detail/CVE-2026-45498

---

### CVE-2026-42897
- **名称**: Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **厂商**: Microsoft
- **产品**: Microsoft
- **添加日期**: 2026-05-15
- **修复截止**: 2026-05-29
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42897 ; https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service ; https://nvd.nist.gov/vuln/detail/CVE-2026-42897

---

### CVE-2026-20182
- **名称**: Cisco Catalyst SD-WAN Controller Authentication Bypass Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN
- **添加日期**: 2026-05-14
- **修复截止**: 2026-05-17
- **备注**: CISA Mitigation Instructions: https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems ; https://www.cisa.gov/news-events/directives/supplemental-direction-ed-26-03-hunt-and-hardening-guidance-cisco-sd-wan-systems ; https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW ; https://nvd.nist.gov/vuln/detail/CVE-2026-20182

---

### CVE-2026-42208
- **名称**: BerriAI LiteLLM SQL Injection Vulnerability
- **厂商**: BerriAI
- **产品**: LiteLLM
- **添加日期**: 2026-05-08
- **修复截止**: 2026-05-11
- **备注**: https://github.com/BerriAI/litellm/security/advisories/GHSA-r75f-5x8p-qvmc ; https://nvd.nist.gov/vuln/detail/CVE-2026-42208

---

### CVE-2026-6973
- **名称**: Ivanti Endpoint Manager Mobile (EPMM) Improper Input Validation Vulnerability
- **厂商**: Ivanti
- **产品**: Endpoint Manager Mobile (EPMM)
- **添加日期**: 2026-05-07
- **修复截止**: 2026-05-10
- **备注**: https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-Multiple-CVEs?language=en_US ; https://nvd.nist.gov/vuln/detail/CVE-2026-6973

---

### CVE-2026-0300
- **名称**: Palo Alto Networks PAN-OS Out-of-bounds Write Vulnerability
- **厂商**: Palo Alto Networks
- **产品**: PAN-OS
- **添加日期**: 2026-05-06
- **修复截止**: 2026-05-09
- **备注**: https://security.paloaltonetworks.com/CVE-2026-0300 ; https://nvd.nist.gov/vuln/detail/CVE-2026-0300

---

### CVE-2026-31431
- **名称**: Linux Kernel Incorrect Resource Transfer Between Spheres Vulnerability
- **厂商**: Linux
- **产品**: Kernel
- **添加日期**: 2026-05-01
- **修复截止**: 2026-05-15
- **备注**: https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/; https://xint.io/blog/copy-fail-linux-distributions#the-fix-6 ; https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/ ; https://nvd.nist.gov/vuln/detail/CVE-2026-31431

---

### CVE-2026-41940
- **名称**: WebPros cPanel & WHM and WP2 (WordPress Squared) Missing Authentication for Critical Function Vulnerability
- **厂商**: WebPros
- **产品**: cPanel & WHM and WP2 (WordPress Squared)
- **添加日期**: 2026-04-30
- **修复截止**: 2026-05-03
- **备注**: https://support.cpanel.net/hc/en-us/articles/40073787579671-cPanel-WHM-Security-Update-04-28-2026 ; https://docs.cpanel.net/release-notes/release-notes/ ; https://docs.wpsquared.com/changelogs/versions/changelog/#13617 ; https://nvd.nist.gov/vuln/detail/CVE-2026-41940"

---

### CVE-2024-1708
- **名称**: ConnectWise ScreenConnect Path Traversal Vulnerability
- **厂商**: ConnectWise
- **产品**: ScreenConnect
- **添加日期**: 2026-04-28
- **修复截止**: 2026-05-12
- **备注**: https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8 ; https://nvd.nist.gov/vuln/detail/CVE-2024-1708

---

### CVE-2026-32202
- **名称**: Microsoft Windows Protection Mechanism Failure Vulnerability
- **厂商**: Microsoft
- **产品**: Windows
- **添加日期**: 2026-04-28
- **修复截止**: 2026-05-12
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-32202 ; https://nvd.nist.gov/vuln/detail/CVE-2026-32202

---

### CVE-2025-29635
- **名称**: D-Link DIR-823X Command Injection Vulnerability
- **厂商**: D-Link
- **产品**: DIR-823X
- **添加日期**: 2026-04-24
- **修复截止**: 2026-05-08
- **备注**: https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10469 ; https://nvd.nist.gov/vuln/detail/CVE-2025-29635

---

### CVE-2024-7399
- **名称**: Samsung MagicINFO 9 Server Path Traversal Vulnerability
- **厂商**: Samsung
- **产品**: MagicINFO 9 Server
- **添加日期**: 2026-04-24
- **修复截止**: 2026-05-08
- **备注**: https://security.samsungtv.com/securityUpdates ; https://nvd.nist.gov/vuln/detail/CVE-2024-7399

---

### CVE-2024-57728
- **名称**: SimpleHelp Path Traversal Vulnerability
- **厂商**: SimpleHelp 
- **产品**: SimpleHelp
- **添加日期**: 2026-04-24
- **修复截止**: 2026-05-08
- **备注**: https://simple-help.com/kb---security-vulnerabilities-01-2025#security-vulnerabilities-in-simplehelp-5-5-7-and-earlier ; https://nvd.nist.gov/vuln/detail/CVE-2024-57728

---

### CVE-2024-57726
- **名称**: SimpleHelp Missing Authorization Vulnerability
- **厂商**: SimpleHelp 
- **产品**: SimpleHelp
- **添加日期**: 2026-04-24
- **修复截止**: 2026-05-08
- **备注**: https://simple-help.com/kb---security-vulnerabilities-01-2025#security-vulnerabilities-in-simplehelp-5-5-7-and-earlier ; https://nvd.nist.gov/vuln/detail/CVE-2024-57726

---

### CVE-2026-39987
- **名称**: Marimo Remote Code Execution Vulnerability
- **厂商**: Marimo
- **产品**: Marimo
- **添加日期**: 2026-04-23
- **修复截止**: 2026-05-07
- **备注**: https://github.com/marimo-team/marimo/security/advisories/GHSA-2679-6mx9-h9xc ; https://nvd.nist.gov/vuln/detail/CVE-2026-39987

---

### CVE-2026-33825
- **名称**: Microsoft Defender Insufficient Granularity of Access Control Vulnerability
- **厂商**: Microsoft
- **产品**: Defender
- **添加日期**: 2026-04-22
- **修复截止**: 2026-05-06
- **备注**: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825 ; https://nvd.nist.gov/vuln/detail/CVE-2026-33825

---

### CVE-2026-20122
- **名称**: Cisco Catalyst SD-WAN Manager Incorrect Use of Privileged APIs Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN Manger
- **添加日期**: 2026-04-20
- **修复截止**: 2026-04-23
- **备注**: CISA Mitigation Instructions: https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems ; https://www.cisa.gov/news-events/directives/supplemental-direction-ed-26-03-hunt-and-hardening-guidance-cisco-sd-wan-systems ; https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-authbp-qwCX8D4v ; https://nvd.nist.gov/vuln/detail/CVE-2026-20122

---

### CVE-2026-20133
- **名称**: Cisco Catalyst SD-WAN Manager Exposure of Sensitive Information to an Unauthorized Actor Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN Manager
- **添加日期**: 2026-04-20
- **修复截止**: 2026-04-23
- **备注**: CISA Mitigation Instructions: https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems ; https://www.cisa.gov/news-events/directives/supplemental-direction-ed-26-03-hunt-and-hardening-guidance-cisco-sd-wan-systems ; https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-authbp-qwCX8D4v ; https://nvd.nist.gov/vuln/detail/CVE-2026-20133

---

### CVE-2025-2749
- **名称**: Kentico Xperience Path Traversal Vulnerability
- **厂商**: Kentico
- **产品**: Kentico Xperience
- **添加日期**: 2026-04-20
- **修复截止**: 2026-05-04
- **备注**: https://devnet.kentico.com/download/hotfixes ; https://nvd.nist.gov/vuln/detail/CVE-2025-2749

---

### CVE-2023-27351
- **名称**: PaperCut NG/MF Improper Authentication Vulnerability
- **厂商**: PaperCut
- **产品**: NG/MF
- **添加日期**: 2026-04-20
- **修复截止**: 2026-05-04
- **备注**: https://www.papercut.com/kb/Main/PO-1216-and-PO-1219 ; https://nvd.nist.gov/vuln/detail/CVE-2023-27351

---

### CVE-2025-48700
- **名称**: Synacor Zimbra Collaboration Suite (ZCS) Cross-site Scripting Vulnerability
- **厂商**: Synacor
- **产品**: Zimbra Collaboration Suite (ZCS)
- **添加日期**: 2026-04-20
- **修复截止**: 2026-04-23
- **备注**: https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories ; https://nvd.nist.gov/vuln/detail/CVE-2025-48700

---

### CVE-2026-20128
- **名称**: Cisco Catalyst SD-WAN Manager Storing Passwords in a Recoverable Format Vulnerability
- **厂商**: Cisco
- **产品**: Catalyst SD-WAN Manager
- **添加日期**: 2026-04-20
- **修复截止**: 2026-04-23
- **备注**: CISA Mitigation Instructions: https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems ; https://www.cisa.gov/news-events/directives/supplemental-direction-ed-26-03-hunt-and-hardening-guidance-cisco-sd-wan-systems ; https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-authbp-qwCX8D4v ; https://nvd.nist.gov/vuln/detail/CVE-2026-20128

---

### CVE-2025-32975
- **名称**: Quest KACE Systems Management Appliance (SMA) Improper Authentication Vulnerability
- **厂商**: Quest
- **产品**: KACE Systems Management Appliance (SMA)
- **添加日期**: 2026-04-20
- **修复截止**: 2026-05-04
- **备注**: https://support.quest.com/kb/4379499/quest-response-to-kace-sma-vulnerabilities-cve-2025-32975-cve-2025-32976-cve-2025-32977-cve-2025-32978 ; https://nvd.nist.gov/vuln/detail/CVE-2025-32975

---

### CVE-2024-27199
- **名称**: JetBrains TeamCity Relative Path Traversal Vulnerability
- **厂商**: JetBrains
- **产品**: TeamCity
- **添加日期**: 2026-04-20
- **修复截止**: 2026-05-04
- **备注**: https://www.jetbrains.com/privacy-security/issues-fixed/ ; https://blog.jetbrains.com/teamcity/2024/03/additional-critical-security-issues-affecting-teamcity-on-premises-cve-2024-27198-and-cve-2024-27199-update-to-2023-11-4-now/ ; https://nvd.nist.gov/vuln/detail/CVE-2024-27199

---

### CVE-2026-34197
- **名称**: Apache ActiveMQ Improper Input Validation Vulnerability
- **厂商**: Apache
- **产品**: ActiveMQ
- **添加日期**: 2026-04-16
- **修复截止**: 2026-04-30
- **备注**: https://activemq.apache.org/security-advisories.data/CVE-2026-34197-announcement.txt ; https://nvd.nist.gov/vuln/detail/CVE-2026-34197

---

### CVE-2009-0238
- **名称**: Microsoft Office Remote Code Execution
- **厂商**: Microsoft
- **产品**: Office
- **添加日期**: 2026-04-14
- **修复截止**: 2026-04-28
- **备注**: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2009/ms09-009 ; https://nvd.nist.gov/vuln/detail/CVE-2009-0238

---

### CVE-2026-32201
- **名称**: Microsoft SharePoint Server Improper Input Validation Vulnerability
- **厂商**: Microsoft
- **产品**: SharePoint Server
- **添加日期**: 2026-04-14
- **修复截止**: 2026-04-28
- **备注**: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-32201 ; https://nvd.nist.gov/vuln/detail/CVE-2026-32201

---

### CVE-2012-1854
- **名称**: Microsoft Visual Basic for Applications Insecure Library Loading Vulnerability
- **厂商**: Microsoft
- **产品**: Visual Basic for Applications (VBA)
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2012/ms12-046 ; https://nvd.nist.gov/vuln/detail/CVE-2012-1854

---

### CVE-2025-60710
- **名称**: Microsoft Windows Link Following Vulnerability
- **厂商**: Microsoft
- **产品**: Windows
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60710 ; https://nvd.nist.gov/vuln/detail/CVE-2025-60710

---

### CVE-2023-21529
- **名称**: Microsoft Exchange Server Deserialization of Untrusted Data Vulnerability
- **厂商**: Microsoft
- **产品**: Exchange Server
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21529 ; https://nvd.nist.gov/vuln/detail/CVE-2023-21529

---

### CVE-2023-36424
- **名称**: Microsoft Windows Out-of-Bounds Read Vulnerability
- **厂商**: Microsoft
- **产品**: Windows
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2023-36424 ; https://nvd.nist.gov/vuln/detail/CVE-2023-36424

---

### CVE-2020-9715
- **名称**: Adobe Acrobat Use-After-Free Vulnerability
- **厂商**: Adobe
- **产品**: Acrobat
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://helpx.adobe.com/security/products/acrobat/apsb20-48.html ; https://nvd.nist.gov/vuln/detail/CVE-2020-9715

---

### CVE-2026-21643
- **名称**: Fortinet FortiClient EMS SQL Injection Vulnerability
- **厂商**: Fortinet
- **产品**: FortiClient EMS
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-16
- **备注**: https://fortiguard.fortinet.com/psirt/FG-IR-25-1142 ; https://nvd.nist.gov/vuln/detail/CVE-2026-21643

---

### CVE-2026-34621
- **名称**: Adobe Acrobat and Reader Prototype Pollution Vulnerability
- **厂商**: Adobe
- **产品**: Acrobat and Reader
- **添加日期**: 2026-04-13
- **修复截止**: 2026-04-27
- **备注**: https://helpx.adobe.com/security/products/acrobat/apsb26-43.html ; https://nvd.nist.gov/vuln/detail/CVE-2026-34621

---

### CVE-2026-1340
- **名称**: Ivanti Endpoint Manager Mobile (EPMM) Code Injection Vulnerability
- **厂商**: Ivanti
- **产品**: Endpoint Manager Mobile (EPMM)
- **添加日期**: 2026-04-08
- **修复截止**: 2026-04-11
- **备注**: Please adhere to Ivanti's guidelines to assess exposure and mitigate risks. Check for signs of potential compromise on all internet accessible Ivanti products affected by this vulnerability. Apply any final mitigations provided by the vendor as soon as possible. For more information please see: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-CVE-2026-1281-CVE-2026-1340?language=en_US ; https://support.mobileiron.com/mi/vsp/AB1786671/ivanti-security-update-1761642-1.1.0S-5.noarch.rpm ; https://support.mobileiron.com/mi/vsp/AB1786671/ivanti-security-update-1761642-1.1.0L-5.noarch.rpm ; https://nvd.nist.gov/vuln/detail/CVE-2026-1340

---

### CVE-2026-35616
- **名称**: Fortinet FortiClient EMS Improper Access Control Vulnerability
- **厂商**: Fortinet
- **产品**: FortiClient EMS
- **添加日期**: 2026-04-06
- **修复截止**: 2026-04-09
- **备注**: Please adhere to Fortinet's guidelines to assess exposure and mitigate risks. Check for signs of potential compromise on all internet accessible Fortinet products affected by this vulnerability. Apply any final mitigations provided by the vendor as soon as they become available. For more information please see: https://fortiguard.fortinet.com/psirt/FG-IR-26-099 ; https://nvd.nist.gov/vuln/detail/CVE-2026-35616

---

### CVE-2026-3502
- **名称**: TrueConf Client Download of Code Without Integrity Check Vulnerability
- **厂商**: TrueConf
- **产品**: Client
- **添加日期**: 2026-04-02
- **修复截止**: 2026-04-16
- **备注**: https://trueconf.com/blog/update/trueconf-8-5 ; https://trueconf.com/downloads/windows.html ; https://nvd.nist.gov/vuln/detail/CVE-2026-3502

---

### CVE-2026-5281
- **名称**: Google Dawn Use-After-Free Vulnerability
- **厂商**: Google
- **产品**: Dawn
- **添加日期**: 2026-04-01
- **修复截止**: 2026-04-15
- **备注**: This vulnerability affects an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_31.html ; https://nvd.nist.gov/vuln/detail/CVE-2026-5281 

---

### CVE-2026-3055
- **名称**: Citrix NetScaler Out-of-Bounds Read Vulnerability
- **厂商**: Citrix
- **产品**: NetScaler
- **添加日期**: 2026-03-30
- **修复截止**: 2026-04-02
- **备注**: https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696300&articleURL=NetScaler_ADC_and_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_3055_and_CVE_2026_4368 ; https://nvd.nist.gov/vuln/detail/CVE-2026-3055

---

### CVE-2025-53521
- **名称**: F5 BIG-IP Stack-Based Buffer Overflow Vulnerability
- **厂商**: F5
- **产品**: BIG-IP
- **添加日期**: 2026-03-27
- **修复截止**: 2026-03-30
- **备注**: Please adhere to F5’s guidelines to assess exposure and mitigate risks. Check for signs of potential compromise on all internet accessible F5 products affected by this vulnerability. For more information please see: https://my.f5.com/manage/s/article/K000156741 ; https://my.f5.com/manage/s/article/K000160486 ; https://my.f5.com/manage/s/article/K11438344 ; https://nvd.nist.gov/vuln/detail/CVE-2025-53521

---

### CVE-2026-33634
- **名称**: Aquasecurity Trivy Embedded Malicious Code Vulnerability
- **厂商**: Aquasecurity
- **产品**: Trivy
- **添加日期**: 2026-03-26
- **修复截止**: 2026-04-09
- **备注**: This vulnerability involves a supply‑chain compromise in a product that may be used across multiple products and environments. Additional vendor‑provided guidance must be followed to ensure full remediation. For more information, please see: https://github.com/advisories/GHSA-69fq-xp46-6x23 ; https://nvd.nist.gov/vuln/detail/CVE-2026-33634

---

### CVE-2026-33017
- **名称**: Langflow Code Injection Vulnerability
- **厂商**: Langflow
- **产品**: Langflow
- **添加日期**: 2026-03-25
- **修复截止**: 2026-04-08
- **备注**: https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx ; https://nvd.nist.gov/vuln/detail/CVE-2026-33017

---

### CVE-2025-32432
- **名称**: Craft CMS Code Injection Vulnerability
- **厂商**: Craft CMS
- **产品**: Craft CMS
- **添加日期**: 2026-03-20
- **修复截止**: 2026-04-03
- **备注**: https://craftcms.com/knowledge-base/craft-cms-cve-2025-32432 ; https://github.com/craftcms/cms/security/advisories/GHSA-f3gw-9ww9-jmc3 ; https://nvd.nist.gov/vuln/detail/CVE-2025-32432

---

### CVE-2025-54068
- **名称**: Laravel Livewire Code Injection Vulnerability
- **厂商**: Laravel
- **产品**: Livewire
- **添加日期**: 2026-03-20
- **修复截止**: 2026-04-03
- **备注**: https://github.com/livewire/livewire/security/advisories/GHSA-29cq-5w36-x7w3 ; https://github.com/livewire/livewire/commit/ef04be759da41b14d2d129e670533180a44987dc ; https://nvd.nist.gov/vuln/detail/CVE-2025-54068

---

### CVE-2025-43510
- **名称**: Apple Multiple Products Improper Locking Vulnerability
- **厂商**: Apple
- **产品**: Multiple Products
- **添加日期**: 2026-03-20
- **修复截止**: 2026-04-03
- **备注**: https://support.apple.com/en-us/125632 ; https://support.apple.com/en-us/125633 ; https://support.apple.com/en-us/125634 ; https://support.apple.com/en-us/125635 ; https://support.apple.com/en-us/125636 ; https://support.apple.com/en-us/125637 ; https://support.apple.com/en-us/125638 ; https://support.apple.com/en-us/125639 ; https://nvd.nist.gov/vuln/detail/CVE-2025-43510

---

### CVE-2025-43520
- **名称**: Apple Multiple Products Classic Buffer Overflow Vulnerability
- **厂商**: Apple
- **产品**: Multiple Products
- **添加日期**: 2026-03-20
- **修复截止**: 2026-04-03
- **备注**: https://support.apple.com/en-us/125632 ; https://support.apple.com/en-us/125633 ; https://support.apple.com/en-us/125634 ; https://support.apple.com/en-us/125635 ; https://support.apple.com/en-us/125636 ; https://support.apple.com/en-us/125637 ; https://support.apple.com/en-us/125638 ; https://support.apple.com/en-us/125639 ; https://nvd.nist.gov/vuln/detail/CVE-2025-43520

---

---

============================================================
## cleaned_CVE-2026-12348
### CVE-2026-12348

**来源**: NVD | **分类**: vulnerability | **字符数**: 319

# CVE-2026-12348

### Description
Address bar spoofing in Arc Search for Android allows a remote attacker to display a trusted domain in the address bar while rendering attacker-controlled content, enabling phishing.

### CVSS
- **Base Score**: 7.4
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35258
### CVE-2026-35258

**来源**: NVD | **分类**: vulnerability | **字符数**: 1026

# CVE-2026-35258

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTPS to compromise WebLogic Server. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all WebLogic Server accessible data as well as unauthorized access to critical data or complete access to all WebLogic Server accessible data. CVSS 3.1 Base Score 8.7 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N).

### CVSS
- **Base Score**: 8.7
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35259
### CVE-2026-35259

**来源**: NVD | **分类**: vulnerability | **字符数**: 733

# CVE-2026-35259

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise WebLogic Server. Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35261
### CVE-2026-35261

**来源**: NVD | **分类**: vulnerability | **字符数**: 817

# CVE-2026-35261

### Description
Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in unauthorized update, insert or delete access to some of Oracle Access Manager accessible data as well as unauthorized read access to a subset of Oracle Access Manager accessible data. CVSS 3.1 Base Score 6.5 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N).

### CVSS
- **Base Score**: 6.5
- **Severity**: MEDIUM

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35262
### CVE-2026-35262

**来源**: NVD | **分类**: vulnerability | **字符数**: 971

# CVE-2026-35262

### Description
Vulnerability in the Oracle Data Integrator product of Oracle Fusion Middleware (component: Market Place). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Data Integrator. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Data Integrator accessible data as well as unauthorized access to critical data or complete access to all Oracle Data Integrator accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Data Integrator. CVSS 3.1 Base Score 8.3 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L).

### CVSS
- **Base Score**: 8.3
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35263
### CVE-2026-35263

**来源**: NVD | **分类**: vulnerability | **字符数**: 764

# CVE-2026-35263

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise WebLogic Server. While the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35265
### CVE-2026-35265

**来源**: NVD | **分类**: vulnerability | **字符数**: 651

# CVE-2026-35265

### Description
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: Security). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35267
### CVE-2026-35267

**来源**: NVD | **分类**: vulnerability | **字符数**: 659

# CVE-2026-35267

### Description
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: REST WebServices). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35268
### CVE-2026-35268

**来源**: NVD | **分类**: vulnerability | **字符数**: 772

# CVE-2026-35268

### Description
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Identity Manager. While the vulnerability is in Identity Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Identity Manager. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35269
### CVE-2026-35269

**来源**: NVD | **分类**: vulnerability | **字符数**: 709

# CVE-2026-35269

### Description
Vulnerability in the Identity Manager product of Oracle Fusion Middleware (component: REST WebServices). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Identity Manager. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Identity Manager accessible data. CVSS 3.1 Base Score 7.5 (Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N).

### CVSS
- **Base Score**: 7.5
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35270
### CVE-2026-35270

**来源**: NVD | **分类**: vulnerability | **字符数**: 811

# CVE-2026-35270

### Description
Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle WebCenter Content. While the vulnerability is in Oracle WebCenter Content, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Content. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.1
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35271
### CVE-2026-35271

**来源**: NVD | **分类**: vulnerability | **字符数**: 1028

# CVE-2026-35271

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Weblogic). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. While the vulnerability is in PeopleSoft Enterprise PT PeopleTools, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all PeopleSoft Enterprise PT PeopleTools accessible data as well as unauthorized access to critical data or complete access to all PeopleSoft Enterprise PT PeopleTools accessible data. CVSS 3.1 Base Score 8.7 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N).

### CVSS
- **Base Score**: 8.7
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35272
### CVE-2026-35272

**来源**: NVD | **分类**: vulnerability | **字符数**: 759

# CVE-2026-35272

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with logon to the infrastructure where PeopleSoft Enterprise PT PeopleTools executes to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.4 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.4
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35274
### CVE-2026-35274

**来源**: NVD | **分类**: vulnerability | **字符数**: 876

# CVE-2026-35274

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all PeopleSoft Enterprise PT PeopleTools accessible data as well as unauthorized update, insert or delete access to some of PeopleSoft Enterprise PT PeopleTools accessible data. CVSS 3.1 Base Score 8.2 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N).

### CVSS
- **Base Score**: 8.2
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35275
### CVE-2026-35275

**来源**: NVD | **分类**: vulnerability | **字符数**: 990

# CVE-2026-35275

### Description
Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Shared Folders). The supported version that is affected is 7.2.8. Difficult to exploit vulnerability allows low privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox. While the vulnerability is in Oracle VM VirtualBox, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle VM VirtualBox accessible data as well as unauthorized access to critical data or complete access to all Oracle VM VirtualBox accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N).

### CVSS
- **Base Score**: 7.5
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35276
### CVE-2026-35276

**来源**: NVD | **分类**: vulnerability | **字符数**: 705

# CVE-2026-35276

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Application Server). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.1
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35278
### CVE-2026-35278

**来源**: NVD | **分类**: vulnerability | **字符数**: 708

# CVE-2026-35278

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Performance Monitor). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35279
### CVE-2026-35279

**来源**: NVD | **分类**: vulnerability | **字符数**: 706

# CVE-2026-35279

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Performance Monitor). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.1
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35280
### CVE-2026-35280

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35280

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35281
### CVE-2026-35281

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35281

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35282
### CVE-2026-35282

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35282

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35283
### CVE-2026-35283

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35283

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35284
### CVE-2026-35284

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35284

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35285
### CVE-2026-35285

**来源**: NVD | **分类**: vulnerability | **字符数**: 857

# CVE-2026-35285

### Description
Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35286
### CVE-2026-35286

**来源**: NVD | **分类**: vulnerability | **字符数**: 686

# CVE-2026-35286

### Description
Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Content. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Content. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35288
### CVE-2026-35288

**来源**: NVD | **分类**: vulnerability | **字符数**: 896

# CVE-2026-35288

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Easily exploitable vulnerability allows high privileged attacker with logon to the infrastructure where PeopleSoft Enterprise PT PeopleTools executes to compromise PeopleSoft Enterprise PT PeopleTools. While the vulnerability is in PeopleSoft Enterprise PT PeopleTools, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.2 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.2
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35289
### CVE-2026-35289

**来源**: NVD | **分类**: vulnerability | **字符数**: 706

# CVE-2026-35289

### Description
Vulnerability in the PeopleSoft Enterprise PT PeopleTools product of Oracle PeopleSoft (component: Deployment Package). Supported versions that are affected are 8.61 and 8.62. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTPS to compromise PeopleSoft Enterprise PT PeopleTools. Successful attacks of this vulnerability can result in takeover of PeopleSoft Enterprise PT PeopleTools. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.1
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35291
### CVE-2026-35291

**来源**: NVD | **分类**: vulnerability | **字符数**: 652

# CVE-2026-35291

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Difficult to exploit vulnerability allows high privileged attacker with network access via HTTP to compromise WebLogic Server. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 6.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 6.6
- **Severity**: MEDIUM

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35292
### CVE-2026-35292

**来源**: NVD | **分类**: vulnerability | **字符数**: 770

# CVE-2026-35292

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise WebLogic Server. While the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 10.0
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35293
### CVE-2026-35293

**来源**: NVD | **分类**: vulnerability | **字符数**: 667

# CVE-2026-35293

### Description
Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). The supported version that is affected is 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35294
### CVE-2026-35294

**来源**: NVD | **分类**: vulnerability | **字符数**: 824

# CVE-2026-35294

### Description
Vulnerability in the Identity Manager Connector product of Oracle Fusion Middleware (component: Mainframe Connectors). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Identity Manager Connector. While the vulnerability is in Identity Manager Connector, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Identity Manager Connector. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35295
### CVE-2026-35295

**来源**: NVD | **分类**: vulnerability | **字符数**: 678

# CVE-2026-35295

### Description
Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Difficult to exploit vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 7.5 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 7.5
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35296
### CVE-2026-35296

**来源**: NVD | **分类**: vulnerability | **字符数**: 681

# CVE-2026-35296

### Description
Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35298
### CVE-2026-35298

**来源**: NVD | **分类**: vulnerability | **字符数**: 789

# CVE-2026-35298

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise WebLogic Server. While the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.1
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35299
### CVE-2026-35299

**来源**: NVD | **分类**: vulnerability | **字符数**: 647

# CVE-2026-35299

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 12.2.1.4.0 and 14.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise WebLogic Server. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35300
### CVE-2026-35300

**来源**: NVD | **分类**: vulnerability | **字符数**: 672

# CVE-2026-35300

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise WebLogic Server. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35301
### CVE-2026-35301

**来源**: NVD | **分类**: vulnerability | **字符数**: 770

# CVE-2026-35301

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 12.2.1.4.0 and 14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise WebLogic Server. While the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 10.0
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35302
### CVE-2026-35302

**来源**: NVD | **分类**: vulnerability | **字符数**: 853

# CVE-2026-35302

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 12.2.1.4.0 and 14.1.1.0.0. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise WebLogic Server. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.3 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.3
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35303
### CVE-2026-35303

**来源**: NVD | **分类**: vulnerability | **字符数**: 647

# CVE-2026-35303

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Console). Supported versions that are affected are 12.2.1.4.0 and 14.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise WebLogic Server. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35304
### CVE-2026-35304

**来源**: NVD | **分类**: vulnerability | **字符数**: 677

# CVE-2026-35304

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle Coherence. Successful attacks of this vulnerability can result in takeover of Oracle Coherence. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35305
### CVE-2026-35305

**来源**: NVD | **分类**: vulnerability | **字符数**: 932

# CVE-2026-35305

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Centralized Third Party Jars). The supported version that is affected is 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. While the vulnerability is in Oracle Coherence, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Coherence accessible data as well as unauthorized update, insert or delete access to some of Oracle Coherence accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N).

### CVSS
- **Base Score**: 9.3
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35306
### CVE-2026-35306

**来源**: NVD | **分类**: vulnerability | **字符数**: 932

# CVE-2026-35306

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Centralized Third Party Jars). The supported version that is affected is 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. While the vulnerability is in Oracle Coherence, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Coherence accessible data as well as unauthorized update, insert or delete access to some of Oracle Coherence accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N).

### CVSS
- **Base Score**: 9.3
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35307
### CVE-2026-35307

**来源**: NVD | **分类**: vulnerability | **字符数**: 795

# CVE-2026-35307

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. While the vulnerability is in Oracle Coherence, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Coherence. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 10.0
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35308
### CVE-2026-35308

**来源**: NVD | **分类**: vulnerability | **字符数**: 819

# CVE-2026-35308

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Centralized Third Party Jars). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. While the vulnerability is in Oracle Coherence, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Coherence. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 10.0
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35309
### CVE-2026-35309

**来源**: NVD | **分类**: vulnerability | **字符数**: 700

# CVE-2026-35309

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Centralized Third Party Jars). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. Successful attacks of this vulnerability can result in takeover of Oracle Coherence. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35310
### CVE-2026-35310

**来源**: NVD | **分类**: vulnerability | **字符数**: 676

# CVE-2026-35310

### Description
Vulnerability in the Oracle Coherence product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Coherence. Successful attacks of this vulnerability can result in takeover of Oracle Coherence. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35311
### CVE-2026-35311

**来源**: NVD | **分类**: vulnerability | **字符数**: 644

# CVE-2026-35311

### Description
Vulnerability in the WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise WebLogic Server. Successful attacks of this vulnerability can result in takeover of WebLogic Server. CVSS 3.1 Base Score 8.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 8.8
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35312
### CVE-2026-35312

**来源**: NVD | **分类**: vulnerability | **字符数**: 696

# CVE-2026-35312

### Description
Vulnerability in the Oracle Virtual Directory product of Oracle Fusion Middleware (component: Virtual Directory Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Virtual Directory. Successful attacks of this vulnerability can result in takeover of Oracle Virtual Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.8
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35313
### CVE-2026-35313

**来源**: NVD | **分类**: vulnerability | **字符数**: 805

# CVE-2026-35313

### Description
Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### CVSS
- **Base Score**: 9.9
- **Severity**: CRITICAL

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## cleaned_CVE-2026-35314
### CVE-2026-35314

**来源**: NVD | **分类**: vulnerability | **字符数**: 926

# CVE-2026-35314

### Description
Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Web Server Plugin). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in unauthorized update, insert or delete access to some of Oracle Access Manager accessible data as well as unauthorized read access to a subset of Oracle Access Manager accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Access Manager. CVSS 3.1 Base Score 7.3 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L).

### CVSS
- **Base Score**: 7.3
- **Severity**: HIGH

---
*Source: NVD | Fetched: 2026-07-17 13:45:55*

---

============================================================
## OWASP_Top10_2021_Detailed
### OWASP Top 10:2021 - Web Application Security Risks

**来源**: OWASP | **分类**: security_standard | **字符数**: 2666

# OWASP Top 10:2021 - Web Application Security Risks
## Web应用安全十大风险

### 概述
OWASP Top 10 是 Web 应用安全领域最权威的风险排名文档，由全球安全专家社区共同维护。
2021 版本是最新正式版本，相对于 2017 版本进行了重大调整。

### 2021版本主要变化
- 新增: A04 不安全设计、A08 软件和数据完整性故障、A10 SSRF
- 移除: XML External Entities (XXE)、Insecure Deserialization (合并入A08)
- 重组: Sensitive Data Exposure → Cryptographic Failures

---


## A01:2021: Broken Access Control (失效的访问控制)

### 风险描述
访问控制强制实施策略，使用户不能在其预期权限之外操作。当这些控制措施失效时，会导致未授权的信息泄露、修改或破坏数据。

### 关联弱点类型 (CWE)
CWE-200, CWE-201, CWE-352

### 预防措施
- 默认拒绝所有访问，除非公开资源
- 实施访问控制机制并复用于整个应用
- 在服务器端强制访问控制
- 记录并监控访问控制失败

---

## A02:2021: Cryptographic Failures (加密失败)

### 风险描述
以前称为敏感数据暴露，侧重于与密码学相关的失败，这些失败通常导致敏感数据泄露或系统被攻破。

### 关联弱点类型 (CWE)
CWE-259, CWE-327, CWE-331

### 预防措施
- 对传输中和存储的数据进行加密
- 使用最新的强加密算法
- 不以明文存储密码，使用自适应哈希
- 禁用含弱加密的旧协议

---

## A03:2021: Injection (注入)

### 风险描述
当不可信数据作为命令或查询的一部分被发送到解释器时，会产生注入类漏洞。攻击者的恶意数据可以诱使解释器执行非预期命令。

### 关联弱点类型 (CWE)
CWE-79, CWE-89, CWE-73

### 预防措施
- 使用参数化查询/预编译语句
- 对输入进行白名单验证
- 使用ORM框架避免直接拼接SQL
- 对特殊字符进行转义处理

---

## A04:2021: Insecure Design (不安全设计)

### 风险描述
这是一个新的类别，侧重于与设计和架构缺陷相关的风险。需要更多的威胁建模、安全设计模式和参考架构。

### 关联弱点类型 (CWE)
CWE-209, CWE-256, CWE-272

### 预防措施
- 建立和使用安全开发生命周期 (SSDLC)
- 进行威胁建模 (STRIDE, PASTA)
- 集成安全语言和框架
- 编写单元测试和集成测试覆盖安全需求

---

## A05:2021: Security Misconfiguration (安全配置错误)

### 风险描述
安全配置错误是最常见的安全问题之一，通常由不安全的默认配置、不完整或临时的配置、开放的云存储等引起。

### 关联弱点类型 (CWE)
CWE-16, CWE-611

### 预防措施
- 实施自动化加固部署流程
- 维持最小化平台，移除不必要功能
- 定期审查和更新配置
- 使用自动化配置验证工具

---

## A06:2021: Vulnerable and Outdated Components (易受攻击和过时的组件)

### 风险描述
使用具有已知漏洞的组件（库、框架和其他软件模块）可能导致严重的数据丢失或服务器接管。

### 关联弱点类型 (CWE)
CWE-1104

### 预防措施
- 维护软件物料清单 (SBOM)
- 持续监控组件漏洞公告
- 使用官方源并验证签名
- 定期升级和修补组件

---

## A07:2021: Identification and Authentication Failures (身份识别和认证失败)

### 风险描述
以前称为'失效的身份认证'，包括与身份管理、认证和会话管理相关的安全风险。

### 关联弱点类型 (CWE)
CWE-287, CWE-384

### 预防措施
- 实施多因素认证 (MFA)
- 不部署默认凭据
- 实施密码强度检查
- 限制登录尝试频率，使用账户锁定

---

## A08:2021: Software and Data Integrity Failures (软件和数据完整性故障)

### 风险描述
与不验证软件更新、关键数据和CI/CD管道的完整性相关的风险。SolarWinds 事件是典型案例。

### 关联弱点类型 (CWE)
CWE-502

### 预防措施
- 使用数字签名验证软件来源
- 确保CI/CD管道安全配置
- 不使用不受信任的序列化格式
- 实施依赖项签名验证

---

## A09:2021: Security Logging and Monitoring Failures (安全日志记录和监控失败)

### 风险描述
不足的日志记录和监控，加上缺少或无效的与事件响应的集成，使攻击者能够进一步攻击系统并持久化。

### 关联弱点类型 (CWE)
CWE-778

### 预防措施
- 记录所有登录、访问控制和输入验证失败
- 确保日志格式统一，可供集中分析
- 建立有效的监控和告警机制
- 制定并演练事件响应计划

---

## A10:2021: Server-Side Request Forgery (SSRF - 服务端请求伪造)

### 风险描述
当Web应用获取远程资源但未验证用户提供的URL时发生SSRF，允许攻击者迫使应用向非预期的目标发送精心构造的请求。

### 关联弱点类型 (CWE)
CWE-918

### 预防措施
- 实施正向（允许列表）验证
- 禁用HTTP重定向
- 对URL进行白名单和模式验证
- 在独立网络中使用防火墙策略

---

---
*Source: OWASP Top 10:2021 | Generated: 2026-07-17 13:46:40*

---
