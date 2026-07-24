# What Is a Prompt Injection Attack? | IBM

### 来源信息
- **URL**: https://www.ibm.com/think/topics/prompt-injection
- **域名**: www.ibm.com
- **检索关键词**: 提示词注入 防护 方案
- **页面抓取**: 成功

### 搜索摘要
February 27, 2026 - In prompt injection attacks, hackers manipulate generative AI systems by feeding them malicious inputs disguised as legitimate user prompts.

### 页面正文
While the two terms are often used synonymously, prompt injections and jailbreaking are different techniques. Prompt injections disguise malicious instructions as benign inputs, while jailbreaking makes an LLM ignore its safeguards.
System prompts don't just tell LLMs what to do. They also include safeguards that tell the LLM what not to do. For example, a simple translation app's system prompt might read:
You are a translation chatbot. You do not translate any statements containing profanity. Translate the following text from English to French:
These safeguards aim to stop people from using LLMs for unintended actions—in this case, from making the bot say something offensive.
"Jailbreaking" an LLM means writing a prompt that convinces it to disregard its safeguards. Hackers can often do this by asking the LLM to adopt a persona or play a "game." The "Do Anything Now," or "DAN," prompt is a common jailbreaking technique in which users ask an LLM to assume the role of "DAN," an AI model with no rules.
Safeguards can make it harder to jailbreak an LLM. Still, hackers and hobbyists alike are always working on prompt engineering efforts to beat the latest rulesets. When they find prompts that work, they often share them online. The result is something of an arm's race: LLM developers update their safeguards to account for new jailbreaking prompts, while the jailbreakers update their prompts to get around the new safeguards.
Prompt injections can be used to jailbreak an LLM, and jailbreaking tactics can clear the way for a successful prompt injection, but they are ultimately two distinct techniques.

---
*检索时间: 2026-07-24 20:48:48*
*搜索来源: DuckDuckGo*
