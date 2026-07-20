# CISA Known Exploited Vulnerabilities (KEV) 目录
## 已知被利用的漏洞目录

### 概述
CISA（美国网络安全和基础设施安全局）维护的已知被利用漏洞目录，
收录了在实际攻击中被证实有活跃利用的漏洞。这是漏洞优先级管理的重要参考。

### 关键特征
- 收录的漏洞均有证据表明在野外被活跃利用
- 联邦机构必须在指定时间内修复
- 可作为漏洞管理优先级排序的重要依据

### 主要漏洞类别

#### 1. 远程代码执行 (RCE)
- 允许攻击者通过网络远程执行任意代码
- 通常影响最大，修复优先级最高
- 示例：Log4Shell (CVE-2021-44228)、ProxyShell (CVE-2021-34473)

#### 2. 权限提升 (Privilege Escalation)
- 允许低权限用户获取更高权限
- 常与RCE漏洞组合使用
- 示例：Windows Print Spooler (CVE-2021-34527)

#### 3. 认证绕过 (Authentication Bypass)
- 绕过身份验证机制获取未授权访问
- 可导致数据泄露或系统控制
- 示例：CVE-2021-40539

#### 4. 信息泄露 (Information Disclosure)
- 导致敏感信息未经授权地暴露
- 可能成为进一步攻击的跳板
- 示例：ProxyLogon (CVE-2021-26855)

### 漏洞管理建议
1. **建立资产清单**: 了解环境中运行的所有软件和硬件
2. **自动化扫描**: 持续扫描KEV中的漏洞
3. **优先级排序**: 根据CVSS评分和利用活跃度确定修复顺序
4. **补丁管理**: 建立及时部署安全补丁的流程
5. **缓解措施**: 对无法立即修补的漏洞实施补偿控制

### 参考链接
- CISA KEV 目录: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA BOD 22-01: https://www.cisa.gov/binding-operational-directive-22-01

---
*数据来源: CISA Known Exploited Vulnerabilities Catalog*
*生成时间: 2026-07-17 13:41:07*
