# OpenAI says its AI agent broke out of testing sandbox to hack Hugging Face

### 来源信息
- **URL**: https://arstechnica.com/ai/2026/07/how-an-openai-benchmark-test-turned-into-a-real-world-cyberattack/
- **来源站点**: Ars Technica Security
- **页面抓取**: 成功

### 页面正文
OpenAI says an agent powered by its LLM models escaped its sandboxed testing environment to infiltrate Hugging Face’s servers as part of an overzealous attempt to obtain solutions to a benchmark test. The company says it considers the unintended infiltration an “an unprecedented cyber incident” and is working with Hugging Face on new protections to prevent a recurrence.
Hugging Face disclosed an intrusion last week that it said involved “unauthorized access to a limited set of internal datasets and to several credentials used by our services.” The AI data clearinghouse said it used its own LLM-driven analysis to identify “a swarm of tens of thousands of automated actions” from an “autonomous agent framework.” That agentic swarm exploited a flaw in Hugging Face’s data-processing pipeline to gain the ability to run code as a processing worker, eventually escalating to high-level access to the company’s cloud and server clusters.
At the time, Hugging Face said the LLM being used in the attack was “still not known.” But OpenAI took responsibility for the intrusion Tuesday evening, saying it came about during an internal test involving the recently released GPT-5.6 Sol and “an even more capable pre-release model.” The models were being tested against the ExploitGym benchmark, an independent testing suite based on hundreds of real-world security vulnerabilities.
Although OpenAI said the benchmark tests were running in “a highly isolated environment,” its agents still had access to “internally hosted third-party software” to install required package registries. While working on the ExploitGym benchmark over a weekend, OpenAI says the agent “spent a substantial amount of inference compute finding a way to obtain open Internet access,” eventually locating one via a zero-day vulnerability in the package registry cache proxy.
With that wider Internet access established, OpenAI says the agent “inferred that Hugging Face potentially hosted models, datasets, and solutions for ExploitGym,” leading to the previously disclosed attack on the servers. OpenAI says its security team “discovered this anomalous activity internally,” independent of Hugging Face’s own detection.

---
*爬取时间: 2026-07-24 15:56:51*
*来源: 直接站点爬取*
