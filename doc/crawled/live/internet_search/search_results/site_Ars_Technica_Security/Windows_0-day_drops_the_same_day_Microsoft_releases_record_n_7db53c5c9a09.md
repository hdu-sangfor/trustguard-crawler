# Windows 0-day drops the same day Microsoft releases record number of patches

### 来源信息
- **URL**: https://arstechnica.com/security/2026/07/windows-0-day-drops-the-same-day-microsoft-releases-record-number-of-patches/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
Right on the heels of Microsoft releasing a record number of security patches, a researcher has published exploit code that can enable low-privilege Windows accounts to make sensitive changes to administrator accounts.
The exploit, which multiple researchers say works, is sending Microsoft scrambling, yet again, to patch a zero-day released by an anonymous researcher who has complained about the software maker’s handling of their bug reports. To date, the pseudonymous NightmareEclypse has published nine such exploits, including Tuesday’s HiveLegacy. The researcher said the proof-of-concept code included in the report was stripped down to prevent attackers from using it maliciously.
A “pretty powerful primitive”
HiveLegacy is an elevation-of-privilege exploit that targets a vulnerability residing in the Windows User Profile Service. It allows users (and with more work likely processes) with limited system rights to compromise an admin user’s account by modifying its classes registry hive, a resource that ensures the correct application opens when certain types of files are clicked on in Windows Explorer.
At a minimum, that means the attacker can modify the Windows registry associated with an administrator account. As written, the exploit requires the attacker to know another user’s credentials. The account need not be admin. An attacker must also know the username of a third account, also with or without admin status, on the machine.

---
*爬取时间: 2026-07-24 15:56:51*
*来源: 直接站点爬取*
