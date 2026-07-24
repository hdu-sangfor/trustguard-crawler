# Novel OAuth Client ID Spoofing Technique Targets Cloud Environments

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/novel-spoofing-technique-targets/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
Cyber-attackers are increasingly deploying a stealthy technique which enables them to spoof OAuth Client IDs to gain access to cloud environments, cybersecurity experts have warned.
According to research by analysts at Proofpoint, cybercriminals are leveraging Microsoft Entra ID, the tech giant’s cloud-based identity and access management solution, formerly known as Azure AD, to gain access to accounts without a registered OAuth client ID.
The nature of the technique means that it is difficult for defenders to identify suspicious activity, while at the same time, the attackers are provided with stealthy access to the organization’s cloud services.
OAuth client ID spoofing has emerged as a novel technique and is increasingly leveraged in campaigns which target the cloud, Proofpoint warned in a blog post published on July 13.
Entra sign‑in logs are common tool for defenders to aid with identifying malicious authentication activity, such user enumeration. User enumeration is an attack technique when a malicious actor uses brute-force and password spraying to guess or confirm the login ID of a real user.
However, the research details how attackers are exploiting OAuth client ID spoofing to bypass detection by Entra sign-in logs, therefore helping them to stealthily compromise enterprise cloud services.
Evading Detection via Microsoft Entra
Proofpoint explained that client ID spoofing was performed by issuing POST requests to Microsoft's OAuth 2.0 token endpoint using the Resource Owner Password Credentials (ROPC) flow, which allowed direct submission of usernames and passwords.
This results in Azure Active Directory Security Token Service (AADSTS) error codes which allows unauthenticated requestors to infer the validity of usernames and passwords, as well as the enforcement of additional controls such as multi-factor authentication (MFA) or zero-trust concepts like conditional access (CA).
With this information, the attackers could identify accounts which could be exploited. Crucially, the use of the spoofed IDs and blank fields in Entra ID logs makes the malicious activity harder for defenders to identify.
Proofpoint said that it has tracked multiple large-scale campaigns deploying this technique, targeting millions of user accounts across thousands of Microsoft Entra tenants in the wild.
They note how the attackers make attempts to spoof common usernames to aid the process of client ID spoofing. Some examples listed in the blog include, initials paired with common surnames such as Smith, Jones, Williams, and Johnson leading to requests made with logins like jsmith, ajohnson and awilliams.
By doing this, attackers are not only taking advantage of how common the names are, but also how unlikely it is that the organization will change their username to something more complex.
Researchers warned that organizations should expect more attackers to look for ways to exploit this technique.
“The emergence of multiple campaigns with unique tools and infrastructure suggests this technique is gaining traction among threat actors targeting cloud environments,” the blog post warned.
Proofpoint said that in response to this tactic, defenders should treat sign-in log entries with blank application IDs, or those without a correspond application name, as potential indicators of client ID spoofing.
They also suggested that defenders should be alert that an AADSTS700016 error code may signal compromised credentials, not just a failed login attempt.

---
*爬取时间: 2026-07-24 21:45:28*
*来源: 直接站点爬取*
