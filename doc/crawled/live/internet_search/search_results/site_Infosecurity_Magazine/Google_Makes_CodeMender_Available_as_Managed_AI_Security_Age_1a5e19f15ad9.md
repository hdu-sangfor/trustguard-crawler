# Google Makes CodeMender Available as Managed AI Security Agent

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/google-codemender-available-ai/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
Users of Google’s Gemini Enterprise Agent Platform and AI Threat Defense can leverage CodeMender, now a fully managed AI code security agent built for the enterprise, to find and fix vulnerabilities.
Developed by Google DeepMind, CodeMender was officially introduced in October 2025 primarily as an advanced security research project.
It initially offered capabilities such as autonomous, research-based software vulnerability discovery, debugging and patching.
The system utilized Gemini reasoning models alongside static and dynamic code analysis tools to perform deep root-cause analysis on codebase defects.
Rather than merely pointing out theoretical security issues, it focused on generating correct patches and automatically validating them to ensure they resolved vulnerabilities without causing regressions.
In its initial research phase, the DeepMind team said CodeMender also demonstrated proactive capabilities by successfully rewriting legacy codebase patterns to pre-emptively eliminate entire classes of vulnerabilities, resulting in the successful upstreaming of 72 security fixes to major open-source projects under human-in-the-loop oversight.
From Research Tool to Enterprise-Ready AI Code Security Agent
Now, Google has expanded CodeMender's capabilities with its transition from a standalone research project to a fully managed, enterprise-ready AI code security agent integrated directly into Google Cloud's infrastructure.
Rather than relying solely on code analysis, the agent now actively builds and runs proof-of-concept (PoC) exploits in customer-managed sandboxes to verify if vulnerabilities are truly exploitable.
It also delivers tested fixes directly to development pipelines as code differences for review, while introducing a large language model-as-a-judge mechanism to guarantee that these changes align with specific organizational rules and do not break core business logic.
CodeMender is now multi-model, allowing developers to choose from different Gemini models, such as Gemini 3.5 Flash, Gemini 3.1 Pro, or Gemini 3 Flash, to balance costs, speed and deep scanning needs.
“It will support third-party frontier model options later this year,” Google said in a statement on July 21.
CodeMender: Current Features and Future Roadmap
Currently, enterprise customers can access CodeMender through the Google Cloud ecosystem.
It is available in public preview as a code security agent on the Gemini Enterprise Agent Platform, where it supports generally available models and integrates directly into local developer environments via a command line interface (CLI) and tools such as VS Code and the Antigravity desktop app.
CodeMender can also be deployed immediately as a core component of Google AI Threat Defense, working in tandem with Mandiant's frontline expertise and Wiz's contextual risk prioritization.
For security and control, features such as secure traffic routing through a customer's Virtual Private Cloud, data isolation, encryption and zero retention of source code data are fully operational today.
At the preview stage, CodeMender officially supports scanning and remediating vulnerabilities across major software languages including C, C++, Go, Java, Python, Ruby, Rust and TypeScript or JavaScript, alongside popular enterprise frameworks like Django, Flask, React, Spring Boot and Express.
While Gemini 3.5 Flash is the default model, Gemini 3.1 Pro and Gemini 3 Flash are also available in preview.
Additionally, a highly specialized, security-tuned model called Gemini 3.5 Flash Cyber – specifically engineered within CodeMender to quickly identify, test and patch critical flaws – is currently in a limited-access pilot program, which Google is restricting exclusively to governments and trusted partners due to its powerful dual-use nature.
Several other features are slated to arrive soon, like the capability for Wiz to actively call on CodeMender to scan code in AI Threat Defense. This will allow Wiz's Green Agent to orchestrate the remediation process directly.
Finally, Google is planning to roll out advanced enterprise governance features in the future, which will include robust user registration and identity management, advanced observability and audit logs and localized data residency controls.
Image credits: Koshiro K / Mijansk786 / Shutterstock.com

---
*爬取时间: 2026-07-24 15:48:24*
*来源: 直接站点爬取*
