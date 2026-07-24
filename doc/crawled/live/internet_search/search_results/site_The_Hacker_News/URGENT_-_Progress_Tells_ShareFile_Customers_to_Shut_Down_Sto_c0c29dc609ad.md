# URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat

### 来源信息
- **URL**: https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
Progress Software has told ShareFile customers to shut down the Windows servers running their Storage Zone Controllers, confirming to The Hacker News that it is responding to a "credible external security threat."
The company has temporarily disabled access to the affected accounts, a step it says it took "out of an abundance of caution" while it works with internal and external security experts.
It says it has no indication of unauthorized access to any ShareFile accounts or data, and that it notified customers after learning of the threat.
What Progress has not said is what the threat is or who is behind it.
The order became public when a customer posted the company's email to Reddit's r/sysadmin on July 10. Progress confirmed the disruption on its status page, listing Storage Zone Controller customers as "not operational" and the incident as under investigation as of a 12:12 p.m. EDT update.
Only the Storage Zone Controller is affected, not standard cloud-only ShareFile accounts. The controller is a server that a company runs itself, so files can stay on its own storage while it still uses ShareFile's cloud to share and manage them.
The controller usually sits at the network's edge, reachable from the internet. That exposure makes it both useful and a target. Ordering customers to take it fully offline, rather than just patch it, is a notable step.
That choice is itself a tell. If a fix for this threat existed, Progress would be telling customers to apply it; the shutdown order suggests there is none yet. That usually means a newly found flaw the company is racing to close, though the same step would also fit a threat a patch cannot address, such as stolen keys or a problem on Progress's own side.
Its statement that no accounts or data were accessed is careful wording, too, and does not rule out trouble on the controllers themselves.
What to do now
- Follow the shutdown order first. Keep the affected controllers offline until Progress says what the threat is and when it is safe to restart.
- Separately, confirm your version is current: 5.12.4 or later on the 5.x line, or a 6.x release. That closes the flaws fixed earlier this year, but Progress has not said it clears the current threat, so do not treat it as permission to restart.
- If a controller is reachable from the internet, handle it as a possible incident. Preserve the logs and start your incident-response process, then check for unfamiliar .aspx files in the web folders and storage paths you did not set. A clean-looking server is not proof that it is clean.
ShareFile has faced this before. In 2023, while the product still belonged to Citrix, attackers exploited an unauthenticated flaw in the same Storage Zones Controller (CVE-2023-24489).
CISA flagged it as actively exploited, and Citrix cut unpatched controllers off from the ShareFile cloud, the same access block Progress has now imposed.
Progress, which acquired ShareFile in 2024, had already weathered a mass file-transfer attack of its own: MOVEit, whose 2023 zero-day was exploited by the Clop group and hit more than 2,700 organizations.
The Storage Zones Controller also had two critical flaws that watchTowr disclosed in April and Progress patched in March, though the company has not connected the current threat to them, and neither has been reported as exploited.
The central question is still unanswered: Progress has pulled these systems offline and is working with outside experts, but has not said what the threat is or when customers can safely bring them back online.
Update
July 14, 2026: Progress has restored access for ShareFile Storage Zone Controller customers, lifting the shutdown order it issued on July 10. In a statement to The Hacker News, the company said its investigation identified a high-severity vulnerability in the Storage Zone Controller affecting versions 5.x and 6.x. It has released patched versions to customers, and says an affected controller returns to operation once the patch is applied.
Progress said it has no evidence of unauthorized access to any ShareFile customer account or data, and has not identified an active threat. That names the "credible external security threat" behind the July 10 order as a vulnerability the company has now patched. The statement does not identify who was behind the threat or name a CVE for the flaw.

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
