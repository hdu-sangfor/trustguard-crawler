# Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can DoJul 24, 2026Enterprise Security / AI Securi

### 来源信息
- **URL**: https://thehackernews.com/2026/07/seeing-ai-agents-is-not-enough-security.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
AI agent security is moving through a familiar maturity curve: adoption, then visibility, and finally, control. But what we've collectively discovered is that enforcing least privilege for AI agents is harder than we ever imagined. This is why there are so many approaches, from prompt filtering to identity-layer access controls. Where we've collectively landed is that understanding the intent of AI agents is essential to securing them. It's not easy, but it's the only path forward.
Organizations approach this challenge with different levels of sophistication. For many, the current goal is simply to find the AI agents already operating across the business. That is a necessary first step. AI agents are appearing in SaaS platforms, developer environments, cloud workflows, customer support systems, productivity tools, and internal applications. Some are sanctioned, and others are not.
But discovery alone isn't useful. AI agents are not passive; they reason, plan, call tools, invoke APIs, access data, and take action without a human in the loop. The risk is not that an organization has too many agents. The risk is that those agents can operate across systems without consistent identity, intent, ownership, and enforcement. There are also different types of AI agents, each requiring a different approach to securing them.
Recent guidance on the careful adoption of agentic AI services makes the point clear: agentic AI introduces privilege, authentication, accountability, design, and behavioral risks that security teams need to address before these systems become embedded in critical workflows. Visibility is the starting line, but enforcement is what matters.
The Visibility Trap
Most security programs begin with the question: "What do we have?" That made sense for cloud, SaaS, endpoints, identities, and vulnerabilities. It also makes sense for AI agents.
But the risk of stopping at visibility alone for AI agents is greater than in every other environment in the list because of the speed with which AI agents are being created, what they have access to, and how they can be shared.
An AI agent inventory that does not connect to enforcement becomes another static asset list. It may show that an agent exists, but it cannot tell you whether the agent's access is appropriate, its behavior matches its purpose, its owner remains accountable, or when its permissions should be revoked as conditions change. For AI agents, visibility without enforcement creates a dangerous kind of confidence, where it's easy to feel in control when the reality is far different.
Why AI Agents Break Static Access Models
Traditional access control assumes some level of predictability. Human Identity and Access Management has it the easiest, as each person has a job function. Non-human or machine identity management is more complex, but a service account still supports a defined workload. These assumptions are imperfect, but they gave security teams a foundation for roles, entitlements, approvals, access reviews, and periodic cleanup.
AI agents are far from static. An agent is defined less by a fixed workflow and more by a goal. It may interpret instructions, call different tools, and adapt its actions based on context. Two agents with similar permissions may have a very different risk profile, depending on what each is trying to accomplish.
Static access is not enough because AI agents are more likely to be used in ways not anticipated when access was granted. The issue is not always malicious behavior but ambiguity that poses a risk, such as a task that expands beyond its original purpose.
The question security teams need to ask is not only "what can this agent access?" The more important question is: What should this agent be allowed to do, under these conditions, for this purpose? That is an enforcement question.
Enforcement Starts With Better Understanding
Effective AI agent enforcement cannot be bolted onto a basic, non-contextual inventory. Security teams need to correlate information across owners, consumers, identities, systems, permissions, and intent before they can define meaningful controls.
That means understanding an agent across several dimensions:
- Ownership: Who owns the agent? (This can be more difficult than you may think.)
- Consumers: Who is using the agent?
- Identity: Which identities, tokens, secrets, OAuth grants, and service accounts does the agent use?
- Intent: What is the agent supposed to accomplish?
- Access: Which systems, applications, data stores, APIs, and infrastructure can it reach?
- Usage: What has the agent actually done, and how often?
- Origin: How was the agent created?
- Lifecycle: Is the agent active, dormant, or no longer tied to its original purpose?
This is where many organizations struggle because agent context is scattered. Identity data lives in one place. Cloud permissions are somewhere else. SaaS integrations have their own models. Infrastructure as code can reveal intended deployment patterns, but that context is rarely correlated with the rest. Ownership may be obvious to the person who created the agent and invisible to everyone else.
Without correlation, enforcement becomes guesswork. With correlation, security teams can begin defining rules that reflect how agents actually operate.
From Remediation to Rules
Many security tools equate enforcement with remediation. Something risky is found, and a playbook opens a ticket, removes access, disables an identity, or notifies an owner. That is useful, but it is not enough for agentic AI. AI agents need enforcement before, during, and after they take action.
Security teams need to move from asking, "What should be removed after risk is detected?" to "What should this agent be allowed to do in the first place?" That shift moves enforcement from cleanup to control. Organizations can then define rules such as:
- A customer support agent can read ticket history, but cannot export customer data in bulk
- A code assistant can suggest changes, but cannot push to production without an approved workflow
- A cloud operations agent can inspect configuration drift, but cannot modify privileged roles
- A finance agent can generate reports, but cannot initiate payments or change vendor details
- A security agent can triage alerts, but cannot delete logs or suppress detections
These rules cannot be managed effectively inside one AI platform at a time. Enterprises will use many agent platforms, SaaS-native agents, internal frameworks, cloud services, and developer tools. Each may have its own controls, logs, and permission models. Security teams need a consistent way to govern agents across that fragmented environment. That is why the next control plane for AI agents has to be identity-centric, context-aware, and platform-agnostic.
The Role of Intent in Enforcement
Identity answers who the agent is. Permissions answer what access exists. Intent answers why that access should be active.
The intent dimension is essential. AI agent risk cannot be understood only by looking at whether an API call is technically permitted. Security teams need to evaluate whether an action aligns with the agent's approved purpose.
Intent-based enforcement gives organizations a more precise control model. It allows security teams to move from broad, static permissions to conditional access based on purpose and context. That does not mean every action must be manually approved. It means high-risk actions should be constrained by the agent's role, owner, task, environment, and expected outcome.
The OWASP Top 10 for Agentic Applications highlights risks such as identity and privilege abuse, tool misuse, insecure inter-agent communication, cascading failures, and rogue agents. These risks all point to the same conclusion: security controls must understand the agent's reason to act.
A Singular Control Plane for Agentic AI
AI agents do not live in one platform. They exist across the enterprise. While "traditional" machine identities were created by IT, Developers, and DevSecOps teams, AI agents are created by people in every role in the organization. Some agents will operate in cloud environments, while others will run locally. Some will be embedded in business workflows that security teams do not directly manage.
Platform-by-platform controls for AI agents will not scale. Each platform may provision its own agents, but no single platform can see the full enterprise picture of identity, access, ownership, and lifecycle. Organizations need a unified control plane that can understand agents across environments and enforce consistent rules.
That control plane should do three things:
- Discover: Find agents wherever they exist
- Understand: Correlate agents with identities, owners, access, infrastructure context, usage, and intent
- Enforce: Apply rules that govern what agents can do, when they can do it, and how access should change as context changes
See how AI-first security solutions like Token Security discover, understand, and enforce what your AI agents can do across every platform.
This is the difference between managing agent sprawl and governing agentic AI. Sprawl happens when every platform, team, and business unit creates agents independently. Governance occurs when the organization can apply consistent controls across that activity without blocking innovation.
What Security Leaders Should Do Now
Security teams do not need to wait for perfect standards or fully mature tooling before acting. They can start building the operating model now.
The first step is to stop treating AI agent visibility as the finish line. Of course, agent inventories are the foundation for enforcement. Every agent should be mapped to an owner, a purpose, an identity, a set of permissions, and a lifecycle state. Unowned agents should be investigated, overprivileged agents should be right-sized, dormant agents should be retired, and high-risk actions should require stronger controls.
But ultimately, enforcement is what matters. Security leaders should align AI agent governance with identity and access management, cloud security, application security, and DevOps workflows. Agentic AI is not a separate universe. It is software with access, autonomy, and business impact. It belongs inside the enterprise security model, but that model has to evolve.
NIST's AI Agent Standards Initiative points in the same direction, with work focused on standards, protocols, authentication, identity infrastructure, and secure human-agent and multi-agent interactions. The market is moving toward the same conclusion: AI agents need to be governed as actors with authority, not treated as ordinary applications with a chatbot interface.
Visibility Is the Beginning, but Enforcement Is the Goal.
The first wave of AI agent security was about awareness. Organizations needed to understand that agents were entering the enterprise and creating new identity risk. That message landed, and every security and IAM team knows they need visibility. The next wave is enforcement.
Enterprises need to define what agents are allowed to do and apply rules consistently across platforms. They need to move from "Which agents exist?" to "Which agents can take which actions, under which conditions, and who is accountable?"
That is the control plane agentic AI requires. Not another dashboard or static inventory. AI agents are becoming active participants in enterprise operations. They will write code, manage infrastructure, move data, update systems, and execute workflows. The organizations that succeed with agentic AI will not be the ones that simply find every agent. They will be the ones who understand every agent well enough to enforce what it can do.

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
