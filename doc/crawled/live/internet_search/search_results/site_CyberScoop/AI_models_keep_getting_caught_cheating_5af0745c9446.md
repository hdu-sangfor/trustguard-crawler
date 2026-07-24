# AI models keep getting caught cheating

### 来源信息
- **URL**: https://cyberscoop.com/ai-models-cheat-deceive-users-aisi-report/
- **来源站点**: CyberScoop
- **页面抓取**: 成功

### 页面正文
Frontier AI companies often refer to their models as “helpful assistants” or try to compare them to entry-level employees.
But new research from the UK’s AI Security Institute reinforces how large language models suffer from a common flaw that would land many human employees in hot water with their employers: they cheat.
In other words, these models are so committed to completing their tasks that they will break the rules, cut corners and deceive their own users to accomplish them.
“Every model we have tested for this behavior attempted to cheat,” the AISI report said.
“Models did not reliably report this behavior when asked, and often did not reason about it in their chain-of-thought, suggesting that detecting cheating will likely require robust monitoring methods.”
The research tested OpenAI’s ChatGPT 5.4, 5.5 and 5.6 models, along with Anthropic’s Claude Opus 4.7 and Mythos Preview.
The AISI ran models through a series of “Capture-the-Flag” cyber evaluations, where they obtained points by performing offensive cybersecurity related tasks, like exploiting a particular vulnerability or reverse engineering compiled code.
The research defines “cheating” as “taking an action that is out of scope for the task or explicitly disallowed by the rules, in order to achieve a goal through a shortcut, workaround, or unintended solution that the task was not meant to, or should not, permit.”
It captures a range of observed behaviors from models, like searching the internet for solutions, attacking or escalating privileges on unrelated systems, probing evaluation software to gain access to the task solution.
Models also failed to acknowledge when they were cheating to complete a task, and less than 50 percent said the rule-breaking was “wrong” when challenged on it by a user.
A model’s propensity for cheating was not related to its capability, meaning newer or advanced models aren’t more likely to cheat. Rather, researchers think it stems from the techniques used during a model’s training and alignment that are to blame.
But even if rates of cheating remain constant, the problem could still worsen over time. As newer models in the future could become more proficient and learn more effective cheating techniques.
This deception also makes it difficult for labs like AISI to verify their own work, which relies on evaluating trustworthy outputs from AI systems.
The research underscores how AI systems can go to drastic lengths to complete their task, including blowing through or circumventing a company’s IT and cybersecurity protections.
In one instance, AISI researchers said a model was inadvertently given a cyber capability evaluation that was misconfigured and impossible to solve.
“The model tested was so persistent in attempting to cheat that it wrote and ran code on an external service, hosted on the open internet outside of AISI’s systems, in an attempt to access our evaluation infrastructure, triggering a security alert in AISI’s systems,” the report said.
While AISI said there were no data leaks or damage from the incident, the model could have successfully accessed their evaluation system had they not had monitoring in place. The institute said it implemented further controls on internal systems in response to the test.
The researchers said there are “significant consequences” to a status quo where we can’t trust models not to cheat. The behaviors are especially problematic in areas like AI safety and security research, as well as cyber operations and military decision-making, where trust outputs from the AI systems are critical.
Today, AISI said it can detect LLM cheating through a mix of manual review and LLM monitoring, but that may not always be true, and future models may be better at hiding their actions from human overseers.
“A more fundamental fix would be to train the models not to cheat in the first place – but given this kind of behavior was reported in frontier models more than a year ago, robustly aligning it away may not be easy,” researchers wrote.

---
*爬取时间: 2026-07-24 15:54:49*
*来源: 直接站点爬取*
