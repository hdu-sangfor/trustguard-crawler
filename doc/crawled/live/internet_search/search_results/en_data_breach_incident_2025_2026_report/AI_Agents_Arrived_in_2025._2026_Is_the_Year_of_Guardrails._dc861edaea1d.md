# AI Agents Arrived in 2025. 2026 Is the Year of Guardrails.

### 来源信息
- **URL**: https://www.linkedin.com/pulse/ai-agents-arrived-2025-2026-year-guardrails-tundji-williams-fulwood-8ymxc
- **域名**: www.linkedin.com
- **检索关键词**: data breach incident 2025 2026 report
- **页面抓取**: 成功

### 搜索摘要
If 2025 was the year AI agents showed up, 2026 is the year organisations learn what it costs to run them safely at scale—in reliability, security, governance, energy, and compliance (Şerban von Davier, 2025; Gartner, 2025).

### 页面正文
If 2025 was the year AI agents showed up, 2026 is the year organisations learn what it costs to run them safely at scale—in reliability, security, governance, energy, and compliance (Şerban von Davier, 2025; Gartner, 2025).
In this LinkedIn article, I’ll turn the “AI agents arrived” narrative into a deployment-grade view: what changed in 2025, what the 2026 failure modes look like, and a practical playbook you can apply inside an enterprise (McKinsey & Company, 2025; Deloitte, 2026).
The 30-second brief (key stats)
AI adoption is broad, but agent scale is still early: 88% of respondents report regular AI use in at least one business function, while 23% report scaling AI agents and 39% report experimenting (McKinsey & Company, 2025).
Agentic AI is about to surge faster than oversight: 74% of companies plan to deploy agentic AI within two years, yet only 21% report a mature governance model for autonomous agents (Deloitte, 2026).
The risk and cost signals are already sharp: global average breach cost is US$4.44M, and among organisations reporting AI-related breaches, 97% lacked proper AI access controls (IBM, 2025).
The energy constraint is real: global data-centre electricity use is projected to double to ~945 TWh by 2030 in the IEA base case, growing ~15% per year from 2024–2030 (IEA, 2025).
And the hype tax is measurable: Gartner predicts over 40% of agentic AI projects will be cancelled by end of 2027 due to costs, unclear value, or inadequate risk controls (Gartner, 2025).
1) What is an AI agent (and what it is not)
An AI agent is typically a foundation-model-driven system that can plan, select tools, execute multi-step workflows, and iterate toward a goal—often across apps, APIs, internal data, and external content (McKinsey & Company, 2025).
What it is not: a basic chatbot, a single-turn copilot, or traditional RPA with hard-coded scripts—though many 2025 products were “agent-flavoured” wrappers around assistants and automation (Gartner, 2025).
Gartner explicitly calls out “agent washing”—rebranding assistants/RPA/chatbots as agents without meaningful autonomous capability—and estimates only about 130 of the thousands of agentic AI vendors are “real” (Gartner, 2025).
2) What changed in 2025: agents moved from demos to deployments
The “arrival” in 2025 wasn’t just capability hype; it was operationalisation: agents started showing up in real workflows, with organisations attempting to move from pilot to production (Şerban von Davier, 2025; Deloitte, 2026).
McKinsey’s 2025 survey captures the shift: agentic AI is no longer niche—62% say their organisations are at least experimenting with agents, even if scaling remains limited (McKinsey & Company, 2025).
PwC’s May 2025 executive survey also points to budget momentum—79% said agents were being adopted at their companies, and 88% planned to increase AI budgets in the following 12 months due to agentic AI (PwC, 2025).
3) Standardisation accelerated: tools and “agent-to-agent” protocols
A key 2025 unlock was the push toward standard ways for models to connect to tools and data, reducing one-off connector chaos and making agent ecosystems more composable (Anthropic, 2024).
Anthropic’s Model Context Protocol (MCP) (announced November 2024) is widely referenced as a step toward a shared “language” between models and tool/data servers—exactly what multi-tool agents need to behave consistently (Anthropic, 2024).
In parallel, Google introduced Agent2Agent (A2A) in April 2025 as a protocol for agents to communicate and coordinate, and later announced donating A2A to the Linux Foundation to support open adoption (Google, 2025; Linux Foundation, 2025).
4) Why 2026 is “the hard year”: adoption is outpacing guardrails
Deloitte’s January 2026 report makes the core tension explicit: 74% plan to deploy agentic AI within two years, but only 21% say they have mature governance for autonomous agents (Deloitte, 2026).
This is what “hard year” means operationally: when agents touch real systems (CRM, finance ops, customer comms, procurement, HR), the business must answer who approves, who audits, who is accountable, and how failures are contained (Deloitte, 2026).
Even where strategy feels “ready,” operational readiness can lag: Deloitte reports organisations feel more prepared strategically than in infrastructure, data, risk, and talent—exactly the substrate agents depend on (Deloitte, 2026).
5) Reliability: multi-step systems fail differently than chat
Agents compound errors: a small failure rate per step becomes a big failure rate across a long workflow, especially when tool calls branch or contexts drift (Gartner, 2025).
Gartner’s forecast is blunt: over 40% of agentic AI projects will be cancelled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls (Gartner, 2025).
This is why 2026 becomes the “unit economics + observability” year: you don’t scale agents until you can measure task success rate, cost per successful outcome, tool-call failure patterns, and human review overhead (Gartner, 2025; Deloitte, 2026).
6) Security: agents expand the attack surface from prompts to systems
When an agent can read emails, browse web pages, and write into internal tools, prompt injection stops being a novelty and becomes a systems security problem (NCSC, 2025).
This risk is now mainstream enough for investor/industry analysis to frame “agentic AI” as a security inflection point, specifically highlighting prompt injection and the danger of agents obeying malicious instructions embedded in content they ingest (Barron’s, 2026).
On the breach-economics side, IBM’s 2025 breach report found the global average breach cost was US$4.44M, and among organisations reporting AI-related breaches, 97% lacked proper AI access controls (IBM, 2025).
IBM also reports that 13% of organisations studied experienced breaches involving their AI models/apps, and that 16% of breaches reportedly involved attackers using AI (IBM, 2025).
7) Tool poisoning and supply chain risk: the “connector layer” becomes the target
As agent ecosystems standardise (MCP servers, plug-ins, tool registries), attackers don’t need to “jailbreak” the model—they can target the tool layer via malicious tool descriptions, compromised servers, or poisoned connectors (Invariant Labs, 2025).
Research has also directly modelled MCP-specific risks and demonstrated exploit paths (e.g., malicious servers manipulating tool invocation), reinforcing that the protocol layer needs its own security discipline (arXiv, 2025).
Even “good news” items like rapid MCP adoption come with operational risk: misconfigured or vulnerable MCP servers can expose sensitive data if security hygiene is weak (TechRadar, 2026).
领英推荐
8) Regulation and accountability: the compliance timeline collides with scale
In the EU, the AI Act is a major forcing function: different obligations phase in over time, including rules affecting general-purpose AI and transparency obligations that become relevant as agent deployments touch regulated domains (European Commission, n.d.).
In practice, agent deployments in HR, credit, healthcare, or public services must assume a world where auditability and traceability matter—because regulators will increasingly ask “show your work” (European Commission, n.d.; Deloitte, 2026).
For Australia, the government has also moved on “safe and responsible AI” via policy and guidance work that organisations can use as a governance baseline—particularly around risk, transparency, and responsible deployment expectations (Australian Government, 2025).
9) The physical constraint: energy and grid capacity now shape agent roadmaps
The IEA projects global data-centre electricity consumption will double to ~945 TWh by 2030 in the base case, growing ~15% per year from 2024 to 2030 (IEA, 2025).
Reuters reporting on U.S. state filings shows the scale of demand pressure: data centre capacity filings imply a potential tenfold jump from ~15 GW to 150+ GW nationwide (Reuters, 2026a).
Grid operators are reacting in real time: Reuters reports PJM initiatives to accelerate large-load connections and procure backup power—often favouring fast, reliable on-site generation to meet peak-demand requirements (Reuters, 2026b).
10) The 2026 deployment playbook: how to ship agents without becoming a statistic
If you’re deploying agents in 2026, your default posture should be: bounded autonomy, least privilege, and full observability—because the failure modes are systemic, not cosmetic (Gartner, 2025; IBM, 2025).
Here’s a practical, enterprise-safe checklist that maps directly to the risks above (Deloitte, 2026).
Guardrail checklist:
  
  
  
  
FAQ
Q: Are AI agents the same as GenAI chatbots? No—agents are designed to act (plan + use tools + execute workflows), not just respond in a conversation (McKinsey & Company, 2025).
Q: What’s the biggest 2026 risk? The biggest combined risk is autonomy + access + untrusted input (prompt injection), because it turns content into a control channel (NCSC, 2025; Barron’s, 2026).
Q: What’s the most important leading indicator that an agent project will succeed? A mature governance and control model—because Deloitte shows deployment intent is high while governance maturity is low (Deloitte, 2026).
Q: What should leaders ask vendors in 2026? Ask for evidence of real agentic capability (not “agent washing”), plus security controls, audit trails, and cost-per-outcome transparency (Gartner, 2025).
Closing take
2026 is when “agents” stop being a product category and start being an operating model change—and the winners will be the teams who treat agents like powerful software with a threat model, not magic automation (IBM, 2025; Deloitte, 2026).
If you want, I can convert this into a one-page internal Agent Deployment Policy (roles, approvals, audit logging, incident response, vendor requirements) aligned to Australia/APAC delivery realities and the EU compliance trajectory (Australian Government, 2025; European Commission, n.d.).
References:
Anthropic. (2024, November 25). Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol
Australian Government Department of Industry, Science and Resources. (2025). Safe and responsible AI in Australia. https://www.industry.gov.au/publications/safe-and-responsible-ai-australia
Barron’s. (2026, January). The Age of AI Agents Brings a Risk No One Is Prepared For. https://www.barrons.com/articles/agentic-ai-cybersecurity-stocks-crowdstrike-ed44bfbf
Deloitte. (2026, January). State of AI in the Enterprise: The untapped edge. https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf
European Commission. (n.d.). AI Act. Shaping Europe’s digital future. Retrieved January 29, 2026, from https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
Gartner, Inc. (2025, June 25). Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 [Press release]. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Google. (2025, April 9). Announcing Agent2Agent (A2A), an open protocol for agent interoperability. https://developers.googleblog.com/en/announcing-agent2agent-a2a/
IBM Security & Ponemon Institute. (2025). Cost of a Data Breach Report 2025. https://www.bakerdonelson.com/webfiles/Publications/20250822_Cost-of-a-Data-Breach-Report-2025.pdf
International Energy Agency. (2025, April 10). Energy and AI. https://www.iea.org/reports/energy-and-ai
International Energy Agency. (2025, April 10). Energy demand from AI. https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
Invariant Labs. (2025). MCP security notification: Tool poisoning attacks. https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
McKinsey & Company. (2025). The State of AI: Global Survey 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
National Cyber Security Centre (NCSC). (2025). Prompt injection is not SQL injection (it may be worse). https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
PwC. (2025, May). AI agent survey. https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html
Reuters. (2026a, January 22). Charting the data center development roadmap in key US states. https://www.reuters.com/business/energy/charting-data-center-development-roadmap-key-us-states-2026-01-22/
Reuters. (2026b, January 27). US grid rules for faster data centers favor on-site gas plants. https://www.reuters.com/business/energy/us-grid-rules-faster-data-centers-favor-on-site-gas-plants--reeii-2026-01-27/
Şerban von Davier, T. (2025, December 29). AI agents arrived in 2025—here’s what happened and the challenges ahead in 2026 (Republished from The Conversation). https://www.seattlepi.com/news/ai-agents-arrived-in-2025-here-s-what-a21266294

---
*检索时间: 2026-07-24 15:13:47*
*搜索来源: DuckDuckGo*
