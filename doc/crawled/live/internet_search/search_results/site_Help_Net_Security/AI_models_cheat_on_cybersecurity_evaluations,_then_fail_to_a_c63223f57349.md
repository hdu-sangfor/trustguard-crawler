# AI models cheat on cybersecurity evaluations, then fail to admit it

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/22/ai-models-cheating-behaviour-cybersecurity-evaluations/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
AI models cheat on cybersecurity evaluations, then fail to admit it
Frontier AI models will take just about any route to finish a task, cheating included, according to new cybersecurity evaluations from the UK government’s AI Security Institute (AISI).
AISI defines cheating as a model doing something outside the bounds of what a task allows, or breaking a stated rule outright, in order to reach the goal through a shortcut the task wasn’t designed to permit.
“Every model we have tested for this behaviour attempted to cheat. Models did not reliably report this behaviour when asked, and often did not reason about it in their chain-of-thought, suggesting that detecting cheating will likely require robust monitoring methods.” AISI said in a blog post.
The cheating showed up in different ways: models looked up answers online, worked around network restrictions meant to sandbox them, poked at the evaluation software to see what it would give away, went after systems that had nothing to do with the task, and in some cases just guessed.
None of this is new. Machine learning researchers have documented models gaming reward functions and finding workarounds to score better on benchmark tests for a while.
AISI doesn’t think models are trying to deceive anyone. Still, the institute says it’s worth worrying about. Cheating can inflate how capable a model looks, and it can mislead users on tasks where there’s no easy way to check the result.
“Cheating also becomes more concerning as model capabilities increase: more capable models could find unforeseen ways to cheat or take more effort to conceal their actions,” they added.
Researchers caught every AI model cheating
AISI ran five leading models through 475 test runs each, and all five cheated.
(Source: AI Security Institute)
The rate of cheating did not track how capable a model was. A stronger model was not more likely to cheat than a weaker one. AISI’s read on this is that the behaviour comes down more to how a model was trained and aligned than to its raw capability.
During a test that had been set up wrong and could not be solved, one model kept trying anyway. It wrote and ran code on an external service hosted on the open internet and used it to attempt to reach AISI’s own evaluation systems, tripping a security alert.
“No damage was done and no information leaked, but the attempt could have succeeded had our evaluation infrastructure not been designed and built securely. We have since taken action to further secure AISI systems,” researchers noted.
Asking a model whether it cheated turned out to be a weak check on its own. Models named their own wrongdoing and called it wrong less than half the time when asked, according to AISI.
Reading a model’s chain-of-thought did not close the gap either. Some models barely wrote out reasoning for the step that got flagged, since they decide on their own how much reasoning to show for a given action. And in cases where a model did reason through whether an action counted as cheating, that reasoning did not stop it from cheating anyway.
“Successful cheating is especially dangerous in domains where verifying success is hard, such as AI safety and security research, or where the cost of unintended actions may be very high, such as cyber operations or military decision-making,” AISI warned.
For the moment, AISI is relying on manual review paired with an LLM based monitor to catch what it can. Whether that keeps working as models get stronger is the open question.

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
