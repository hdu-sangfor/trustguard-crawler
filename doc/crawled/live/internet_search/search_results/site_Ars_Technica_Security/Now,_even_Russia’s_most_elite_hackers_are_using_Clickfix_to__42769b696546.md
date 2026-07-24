# Now, even Russia’s most elite hackers are using Clickfix to infect devices

### 来源信息
- **URL**: https://arstechnica.com/security/2026/07/now-even-russias-most-elite-hackers-are-using-clickfix-to-infect-devices/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
One of the Russian government’s most elite hacking groups has adopted an attack, known as Clickfix, to compromise devices belonging to sensitive organizations in Ukraine, the latter country’s CERT center is warning.
Clickfix has emerged as an effective attack technique that attackers, primarily financially motivated criminals, began using in the last year or so. Websites under the control of the attackers display a CAPTCHA that requires the visitor to copy a jumble of text and paste it into the terminal. The text contains scripts that, once entered, perform malicious actions, typically by installing malware or exfiltrating sensitive data. Ukraine’s CERT said Wednesday that Sandworm, an advanced hacking unit inside the GRU, Russia’s military intelligence arm, is now using the technique.
“GhettoVibe,” “ScoutCurl,” and many more
The Clickfix attacks began in the spring and have continued through the summer. The campaign has resulted in the network compromise of at least one organization when a connected device was found to be infected by FreakyPoll, the name of one of Sandworm’s custom malware packages. Ukrainian authorities discovered 10 compromised websites that displayed a PowerShell command as part of a fake CAPTCHA that said it had to be passed to ensure a real human was behind the visiting device’s keyboard.
Once the user entered the script, it could install malicious Visual Basic scripts and other malicious wares that went on to install a variety of Sandworm malware. Typically, the first malware to run was a reconnaissance program that gathered information from the infected device. Machines deemed important would then receive follow-on malware that backdoored the system.
“The command, as an example, could be intended to load and save a VBS file in the Startup directory,” a translated version of Tuesday’s advisory stated. “One of the variants of such a program was called GHETTOVIBE. At the next stage, in order to determine the importance of the cyberattack object, the SCOUTCURL software tool can be loaded onto the attacked computer, which is a PowerShell script that performs basic reconnaissance by collecting and exfiltrating information about the computer: basic characteristics, programs, files, Internet browser data, etc.”

---
*爬取时间: 2026-07-24 15:56:51*
*来源: 直接站点爬取*
