# Docker 供应链安全：SBOM 与镜像签名落地 | BvBeJ的小站

### 来源信息
- **URL**: https://www.bvbej.com/posts/docker-sbom-signing-pipeline/
- **域名**: www.bvbej.com
- **检索关键词**: 软件供应链安全 SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Docker 供应链安全：SBOM 与镜像签名落地. 2026年5月2日 · 1 分钟 · BvBeJ. 背景. 镜像漏洞扫描只是起点。 上线前还需要回答：这个镜像是谁构建的，包含了什么依赖，是否被篡改。

### 页面正文
背景
镜像漏洞扫描只是起点。上线前还需要回答：这个镜像是谁构建的，包含了什么依赖，是否被篡改。
落地步骤
- 构建后生成 SBOM
- 对镜像做签名
- 部署侧验证签名
syft packages ghcr.io/org/app:latest -o spdx-json > sbom.json
cosign sign ghcr.io/org/app:latest
cosign verify ghcr.io/org/app:latest
总结
供应链安全要形成闭环：生成、签名、验证，缺一不可。
可观测运行时，也要可追溯构建时。

---
*检索时间: 2026-07-24 13:08:38*
*搜索来源: DuckDuckGo*
