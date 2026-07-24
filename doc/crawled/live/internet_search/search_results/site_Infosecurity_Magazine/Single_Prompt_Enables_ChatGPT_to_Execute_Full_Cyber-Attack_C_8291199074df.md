# Single Prompt Enables ChatGPT to Execute Full Cyber-Attack Chain, Researchers Claim

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/chatgpt55-to-execute-full/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
A single prompt is enough to encourage OpenAI’s ChatGPT-5.5 large language model (LLM) to conduct full-scale offensive cyber-attacks, complete with the ability to gain domain-level access to a network in under 40 minutes, according to tests conducted by cybersecurity researchers.
Threat researchers at Cato Networks, a member of OpenAI's Daybreak Program for authorized cybersecurity testing, said they set out to test how far an agentic attack could go when a frontier model was given a single high-level objective, the offensive, and enough autonomy to execute the attack path.
A paper published on July 15 by the cybersecurity firm detailed how this experiment was performed in a controlled Active Directory environment, designed to look like that of a typical enterprise.
The result was that following a single prompt, the agent was able to plan and execute the entire attack lifecycle. This included reconnaissance, exploitation, internal discovery, privilege escalation, lateral movement and exfiltration activities.
Cato Networks conducted the research to examine how AI tools could be exploited at a time when threat actors are increasingly incorporating AI into offensive cyber operations.
This includes attempts to jailbreak publicly available AI models that are protected by built-in safety guardrails.
Cato Networks focused on GPT-5.5 rather than the cybersecurity focused GPT-5.5-Cyber.
“While both GPT-5.5 and GPT-5.5-Cyber were evaluated during the research, the later scenarios focused on GPT-5.5 to better reflect the publicly available frontier models accessible to most attackers at the time of the study,” Cato Networks explained in a blog post.
The specific prompts used to direct the model have not been revealed, likely as a cybersecurity measure to prevent malicious actors from repeating the experiment.
The Agentic Attacker in Action
Cato Networks tested six different scenarios and found that the agentic AI was highly adept at devising new strategies when environmental conditions were changed.
Examples of this activity included generating custom vulnerability probes, modifying collection workflows, and designing alternative communication paths to meet the end goal set out by the prompt.
In one of the tests, the agent developed an Server Message Block (SMB)-based tunneling approach to support data movement through an existing foothold.
By combining the lessons learned in the previous six experiments the model was able to perform the offensive cyber maneuvers at speed, successfully reaching the objective of admin level privileges in approximately 40 minutes. Researchers cited the effectiveness of this to the model’s ability to adapt.
“Several executions demonstrated adaptive behavior when expected attack paths failed or environmental conditions changed. Rather than following a rigid sequence of actions, the agent adjusted its approach based on observations gathered during execution,” researchers said.
“While these observations should not be interpreted as evidence of novel attack discovery, they do suggest that frontier models can contribute goal-oriented problem solving during offensive operations,” they added.
Cato Networks also noted that while the patterns remained consistent across multiple examples, they should not be interpreted as universally representative of all enterprise environments.
Nonetheless, the research contains useful lessons for cybersecurity leaders at a time when AI tools are not only becoming further embedded in the workplace, but malicious threat actors are looking for ways to exploit them, particularly to increase the speed of cyber-attacks. And this capability is likely to evolve.
"A threat actor is only one part of the risk. The real capability emerges when that model is harnessed with orchestration, operational context, and battle-tested tools that can translate reasoning into action. Our research shows that this combination can dramatically accelerate known attack workflows, reduce the amount of hands-on expertise required, and enable more coordinated execution across multiple stages of the attack lifecycle," Dr. Guy Waizel, tech evangelist at Cato Networks told Infosecurity.
Infosecurity has contacted OpenAI for comment.

---
*爬取时间: 2026-07-24 21:45:28*
*来源: 直接站点爬取*
