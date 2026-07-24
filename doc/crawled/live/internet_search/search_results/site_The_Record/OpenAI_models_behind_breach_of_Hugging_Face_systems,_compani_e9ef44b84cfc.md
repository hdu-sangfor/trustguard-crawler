# OpenAI models behind breach of Hugging Face systems, companies sayAlexander Martin| July 22nd, 2026

### 来源信息
- **URL**: https://therecord.media/openai-cyberattack-hugging-face
- **来源站点**: The Record
- **页面抓取**: 成功

### 页面正文
OpenAI models behind breach of Hugging Face systems, companies say
OpenAI announced Tuesday that its models were behind a breach of AI platform Hugging Face, five days after Hugging Face disclosed catching and containing an “end to end” attack “by an autonomous AI agent” without knowing who was responsible.
Hugging Face published a security disclosure on July 16 saying it had reported the intrusion to law enforcement. It is not clear if the company will withdraw its complaint following OpenAI publishing its own account of what happened on Tuesday.
Clement Delangue, Hugging Face's co-founder and chief executive, said Tuesday “we strongly believe there was no malicious intent” on OpenAI’s part, however the incident is likely to raise questions about liability, disclosure standards, and the adequacy of containment practices as AI systems become more capable.
OpenAI called the incident “unprecedented” and said it occurred when models being evaluated internally, including a pre-release system running without standard safety filters, escaped a sandboxed testing environment.
The company said its agent exploited a vulnerability in a software package registry proxy, then identified Hugging Face as a likely source of answers for the evaluation it was tasked with. It then breached Hugging Face’s systems using what OpenAI described as stolen credentials and a second zero-day vulnerability.
Hugging Face’s account described a materially different attack path, with initial access coming via a malicious dataset that abused code-execution paths in its data processing pipeline. From there, the attacker escalated to node-level access, harvested credentials, and moved laterally across internal clusters, they said.
Hugging Face said it identified unauthorized access to a limited set of internal datasets and several service credentials, and was still assessing whether partner or customer data was affected. It found no evidence of tampering with public models, datasets, or its software supply chain.
OpenAI did not say what data was accessed or how long the agent had access before detection, nor did it identify the specific vulnerable software.
Hugging Face said its security team attempted to use frontier AI models to analyze more than 17,000 recorded attack events logged during the incident, but complained those models’ safety filters blocked its analysis of exploit payloads and attack commands.
The team instead turned to using a self-hosted open-weight model to analyze the incident. Hugging Face noted that “the attacker was bound by no usage policy, while our own forensic work was blocked.”
It is not clear whether OpenAI would have identified the attack if Hugging Face had not initially turned to open-weight models for this analysis.
OpenAI said it has implemented unspecified infrastructure controls and brought Hugging Face into a “trusted access program” following the incident to allow the company use of its frontier models without the restrictive safety filters.
“We will continue to conduct a thorough investigation alongside Hugging Face and will share more details on the vulnerabilities, incident, and findings when our investigation is complete,” OpenAI stated.
Alexander Martin
is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

---
*爬取时间: 2026-07-24 15:55:49*
*来源: 直接站点爬取*
