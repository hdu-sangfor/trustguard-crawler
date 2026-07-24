# FeatureMicrosoft’s 3-day patching directive comes with added operational riskBy John LeydenJul 23, 20267 minsEndpoint Pr

### 来源信息
- **URL**: https://www.csoonline.com/article/4200366/microsofts-3-day-patching-directive-comes-with-added-operational-risk.html
- **来源站点**: CSO Online
- **页面抓取**: 成功

### 页面正文
Microsoft 365 Director Jeremy Chapman this month took to video to tell Windows admins that the days of delaying security patches are over.
Complex enterprise systems and historic incidents involving patch problems have caused many admins to hold fire on immediately applying security patches, in many cases deferring patch rollouts for two to four weeks or more to ensure stability. Microsoft argues that this cautious approach, though understandable, is no longer viable because AI is accelerating the discovery and exploitation of software vulnerabilities.
As a result, Microsoft has advised admins to act on patches within three days.
Independent experts agree with Microsoft’s diagnosis of the problems posed by AI-powered vulnerability discovery, but many say Microsoft’s three-day remediation window is unrealistic for large enterprises with heavy testing, change-control, and compatibility constraints.
Instead of taking a blanket approach, enterprises need to focus more on quickly resolving those vulnerabilities that are under active exploitation and relevant to their environments, according to critics of Microsoft’s revised approach.
Tighter patching deadlines
Microsoft’s revised vulnerability remediation advice comes in the wake of its work with Anthropic’s Project Glasswing and findings from Microsoft’s own MDASH multi-model agentic scanning harness. Tighter patching deadlines are configurable via Windows Autopatch and Microsoft Intune or update tooling options such as Microsoft Configuration Manager and Windows Server Update Services.
As IT environments become increasingly more complex, inadvertent issues can occur with what appears to be a simple patch.
Unique or complex deployments may not be compatible with a patch, resulting in potential data corruption, system shutdown, or the dreaded “Blue Screen of Death.” Multiple vendors in the operating system and the enterprise software and security market have released patches that have broken products and caused outages, so the issue goes well beyond Windows shops.
Increasing both the volume and the speed of patching is unsustainable for most security teams because organizations are already struggling with successful remediation as it is.
“Many organizations have patch windows, review cycles, and test environments to identify these issues prior to patching production environments,” says Scott Caveza, senior research manager at exposure management and vulnerability assessment firm Tenable. “Organizations lacking the resources for extended validation risk deploying faulty patches that cause downtime or force last-minute configuration changes.”
Caveza adds: “The mitigation steps will vary for each organization, but blindly relying on auto-updates without contextual validation is not a defensible security posture.”
CISA’s Known Exploited Vulnerabilities list and other industry data suggest that only a small fraction of disclosed vulnerabilities are confirmed as exploited in the wild.
“[Enterprises should focus on] identifying vulnerabilities with credible and functional PoCs, verified exploitation, or sustained attention from ransomware groups, threat actors, and botnets,” says Caitlin Condon, vice president of security research at VulnCheck. “Timely exploit intelligence helps organizations identify the bugs that require immediate attention, while allowing lower-risk issues to proceed through appropriate testing and change control.”
Other independent experts are more sympathetic to Microsoft’s argument that AI has made vulnerability discovery and exploit development faster than ever and, as a result, the risks of delaying patches are far greater.
“Organizations sometimes delay patches to protect the uptime of critical systems, and many updates still require a restart,” says Danny Jenkins, CEO and co-founder at endpoint protection technology vendor ThreatLocker. “Some teams also stay one update cycle behind because they are concerned that a new patch could introduce bugs or break an overlooked dependency. Unfortunately, delaying patches to preserve uptime is becoming much harder to justify.”
Jenkins adds: “Organizations should not leave critical systems exposed while waiting for the next maintenance window. Patches should still be tested, but that process needs to move quickly, with the highest priority given to vulnerabilities that are actively exploited or exposed to the internet. A controlled interruption is usually far less costly than a successful attack exploiting a known vulnerability.”
Wider cross-industry impact
Microsoft’s three-day recommendation reflects a fundamental change in the threat landscape. Other vendors might be expected to follow suit and that means CISOs need to revise their approach to vulnerability remediation.
“Organizations should expect faster disclosure-to-exploitation timelines to become the norm, which means security programs must emphasize automation, trusted software supply chains, and continuous visibility rather than relying on periodic maintenance windows,” says Mike Nelson, VP and field CTO at DigiCert.
AI is compressing the time between vulnerability discovery and exploitation, and the industry is moving rapidly from 30-, 60-, and 90-day patching windows toward a matter of days.
However a “blanket three-day requirement for every vulnerability is neither realistic nor safe for most large organizations,” says Jeff Williams, founder and CTO at Contrast Security.
Failing to patch opens up security threats, but rushing an inadequately tested patch into production creates operational risk.
“The goal cannot be to treat every CVE [vulnerability] as an emergency,” according to Williams. “It has to be identifying, within hours, which vulnerabilities are actually exploitable and require immediate action.”
Holistic remediation
Security teams are already facing significant pressure to patch faster and to remediate a rising tide of new vulnerabilities, yet many practitioners are losing ground. Verizon’s Data Breach Investigation Report, published earlier this year, found that the median time to patch had actually increased to 43 days.
Patch deployment in enterprise environments involves configuration changes, reviews, testing, and validation.
Enterprises need to become more proficient at exposure management so that they have a holistic view of their environment that’s necessary to identify which assets are at greatest risk.
“By pinpointing the misconfigurations, identity flaws, and specific vulnerabilities that pose the greatest risk to their environment, security teams can prioritize exactly what to patch first,” Tenable’s Caveza says. “The idea of ‘patch everything’ is really outdated, and ‘patch faster’ isn’t feasible with the rapidly increasing number of vulnerabilities disclosed each day.”
CISOs will have to re-engineer their vulnerability and exposure management processes. “The traditional model of scanning everything, assigning generic severity scores, and tilting at a massive and expanding backlog is no longer fast enough,” says Contrast Security’s Williams.
Organizations need to identify the small number of vulnerabilities that matter, protect against them immediately, and remediate them on a timeline the business can safely support.
Enterprises should prioritize on resolving “internet facing, remotely exploitable vulnerabilities and any of the CISA Known Exploited Vulnerability list,” says Jose Lejin, an IEEE senior member.
Businesses that cannot safely validate and deploy patches within three days still have options, including “compensating controls, reducing an asset’s exposure, or in some cases removing the component entirely, all of which shrink the exploitable risk and buy time to patch properly,” says Brad Hibbert, CSO of vulnerability management provider Brinqa.

---
*爬取时间: 2026-07-24 21:46:15*
*来源: 直接站点爬取*
