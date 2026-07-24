# New attack provides one more reason why AI browsers are a bad idea

### 来源信息
- **URL**: https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
Makers of AI browsers make lofty promises. With a single prompt, users can ask one to find a restaurant in a particular part of town, reserve a table, invite a colleague to lunch, and email a confirmation. These makers are much more reticent about the risks of blurring the once fine line between browsing sites and asking a large language model a question or instructing it to take potentially sensitive actions.
LLM developers’ answer so far has been to build guardrails that make some requests off-limits. Developing software exploits, stealing credentials, or teaching how to build a pipe bomb are examples. The problem with this approach is that the guardrails are reactive and treat the symptoms rather than solve the root cause. It’s tantamount to the manufacturer of an unsafe vehicle advocating for new road designs rather than fixing the flaws that make it prone to accidents.
Lulling LLMs into an alternate reality
New research puts this predicament on sharp display. It demonstrates how a website can lull AI browsers into a false reality where the rules governing its behavior no longer apply. After that, an attacker has free rein to invoke all kinds of destructive actions, such as extracting code from a private repository or extracting credentials from the built-in password manager.
The malicious site in the proof-of-concept exploit presents the browser with an instruction to win a game by solving a puzzle. The puzzle, however, rewards incorrect answers, such as 2 + 2 = 5. Once the LLM embedded in the browser discovers that the answer is no longer 4, it enters a state of delusion in which the normal laws of reality no longer exist. In this dream world, the guardrail restrictions are no longer enforced.
“The AI operates under the assumption that its context is real, and its behavior must therefore fall within the bounds of its safety guardrails,” Roy Paz, a researcher at security company LayerX, wrote Monday. “But if we can trick the AI into changing its context into fantasy—where the rules are made up and anything goes—then it can behave as though its actions don’t have real world consequences.”

---
*爬取时间: 2026-07-24 21:50:58*
*来源: 直接站点爬取*
