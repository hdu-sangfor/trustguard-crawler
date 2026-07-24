# Google gives developers an AI bug hunter that also writes patches

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/24/google-codemender-ai-agent-code-security/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
Google gives developers an AI bug hunter that also writes patches
Google has launched a preview of CodeMender, an AI agent built to scan code for security flaws, confirm they are exploitable, and generate fixes for developers to review.
(Source: Google)
The company describes it as a response to attackers who are already using AI to speed up their work, arguing that defenders need automation that moves at the same speed.
“CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk,” Google said.
CodeMender is now available through Gemini Enterprise Agent Platform, using Google’s generally available Gemini models, or as a component of AI Threat Defense, Google’s AI-powered security platform.
A separate version paired with Gemini 3.5 Flash Cyber is limited to a small number of governments and trusted partners, with Google planning to expand access over time. Google plans to support third-party frontier models later this year.
“We’ve fine-tuned CodeMender’s harness to be continuously updated with the latest Google DeepMind research, including the up-to-date agent skills, security tools, and system prompts,” the company explained.
“Operating in the secure-by-design Agent Platform, CodeMender is protected by enterprise-grade, built-in governance and security guardrails, including secure traffic routing through your VPC, data isolation and encryption, and zero retention of source code data,” Google added.
How the agent works
CodeMender runs in three stages. It first scans repositories for vulnerabilities that static tools often miss, including memory corruption, injection flaws, web security issues, cryptographic weaknesses, and insecure data handling. It supports C/C++, Go, Java, Python, Ruby, Rust, and TypeScript.
Second, it tries to confirm a flaw is worth acting on. Rather than stopping at a pattern match, CodeMender builds a proof-of-concept exploit and runs it in a sandbox the customer controls, a step Google says cuts down on false positives.
Once a flaw is confirmed, the agent writes a patch and checks it with a model acting as judge, meant to catch cases where a fix breaks something else in the application. The patch reaches a developer as a code diff, and no change reaches a repository without manual approval.
When deployed within AI Threat Defense, CodeMender works alongside Wiz to link vulnerabilities with deployment context and trigger automated penetration testing.
“CodeMender is a critical step towards a continuous, self-healing agentic software development lifecycle, a future where code is autonomously secured, validated, and patched before it ever hits production,” the company concluded.

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
