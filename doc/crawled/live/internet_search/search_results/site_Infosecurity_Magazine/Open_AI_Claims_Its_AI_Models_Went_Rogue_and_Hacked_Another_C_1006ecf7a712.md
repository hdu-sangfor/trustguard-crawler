# Open AI Claims Its AI Models Went Rogue and Hacked Another Company

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/open-ai-hacked-another-company/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
Two of OpenAI’s frontier artificial intelligence models acted of their own accord to breach the systems of Hugging Face, the AI software development company.
In a blog post disclosing the incident, published on July 21, OpenAI claimed that a combination of its models, including GPT‑5.6 Sol and an unspecified pre-release model resulted in what the company described as “unprecedented cyber incident”.
Hugging Face had disclosed the unauthorized intrusion into its production infrastructure on July 16. This included access to what was described as a limited set of internal datasets and several credentials used by Hugging Face’s services.
At the time, Hugging Face noted that it suspected the intrusion was the work of an autonomous AI agent system.
“We suspected last week's cyberattack might have come from a frontier lab, given the sophistication of the agent. Turns out it did!,” Clement Delangue, co-founder and CEO of Hugging Face posted on social media.
According to Open AI, the incident occurred during an internal evaluation of how AI models can conduct offensive cyber operations. The test was run in a constrained environment with limited network access and restricted abilities.
The intent of the test was not for the model to act maliciously or cause harm. Despite this, the models identified then linked together vulnerabilities across OpenAI’s research environment and Hugging Face’s production infrastructure to obtain test solutions directly from Hugging Face’s production database.
This included uncovering and exploiting a zero-day vulnerability to obtain open internet access and using a series of privilege escalation and lateral movement actions to get there.
Open AI has not publicly disclosed the newly uncovered zero-day vulnerability but noted that it has responsibility disclosed it to the vendor.
AI Model ‘Cheated’ to Bypass Guardrails
After gaining internet access, the model inferred that Hugging Face potentially held datasets related to its goal.
“Knowing this, the model searched for and successfully found ways to gain access to secret information that it could use to cheat the evaluation,” said OpenAI.
These ‘cheats’ included using stolen credentials and zero-day vulnerabilities to find a remote code execution path on the Hugging Face servers – which was the intrusion which Hugging Face disclosed on July 16.
OpenAI and Hugging Face have worked together to investigate the incident. OpenAI has said it will be introducing stronger protections around future training and evaluations.
The AI firm also invited Hugging Face into its Trusted Access for Cyber program.
The disclosure of the incident has prompted strong reactions from information security leaders.
Sean Cassidy, CISO at Plaid and until recently, head of security at Asana, took to LinkedIn to highlight how the ramifications for security programs is “immense.”
“Before today, the capabilities of frontier models were a theoretical problem for security programs that maybe we can fit on the roadmap in the future. After today, the problems have been realized and we need to account for them now,” Cassidy said.
“Good luck to all the defenders out there. Our job just got significantly harder,” he added.
Others have pointed out that even though GPT-5.6 Sol was not instructed to act in a malicious way, the model nonetheless did so because it deemed this the optimal strategy.
"What makes the OpenAI and Hugging Face incident important is that the models did not need malicious intent to cause harm,” said Nathaniel Jones VP of security and AI strategy at Darktrace.
“They were given the legitimate goal of solving a cybersecurity benchmark and found an unexpected route to the answers, escaping their test environment and compromising another organization in the process. From the models’ perspective, this appears to have been an effective solution to the task,” he added.
Ansgar Dodt, VP of product management at Thales, warned that organizations should prepare themselves for malicious threat actors attempting to use similar AI-powered techniques.
“It’s only a matter of time before these hacking capabilities are in the hands of malicious actors. Organizations need to act now to harden their applications against AI-driven analysis, or risk being exposed at machine speed,” he said.
“The conversation needs to move quickly from awareness to implementation. Failing to protect software applications from vulnerabilities can lead to reputational damage, potential penalties, product recalls, and loss of market access.”
Image credit: Samuel Boivin / Shutterstock.com

---
*爬取时间: 2026-07-24 12:31:41*
*来源: 直接站点爬取*
