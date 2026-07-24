# 9 Identity and Access Management Trends to Watch in 2025

### 来源信息
- **URL**: https://www.techtarget.com/searchsecurity/tip/Identity-and-access-management-trends-to-watch
- **域名**: www.techtarget.com
- **检索关键词**: identity access management trends 2025 2026
- **页面抓取**: 成功

### 搜索摘要
The rise of machine identity management. More mature zero-trust practices. Applying AI and generative AI (GenAI) to IAM. More teams handling IAM responsibilities. Preparing for post-quantum cryptography.

### 页面正文
Better technologies and safer practices can reduce the risks of identity-related cyberthreats. Still, the threats persist and evolve.
Let's examine some of the trends in identity access and management (IAM) to see how the problems and potential solutions are taking shape. Key ones include the following:
- The rise of machine identity management.
- More mature zero-trust practices.
- Applying AI and generative AI (GenAI) to IAM.
- More teams handling IAM responsibilities.
- Preparing for post-quantum cryptography.
- Fewer VPNs.
- A push toward single sign-off.
- Automation.
- Improved MFA.
Organizations are increasingly aware that they have vast numbers of identities that aren't people. Devices, VMs, accounts and APIs are just some of the nonhuman things with identities that need to be secured through IAM processes.
To secure and manage these, organizations turn to activities known by a variety of terms: machine identity management, workload identity management, nonhuman identity management. Whatever the label, the work is the same.
"All of the cloud adoption, all of the automation, this has led to an explosion of the access for workloads," said Felix Gaehtgens, security analyst at Gartner. "They are being created -- left, right and center -- by all types of different teams, and most organizations don't properly manage them."
These soft targets hold special appeal to bad actors. "A significant portion of breaches happen not because a human account is breached, but because a machine account is breached," Gaehtgens said.
And, when such a nonhuman account is compromised, the fix is more complicated. It might not be immediately clear, for instance, how that machine identity was created.
"If you don't have a handle on this, you're going to be in a world of hurt," said Todd Thiemann, security analyst with Informa TechTarget's Enterprise Strategy Group. "Your mean time to response is going to suffer, and it's going to take a lot more time to remediate that situation."
IAM tools can help a security team discover machine identities that they might not have known about. IAM systems can also manage those identities through a full creation-to-retirement lifecycle.
The zero-trust security model will evolve to include more and better secondary attributes. This approach, which is sometimes referred to as adaptive authentication, results in a deeper and more continuous assessment of risk.
"It's being more context-aware," said Matthew McFadden, vice president at General Dynamics Information Technology. "Are you signing in from the same place you typically do during your workday? Or is it overseas?"
Looking at these sorts of attributes makes zero trust not just better at securing access, but also at improving an organization's broader security posture.
"Now, we're looking at device health," McFadden said. "Do you have all your patching? Do you have your endpoint security?"
When zero trust is applied with greater sophistication, security professionals see deeper into their organization, ask better questions about access and manage user permissions more granularly.
AI could be an ally to security teams by taking over some of the drudgery of IAM.
Thiemann sees AI as being of particular use with a task such as entitlement reviews, which is a slow but important task to be sure a user's privileges are appropriate. IAM experts still need to evaluate those reviews done by AI, Thiemann said, but the result is a smoother, less manual process. "We're able to do them a lot more quickly, effectively and frequently by applying AI to the problem."
Access management matters in application security, infrastructure security, endpoint security and elsewhere. "A lot of other teams are doing IAM now," Gaehtgens said.
With this work distributed more widely across an organization, IAM specialists should be ready to provide leadership and guidance to their colleagues. The right policies and support enhance security, Gaehtgens said, as does a willingness by IAM specialists to learn more about what those other teams are up to -- and why.
Encryption is the core ingredient to identity security. It's what makes identity management possible. But what if we can no longer encrypt things? That jarring question is being asked with more urgency now that quantum computing appears to be a not-so-distant prospect.
If unleashed against current cryptography, a quantum computer would be able to do what current computers do not have the power to do: break the unbreakable. Current key encryption methods would simply not be able to withstand the calculation powers that quantum computing unleashes.
It is far from clear when that moment might arrive, but cryptographers have been preparing as if it is an inevitability. Since 2016, the U.S. government's NIST has been coordinating efforts to develop what it calls "quantum-resistant" public key cryptographic algorithms. NIST made three of those algorithms available for the first time in 2024.
"Now, the race is on to implement those," McFadden said, noting that this will be a significant undertaking involving everything from browsers to certain legacy technologies that might never be able to make the transition.
The shift to post-quantum encryption is a milestone in information security. It's a big and necessary transition.
"Encryption underpins a lot of stuff in identity," Gaehtgens said.
McFadden expects to see more organizations shift away VPNs in favor of tools that assess risk more dynamically. Specifically, he pointed to zero trust network access (ZTNA). This technology does more than check to see who it is that's logging in.
ZTNA, for example, restricts network traffic until a specific policy gives the green light. It also verifies the identities of all users involved in that network flow before allowing the traffic; plus, it checks again later to ensure nothing has changed since the prior verification. ZTNA borrows its logic from the zero-trust architecture's prove-first, prove-often demands.
"With the traditional model, once you're in their perimeter, you're kind of in," McFadden said. "Now, we're inspecting every aspect of what's happening -- from user to device to applications to data."
These capabilities are finding their way into the security market, including in the AWS Verified Access service and Palo Alto Networks' Prisma Access products.
ZTNA helps organizations better manage access for their evermore far-flung workforces, but these tools can also deliver better performance than VPNs, McFadden said.
Single sign-on (SSO) has been welcomed, but could single sign-off be next? Developments in Continuous Access Evaluation Profile (CAEP) could make that possible, Gaehtgens said.
Proponents of the CAEP framework see it as a way sessions can be terminated in an orderly and secure manner. It would provide the mechanism that, in effect, closes the interoperability loop that opens when users access multiple systems with SSO. "We establish trust, but we can't really tear the trust down," Gaehtgens said. "CAEP actually does this."
A system that uses CAEP could, for example, close a user's session if it detects that the device in use falls out of compliance.
"It can send real-time risk signals across the identity provider and the SaaS provider," Gaehtgens said.
Google, Okta, Microsoft, Cisco, Apple and others have backed the standard. CAEP could become more mainstream in 2025 and 2026, Gaehtgens predicted.
Another move toward standardization worth watching is Interoperability Profile for Secure Identity in the Enterprise (IPSIE). A working group organized by the OpenID Foundation, which includes representatives from Okta, Microsoft, Google and others, envisions IPSIE aligning disparate identity standards into a single standard. If adopted, the new interoperability standard could improve SSO, lifecycle management and session termination.
Thiemann sees interoperability as especially important to achieve more orderly session termination, which logs users out of applications in a systematic way. "There's the hope that systemizing it, putting standards in place, will make it less of a one-off thing."
Sessions that aren't well managed or that don't require periodic reauthentication are vulnerable to hijacking.
In most respects, the challenge of identity security isn't getting easier. The scale of the problem is too vast for even the most capable security pros who lean on IAM best practices. They need to implement useful IAM tools.
McFadden urges teams to automate as much as they can in their IAM and zero-trust initiatives.
"You can't keep throwing humans at this challenge. You've got to automate it to scale," McFadden said. "I'm doubling down, tripling down on automation wherever possible."
More organizations now use MFA to enhance their cyberdefenses. Requirements for users to provide two or more authentication factors are an obvious upgrade over methods that ask only for a password.
Experts expect even greater adoption of MFA, but they recognize there's room for improvement. MFA tactics should become more sophisticated -- be it through interoperability standards or tools that better fend off hackers trying to intercept a text message intended for an authorized user.
"Phishing-resistant MFA is an area we want to move toward," McFadden said.
Phil Sweeney is an industry editor and writer focused on information security topics.

---
*检索时间: 2026-07-24 15:40:12*
*搜索来源: DuckDuckGo*
