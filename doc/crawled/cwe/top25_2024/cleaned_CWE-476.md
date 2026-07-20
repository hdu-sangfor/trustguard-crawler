# 弱点编号: CWE-476
## 弱点名称: NULL Pointer Dereference

###  Top 25 排名
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
