# weakness

## CWE-119: 弱点编号: CWE-119
**来源**: MITRE CWE

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

## CWE-125: 弱点编号: CWE-125
**来源**: MITRE CWE

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

## CWE-1321: 弱点编号: CWE-1321
**来源**: MITRE CWE

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

## CWE-20: 弱点编号: CWE-20
**来源**: MITRE CWE

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

## CWE-200: 弱点编号: CWE-200
**来源**: MITRE CWE

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

## CWE-22: 弱点编号: CWE-22
**来源**: MITRE CWE

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

## CWE-287: 弱点编号: CWE-287
**来源**: MITRE CWE

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

## CWE-295: 弱点编号: CWE-295
**来源**: MITRE CWE

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

## CWE-352: 弱点编号: CWE-352
**来源**: MITRE CWE

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

## CWE-401: 弱点编号: CWE-401
**来源**: MITRE CWE

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

## CWE-416: 弱点编号: CWE-416
**来源**: MITRE CWE

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

## CWE-434: 弱点编号: CWE-434
**来源**: MITRE CWE

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

## CWE-476: 弱点编号: CWE-476
**来源**: MITRE CWE

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

## CWE-502: 弱点编号: CWE-502
**来源**: MITRE CWE

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

## CWE-611: 弱点编号: CWE-611
**来源**: MITRE CWE

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

## CWE-77: 弱点编号: CWE-77
**来源**: MITRE CWE

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

## CWE-78: 弱点编号: CWE-78
**来源**: MITRE CWE

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

## CWE-787: 弱点编号: CWE-787
**来源**: MITRE CWE

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

## CWE-79: 弱点编号: CWE-79
**来源**: MITRE CWE

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

## CWE-798: 弱点编号: CWE-798
**来源**: MITRE CWE

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

## CWE-862: 弱点编号: CWE-862
**来源**: MITRE CWE

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

## CWE-863: 弱点编号: CWE-863
**来源**: MITRE CWE

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

## CWE-89: 弱点编号: CWE-89
**来源**: MITRE CWE

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

## CWE-918: 弱点编号: CWE-918
**来源**: MITRE CWE

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

## CWE-94: 弱点编号: CWE-94
**来源**: MITRE CWE

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

