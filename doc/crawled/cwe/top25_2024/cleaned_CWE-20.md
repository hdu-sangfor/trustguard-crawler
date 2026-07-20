# 弱点编号: CWE-20
## 弱点名称: Improper Input Validation

###  Top 25 排名
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
