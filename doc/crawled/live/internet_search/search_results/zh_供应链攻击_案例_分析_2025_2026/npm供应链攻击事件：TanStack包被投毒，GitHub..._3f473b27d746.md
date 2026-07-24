# npm供应链攻击事件：TanStack包被投毒，GitHub...

### 来源信息
- **URL**: https://xmsumi.com/detail/3222
- **域名**: xmsumi.com
- **检索关键词**: 供应链攻击 案例 分析 2025 2026
- **页面抓取**: 成功

### 搜索摘要
被攻击的包包括前端开发者熟悉的 @tanstack/react-router、@tanstack/query、@tanstack/history 等。GitHub 安全跟踪 Issue. Socket Security 攻击追踪.

### 页面正文
如果你使用 npm 安装过 TanStack 系列的包，需要立即检查——在 2026年5月11日晚间的短时间内，AWS 密钥、GitHub Token、SSH 私钥可能已经被窃取。更危险的是，攻击者设置了一个「死亡开关」：一旦你撤销 GitHub Token，就会触发 rm -rf ~/，直接清空你的主目录。
事件概述
2026年5月11日北京时间凌晨3点20分，一场精心策划的供应链攻击悄然启动。攻击者发布了 84 个恶意版本，覆盖 42 个 @tanstack/* npm 包。只要在那段时间运行过 npm install，机器就可能被植入后门。
被攻击的包包括前端开发者熟悉的 @tanstack/react-router、@tanstack/query、@tanstack/history 等。TanStack 系列每周下载量超过千万，广泛应用于全球无数公司的生产系统中。
三环连环攻击
TanStack 官方的事后复盘显示，这不是单一漏洞的利用，而是三个已知漏洞的环环相扣。
第一环：伪造身份混入代码
攻击者注册 GitHub 账号 zblgg，从 TanStack/router fork 仓库后向官方仓库提交了一个 PR，标题为「WIP: simplify history build」，看起来像普通的代码优化。
关键问题在于，这个 PR 中隐藏了一个 vite_setup.mjs 文件，里面包含约 3 万行混淆过的 JavaScript 代码。提交者身份信息被伪造为 claude。
第二环：毒化 GitHub Actions 缓存
TanStack 的 bundle-size.yml 工作流使用了 pull_request_target 触发器。这个触发器有一个危险特性：它会在 base 仓库的权限下运行来自 fork 的代码，并且能写入 base 仓库的 Actions 缓存。
攻击者的 PR 触发了该工作流，执行了恶意代码，将毒化的 pnpm 存储写入缓存。缓存 key 精确匹配了发布工作流 release.yml 会使用的那个 key——就像在面粉厂的原料仓里掺入毒药，等着下游的面包厂使用。
第三环：从内存中提取 OIDC Token
当 TanStack 开发者正常合并 PR 触发 release.yml 时，被毒化的缓存被恢复到 CI 运行环境中。恶意代码通过 /proc/*/cmdline 找到 GitHub Actions Runner 进程，读取 /proc/*/maps 和 /proc/*/mem，直接从内存中提取 OIDC token。
然后攻击者用这个 token 直接向 npm registry 发包，完全绕过了正常的发布流程。官方复盘中提到：这个内存提取脚本「是来自 2025年3月 tj-actions/changed-files 事件的逐字照抄版本，连代码注释都没改」。
恶意代码行为
一旦有人在受感染环境中运行 npm install，router_init.js（2.3MB 混淆脚本）就会在安装过程中自动执行。
凭证窃取
恶意脚本会收集以下凭证：
- AWS IMDS / Secrets Manager 凭证
- GCP 元数据服务 Token
- Kubernetes service account Token
- Vault Token
- ~/.npmrc中的 npm 发布密钥
- GitHub Token（环境变量、gh CLI、.git-credentials）
- SSH 私钥
数据外泄
数据通过 Session/Oxen 加密通讯网络传输（filev2.getsession.org、seed{1,2,3}.getsession.org），采用端对端加密，没有中央服务器可以封锁。
蠕虫传播
脚本会枚举受害者在 npm 上维护的所有包，自动将恶意代码注入并发布。这就是为什么此次攻击从 TanStack 蔓延到了 OpenSearch Python SDK（130万周下载）、mistralai Python 包、guardrails-ai 等多个项目。
死亡开关
安全研究员 carlini 在 GitHub Issue 中发现了最危险的细节：脚本在 Linux 系统中安装 systemd 用户服务，在 macOS 中安装 LaunchAgent，每 60 秒检查一次被盗的 GitHub Token 是否仍然有效。
一旦你撤销 Token，立刻执行 rm -rf ~/。
如何判断是否中招
第一步：运行快速扫描工具
社区开发者 Rohit Tyagi 制作了扫描工具：
npx supply-chain-attack
该工具会检查本机是否安装了已知受感染的包版本、npm 缓存中是否有痕迹、全局安装状态以及可疑文件。
第二步：手动检查 package.json
在任何 @tanstack/* 包的 package.json 中，如果看到以下内容即为感染标志：
"optionalDependencies": {
  "@tanstack/setup": "github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c"
}
可以用以下命令验证（npm pack 不会执行安装脚本，是安全操作）：
npm pack @tanstack/@
tar -xzf *.tgz
cat package/package.json | grep -A3 optionalDependencies
ls -la package/router_init.js
第三步：检查持久化后门
Linux 用户：
ls ~/.config/systemd/user/ | grep gh-token-monitor
systemctl --user status gh-token-monitor
macOS 用户：
ls ~/Library/LaunchAgents/ | grep com.user.gh-token-monitor
受影响时间窗口： 2026年5月11日 19:20 到 19:30 UTC（北京时间5月12日凌晨3:20–3:30），仅在这段时间内运行过 TanStack 包的 npm install 才可能中招。
中招后的处理步骤
⚠️ 重要：必须先处理持久化后门，再撤销 Token。如果先撤销 GitHub Token，会触发 rm -rf ~/。
- 找到并停止 gh-token-monitor服务
- 删除相关服务文件
- 轮换所有凭证：
- GitHub Token
- AWS / GCP / Kubernetes 凭证
- npm Token（~/.npmrc）
- SSH 私钥
- 审计过去几小时的云服务操作日志，检查异常调用
- 用干净的 lockfile 重新安装依赖
npm 包维护者注意： 检查你的包是否也被蠕虫感染——如果机器中招，攻击者可能已经用你的凭证发布了新版本。
事件启示
TanStack 官方复盘中的一句话令人深思：
「检测是靠外部的。我们是从第三方那里知道自己被攻击的。」
一个每周数千万下载量的顶级开源项目，被攻击 20 分钟后才靠外部研究员发现。
此次攻击使用的每种技术都是公开资料：pull_request_target 滥用问题在 2023 年已被研究透彻，cache poisoning 攻击在 2024 年有完整分析，内存提取 OIDC token 的脚本是 2025 年事件的原版照抄。攻击者没有发明任何新技术，只是将三个已知漏洞组合在一起。
对开发者而言，npm install 这个每天运行无数次的命令背后，存在相当大的供应链攻击面。社区建议的防护措施包括：
- 使用 pnpm 并开启 minimumReleaseAge: 7d，让新发布的包等待 7 天再安装
- 定期审计依赖
- 监控自己的发布管道
但此次攻击从发布到被发现仅用了 20 分钟，7 天等待期也不够。更根本的防护仍需依赖持续的审计和监控。

---
*检索时间: 2026-07-24 14:08:46*
*搜索来源: DuckDuckGo*
