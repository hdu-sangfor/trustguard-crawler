# NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private ChatsJul 24, 2026Web Security / VulnerabilityEigh

### 来源信息
- **URL**: https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
Eight security flaws in NodeBB went public on Wednesday, along with the code to exploit them. Aikido Security rates all eight as high severity and says its AI pentest agents found them in a six-hour review of the forum software's source code.
Every version before 4.14.0 is affected. NodeBB has fixed them all, and administrators should be on 4.14.2.
The simplest one takes a settings change. A regular forum member could point their homepage setting at the admin address, reload the page, and the admin dashboard opened for them. No password, no exploit code.
The forum's own interface blocks that setting, but the block only ran in the browser and could be sidestepped. Most of what a member could then reach was read-only, including the error log and any user list an admin had exported, though they could also swap the site logo.
Two more gave an attacker with no account at all access to things meant to be private. One let anyone claim to be any user and read private messages one at a time. The other handed over the contents of private categories to anyone who asked for them the right way.
The widest flaw was in how NodeBB builds its pages. The software fills a page in, then makes a second pass to swap in translated text. User input was already sitting in the page by then, and it could smuggle in the codes that second pass looks for. That let an attacker plant a link almost anywhere on the site, including inside ordinary forum posts, that runs their code when a visitor clicks it.
The rest let an attacker take over an existing post, inflate a post's vote count, and run two attacks that plant malicious code by way of a fake server on the fediverse, the network of connected social sites a NodeBB forum can join.
Who Was Actually Exposed
The eight are not equal. Three need no account on the target forum. Two need an ordinary member account. The last three need someone to click a link or open a page.
Five of the eight, by The Hacker News' count, sit in NodeBB's federation code, the part that connects a forum to Mastodon and other social sites. That decides who was at risk. Forums installed fresh on version 4 federate by default, so they had all eight. Forums that upgraded from version 3 had federation switched off automatically, and unless an administrator turned it back on, only three of the flaws applied.
Aikido published no severity scores for the individual flaws, and NodeBB's release notes do not rate them. NodeBB's own bug bounty scale rates cross-site scripting and account takeover as high, and getting admin access as critical.
Patched in Pieces Since May
NodeBB fixed most of them quietly, without saying what they were. The Hacker News checked each fix against NodeBB's release history: four shipped in May, two in June, and the biggest, a rebuild of how the software handles page text, arrived in 4.14.0 on July 9. That rebuild touched 325 files.
Aikido's writeup says the issues were fixed in early July, which does not match that record. Its link for the admin-panel fix points to a change made in January 2024, two years before the review, while NodeBB's own release notes name a different change from May. Neither side explains the gap.
Administrators should upgrade to 4.14.2, released July 23. Expect some work, because 4.14.0 changed how page templates handle text and custom themes and plugins may need updating. Switching federation off is not a full answer either, since three of the flaws have nothing to do with it.
None of the eight has a CVE tracking number, and nobody has reported attacks using them. A separate NodeBB federation flaw does have one, CVE-2026-58593, filed on July 1. It is not one of Aikido's eight, but it sits in the same code and lets an outside server post and send messages in the name of any local account, the administrator's included. It needs federation switched on, and the record names no fixed version.
NodeBB's bug bounty page says it rejects AI-generated reports and pays only for work the submitter did themselves. That governs payouts rather than fixes, and these eight were reported to the maintainers directly and patched.
NodeBB is not the only project fielding them: the automation platform n8n patched a login flaw in June that a different AI pentest agent found. Co-founder Julian Lam's note in the release announcement says valid security reports arrived steadily through the month, "though almost all AI discovered and generated."
The pattern behind all eight is the same. NodeBB checked who you were on the main way into a feature, and skipped the check on the side route that reached the same place.

---
*爬取时间: 2026-07-24 15:42:35*
*来源: 直接站点爬取*
