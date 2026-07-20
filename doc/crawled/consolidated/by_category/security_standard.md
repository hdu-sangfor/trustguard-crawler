# security_standard

## OWASP_ASVS_v4.0.3: OWASP ASVS (Application Security Verification Standard) v4.0.3
**来源**: OWASP

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

## OWASP_WSTG_v4.2: OWASP WSTG (Web Security Testing Guide) v4.2
**来源**: OWASP

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

## OWASP_Top10_2021_Detailed: OWASP Top 10:2021 - Web Application Security Risks
**来源**: OWASP

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

