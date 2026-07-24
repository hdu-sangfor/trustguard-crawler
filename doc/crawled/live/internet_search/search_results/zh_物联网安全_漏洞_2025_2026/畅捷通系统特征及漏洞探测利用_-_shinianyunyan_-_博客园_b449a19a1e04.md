# 畅捷通系统特征及漏洞探测利用 - shinianyunyan - 博客园

### 来源信息
- **URL**: https://www.cnblogs.com/priv/p/19296977
- **域名**: www.cnblogs.com
- **检索关键词**: 物联网安全 漏洞 2025 2026
- **页面抓取**: 成功

### 搜索摘要
合集: Web安全 , 常见CMS&OA-无漏洞复现.3. 泛微OA系统特征及漏洞探测利用(934). 4. kkFileView文件预览特征及漏洞复现(834).

### 页面正文
Web特征
常见icon：
fofa语法：app="畅捷通-TPlus"、app="畅捷通-好会计"、app="畅捷通-好业财"、app="畅捷通-T1"、host="/tplus/"、path="/tplus/UploadHandler.ashx" || path="/tplus/keyEdit.aspx"、body="畅捷通服务专线"
通过默认端口80/443/8888/8080即可访问默认页面：
其他常见端口：1433/3433（T+系列SQL server端口）、7980（T+C系列SVN服务）、8992（云代理）、6379（T+C系列Redis）
出错页面：
web页面常见特征：
- 页面title/body中含有关键字：畅捷通 T+、T+Cloud、畅捷通服务专线、授权单位：
- 页面中的相关logo：
- 版权信息：Copyright 2008-2019 Chanjet Information Technology Company Limited all rights reserved.
网页URL路径特征：/tplus/、/tplus/view/
存在多个默认账户：admin/123456、system/system、admin/admin、demo/demo、企业ID/123456

---
*检索时间: 2026-07-24 13:17:43*
*搜索来源: DuckDuckGo*
