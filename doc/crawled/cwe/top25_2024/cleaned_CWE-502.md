# 弱点编号: CWE-502
## 弱点名称: Deserialization of Untrusted Data

###  Top 25 排名
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
*采集时间: 2026-07-24 12:07:54*
