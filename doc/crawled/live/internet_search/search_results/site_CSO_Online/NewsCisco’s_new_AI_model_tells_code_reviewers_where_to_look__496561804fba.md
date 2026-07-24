# NewsCisco’s new AI model tells code reviewers where to look for vulnerabilitiesBy Shweta SharmaJul 22, 20264 minsCode Se

### 来源信息
- **URL**: https://www.csoonline.com/article/4200151/ciscos-new-ai-model-tells-code-reviewers-where-to-look-for-vulnerabilities-2.html
- **来源站点**: CSO Online
- **页面抓取**: 成功

### 页面正文
Cisco has revealed a family of open-weight AI models called Antares that, it said, can help security teams isolate potentially vulnerable parts of a software repository before deeper investigation begins.
Rather than detecting a specific CVE or generating a patch, these models search a codebase using only a Common Weakness Enumeration (CWE) description and return the files most likely to contain that class of vulnerability.
“Its purpose is to reduce a large codebase to a focused set of files that a security professional or a downstream security workflow should investigate,” Cisco’s AI researcher Supriti Vijay said via email. “The goal is not to replace a security engineer’s judgement or send them on a wild-goose chase, but to reduce fatigue and workload by helping them triage an issue earlier and focus their investigation on the most relevant parts of the codebase.”
The Antares family consists of models with 350 million, 1 billion, and 3 billion parameters trained specifically for repository-scale vulnerability localization.
The company said its largest model approaches the performance of GPT-5.5 on its internal vulnerability localization (Vloc) benchmark while remaining small enough for low-cost local deployment.
A search assistant, not a vulnerability detector
Cisco is careful to define what Antares is, and what it is not.
“Antares outputs a ranked list of source files likely to contain a relevant vulnerability, along with the terminal exploration trace that led to that result,” Cisco Foundation AI Chief Scientist Amin Karbasi wrote in a blog post, adding that the models are not meant to replace the broader application security toolchain: Human analysts or downstream security tools will still be needed to confirm exploitability, identify vulnerable lines of code, assess severity and generate fixes.
Antares differs from conventional static analysis platforms such as Semgrep or CodeQL, which primarily rely on predefined rules or queries. Cisco instead describes Antares as an evidence-driven exploration agent that adapts its search as it traverses the repository.
Cisco’s argument is that large repositories often contain thousands of files, making manual reviews exhaustive and unrealistic. By reducing the search space to a manageable shortlist, the company hopes to reduce investigation fatigue without replacing human judgement.
Claims of specialization over scale
Cisco is also making a statement about how cybersecurity models should evolve.
Instead of pursuing larger foundational models, Cisco argued that specialized, task-trained models can outperform much larger open-weight alternatives for vulnerability localization. In its evaluation Antares-3B, the largest model intended for single-GPU deployments, produced results comparable to GPT-5.5 while outperforming several substantially larger open models by Google, OpenAI and Meta.
The family also includes Antares-350M for resource-constrained environments and Antares-1B for laptops and workstations, which Cisco has made available as open-weight models on Hugging Face.
The command line interface (CLI) on the models supports targeted CWE investigations, repository-wide scans, SARIF output and local inference, which Cisco said enables organizations to keep proprietary code inside their own trust boundary.
However, because Antares identifies candidate files rather than confirmed vulnerabilities, organizations will still need to understand how often such repository-wide searches should be run, how much they improve existing triage workflows, and whether the reduction in investigation effort ultimately translates into measurable security or cost benefits.
This article first appeared on InfoWorld.

---
*爬取时间: 2026-07-24 21:46:15*
*来源: 直接站点爬取*
