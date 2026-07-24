# How to Implement Zero Trust: 7 Expert Steps

### 来源信息
- **URL**: https://www.techtarget.com/searchsecurity/feature/How-to-implement-zero-trust-security-from-people-who-did-it
- **域名**: www.techtarget.com
- **检索关键词**: zero trust architecture implementation guide
- **页面抓取**: 成功

### 搜索摘要
Follow these high-level steps to deploy an effective zero-trust strategy. Dedicate a small team tasked with implementing the zero-trust migration. Identify key personnel to plan and design the zero-trust strategy.

### 页面正文
Zero trust is a cybersecurity model, not a technology or a control. It takes the principle of least privilege to the next level by adding new restrictions governing how users access resources.
The term zero trust is itself a misnomer. Trust is a continuum. As a result, zero trust means shifting away from "trust everything" toward "trust nothing" -- limiting access commensurate with risk and with the usability of trust verification measures.
In short, the zero-trust security model assumes active threats exist inside and outside a network's perimeter, with on-site and remote users alike required to meet stringent authentication and authorization requirements before being granted access to data and resources.
A zero-trust initiative, implemented effectively, must strike a reasonable balance between security and usability. Compromises are less likely to occur, and those that do will cost attackers more time and effort to achieve. Security teams will also detect attacks sooner, reducing their impact.
Let's examine how to implement zero trust at your organization.
Follow these high-level steps to deploy an effective zero-trust strategy.
1. Form a dedicated zero-trust team
Dedicate a small team tasked with implementing the zero-trust migration. Identify key personnel to plan and design the zero-trust strategy. Educate the team about zero-trust principles and how implementation is made possible through a combination of architectural changes, cybersecurity technologies and policies.
Consider recruiting team members with expertise across multiple security areas, including application, data, network, infrastructure and device security.
2. Conduct an asset inventory
This step helps define the organization's attack surface and its potential risks. It outlines every asset an organization needs to secure and helps prioritize updates or changes based on risk levels.
First, inventory all cybersecurity assets, including data, devices, services, applications, systems and networks. Make it as comprehensive and up to date as possible. The inventory should include the following details on each asset:
- Rank its importance.
- Pinpoint its geographic location and owner.
- Designate who and/or what should be able to access it.
- Determine how important or sensitive that access is -- for example, initiating large bank transfers versus submitting expense reports.
Also, start to identify any possible zero-trust components already in place. Check existing cybersecurity technology acquisition plans to see if any technologies to be deployed in the coming months or years could be part of a zero-trust strategy.
3. Conduct a gap analysis
Determine your business's goal for zero trust. Conduct a gap analysis to determine where the company is today and what it wants to achieve. The key is to limit access commensurate with risk while keeping technology usable. Zero trust will look different for every organization. The gap analysis should include techniques, such as threat modeling, that identify weaknesses that zero trust can mitigate.
4. Choose a zero-trust implementation approach
There is no one-size-fits-all approach to implementing zero trust. It is a combination of technologies, processes and controls unique to your organization.
NIST has defined four common zero-trust architecture approaches:
- Enhanced identity governance. This approach centers on user and entity identity. It permits access based on identity and assigned attributes using technologies such as identity and access management, credential management, MFA, biometrics, federated identity, identity governance, endpoint security, SIEM and security analytics.
- Software-defined perimeter. This approach uses network infrastructure to implement zero trust. It involves an overlay network and uses agents and gateways to establish a secure communication channel between clients and resources.
- Microsegmentation. This approach splits individual assets or groups of assets on network segments protected by gateway security components. It uses infrastructure such as intelligent switches, routers, next-generation firewalls (NGFWs) or gateways. It could also involve host-based microsegmentation using software agents or firewalls on endpoint assets. It also requires an identity governance program.
- Secure access service edge. The SASE approach uses SD-WAN, secure web gateways, cloud access security brokers, NGFWs and zero-trust network access to create zero-trust architecture for branch offices, remote workers and on-premises networks.
5. Plan the zero-trust implementation
Expect full implementation to take at least a few years. Your organization probably has some components in place already and can reconfigure others to support zero trust, but nearly every organization will need to acquire new enterprise-level cybersecurity technologies.
This involves product evaluation, acquisition and implementation -- all of which could easily require a year or more. While this unfolds, repurpose the components and processes already in place to support zero trust.
Planning should include the following:
- Foundational elements of zero trust. Includes user identity proofing, device identities, credentials, authentication methods, access control and access management technologies, and network architectures -- e.g., increased segmentation, remote access.
- Scaling of supporting technologies. Ensure technologies such as event logging, monitoring and analysis can support the implementation. Zero trust is likely to increase the burden on these technologies.
- Zero-trust policy development. Deny everything by default and only allow that which is explicitly permitted. Deploy dynamic risk assessment measures, such as requiring more rigorous and/or more frequent authentication in high-risk situations.
- Accommodations for legacy technology. Parts of an organization might use legacy technologies that can't fully support zero trust. Determine which zero-trust aspects these systems can provide and decide if zero trust can exist outside the legacy technology to protect it. For example, use network segmentation to minimize access to and from the legacy devices.
6. Gradually implement the zero-trust plan
Implementing zero trust might seem overwhelming, but the good news is that it's best done gradually and over an extended period of time -- a series of small changes every so often as opposed to many changes all at once. Prioritize changes that provide quick wins for users, such as single sign-on (SSO) technologies that improve usability. Focus on changes, especially behind the scenes, that are prerequisites for making other modifications.
Assess the effect on usability before changes are deployed. Conduct usability testing and consider users' feedback before widely implementing zero trust-related adjustments. If formal usability testing isn't feasible, consider having part of the technology staff act as early adopters. Then, gather and address their comments before wider deployment.
Review the zero-trust plan at key points during its implementation to determine if the plan needs any updates. Perhaps an existing security control recently added zero trust support, thus eliminating the need to add a separate product or service with those same capabilities.
7. Maintain the zero-trust implementation
Remember that deploying a zero-trust strategy is not a one-time activity. As a framework, it is critical to foster and maintain zero trust over time.
When learning how to implement a zero-trust model, keep in mind that its policies will require updating as cyber assets change and usage evolves. Monitor and maintain existing assets to ensure they continue to support the zero-trust plan, and ensure any new assets are included in the strategy.
Cloud service provider Akamai Technologies, based in Cambridge, Mass., began exploring zero trust after suffering a data breach in the 2009 Operation Aurora cyberattack.
"There wasn't really a roadmap to follow," said Andy Ellis, former Akamai CSO. "We just said, 'We need to figure out how we can better protect our corporate network and our users.'"
Akamai initially aimed to restrict lateral movement within the enterprise network using microsegmentation. That presented a challenge, however, since lateral movement often happened between applications that had permission to talk to each other.
"It's really difficult to microsegment things when your backup server can talk to everything," Ellis said. "That's where you get compromised."
First, the Akamai team focused on securing domain administrators' accounts, working on authentication protocols and mandating separate passwords for each additional level of access. It also explored using X.509 certificates to enable hardware authentication on a device-by-device basis.
"But we were still thinking in network terms," Ellis said. Then, the team had a breakthrough. "We realized it wasn't about the network; it's really about the application."
It wanted to find a way to let employees securely access internal applications from a login point on the company's content delivery network (CDN), thus keeping end-user devices off the corporate network entirely. Ellis' team opened a hole in the firewall and started manually integrating one application at a time -- a slow and tedious process. "Let me tell you, our system administrators were getting pretty cranky," Ellis said.
But, about halfway through the project, the organization discovered a small company called Soha Systems that enabled an alternative access model: dropping a VM between Akamai's firewall and application servers to connect apps on one side with the CDN-based SSO service on the other. Ellis and his team found the Soha connector supported granular role-based access for employees and third-party contractors on a user-by-user and app-by-app basis, via a browser with no VPN required. If hackers managed to commandeer an employee's credentials, they would theoretically see only the limited applications and services that particular worker was entitled to use.
Akamai deployed Soha's technology, ultimately buying the company and folding the technology into its Enterprise Application Access service, enabling customers to gradually offload VPN traffic as they build their own zero-trust environments.
"You don't have to do it all at once," Ellis said, pointing out that Akamai's zero-trust journey unfolded over the course of years. "It's step by step. You're going to transform your whole business by the time you're done."
Karen Scarfone is a general cybersecurity expert who helps organizations communicate their technical information through written content. She co-authored the Cybersecurity Framework (CSF) 2.0 and was formerly a senior computer scientist for NIST.
Alissa Irei is senior site editor of Informa TechTarget's SearchSecurity site.

---
*检索时间: 2026-07-24 15:20:57*
*搜索来源: DuckDuckGo*
