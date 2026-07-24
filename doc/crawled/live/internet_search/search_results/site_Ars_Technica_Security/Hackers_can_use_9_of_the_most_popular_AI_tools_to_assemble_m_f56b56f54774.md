# Hackers can use 9 of the most popular AI tools to assemble massive botnets

### 来源信息
- **URL**: https://arstechnica.com/security/2026/07/hackers-can-use-9-of-the-most-popular-ai-tools-to-assemble-massive-botnets/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
In the brief history of AI security, the prompt injection has quickly become the top threat. Large language models are inherently unable to distinguish between legitimate instructions provided by users and malicious ones sneaked into emails, source code, and other third-party content the models are processing. This makes it trivial to surreptitiously inject malicious commands that the LLM readily follows.
With no way to enforce this crucial boundary between trusted and untrusted sources, AI engine developers are left to erect elaborate guardrails designed to mitigate the damage rather than solve the root cause.
To date, most prompt injections have fallen into a class known as push, in which each potential victim is targeted. For example, the adversary injects malicious instructions into an individual email or calendar invitation. Because the injection must then be sent (or pushed) to each specific target, the scale of the attack is limited, hampering mass exploits that hit the Internet at large.
Meanwhile, pull-based attacks, in which an LLM actively seeks out the adversarial prompts planted on websites, remain limited. With no way to lure large numbers of LLMs to a malicious site, these sorts of attacks don’t scale either.
Enter HalluSquatting
Now, researchers have devised a pull-based attack that changes all that. A new attack the researchers have named HalluSquatting has the potential to assemble massive botnets, perform large-scale DDoSes, and infect devices at scale, a first for prompt-injection attacks. The attack works against AI coding assistants and agents, including Cursor, Cursor CLI, Gemini CLI, Windsurf, GitHub Copilot, Cline, OpenClaw, ZeroClaw, and NanoClaw, which are all susceptible. In the normal course of performing day-to-day activities, these assistants and agents routinely pull code and other resources from repositories and registries.
Short for adversarial hallucination squatting, HalluSquatting is built on an LLM’s inherent tendency to hallucinate the resource identifiers hosted in repositories and registries. It works against coding agents and assistants, which commonly access high-privilege command lines to run code from third-party resources. By predicting the identifiers LLMs are most likely to hallucinate and then registering and seeding them with instructions to install reverse shells or other malicious wares, the attack can indiscriminately infect massive numbers of devices without having to target each one.

---
*爬取时间: 2026-07-24 21:50:58*
*来源: 直接站点爬取*
