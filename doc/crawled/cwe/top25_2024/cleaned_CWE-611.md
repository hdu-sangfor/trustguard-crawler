# 弱点编号: CWE-611
## 弱点名称: Improper Restriction of XML External Entity Reference

###  Top 25 排名
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
