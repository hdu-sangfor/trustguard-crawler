# Watering Hole Attacks Push ScanBox Keylogger

### 来源信息
- **URL**: https://threatpost.com/watering-hole-attacks-push-scanbox-keylogger/180490/
- **来源站点**: Threatpost
- **页面抓取**: 成功

### 页面正文
A China-based threat actor has ramped up efforts to distribute the ScanBox reconnaissance framework to victims that include domestic Australian organizations and offshore energy firms in the South China Sea. The bait used by the advanced threat group (APT) is targeted messages that supposedly link back to Australian news websites.
The cyber-espionage campaigns are believed to have launched April 2022 through mid-June 2022, according to a Tuesday report by Proofpoint’s Threat Research Team and PwC’s Threat Intelligence team.
The threat actor, according to researchers, is believed to be the China-based APT TA423, also known as Red Ladon. “Proofpoint assesses with moderate confidence that this activity may be attributable to the threat actor TA423 / Red Ladon, which multiple reports assess to operate out of Hainan Island, China,” according to the report.
The APT is most recently known for a recent indictment. “A 2021 indictment by the US Department of Justice assessed that TA423 / Red Ladon provides long-running support to the Hainan Province Ministry of State Security (MSS),” researchers said.
MSS is the civilian intelligence, security and cyber police agency for the People’s Republic of China. It is believed responsible for counter-intelligence, foreign intelligence, political security and tied to industrial and cyber espionage efforts by China.
Dusting Off the ScanBox
The campaign leverages the ScanBox framework. ScanBox is a customizable and multifunctional Javascript-based framework used by adversaries to conducting covert reconnaissance.
ScanBox has been used by adversaries for nearly a decade and is noteworthy because criminals can use the tool to conduct counter intelligence without having to plant malware on a targets system.
“ScanBox is particularly dangerous as it doesn’t require malware to be successfully deployed to disk in order to steal information – the keylogging functionality simply requires the JavaScript code to be executed by a web browser,” according to PwC researchers referring to a previous campaign.
In lieu of malware, attackers can use ScanBox in conjunction with watering hole attacks. Adversaries load the malicious JavaScript onto a compromised website where the ScanBox acts as a keylogger snagging all of a user’s typed activity on the infected watering hole website.
TA423’s attacks began with phishing emails, with such titles as “Sick Leave,” “User Research” and “Request Cooperation.” Often, the emails purported to come from an employee of the “Australian Morning News,” a fictional organization. The employee implored targets to visit their “humble news website,” australianmorningnews[.]com.
“Upon clicking the link and redirecting to the site, visitors were served the ScanBox framework,” researchers wrote.
The link directed targets to a web page with content copied from actual news sites, like the BBC and Sky News. In the process, it also delivered the ScanBox malware framework.
ScanBox keylogger data culled from waterholes is part of a multi-stage attack, giving attackers insight into the potential targets that will help them launch future attacks against them. This technique is often called browser fingerprinting.
The primary, initial script sources a list of information about the target computer, including the operating system, language and version of Adobe Flash installed. ScanBox additionally runs a check for browser extensions, plugins and components such WebRTC.
“The module implements WebRTC, a free and open-source technology supported on all major browsers, which allows web browsers and mobile applications to perform real-time communication (RTC) over application programming interfaces (APIs). This allows ScanBox to connect to a set of pre-configured targets,” researchers explain.
Adversaries can then leverage a technology called STUN (Session Traversal Utilities for NAT). This is a standardized set of methods, including a network protocol, that allows interactive communications (including real-time voice, video, and messaging applications) to traverse network address translator (NAT) gateways, researchers explain.
“STUN is supported by the WebRTC protocol. Through a third-party STUN server located on the Internet, it allows hosts to discover the presence of a NAT, and to discover the mapped IP address and port number that the NAT has allocated for the application’s User Datagram Protocol (UDP) flows to remote hosts. ScanBox implements NAT traversal using STUN servers as part of Interactive Connectivity Establishment (ICE), a peer-to-peer communication method used for clients to communicate as directly as possible, avoiding having to communicate through NATs, firewalls, or other solutions,” according to researchers.
“This means that the ScanBox module can set up ICE communications to STUN servers, and communicate with victim machines even if they are behind NAT,” they explain.
Threat Actors
The threat actors “support the Chinese government in matters related to the South China Sea, including during the recent tensions in Taiwan,” Sherrod DeGrippo, vice president of threat research and detection at Proofpoint, explained in a statement, “This group specifically wants to know who is active in the region and, while we can’t say for certain, their focus on naval issues is likely to remain a constant priority in places like Malaysia, Singapore, Taiwan, and Australia.”
The group has, in the past, expanded well beyond Australasia. According to a Department of Justice indictment from July, 2021, the group has “stolen trade secrets and confidential business information” from victims in “the United States, Austria, Cambodia, Canada, Germany, Indonesia, Malaysia, Norway, Saudi Arabia, South Africa, Switzerland and the United Kingdom. Targeted industries included, among others, aviation, defense, education, government, health care, biopharmaceutical and maritime.”
Despite the DoJ indictment, analysts “have not observed a distinct disruption of operational tempo” from TA423, and they “collectively expect TA423 / Red Ladon to continue pursuing its intelligence-gathering and espionage mission.”

---
*爬取时间: 2026-07-24 15:46:36*
*来源: 直接站点爬取*
