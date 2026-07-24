# ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing LinkJul 24, 2026Vulnerability / Enterprise 

### 来源信息
- **URL**: https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
Cybersecurity researchers have disclosed a critical vulnerability in OpenAI's ChatGPT Workspace Agents that could have allowed a single phishing link to stealthily build, authorize, and deploy an autonomous artificial intelligence (AI) agent inside a victim's organization.
The vulnerability has been codenamed AgentForger by Zenity Labs. The issue has since been addressed by OpenAI as of June 8, 2026, following responsible disclosure.
"A single link could hijack OpenAI's ChatGPT Agent Builder to stand up an attacker-controlled AI agent with a real employee's access and its approvals switched off," the AI security company said in a two-part report shared with The Hacker News.
The attack occurs when an unsuspecting employee clicks open a benign-looking ChatGPT link, causing it to spawn a new AI agent within the company's trust boundary that does the attacker's bidding. The issue is a case of cross-site request forgery (CSRF) that forges an attacker-controlled autonomous AI agent.
Agent Builder is a visual, drag-and-drop canvas that allows users to build multi-step agent workflows. Last month, OpenAI announced that it's deprecating the product effective November 30, 2026, urging users to switch to the Agents SDK.
Zenity said its testing found the Builder tool to accept an initialization state through URL parameters, two of which include an agent template and the prompt to the Builder.
"We found that when the page loads, the value of initial_assistant_prompt is not merely placed into the prompt box. It is automatically submitted and executed," AI Red Team Researcher Mike Takahashi said. "That means an instruction embedded inside a URL can become the first command the Builder acts on."
Given that a prompt can be inserted directly into the URL, an attacker can send the URL to a target in the form of a phishing link that adheres to the following pattern: "chatgpt[.]com/agents/studio/new?template_name=[template name]&initial_assistant_prompt=[malicious prompt]."
Should a logged-in user click on the link, ChatGPT opens the Builder in the victim's authenticated session and automatically submits the prompt embedded in the URL without requiring any further interaction. The attacker, however, needs to meet the below prerequisites -
- A victim who is logged into ChatGPT
- The victim has access to Workspace Agents
- The victim has at least one authorized connector (i.e., an already existing ChatGPT integration to an enterprise app like Outlook, Gmail, Google Calendar, Google Drive, Slack, or Teams)
The connector integration is necessary because the crafted ChatGPT URL passes as input a chief-of-staff template that allows the agent to pull necessary data from the workspace applications to prepare a "high-signal operating brief."
Specifically, the payload passed through the malicious prompt instructs the Builder to perform the following sequence of actions -
- Create an agent from the chief-of-staff template.
- Attach all already-available connectors and set every connector to "Never ask" so that no user approval is needed.
- Make the agent live and schedule it such that it runs every hour, turning it into a persistence mechanism.
- During each run, check for emails from a specific email address whose subject line begins with the phrase "TASK," execute those tasks, and report the results back by sending an email message to the attacker's address.
- Invoke Preview Mode to run the agent immediately.
"Preview Mode is meant to allow users to test an agent before publishing it," Zenity explained. "In this flow, however, Preview is not just a visual preview or dry run. It executes the newly created agent against the victim's connected accounts using the approval settings that have just been configured."
"In other words, the forged agent becomes a persistent operator. The original click installs it; the schedule keeps it alive; and the connected apps give it a source of commands, access to sensitive actions and data, as well as a path to return results."
Armed with this capability, the forged agent can burrow deeper into the organization, conducting reconnaissance, harvesting sensitive documents from cloud storage services, and stealing passwords mentioned in Slack messages, essentially turning it into a persistent, autonomous insider capable of doing what the attacker wants to do.
What's more, the rogue workspace agent can impersonate the victim to send phishing links on Teams on their behalf, which can then redirect recipients to a fake Microsoft login page designed to siphon their credentials. This scenario is troubling as it can open the door to broader compromise and other business email compromise (BEC) scenarios.
"The attacker does not need the victim to click another link," Takahashi explained. "They do not need the Builder tab to stay open. Once the agent is published and scheduled, the attacker can keep sending it assignments through the victim's mailbox. Each TASK email becomes a new assignment for the agent. The agent is not waiting for another click. It is waiting for instructions."
"At its core, AgentForger is an agent trust failure: the platform trusts that the user intentionally created, approved, scheduled, and operated the agent."
The findings come nearly a month after the AI security company revealed how bad actors are exploiting critical LiteLLM vulnerabilities and exposed Ollama endpoints and hijacking AI infrastructure to conduct attacks against third-parties and power their own offensive operations. These efforts involve the abuse of CVE-2024-6587, CVE-2026-40217, and CVE-2026-35029.
"Self-hosted model servers and agent frameworks keep getting deployed while being misconfigured and unauthenticated, on predictable ports, willing to serve any client," Zenity said. "This turns exposed AI infrastructure into convenient, deniable backend compute for offensive AI agents."

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
