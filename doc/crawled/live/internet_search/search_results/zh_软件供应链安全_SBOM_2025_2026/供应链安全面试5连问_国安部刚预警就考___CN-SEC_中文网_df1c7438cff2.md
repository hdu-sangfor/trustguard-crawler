# 供应链安全面试5连问:国安部刚预警就考 | CN-SEC 中文网

### 来源信息
- **URL**: https://cn-sec.com/archives/5296918.html
- **域名**: cn-sec.com
- **检索关键词**: 软件供应链安全 SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
A: SBOM（Software Bill of Materials，软件物料清单）是软件产品中所有组件的完整列表，包含组件名称、版本、供应商、依赖关系等信息。fake-useragent pypi包供应链投毒事件 567 views 0. 供应链安全.

### 页面正文
🎯 供应链安全面试5连问：国安部刚预警，面试就考
国安部6月18日刚发布供应链投毒预警，如果你最近要面试安全岗位，这道题大概率会出现。以下是5道高频面试问答，全部经过搜索验证，确保答案严谨准确。
Q1: 什么是软件供应链攻击？与直接攻击有什么区别？
A: 软件供应链攻击是指攻击者通过在软件供应链的上游环节（如开源组件仓库、CI/CD工具链、更新分发服务器）植入恶意代码，间接影响下游所有使用该组件的用户。
与直接攻击的核心区别：
- 攻击路径不同
 ：直接攻击针对目标系统本身（如SQL注入、RCE），供应链攻击针对目标所依赖的上游组件 
- 影响范围不同
 ：直接攻击通常影响单一目标，供应链攻击可一次性影响成千上万的下游用户（"一毒千杀"） 
- 检测难度不同
 ：直接攻击有较成熟的WAF/IDS检测手段，供应链攻击的恶意代码隐藏在"合法"更新中，传统安全设备几乎无法识别 
- 典型案例
 ：SolarWinds事件（2020）——攻击者入侵Orion更新服务器，在合法更新中植入SUNBURST后门，影响18000+组织 
Q2: 供应链投毒的常见技术手段有哪些？请至少列举4种。
A:
- 1. Typo Squatting（ typo抢注）
 ：注册与热门包名称相似的恶意包，如 reqeusts模仿requests，依赖开发者输入错误
- 2. Package Hijacking（包劫持）
 ：接管已废弃/无维护的包，其npm/PyPI账号可能已无人管理，攻击者获取控制权后注入恶意代码 
- 3. Dependency Confusion（依赖混淆）
 ：利用包管理器的优先级机制——当私有包和公共仓库同名时，公共仓库的恶意包可能被优先拉取。2021年Alex Birsan凭此方法入侵了Apple、Microsoft等公司的内部系统 
- 4. Maintainer Account Compromise（维护者账号入侵）
 ：通过钓鱼/凭据泄露获取热门包维护者的账号，直接在合法包中推送恶意更新（如2022年ua-parser-js事件） 
- 5. Star-Jacking（星标劫持）
 ：将GitHub仓库的星标转移到恶意fork，诱导开发者使用恶意版本 
Q3: 如何检测和防御供应链投毒？企业级方案是什么？
A: 检测和防御需要分层实施：
检测层：
- SCA工具
 ：Snyk、Dependabot、OWASP Dependency-Check，持续扫描已知漏洞 
- 行为监控
 ：对安装后的包进行运行时行为分析，检测异常网络外联、文件操作 
- 完整性校验
 ：验证包的SHA256/PGP签名，与registry公布的哈希比对 
防御层：
- 版本锁定
 ：使用lockfile（package-lock.json/poetry.lock）精确锁定依赖版本和哈希 
- 私有Registry
 ：企业使用Verdaccio/nexus等私有镜像，只代理经审核的包 
- CI/CD门禁
 ：在流水线中集成 npm audit/pip audit，高危漏洞阻断部署
- SBOM（软件物料清单）
 ：生成完整的组件依赖图，快速定位受影响范围（SPDX/CycloneDX格式） 
Q4: 解释Dependency Confusion攻击的原理，以及npm/pip如何配置防御。
A: Dependency Confusion的核心原理是包管理器的解析优先级：
当项目声明依赖一个内部私有包@company/internal-lib时，如果公共仓库中存在同名包，某些包管理器的默认行为会优先拉取公共仓库的版本（因为公共版本通常更新）。
攻击者只需在npm/PyPI上发布一个同名包，版本号设为超高（如99.99.99），包管理器就会"自动升级"到恶意版本。
防御配置：
- npm
 ：在 .npmrc中配置registry=https://your-private-registry，或使用publishConfig明确区分内部包的registry
- pip
 ：使用 --index-url指定私有PyPI源，--extra-index-url仅用于补充外部依赖，并在私有源中预先占位同名包
- 通用方案
 ：在私有registry中为所有内部包创建占位包（版本号高于任何公共包），确保解析时命中私有源 
Q5: SBOM是什么？为什么说它是供应链安全的"基础设施"？
A: SBOM（Software Bill of Materials，软件物料清单）是软件产品中所有组件的完整列表，包含组件名称、版本、供应商、依赖关系等信息。
类比制造业：正如一台汽车有物料清单（BOM）记录所有零件来源，软件也需要SBOM记录所有组件来源。
为什么是"基础设施"：
- 快速应急响应
 ：当某组件爆出0-day漏洞，有SBOM的组织可以在分钟级定位所有受影响系统，没有SBOM的可能需要数天甚至无法定位 
- 合规要求
 ：美国EO 14028（改善国家网络安全行政令）已要求联邦供应商必须提供SBOM 
- 审计追踪
 ：为安全审计、许可证合规提供完整的数据基础 
主流格式：SPDX（Linux基金会）和CycloneDX（OWASP）
生成工具：
- 
Java生态：cyclonedx-maven-plugin 
- 
Python生态：cyclonedx-bom 
- 
Node.js生态：cyclonedx-npm 
- 
容器镜像：syft（Anchore） 
记住：供应链安全面试，不只是背答案。能结合最近国安部的通报谈实际案例，才是加分项。
原文始发于微信公众号（306Safe）：供应链安全面试5连问:国安部刚预警就考
- 左青龙
- 微信扫一扫
- 右白虎
- 微信扫一扫

---
*检索时间: 2026-07-24 13:10:07*
*搜索来源: DuckDuckGo*
