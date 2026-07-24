# newsTycoon2FA takedown reshapes the phishing landscapeSome of the most common phishing techniques are declining, but not

### 来源信息
- **URL**: https://www.csoonline.com/article/4201146/tycoon2fa-takedown-reshapes-the-phishing-landscape.html
- **来源站点**: CSO Online
- **页面抓取**: 成功

### 页面正文
Traditional phishing techniques are in decline as a result of the disruption of the Tycoon2FA phishing-as-a-service (PHaaS) platform, Microsoft said in a new report, “Email threat landscape: Q2 2026 trends and insights”.
“Phishing volume linked to the platform fell 92% from pre-disruption averages, including QR code phishing and CAPTCHA-gated phishing both declining from their March highs,” the company wrote in the report.
The takedown reduced activity across multiple phishing categories, forcing attackers to shift to newer delivery methods.
Riding this shift in were a few notable phishing campaigns, including an automated business email compromise (BEC) campaign that reached 42,000 organizations in under three hours, and a multi-stage phishing campaign that used nested email (EML) files, calendar invitations, and a Microsoft authentication redirect to deliver malware.
To counter phishing attacks, Microsoft recommends blocking emails containing known bad URLs/ subject fields, enabling password-less authentication methods, or moving to MFA for accounts that still require passwords.
Tycoon2FA disruption sent attackers exploring
The take-down of Tycoon2FA forced its operators to abandon portions of their infrastructure and rework hosting, domain registrations, and delivery mechanisms.
“After falling 15% in March and another 22% in April, Tycoon2FA-linked phishing volume dropped 74% in May to just 1.5 million messages, then fell another 20% in June to 1.2 million, by far the lowest monthly volumes observed in at least a year,” Microsoft said.
The decline extended to QR Code lures and fake CAPTCHA pages, two phishing techniques in which Tycoon2FA accounted for 12% and 14% of industry activity in June, respectively. This indicated that the platform’s customer base had not been able to migrate to a replacement infrastructure.
But cutting off one head of the hacker hydra only gave rise to new tactics elsewhere.
The adaptation came in the form of using Microsoft Teams as a social engineering channel. Attackers established conversations to build trust before attempting credential theft or delivering malicious payloads. “Teams-based phishing volume climbed steadily throughout Q2, with the average number of detected attacks rising 19% from March to April, holding roughly flat into May (+1%), then increasing another 10% into June,” Microsoft said.
Microsoft also observed a highly automated BEC campaign that reached over 67,000 users using scripted emails, Amazon Simple Email Service (SES), and engagement tracking, alongside a separate phishing campaign targeting 107,000 users that abused Microsoft’s authentication flow and trusted cloud services, including Teams archive recording and ICS calendar invite, to disguise malware delivery behind legitimate infrastructure.
Phishing changes but the defense doesn’t
While QR Code and Captcha-based phishing attacks dropped significantly in the second quarter, business email compromise (BEC) charted jumped 121% between March and April, before dropping down again in May.
QR Code phishing represented 8.3 million attacks in June 2026, down from a peak of 18.7 million in March. Similarly, Captcha-gated phishing fell from 12 million attacks in March to 2.2 million in June.
BEC attacks hit 9 million in March, falling to 3.9 million in June.
But even as these phishing classics lost momentum and newer techniques emerged, Microsoft’s defensive advice remained rooted in the basics. It noted organizations should complement email filtering with phishing-resistant authentication such as passkeys and phishing-resistant MFA to reduce the effectiveness of credential theft campaigns.
The company also recommended strengthening Exchange Online Protection and Microsoft Defender for Office 365 with capabilities such as Safe links and Zero-hour Auto Purge (ZAP), in which malicious emails already delivered to mailboxes are removed before they are read, alongside enforcing password-less authentication methods like Windows Hello, FIDO keys, and Microsoft Authenticator.
Microsoft concluded its report with a list of indicators of compromise (IoCs) from the threats observed in the quarter to support detection efforts.

---
*爬取时间: 2026-07-24 21:46:15*
*来源: 直接站点爬取*
