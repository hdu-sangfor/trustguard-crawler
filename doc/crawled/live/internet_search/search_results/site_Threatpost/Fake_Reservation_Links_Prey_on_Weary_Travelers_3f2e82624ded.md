# Fake Reservation Links Prey on Weary Travelers

### 来源信息
- **URL**: https://threatpost.com/reservation-links-prey-on-travelers/180462/
- **来源站点**: Threatpost
- **页面抓取**: 成功

### 页面正文
A longtime threat group identified as TA558 has ramped up efforts to target the travel and hospitality industries. After a lull in activity, believed tied to COVID-related travel restrictions, the threat group has ramped up campaigns to exploit an uptick in travel and related airline and hotel bookings.
Warnings come from security researchers who say TA558 cybercriminals have revamped their 2018 campaigns with fake reservation emails that contain links – that if clicked – deliver a malicious malware payload containing a potpourri of malware variants.
What makes this most recent campaign unique, according to a report by Proofpoint, is the use of RAR and ISO file attachments linked to messages. ISO and RAR are single compressed files, that if executed, decompress the file and folder data inside of them.
“TA558 began using URLs more frequently in 2022. TA558 conducted 27 campaigns with URLs in 2022, compared to just five campaigns total from 2018 through 2021. Typically, URLs led to container files such as ISOs or zip [RAR] files containing executables,” Proofpoint wrote.
To become infected, the targeted victim would have to be tricked into decompressing the file archive. “The reservation link… led to an ISO file and an embedded batch file. The execution of the BAT file led to a PowerShell helper script that downloaded a follow-on payload, AsyncRAT,” researchers wrote.
Upgrade Your Itinerary To Malware Infection Status
Past TA558 campaigns, tracked by Palo Alto Networks (in 2018), Cisco Talos (in 2020 and 2021) and Uptycs (in 2020), have leveraged malicious Microsoft Word document attachments (CVE-2017-11882) or remote template URLs to download and install malware, according to Proofpoint.
The shift to ISO and RAR files “is likely due to Microsoft’s announcements in late 2021 and early 2022 about disabling macros [VBA and XL4] by default in Office products,” researchers said.
“In 2022, campaign tempo increased significantly. Campaigns delivered a mixture of malware such as, Loda, Revenge RAT, and AsyncRAT. This actor used a variety of delivery mechanisms including URLs, RAR attachments, ISO attachments, and Office documents,” researchers wrote.
Malware payloads of recent campaigns typically include remote access trojans (RATs), that can enable reconnaissance, data theft and distribution of follow-on payloads, Proofpoint said.
Through all their evolutions, though, the goal of the group has always remained the same. The analysts concluded “with medium to high confidence” that TA558 is financially motivated, using stolen data to scale up and steal money. “Its possible compromises could impact both organizations in the travel industry as well as potentially customers who have used them for vacations,” Sherrod DeGrippo, vice president of threat research and detection organizations at Proofpoint, wrote in a statement. “Organizations in these and related industries should be aware of this actor’s activities and take precautions to protect themselves.”
TA558’s History
Since at least 2018, TA558 has primarily targeted organizations in the fields of travel, hospitality, and related industries. Those organizations tend to be located in Latin America, and sometimes in North America or Western Europe.
Throughout their history, TA558 has used socially engineered emails to lure victims into clicking on malicious links or documents. Those emails – most often written in Portuguese or Spanish – usually purported to concern hotel reservations. The subject line, or the name of the attached document, was often, simply, “reserva.”
In their early exploits, the group would leverage vulnerabilities in Microsoft Word’s Equation Editor – for example, CVE-2017-11882, a remote code execution bug. The goal was to download a RAT – most commonly Loda or Revenge RAT – to the target machine.
In 2019 the group expanded its arsenal, with malicious macro-laced Powerpoint attachments and template injections against Office documents. They also expanded to new demographics, utilizing English-language phishing lures for the first time.
Early 2020 was TA558’s most prolific period, as they churned out 25 malicious campaigns in January alone. They predominantly used macro-laden Office documents, or targeted known Office vulnerabilities during this period.
“Organizations, especially those operating in targeted sectors in Latin America, North America, and Western Europe should be aware of this actor’s tactics, techniques, and procedures,” researchers advise.

---
*爬取时间: 2026-07-24 21:43:44*
*来源: 直接站点爬取*
