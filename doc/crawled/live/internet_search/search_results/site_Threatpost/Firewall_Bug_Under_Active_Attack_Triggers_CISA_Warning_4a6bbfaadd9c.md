# Firewall Bug Under Active Attack Triggers CISA Warning

### 来源信息
- **URL**: https://threatpost.com/firewall-bug-under-active-attack-cisa-warning/180467/
- **来源站点**: Threatpost
- **页面抓取**: 成功

### 页面正文
Software running Palo Alto Networks’ firewalls is under attack, prompting U.S. Cybersecurity and Infrastructure Security Agency (CISA) to issue a warning to public and federal IT security teams to apply available fixes. Federal agencies urged to patch the bug by September 9.
Earlier this month, Palo Alto Networks issued a fix for the high-severity bug (CVE-2022-0028) that it says adversaries attempted to exploit. The flaw could be used by remote hackers to carry out reflected and amplified denial-of-service (DoS) attacks without having to authenticate targeted systems.
Palo Alto Networks maintains the flaw can only be exploited on a limited number of systems, under certain conditions and that the vulnerable systems are not part of a common firewall configuration. Any additional attacks exploiting the bug have either not occurred or been publicly reported.
Affected Products and OS Versions
Affected products include those running the PAN-OS firewall software include PA-Series, VM-Series and CN-Series devices. PAN-OS versions vulnerable to attack, with patches available, include PAN-OS prior to 10.2.2-h2, PAN-OS prior to 10.1.6-h6, PAN-OS prior to 10.0.11-h1, PAN-OS prior to 9.1.14-h4, PAN-OS prior to 9.0.16-h3 and PAN-OS prior to 8.1.23-h1.
According to Palo Alto Networks advisory; “A PAN-OS URL filtering policy misconfiguration could allow a network-based attacker to conduct reflected and amplified TCP denial-of-service (RDoS) attacks. The DoS attack would appear to originate from a Palo Alto Networks PA-Series (hardware), VM-Series (virtual) and CN-Series (container) firewall against an attacker-specified target.”
The advisory describes the non-standard configuration at risk as the “firewall configuration must have a URL filtering profile with one or more blocked categories assigned to a security rule with a source zone that has an external facing network interface.”
The configuration is likely unintended by the network administrator, the advisory said.
CISA Adds Bug to KEV Catalog
On Monday, CISA added the Palo Alto Networks bug to its list of Known Exploited Vulnerabilities Catalog.
The CISA Known Exploited Vulnerabilities (KEV) Catalog is a curated list of flaws that have been exploited in the wild. It is also a list of KEVs that the agency “strongly recommends” public and private organizations pay close attention to in order to “prioritize remediation” to “reduce the likelihood of compromise by known threat actors.”
Reflective and Amplification DoS Attacks
One of the most notable evolutions in the DDoS landscape is the growth in the peak size of volumetric attacks. Attackers continue to use reflection/amplification techniques to exploit vulnerabilities in DNS, NTP, SSDP, CLDAP, Chargen and other protocols to maximize the scale of their attacks.
Reflected and amplified denial-of-service attacks are not new and have steadily become more common over the years.
Distributed denial of service attacks, bent on taking websites offline by overwhelming domains or specific application infrastructure with massive traffic flows, continue to pose a major challenge to businesses of all stripes. Being knocked offline impacts revenue, customer service and basic business functions – and worryingly, the bad actors behind these attacks are honing their approaches to become ever more successful over time.
Unlike limited volume DDoS attacks, reflective and amplified DoS attacks can produce much higher volumes of disruptive traffic. This type of attack allows an adversary to magnify the amount of malicious traffic they generate while obscuring the sources of the attack traffic. An HTTP-based DDoS attack, for example, sends junk HTTP requests to a target’s server tying up resources and locking out users from using a particular site or service.
A TCP attack, believed used in the recent Palo Alto Networks attack, is when an attacker sends a spoofed SYN packet, with the original source IP replaced by the victim’s IP address, to a range of random or pre-selected reflection IP addresses. The services at the reflection addresses reply with a SYN-ACK packet to the victim of the spoofed attack. If the victim does not respond, the reflection service will continue to retransmit the SYN-ACK packet, resulting in amplification. The amount of amplification depends on the number of SYN-ACK retransmits by the reflection service, which can be defined by the attacker.

---
*爬取时间: 2026-07-24 21:43:44*
*来源: 直接站点爬取*
