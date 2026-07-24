# Hotel Wi-Fi Routers Compromised to Steal Corporate Login Credentials From Visitors

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/hotel-wifi-dns-poisoning/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
A widespread DNS poisoning campaign is targeting the hotels, conference venues and the hospitality sector with credential harvesting attacks designed to steal corporate login credentials from visitors, researchers have warned.
Identified by cybersecurity analysts at ReliaQuest, the campaign begins by targeting routers used to provide public Wi-Fi to visitors to hotels, conference centers and other shared venues frequently visited by corporate employees.
These compromised Wi-Fi gateways were identified around the world, including across multiple US cities, India and Saudi Arabia.
In a blog post published on July 23, ReliaQuest researchers said that they believed initial access to the devices was achieved by exploiting exposed management interfaces, such as SSH, SNMP and web administration consoles, as well as weak or reused admin login credentials.
With this access, the attacker modifies the configurations of the compromised routers and use DNS poisoning to redirect the web traffic, funneling connections for legitimate domains through attacker-controlled infrastructure.
This means that a user can be compromised without the need for a phishing link, a malicious attachment or the attacker touching the device in any way.
With no indication that anything could be amiss, the user will continue to use their device normally, oblivious to how the attackers can now monitor their activity, complete with being provided with the username, password and other sensitive information which belongs to the victim.
Targeting Corporate Business Travelers
By targeting hotels and conference venues known to be used by traveling corporate employees, the attackers can potentially get hold of a wide range of credentials which could be exploited to access sensitive information.
“The compromised devices we investigated were appliances primarily used at hotels and other organizations running captive Wi-Fi services,” ReliaQuest researchers warned.
“However, any operator of a captive portal network –such as airports, conference centers, co-working spaces, universities, healthcare facilities and event venues –faces a structurally similar attack surface, they added.
The researchers noted that the tradecraft used in the DNS poisoning campaign, which is still ongoing, is similar to previous campaigns attributed to APT28, also known as Fancy Bear and Forest Blizzard, a cyber espionage group linked to the Russian military intelligence agency (GRU).
ReliaQuest has issued advice on how to prevent DNS poisoning from reaching endpoints, eliminating the attack surface and detecting credential-harvesting activity if it occurs. The recommendations include:
- Enforcing always-on VPN with full-tunnel configuration: Require all corporate devices to use a VPN with full-tunnel configuration, ensuring all DNS requests route through trusted corporate resolvers
- Auditting proxy authentication logs for authentications from unknown hosts: Look for suspicious logs from known abused infrastructure
- Disabling web proxy auto-discovery (WPAD) where not required
- Validating the site before entering credentials: Train employees to verify the URL and certificate of any page requesting credentials before entering them, particularly when connected to hotel, conference center, airport or other public Wi-Fi networks
- Disabling the device code authentication flow at the identity provider: In Microsoft Entra ID, configure a Conditional Access policy that blocks the device-code flow

---
*爬取时间: 2026-07-24 21:45:28*
*来源: 直接站点爬取*
