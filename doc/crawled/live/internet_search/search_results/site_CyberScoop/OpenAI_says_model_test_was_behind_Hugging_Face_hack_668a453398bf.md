# OpenAI says model test was behind Hugging Face hack

### 来源信息
- **URL**: https://cyberscoop.com/openai-chatgpt-hugging-face-cyberattack-data-poisoning/
- **来源站点**: CyberScoop
- **页面抓取**: 成功

### 页面正文
A cyberattack that poisoned the data pipeline of a major AI code platform was carried out using OpenAI’s ChatGPT, the company said Tuesday.
Last week, Hugging Face, a platform for sharing and working on AI code, disclosed that an external attacker had compromised its data processing pipeline. According to a July 21 blog post, the attacker poisoned a dataset to run code on a processing worker, eventually gaining node-level access and stealing cloud credentials.
The attack is notable, the blog said, because it appears to have been carried out by an autonomous AI system, which executed “many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services.”
At the time, Hugging Face said it wasn’t clear which LLM was used in the attack, but noted that their own attempts to recreate parts of the attack using an in-house commercial model failed due to guardrail restrictions.
The incident and its ultimate impact are still being investigated, and Hugging Face said it reported the incident to law enforcement and is engaging with third-party cybersecurity forensic specialists to learn more.
“This experience points to a gap worth planning for,” the company wrote. “We do not know which model powered the attacker’s agents, whether a jailbroken hosted model or an unrestricted open-weight one; either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried.”
Now OpenAI is confirming one of their models was used in the attack.
“After investigating, we now know that this particular incident was driven by a combination of OpenAI models — including GPT‑5.6 Sol and an even more capable pre-release model, all with reduced cyber refusals for evaluation purposes — while being internally tested on a benchmark of cyber capabilities,” the company wrote in a blog post Tuesday.
OpenAI called the incident “unprecedented” but also predicted that such attacks would  become increasingly more common as AI adoption continues to grow.
According to the company , the incident happened during an internal evaluation,  where the company deliberately prompts models to “pursue advanced exploitation using complex attack paths” in order for the company to study and measure the model’s cybersecurity capabilities.
To assess the model’s full potential, the team disabled the production classifiers that normally prevent OpenAI models from carrying out high-risk cyber activity. Without these safeguards, the models were able to install software packages through registries like Hugging Face.
The model collected and chained vulnerabilities from OpenAI’s systems as well as Hugging Face’s production infrastructure.
OpenAI further explained that the activity stemmed from models attempting to solve a specific challenge posed by ExploitGym, a benchmarking system for AI agents.While such tests normally run in isolated environments, in this instance,  the model spent a “substantial” amount of compute resources figuring  out how to access the open internet. It did so by using a zero-day vulnerability in a third-party vendor’s system used by OpenAI (the company said it disclosed the flaw to the vendor).
“After gaining Internet access, the models inferred that Hugging Face potentially hosted models, datasets and solutions for ExploitGym,” OpenAI wrote. “Knowing this, the model searched for and successfully found ways to gain access to secret information that it could use to cheat the evaluation.”
In one instance, the model chained together multiple stolen credentials and zero-day vulnerabilities to find a remote code execution path on Hugging Face servers.
OpenAI said it was implementing new controls for infrastructure configuration, something that would come at “the cost of research velocity while the vulnerabilities are patched.”
Hugging Face was also added to OpenAI’s Trusted Access for Cyber program, which will give them access to more advanced models like Daybreak to scour their systems for other AI-discovered vulnerabilities.

---
*爬取时间: 2026-07-24 15:54:49*
*来源: 直接站点爬取*
