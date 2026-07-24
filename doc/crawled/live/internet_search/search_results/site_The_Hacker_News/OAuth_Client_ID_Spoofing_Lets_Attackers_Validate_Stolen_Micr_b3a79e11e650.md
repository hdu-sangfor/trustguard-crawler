# OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials

### 来源信息
- **URL**: https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
At least two distinct threat actors are weaponizing a novel evasion technique called OAuth client ID spoofing in cloud campaigns, while slipping past telemetry.
The activity allows users to enumerate user accounts and validate stolen credentials in Microsoft Entra ID environments, without ever generating a successful sign-in event that would otherwise alert defenders. And bad actors have begun to exploit this gap to obtain unauthorized access to an organization's cloud services.
"A blind spot in cloud sign-in telemetry: Entra ID returns different error responses depending on whether a supplied OAuth client ID is valid," Proofpoint said in a statement. "Attackers exploit this to infer valid usernames and correct passwords at scale, effectively checking stolen credential lists without logging a successful login."
In other words, the attacks leverage the OAuth client ID, a globally unique identifier (GUID) assigned to applications when requesting access to user data, and is passed as "client_id" in authentication requests. By providing spoofed client IDs, it enables account enumeration without a registered OAuth application and permits attackers to infer both password and account validity without generating a successful sign-in event.
"The Entra sign‑in logs are a primary telemetry source for identifying malicious authentication activity, including user enumeration, password spraying, and initial access attempts," Proofpoint researcher Rachel Rabin said.
Threat clusters like UNK_CustomCloak have been observed spoofing User-Agent strings to orchestrate brute-force campaigns targeting Microsoft Entra ID environments by exploiting a legacy, discontinued first-party application called Windows Live Custom Domains to bypass standard sign-in restrictions and probe user passwords across over 4,000 tenants.
But the latest efforts mark an evolution of this tradecraft by spoofing the OAuth client IDs via HTTP POST requests to Microsoft's OAuth 2.0 token endpoint using the Resource Owner Password Credentials (ROPC) flow. Specifically, this involves supplying a syntactically valid client ID but one that does not correspond to a real application.
In such scenarios, only the application ID is recorded in the Entra sign-in log without a corresponding application name. The response, which contains an Azure Active Directory Security Token Service (AADSTS) error code, can then be used to infer whether the account exists and whether the password is correct without a registered application.
"If the spoofed client ID is not a proper UUIDv4, Entra does not reject the request outright," Proofpoint explained. "Attackers can therefore analyze this error response to identify valid accounts and passwords, despite using malformed client IDs."
"When a spoofed client ID is used, no corresponding application name is recorded in the sign-in log. This means that detections that look for surges against a specific application name may miss this activity entirely, as the field is blank."
Armed with this information, attackers could identify accounts that could be exploited for stealthy access, at the same time making it challenging for defenders to identify suspicious activity.
Proofpoint said it has identified two large campaigns that have independently adopted the technique towards the end of December 2025, indicating the approach is being increasingly incorporated into attacker tradecraft as opposed to being an isolated incident:
- UNK_pyreq2323 (from January to March 2026), which used more than 700,000 spoofed client IDs from Amazon Web Services (AWS) infrastructure to target more than 1 million accounts across nearly 4,000 tenants, causing lockouts for roughly 28% of targeted users due to failed attempts.
- UNK_OutFlareAZ (starting Dec 2025), which leveraged Cloudflare infrastructure to target over 2 million users with 3.7 million randomized spoofed application IDs.
Both the campaigns have been observed using valid UUIDs rather than malformed identifiers and demonstrate patterns that align with precompiled username wordlists. That said, while UNK_OutFlareAZ enumerated users alphabetically, UNK_pyreq2323 did not. Another aspect in which they differed was in how the client IDs were spoofed.
UNK_pyreq2323 is said to have modified the trailing digits of a known application ID, and then reused spoofed IDs across up to 12 users. In contrast, UNK_OutFlareAZ generated a unique client ID per request.
"By fragmenting authentication attempts across many fictional applications, activity becomes harder to correlate and may evade per-application detections and rate limiting," Proofpoint said. "Organizations may attempt to mitigate traditional enumeration attacks by applying Conditional Access policies scoped to applications commonly targeted for enumeration. Spoofed client IDs won't trigger CA policies that are scoped to a specific application."
Although the problem of OAuth client ID spoofing is specific to Microsoft, Yaniv Miron, director of threat research at Proofpoint, told The Hacker News that "we do believe that other identity providers are possibly exposed to such issues."
"Spoofing in general has been a well-known method for years; adversaries will attempt to spoof anything that they can (different fields usually), including client ID," Miron added. "Adversaries are constantly monitoring threat researchers' blogs and publications, so we believe that they are adopting public research into their attacks."
(The story was updated after publication to include a response from Proofpoint.)

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
