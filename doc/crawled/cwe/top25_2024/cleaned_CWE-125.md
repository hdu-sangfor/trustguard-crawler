# 弱点编号: CWE-125
## 弱点名称: Out-of-bounds Read

###  Top 25 排名
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
