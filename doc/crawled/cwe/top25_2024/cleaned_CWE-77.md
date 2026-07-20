# 弱点编号: CWE-77
## 弱点名称: Improper Neutralization of Special Elements used in a Command ('Command Injection')

###  Top 25 排名
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
