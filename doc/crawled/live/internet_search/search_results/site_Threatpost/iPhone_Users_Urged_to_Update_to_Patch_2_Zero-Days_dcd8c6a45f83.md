# iPhone Users Urged to Update to Patch 2 Zero-Days

### 来源信息
- **URL**: https://threatpost.com/iphone-users-urged-to-update-to-patch-2-zero-days-under-attack/180448/
- **来源站点**: Threatpost
- **页面抓取**: 成功

### 页面正文
Apple is urging macOS, iPhone and iPad users immediately to install respective updates this week that includes fixes for two zero-days under active attack. The patches are for vulnerabilities that allow attackers to execute arbitrary code and ultimately take over devices.
Patches are available for effected devices running iOS 15.6.1 and macOS Monterey 12.5.1. Patches address two flaws, which basically impact any Apple device that can run either iOS 15 or the Monterey version of its desktop OS, according to security updates released by Apple Wednesday.
One of the flaws is a kernel bug (CVE-2022-32894), which is present both in iOS and macOS. According to Apple it is an “out-of-bounds write issue [that] was addressed with improved bounds checking.”
The vulnerability allows an application to execute arbitrary code with kernel privileges, according to Apple, which, in usual vague fashion, said there is a report that it “may have been actively exploited.”
The second flaw is identified as a WebKit bug (tracked as CVE-2022-32893), which is an out-of-bounds write issue that Apple addressed with improved bounds checking. The flaw allows for processing maliciously crafted web content that can lead to code execution, and also has been reported to be under active exploit, according to Apple. WebKit is the browser engine that powers Safari and all other third-party browsers that work on iOS.
Pegasus-Like Scenario
The discovery of both flaws, about which little more beyond Apple’s disclosure are known, was credited to an anonymous researcher.
One expert expressed worry that the latest Apple flaws “could effectively give attackers full access to device,” they might create a Pegasus-like scenario similar to the one in which nation-state APTs barraged targets with spyware made by Israeli NSO Group by exploiting an iPhone vulnerability.
“For most folks: update software by end of day,” tweeted Rachel Tobac, the CEO of SocialProof Security, regarding the zero-days. “If threat model is elevated (journalist, activist, targeted by nation states, etc): update now,” Tobac warned.
Zero-Days Abound
The flaws were unveiled alongside other news from Google this week that it was patching its fifth zero-day so far this year for its Chrome browser, an arbitrary code execution bug under active attack.
The news of yet more vulnerabilities from top tech vendors being barraged by threat actors demonstrates that despite the best efforts from top-tier tech companies to address perennial security issues in their software, it remains an uphill battle, noted Andrew Whaley, senior technical director at Promon, a Norwegian app security company.
The flaws in iOS are especially worrying, given the ubiquity of iPhones and users’ utter reliance on mobile devices for their daily lives, he said. However, the onus is not only on vendors to protect these devices but also for users to be more aware of existing threats, Whaley observed.
“While we all rely on our mobile devices, they are not invulnerable, and as users we need to maintain our guard just like we do on desktop operating systems,” he said in an email to Threatpost.
At the same time, developers of apps for iPhones and other mobile devices also should add an extra layer of security controls in their technology so they are less reliant on OS security for protection, given the flaws that frequently crop up, Whaley observed.
“Our experience shows that this is not happening enough, potentially leaving banking and other customers vulnerable,” he said.

---
*爬取时间: 2026-07-24 21:43:44*
*来源: 直接站点爬取*
