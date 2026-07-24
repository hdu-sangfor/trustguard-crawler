# SBOMs in 2026: Some Love, Some Hate, Much Ambivalence

### 来源信息
- **URL**: https://www.darkreading.com/application-security/sboms-in-2026-some-love-some-hate-much-ambivalence
- **域名**: www.darkreading.com
- **检索关键词**: 软件供应链安全 SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
December 31, 2025 - In 2021, the outgoing Biden administration issued Executive Order 14028, which required that SBOMs be provided to purchasers of critical software. Two years later, SBOMs remained more of a mandate than a prescription for better software supply chain security. Related:Supply Chain Attacks Targeting GitHub Actions Increased in 2025

### 页面正文
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.
SBOMs in 2026: Some Love, Some Hate, Much Ambivalence
With a new year upon us, software and cybersecurity experts disagree on the utility of software bill of materials — in theory, SBOMs are great, but in practice, they're a mess.
A software bill of materials (SBOMs) has been touted as a critical tool in solving software supply-chain security issues, but the rapid change of software ecosystems and the complexity of creating an end-to-end verified chain of code continue to foil widespread adoption.
Docker, for example, has fully embraced the software ingredient lists in its Docker Hardened Images, the company's minimal, security-focused recipes for building secure software containers. The images are built from the ground up to minimize unnecessary software components — also known as artifacts — and sport complete SBOMs and proof of provenance using Level 3 of the Supply-chain Levels for Software Artifacts (SLSA), a way to digitally ensure build integrity and provide verification of software sources.
"We believe SBOMs should exist for every artifact, [and] especially container images, because they often include dozens of software packages, many of which are [open source software] components," says Michael Donovan, vice president of product management at Docker.
Yet companies struggle to create an SBOM for every piece of software, he says. Even businesses with mature software-development practices generate incomplete SBOMs because so many open source projects have not generated the supply chain artifact for their own software.
Earlier this year, the US Cybersecurity and Infrastructure Security Agency (CISA) updated its guidance for SBOMs, requiring that the manifests use a machine-readable format, such as Software Package Data Exchange (SPDX) or CycloneDX, to aid in automating the generation of and consumption of SBOMs in software development pipelines. Yet cybersecurity professionals continue to disagree about the feasible degree of SBOM operationalization.
The result is that the focus has changed, says Joseph Saunders, founder and CEO of RunSafe Security, a cybersecurity provider for embedded systems. Companies requiring SBOMs are no longer asking whether their suppliers can provide SBOMs, but whether the provided SBOMs are accurate and actionable, he says.
"Many SBOMs today are generated too late in the life cycle, lack context about how components are actually used, or fail to reflect what's truly shipped in embedded and compiled software," Saunders says. "An SBOM by itself doesn't reduce risk. Accurate SBOMs are the foundation of vulnerability identification, prioritization, and, ultimately, software supply chain security."
Know Your Software
Just like regulated industries have "know your customer" provisions, SBOMs are the actualization of a similar concept: Know your software. In 2021, the outgoing Biden administration issued Executive Order 14028, which required that SBOMs be provided to purchasers of critical software. Two years later, SBOMs remained more of a mandate than a prescription for better software supply chain security.
Since then, the European Union has passed the Cyber Resilience Act (CRA), which requires that software makers create and maintain SBOMs in a standardized, machine-readable format. Many open source ecosystems have begun to push for more support and have provided tools and processes for building SBOMs into projects and repositories.
The result is that companies are being dragged into a future that requires them to provide SBOMs, says Biswajit De, co-founder and chief technology officer of CleanStart, a provider of hardened software images.
"SBOMs are no longer theoretical. In most regulated and enterprise buying cycles, they're simply expected, not always as an explicit mandate, but very real in practice" he says. "Containers are where this shows up first because SBOMs are easy to generate and attach at build time."
A Problematic Cybersecurity Solution
Problems remain, however. Most companies that are required to provide SBOMs are generating them as the last step in a build process, producing inaccurate SBOMs to check a compliance box, says Dan Lorenc, co-founder and CEO of software supply chain security firm Chainguard. As companies look to improve the security of their software in the coming year, SBOMs may not be the most effective approach, he says.
"If you're the US government, and you get to put your finger on the scale in a few areas that are actually going to move the needle in security, [pushing SBOMs will always be] baffling to me," he says. "There are a couple of cases where they can kind of make sense, but the way they've been adopted and rolled out everywhere [just produces] more confusion and more focus on 'let's check a box' ... rather than 'let's actually integrate this and get real security."
A lack of knowledge or expertise is the top reason for failure to adopt SBOMs (69%), with all software developers citing the issue. Source: Kloeg, Berend, et al., "Charting the Path to SBOM Adoption: A Business Stakeholder-Centric Approach"
In some ways, he says, using a software composition analysis system — although it might miss some components — can be better, because it's an independent system.
"An SBOM could give people a false sense of security: [Consider an attack] happening on the build system, [which is] where the SBOM is generated," he says. "In some ways, the black-box software that scans it at the end is ... doing its best work to guess: But at least it's an independent system doing that guess, instead of the same one that may have already been compromised."
In addition, for some classes of software, SBOMs may not fully capture the state of the software on the system. For embedded devices, which often rely heavily on open source components, the manifest can be inaccurate, says RunSafe Security's Saunders.
"Producing an accurate SBOM is still tricky, especially for compiled and embedded software," he says. "Many organizations fall back on manual processes because existing tools don't fully capture the mix of open source, third-party, and proprietary components, and complex build systems only compound the challenge."
Not Just SBOMs
With supply chain attacks on the rise, leaving companies wondering whether the open source software components they use are secure, SBOMs will not be the only major software supply chain security initiative likely to see more interest in the coming year: SLSA — pronounced "salsa" — will be another focus for security-concerned development teams.
"We see demand for more than just SBOMs in the market: most notably, SLSA as a framework to ensure that build systems become just as secure as production environments," says Docker's Donovan. "It's critical for organizations to secure their build pipelines, and the SLSA framework sets a great standard for the industry, [which] we hear requested by more and more organizations."
At the end of November, the Linux Foundation released the latest major update to its supply chain security standard, SLSA 1.2. The update defines more granular build and source tracks for tracking the provenance of binary components in the build process and the source-code development process, respectively.
And, of course, the concept of ingredient lists is being applied to artificial intelligence (AI). As AI becomes an increasingly common component of software, services, and the development process, companies are beginning to generate AI bills of materials, or AI BOMs.
A useful AI BOM captures information about the datasets used to train and build an AI product, including the provenance of the data, sensitivity levels, and formats; information about the AI models, including names, versions, algorithms, training parameters, and methods; and a link to the original training set. AI BOMs should also include information on dependencies, security, governance, and the people and processes managing the process, according to a description published by cloud security provider Wiz.
"AI systems are constantly evolving, resulting in rapid dependency updates and infrastructure changes," the company said. "Even small shifts — like swapping a dataset without approval, retraining a model with different parameters, or updating a dependency to a vulnerable version — can open attack paths and undermine governance and compliance efforts."

---
*检索时间: 2026-07-24 20:51:36*
*搜索来源: DuckDuckGo*
