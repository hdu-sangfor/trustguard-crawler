# 弱点编号: CWE-401
## 弱点名称: Missing Release of Memory after Effective Lifetime

###  Top 25 排名
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
*采集时间: 2026-07-24 12:08:36*
