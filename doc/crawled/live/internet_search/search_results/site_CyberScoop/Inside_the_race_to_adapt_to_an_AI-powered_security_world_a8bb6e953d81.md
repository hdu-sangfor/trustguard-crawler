# Inside the race to adapt to an AI-powered security world

### 来源信息
- **URL**: https://cyberscoop.com/ai-powered-cybersecurity-mythos-xbow-agentic-pen-testing/
- **来源站点**: CyberScoop
- **页面抓取**: 成功

### 页面正文
Troy West was in Warsaw when his dinner was interrupted by his phone. But he was happy about it.
West, associate director of cybersecurity at Moderna, the pharmaceutical company primarily known for its work related to mRNA vaccines, had just learned that a trial version of XBOW’s AI-powered red teaming platform had found a vulnerability that led to a full takedown of a his company’s development environment.
It was, by most measures, exactly the kind of outcome a security team dreads. But for West and Farzan Karimi, Moderna’s deputy CISO, it was something closer to a proof of concept. XBOW’s product had done in hours what a human penetration tester could not — and it had done so with a level of persistence and creativity that neither of them had fully anticipated.
The episode is one data point in a much larger shift now rippling through the cybersecurity industry: The artificial intelligence models discovering vulnerabilities are moving faster than the teams that have to patch them.
Across recent conversations and presentations, industry experts said the tools are getting sharper, the attack surface is getting larger, and the gap between finding a problem and fixing it is not closing fast enough. For now, most organizations are caught between the speed of discovery and the slowness of remediation, with vendors across the industry rushing to position their products as the way through.
A shift in scale
The inflection point came with Claude Mythos. When Anthropic announced the highly guarded model, security executives at major enterprise technology companies took notice in a way they had not with prior frontier releases.
Zscaler was among the early organizations given access to the model, and CEO Jay Chaudhry told CyberScoop that he directed his team to use it to probe the company’s own applications.
“Are we finding some serious stuff? Yes, indeed,” Chaudhry told CyberScoop at Gartner’s Security & Risk Management Summit. He was careful to note that the findings were not necessarily more severe than those produced by other models. The issue, he said, was volume.
“There aren’t enough resources and cycles to fix all those,” he said.
The reason Mythos changed the calculus, according to Tom Gillis, general manager for infrastructure and security products at Cisco, comes down to code complexity. Legacy network infrastructure was built on tens of millions of lines of code developed over decades, and earlier AI models lacked the context window and reasoning capacity to comprehend it in full.
“The models couldn’t understand the entirety of it before,” he told CyberScoop. “Now they can. That’s why they’re finding all these vulnerabilities.”
The problem runs deeper than application code. Firewalls and network switches often run for decades without updates or reboots, and many have never been patched in any meaningful way. The combination of aging infrastructure and newly capable AI models has created what Gillis described as a meaningful and accelerating shift in attacker capability that the industry’s existing operational rhythms were not built to absorb.
An opportunity in existing technology
Cisco’s answer to the oncoming vulnerability deluge is a technology it calls Live Protect, a compensated control built on eBPF, a Linux feature that lets security software operate at the kernel level to block threats without rewriting system code.
“It’s a pinpoint, laser-fine control that can shield a vulnerability on a production system,” Gillis said. “We’re not touching or modifying the binaries of that production system.”
The intent is to shrink the window between discovering a vulnerability and the next scheduled patch, allowing IT teams to fix issues without taking systems offline.
“This is a finger in the dike that plugs a hole until you get to new change control windows,” he said, acknowledging that some customers may be tempted to treat the shields as a permanent solution.
The product has been shipping since October, but customer urgency shifted noticeably after Mythos. “Customers are like, ‘Oh, good story, Tom. I’ll think about it.’ Now it’s like, ‘Oh my God, turn this thing on right now.’”
He also noted that eBPF is open source, and said he expects the broader industry to follow.
“While I’m very proud of Cisco leading the market with these compensated controls, I know my competitors have to do this.”
The bot that broke everything
But shielding vulnerabilities only works if you know they exist. Karimi, the Moderna deputy CISO, faced a different problem: His vulnerability management system was surfacing hundreds of high-severity findings with no reliable way to know which ones an attacker could actually exploit. His team had skilled red-teamers, but they were finite resources. What he needed was something that could test continuously, everywhere.
“We have some very senior red-teamers and pen-testers in our organization that are pointed in a specific direction,” Karimi said during a presentation at the Gartner summit. “XBOW is covering different attack stories for us.”
West describes the platform as a response to a structural problem in how offensive security has traditionally worked. Human testers scope an engagement, run it, write a report, and move on. The window between tests is where risk accumulates.
“Historically you have exploit developers spending time finding the right vulnerabilities, writing the exploits, finding if those exploits are reachable, and then finding a way to chain them all together,” West said. “That takes a long time.”
Given the realities, West and Karimi decided to put XBOW through a trial, which produced two notable findings.
In the first, XBOW identified a web application firewall bypass on a company application built on the Spring Boot framework. The bypass involved encoding a single character (a capital “A”) as its percent-encoded URL equivalent (A), which the WAF interpreted as a legitimate request, allowing the bot unfettered access. 
The second finding, which was the cause for West’s dinner interruption, was more consequential. West had provided XBOW with access to the source code of an internal application called Orders, used by Moderna’s research partners to procure drug substances, but no login credentials. The platform identified a valid API key embedded in the source code, used it to authenticate, and then began probing the application’s APIs for SQL injection vulnerabilities.
What happened next was not entirely planned. One of those APIs handled a malformed SQL injection attempt in an unexpected way, dumping garbage data into a shared routing application that other services depended on.
“Not only was it able to kick that Orders app I showed you, but it somehow kicked over the entire ecosystem of apps,” West said.
Human pen-testers who reviewed the findings afterward confirmed they were valid, and said they would not have found them on their own. Karimi said despite the outage, his team recognized the value immediately.
“If we’re able to demonstrate where you could have an outage in a safe testing environment, that’s a great signal,” he said.
The broader value, Karimi argued, is in forcing prioritization when bugs are discovered. “If you have exploit proofs, you can provide that plus-one modifier and really point your developers to remediate the top tier of real risk that’s been validated.”
But he does worry about the volume of bugs that will be surfaced by these tools.
“How do we now handle the volume of bugs that have gone up due to AI-driven scale?” he said. “That’s a whole other problem space.”
A broader reckoning
Across these conversations, a consistent theme was that even as defenders are trying to get arms around the forthcoming wave of bugs, it’s going to be a tremendously uphill battle. That mirrors what some of the industry’s top leaders have been saying for months.
It also mirrors what the model developers themselves have consistently been warning about. In its announcement about expanding access to Mythos, Anthropic admitted the timeline for a publicly available tool similar to its cybersecurity-focused model is shortening, and there are no guarantees it will be released with safeguards.
“In that world, cyberattacks could occur much more often, and in much more unpredictable forms,” the blog post reads.
Gillis was blunter about what happens to organizations that don’t move. 
“Some people will be slow to change,” he said. “But the consequence of not making that change is gonna be front-page news. It’s a massive, massive compromise. You know, like, ‘you gave up every credit card number.’ Bummer.”
Update, June 18: This story has been edited to reflect Troy West’s correct job title.

---
*爬取时间: 2026-07-24 21:49:31*
*来源: 直接站点爬取*
