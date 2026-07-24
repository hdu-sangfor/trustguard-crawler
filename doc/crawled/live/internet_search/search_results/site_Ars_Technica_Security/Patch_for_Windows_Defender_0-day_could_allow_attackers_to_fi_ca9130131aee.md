# Patch for Windows Defender 0-day could allow attackers to fill hard disk

### 来源信息
- **URL**: https://arstechnica.com/security/2026/07/patch-for-windows-defender-0-day-could-allow-attackers-to-fill-hard-disk/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
A patch Microsoft released on Wednesday to fix a zero-day vulnerability in its Defender security engine may cause Windows machines to write files large enough to completely consume available disk space, the researcher who discovered the flaw said.
RoguePlanet, tracked as CVE-2026-50656, came to public notice in June when NightmareEclipse, the pseudonymous name used by a researcher, disclosed it along with code for exploiting it. The vulnerability allows remote attackers to gain administrative control of Windows 10 and Windows 11 machines, even when real-time protection has been disabled. Over the past few months, the anonymous researcher has published a handful of other zero-days that have sent Microsoft scrambling to develop patches.
Writing files of unlimited size
Microsoft said Wednesday that it patched RoguePlanet with an update to the Microsoft Malware Protection Engine, which is used by the Defender antivirus app. The fix will automatically be downloaded and installed without users having to take any action. Wednesday’s update also includes “defense-in-depth updates to help improve security-related features.”
In a post on Thursday, NightmareEclipse said the defense-in-depth additions produce behavior that may allow attackers to exhaust all available space on a hard drive by writing massive amounts of data to it. The newly introduced mitigations create a problem in mpengine.dll, the driver associated with the Microsoft Malware Protection Engine, that in some cases causes it to leak 8 bytes of data when trying to open a file. New functionality in SpyNet, a cloud service that allows Microsoft Security Essentials or Forefront Endpoint Protection to send reports about suspicious software and programs to Microsoft, also plays a role in the potential mass file-writing behavior.
Defender normally places hard limits on how big a file can be written to disk when scanning and quarantining a machine.
“This implementation make [sic] sense, because quarantining a huge file will cause Defender to completely exhaust the available disk space,” the researcher wrote. “I found a small exception to this rule, apparently the spynet functions in mpengine.dll really wants [sic] to keep a local copy of Zone.Identifier ADS file and it does not matter how big this file is, Windows Defender will cache it locally anyways.”

---
*爬取时间: 2026-07-24 21:50:58*
*来源: 直接站点爬取*
