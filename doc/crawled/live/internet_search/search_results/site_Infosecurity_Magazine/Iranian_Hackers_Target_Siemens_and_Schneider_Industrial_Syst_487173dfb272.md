# Iranian Hackers Target Siemens and Schneider Industrial Systems, CISA Warns

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/iran-hackers-siemen-schneider-ics/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
Iranian cyber adversaries are actively targeting internet-exposed industrial systems across brands like Rockwell Automation, Allen-Bradley, Schneider Electric and Siemens.
In an advisory update published on July 22, the US Cybersecurity and Infrastructure Security Agency (CISA) said the FBI had observed Iran-affiliated cyber threat actors download a malicious project file to a targeted programmable logic controller (PLC) at a US-based critical infrastructure organization using configuration software.
The Bureau also saw the manipulation of data on human machine interface (HMI) and supervisory control and data acquisition (SCADA) displays, resulting in operational disruption and financial loss.
Further analysis indicated the project file retained ladder logic for downstream function but added logic that overrode specific instruction sets responsible for maintaining safe operating parameters in the victim’s environment.
Iranian Cyber Campaign Targets US Critical Infrastructure
This follows an April advisory warning of an ongoing cyber campaign from Iranian actors against US critical infrastructure.
According to CISA, these actions disrupted PLCs across several US critical infrastructure sectors, notably government services and facilities, water and wastewater systems and energy.
In the initial warning, the agency named PLCs from Rockwell Automation and Allen-Bradley (a subsidiary of Rockwell Automation) as being targeted by these actors, following malicious changes detected in reusable code modules exploited within Rockwell Automation PLC programs.
The July update confirmed that the same advanced persistent threat (APT) actors are also targeting PLCs manufactured by Schneider Electric and Siemens.
This new assessment comes from findings that the APT actors have been using configuration software, like Rockwell Automation’s Studio 5000 Logix Designer, Schneider Electric’s EcoStruxure Control Expert and Siemens’ Totally Integrated Automation (TIA) Portal on leased, third-party hosted infrastructure to exfiltrate device project files from PLC devices to threat-actor-controlled infrastructure.
CISA named some of the specific models being targeted – Allen Bradley’s CompactLogix and Micro850 PLCs, Schneider Electric’s BMX P34 and Modicon M340 models and Siemens’ S7-1200 series PLCs.
The agency also said PLCs of other brands could also “potentially” be targeted.
While the advisory did not refer to any specific threat group, CISA noted that the ongoing campaign bears similarities with a November 2023 operation that involved a group affiliated to Iran’s Islamic Revolutionary Guard Corps Cyber-Electronic Command (IRGC CEC). The group in question is commonly known as ‘CyberAv3ngers’ and tracked by cybersecurity companies under many names including Bauxite, Hydro Kitten, the Shahid Kaveh Group, Soldiers of Solomon, Storm-0784 and UNC5691.
How US CNI Organizations Can Mitigate the Threat
The advisory urged US CNI providers to:
- Install PLCs consistent with manufacturers' guidelines and security best practices
- Remove PLCs from direct internet exposure via secure gateway and firewall
- Query available logs for the provided indicators of compromise (IOCs) and check available logs for suspicious traffic on the ports associated with OT devices, including 44818, 2222, 102 and 502
- For Rockwell Automation devices, place the physical mode switch on the controller into run position
Image credits: miamariapia / Dwi Doyo / Shutterstock.com

---
*爬取时间: 2026-07-24 15:48:24*
*来源: 直接站点爬取*
