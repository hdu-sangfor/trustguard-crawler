# 弱点编号: CWE-918
## 弱点名称: Server-Side Request Forgery (SSRF)

###  Top 25 排名
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
*采集时间: 2026-07-24 12:08:22*
