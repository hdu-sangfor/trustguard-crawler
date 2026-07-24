# How software development’s speed obsession enabled TeamPCP’s chaos crusade

### 来源信息
- **URL**: https://cyberscoop.com/teampcp-breaks-open-source-software-trust-model/
- **来源站点**: CyberScoop
- **页面抓取**: 成功

### 页面正文
TeamPCP is on a rampage through open-source software.
In less than four months, the threat actor has compromised and injected malicious code into more than 1,000 software packages. The extraordinary spree has transformed how software developers and maintainers distribute and manage their code, as their dependencies and repositories have become one of the most effective and prevalent attack vectors this year.
While there has been a host of technical exploits, TeamPCP’s greatest attack has been the uprooting of trust — repeatedly proving that most organizations fail to verify the code they ingest into their systems is legitimate, abusing a nearly blind faith that much of the software development industry relies on to power today’s modern economy.
Starting with Trivy in February, TeamPCP’s attacks have shaken that trust many times over.
The scale of TeamPCP’s attacks lies partly in the automated systems companies use to deploy code, like CI/CD pipelines. It is also capitalizing on new security gaps created by developers’ increasing reliance on AI. Yet, with relatively low effort and unoriginal tactics, TeamPCP is wrecking open-source frameworks and underlying systems at levels the technology community has rarely reckoned with.
“Developers didn’t do a great job of analyzing the security of their open-source dependencies before but, now with AI, there’s in some cases virtually no human in the loop or any kind of sanity check on what these tools are doing,” Feross Aboukhadijeh, founder and CEO at Socket, told CyberScoop.
“You have agents installing packages that haven’t been vetted,” he said. “When an attacker gets in, the impact is even broader because there’s less checks and balances to stop it from affecting everybody.”
TeamPCP hasn’t identified a new problem or proved anything novel. The crux of these attacks hinge on a central theme — defensive vulnerabilities the entire software industry has known about for years. Researchers and developers know the open source trust model is broken and susceptible to sabotage. Yet, the software industry has not fixed this problem.
“The speed and scale of these attacks is what makes it most notable, not necessarily the methodology behind it, because at the core it is really about exploiting third-party trusts that we have,” said Kimberly Goody, senior manager at Google Threat Intelligence Group.
Software packages are typically subjected to intensive security monitoring to test for vulnerabilities and poisoned updates before they are released to live environments.
Yet, the real vulnerability highlighted by TeamPCP lies further up the chain of command with the organizations or individuals that publish these packages to the wider market, according to Nathaniel Quist, manager of cloud threat intelligence at Palo Alto Networks.
“It is their responsibility to secure their credentials and not provide a jump off point to trigger a supply-chain event,” he said. “Everything that interacts with or crosses through that zone must be highly monitored and controlled to ensure a compromise can be contained quickly and easily.”
TeamPCP’s motivation
TeamPCP, like any prolific cybercriminal, has captured significant attention from threat hunters since it emerged in late 2025. Google attributes the activity to one core operator.
The company said it traced TeamPCP’s residential and mobile IP address connections to South Africa, indicating the primary operator was located there during at least some of its attacks.
“We don’t believe that there’s an established core group, at least not yet, and that a lot of this has been conducted by an individual,” Goody said. Google declined to name the core operator or confirm it knows the person’s true identity.
Palo Alto Networks said the core manager of TeamPCP uses the “ResoluteXBF” handle on multiple platforms. The cybersecurity firm is also tracking two additional core members: “diencracked” and “Shinigami.”
If TeamPCP is primarily run by one person, law enforcement has a rare opportunity to make a lasting impact with a single arrest.
TeamPCP has collaborated with other cybercriminals, but most of those partnerships were short-lived and ended in a public feud or otherwise failed to get off the ground in any meaningful way, Goody said.
Researchers have linked TeamPCP to extortion crews, dark web forums and affiliates including Lapsus$, ShinyHunters, Vect, DragonForce, BreachForums and “HasanBroker.” TeamPCP listed about 4,000 private code repositories on a dark web forum with an asking price of $95,000.
The actions to date, including unpredictable behavior, indicate motivations beyond financial gain and a “clear desire for notoriety,” Goody said. “They seem to like to make chaos.”
Quist draws the same conclusion from his months-long investigation, noting that it encourages other cybercriminals to get in on the action, at one point offering financial rewards for the largest software supply-chain attack.
TeamPCP isn’t in the game for extortion payments, he said. “These actors are more interested in the underground street cred they are gaining” and “causing as much damage and mayhem as possible.”
Victims abound, but exposure limited
TeamPCP has been remarkably noisy, opportunistically injecting malware into open-source software for the purpose of stealing credentials for Kubernetes environments, Amazon Web Services, Microsoft Azure, Google Cloud and many other connected services.
The group’s claimed victim list is staggering: Checkmarx, Bitwarden, LiteLLM, Telnyx, Mercor AI, PyTorch Lightning, AntV, SAP, GitHub, TanStack, UiPath, MistralAI, Microsoft DurableTask, Red Hat and Nx Console.
The full collection of packages compromised or poisoned by TeamPCP to date accounts for roughly 500 million weekly downloads combined, according to Quist.
While the breadth of potential downstream compromise flowing from those downloads is substantial, many endpoints infected with those malware-riddled packages aren’t exposed to the internet and less susceptible to attack, he added.
“I don’t think there’s going to be a very extremely large number of victims,” Quist said. “There’s going to be a lot of people who potentially could be compromised and have potentially vulnerable packages in their environment, but that doesn’t necessarily mean they’re in an exploitable position.”
While these incidents have grabbed headlines, TeamPCP hasn’t accumulated payouts nearly as large as other cybercriminals. The broader reputational impact it has wrought, however, is massive.
TeamPCP has publicly claimed more than 10,000 victims and about $90,000 in extortions, according to Quist.
“They might not be making a lot of money, but they are causing a lot of impact,” Goody said. “Their campaigns have been very disruptive.”
How TeamPCP’s operating model targets development
TeamPCP’s victim list has grown as its hijacked open-source repositories on npm, PyPI, GitHub and other outsourced developer tools that are incorporated into upstream code running in production environments.
Developer laptops and other endpoints that are assigned to install, build and publish software widely contain keys and access to source code that create incredibly valuable supply-chain targets for attackers, Amitai Cohen, head of the attack vector intel team at Wiz, explained during a June presentation on TeamPCP at SleuthCon in Arlington, Va.
The group targets CI runners, which are automated systems that build, test, and publish code. TeamPCP injects malware into the code repositories these runners maintain. When other developers pull that code into their own systems, they unknowingly download the malware alongside it.
Some of these artifacts, including Python libraries, npm registries and GitHub Actions, are downloaded almost immediately by thousands or millions of developers who’ve set their runners up to consistently pull the latest version, according to Cohen. “We as a security industry have taught them that that is the right thing to do. You want to use the latest version because you want to be protected against vulnerabilities, and obviously you want to benefit from all the latest features.”
That instinct is exactly what TeamPCP exploits. By compromising one company’s CI/CD workflow, the group gains access to every downstream user who automatically pulls that infected code. “This is what allows [TeamPCP] to leverage initial access to some patient zero, some company that had a vulnerability in their CI/CD workflow, in order to gain access to their downstream users,” Cohen said. “That’s just how the software supply chain works. Everything has dependencies upon dependencies upon dependencies.”
Some of the packages compromised by TeamPCP were live for almost 13 hours, but security practitioners have responded by identifying code-injection attacks much quicker now, pulling some compromised repositories within 15 minutes, said Ben Read, director of strategic intelligence at Wiz.
The threat group’s operations remain high-tempo. TeamPCP infects new software packages almost daily, validates compromises and captures sensitive data within 24 hours, according to Wiz researchers.
The threat group has consistently evolved its tactics, developing payloads in JavaScript and Python while spreading from local files to Kubernetes application programming interfaces and bundled software development kits. Most recently, it’s been stealing credentials via custom protocols.
The group’s ambitions have expanded beyond its own attacks. TeamPCP is also responsible for a self-replicating piece of malware known as Mini Shai-Hulud, which infected hundreds of software packages across open-source registries in back-to-back attack sprees last month. A TeamPCP affiliate published the full source code for the malware on GitHub last month and encouraged other cybercriminals to use it for their own campaigns.
“TeamPCP is going for volume. They are not being discriminating, they’re not necessarily trying to be stealthy or trying to maximize ROI. They’re going for an all-of-the-above strategy,” Read said during the Sleuthcon presentation.
Defensive gaps create openings for attack
TeamPCP’s attack spree has also underscored how difficult it is for organizations to revoke compromised secrets. Multiple victims have experienced recurring infections, sometimes falling prey to TeamPCP three times within a month, because they didn’t rotate secrets properly, Cohen said.
At its core, these attacks highlight a direct trade-off organizations accept when they update software quickly to fix vulnerabilities, but learn that doing so too quickly could expose them to illegitimate registries containing malware.
TeamPCP has targeted what Aboukhadijeh describes as a “public good,” open-source registries that were never perfect but widely trusted and rarely turned into a point of entry for supply-chain attacks.
Rapid open source software installation is one of the most dangerous things an organization can do right now, he said, adding that there’s a roughly 1 in 10 chance that any package installed by an organization could trigger an active attack.
TeamPCP has compromised security scanners, password managers, automation tools, data visualization software, and CI/CD infrastructure across various environments.
And it’s lifted a trove of credentials and other sensitive data from victims.
Researchers like Cohen at Wiz, who have been tracking this attack spree since the beginning, are nearing a breaking point.
“This is also too hard on us. We’re very tired. I’m sure a lot of people working on this problem space are very tired, and it’s just kind of become untenable,” Cohen said.
“You can’t keep existing in a world where you wake up every morning and some super prevalent package is compromised and everybody’s just going to be using it like nothing,” he added. “We need to start taking this a bit more seriously.”

---
*爬取时间: 2026-07-24 15:54:49*
*来源: 直接站点爬取*
