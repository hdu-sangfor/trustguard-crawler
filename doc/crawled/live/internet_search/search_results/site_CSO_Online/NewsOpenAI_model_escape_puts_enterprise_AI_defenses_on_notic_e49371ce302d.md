# NewsOpenAI model escape puts enterprise AI defenses on noticeBy Prasanth Aby ThomasJul 22, 20265 minsArtificial Intellig

### 来源信息
- **URL**: https://www.csoonline.com/article/4200043/openai-model-escape-puts-enterprise-ai-defenses-on-notice.html
- **来源站点**: CSO Online
- **页面抓取**: 成功

### 页面正文
Some of OpenAI’s most powerful AI models teamed up to escape their sandbox and attack systems at Hugging Face in a cybersecurity evaluation gone wrong, the company has admitted. The models under test were modified to allow them to perform potentially harmful actions that production versions would refuse. The incident highlights how, if AI prompt guardrails fail or, as in this incident, are removed, then enterprises must have robust sandboxing or other technical restrictions in place to protect systems.
In OpenAI’s evaluation, GPT-5.6 Sol and a more capable pre-release model were competing to solve cybersecurity challenges in ExploitGym, a benchmarking tool for cybersecurity capabilities. They concluded that systems at Hugging Face could have the answers, and set out to gain access, OpenAI wrote in a blog post about the attack on Hugging Face.
ExploitGym challenges AI models to turn security vulnerabilities into attack exploits. OpenAI gave its models limited access to the internet through a package-registry proxy to download code to build their attacks. However, the models exploited a zero-day vulnerability in the proxy to obtain unrestricted internet access, then used stolen credentials and other flaws to access Hugging Face systems.
For CIOs and CISOs, the concern extends beyond cybersecurity research. AI agents connected to corporate databases, source code repositories, or payment systems could expose sensitive resources unless access controls and sandboxing continue to work when model-level safeguards fail.
“Prompt guardrails are not security controls,” said Biswajeet Mahapatra, principal analyst at Forrester. “They are behavioral controls that can fail, be bypassed, or be intentionally disabled during testing.”
How containment failed
Despite the relaxed model safeguards, the surrounding infrastructure was supposed to contain the activity. Network access was restricted to an internally hosted third-party service that acted as a proxy and cache for software package registries. Such proxies are typically used in the enterprise to protect against software supply chain attacks coming from the outside.
OpenAI said the models discovered a zero-day vulnerability in the service, exploited it and carried out privilege escalation and lateral movement until they reached a node with open internet access.
Once online, the models inferred that Hugging Face might hold models, datasets or solutions related to ExploitGym. OpenAI said that, in one attack path, the models combined stolen credentials with zero-day vulnerabilities to obtain remote code execution on Hugging Face servers.
In its account of the activity on its infrastructure, Hugging Face said a malicious dataset abused two code-execution paths in its data-processing pipeline. The actor then obtained node-level access, harvested cloud and cluster credentials, and moved into several internal clusters.
OpenAI said the models ultimately obtained ExploitGym test solutions directly from a Hugging Face production database. The models remained focused on solving the benchmark, despite the lengths to which they went to achieve that objective, it said.
Sanchit Vir Gogia, chief analyst at Greyhound Research, said the package-registry proxy should concern enterprise security teams because it was a narrowly permitted exception inside an otherwise restricted environment.
“Every enterprise estate is built from exceptions of exactly that kind,” he said.
In this incident, OpenAI’s models were performing the intended — albeit by unintended means — but enterprises should take care that their own AI systems are kept on target.
Mahapatra said enterprises should treat AI agents as “high-risk non-human identities,” confining each one to an isolated environment where access is limited to the assigned task and credentials expire quickly.
“An acceptable blast radius means a compromised agent can affect only a single workflow, dataset, or application rather than providing a pathway into broader enterprise infrastructure,” Mahapatra said.
And Gogia warned that services allowed to reach package registries, update systems, or other external resources can become escape routes if they are not subjected to the same scrutiny as the agent itself.
Defenses enterprises need
Hugging Face said the intrusion resulted in unauthorized access to a limited number of internal datasets and several credentials used by its services. It found no evidence that public models, datasets or Spaces had been altered and said its published software packages and container images were not compromised.
The company closed the code-execution paths used to gain access and rebuilt the affected nodes. It also revoked exposed credentials and tightened the rules governing workloads admitted to its clusters.
Whether they are keeping their own AIs in or rogue Ais out, Gogia said enterprises should test whether their containment boundaries work, rather than relying on architecture diagrams or stated policies. Such tests should attempt to obtain credentials, cross trust boundaries and reach systems outside the agent’s assigned task.
Mahapatra said enterprises should assume that one containment layer may fail and ensure that an agent’s access cannot provide a route into unrelated applications or broader corporate infrastructure.
OpenAI said it is still investigating the incident with Hugging Face, and is imposing stricter configurations on its research environment while the vulnerabilities are being addressed, even if that means slowing down its research. It is also strengthening containment and monitoring around future evaluations.

---
*爬取时间: 2026-07-24 21:46:15*
*来源: 直接站点爬取*
