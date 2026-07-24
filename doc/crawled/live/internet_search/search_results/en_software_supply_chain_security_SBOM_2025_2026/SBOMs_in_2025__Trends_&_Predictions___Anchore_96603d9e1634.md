# SBOMs in 2025: Trends & Predictions | Anchore

### 来源信息
- **URL**: https://anchore.com/blog/software-supply-chain-security-in-2025-sboms-take-center-stage/
- **域名**: anchore.com
- **检索关键词**: software supply chain security SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Software Supply Chain Security in 2025: SBOMs Take Center Stage. By: Josh Bressers. Jan 14, 2025. {minutes} min read. In recent years, we’ve witnessed software supply chain security transition from a quiet corner of cybersecurity into a primary battlefield.

### 页面正文
In recent years, we’ve witnessed software supply chain security transition from a quiet corner of cybersecurity into a primary battlefield. This is due to the increasing complexity of modern software that obscures the full truth—applications are a tower of components of unknown origin. Cybercriminals have fully embraced this hidden complexity as a ripe vector to exploit.
Software Bills of Materials (SBOMs) have emerged as the focal point to achieve visibility and accountability in a software ecosystem that will only grow more complex. SBOMs are an inventory of the complex dependencies that make up modern applications. SBOMs help organizations scale vulnerability management and automate compliance enforcement. The end goal is to increase transparency in an organization’s supply chain where 70-90% of modern applications are open source software (OSS) dependencies. This significant source of risk demands a proactive, data-driven solution.
Looking ahead to 2025, we at Anchore, see two trends for SBOMs that foreshadow their growing importance in software supply chain security:
- Global regulatory bodies continue to steadily drive SBOM adoption
- Foundational software ecosystems begin to implement build-native SBOM support
In this blog, we’ll walk you through the contextual landscape that leads us to these conclusions; keep reading if you want more background.
Global Regulatory Bodies Continue Growing Adoption of SBOMs
As supply chain attacks surged, policymakers and standards bodies recognized this new threat vector as a critical threat with national security implications. To stem the rising tide supply chain threats, global regulatory bodies have recognized that SBOMs are one of the solutions.
Over the past decade, we’ve witnessed a global legislative and regulatory awakening to the utility of SBOMs. Early attempts like the US Cyber Supply Chain Management and Transparency Act of 2014 may have failed to pass, but they paved the way for more significant milestones to come. Things began to change in 2021, when the US Executive Order (EO) 14028 explicitly named SBOMs as the foundation for a secure software supply chain. The following year the European Union’s Cyber Resilience Act (CRA) pushed SBOMs from “suggested best practice” to “expected norm.”
The one-two punch of the US’s EO 14028 and the EU’s CRA has already prompted action among regulators worldwide. In the years following these mandates, numerous global bodies issued or updated their guidance on software supply chain security practices—specifically highlighting SBOMs. Cybersecurity offices in Germany, India, Britain, Australia, and Canada, along with the broader European Union Agency for Cybersecurity (ENISA), have each underscored the importance of transparent software component inventories. At the same time, industry consortiums in the US automotive (Auto-ISAC) and medical device (IMDRF) sectors recognized that SBOMs can help safeguard their own complex supply chains, as have federal agencies such as the FDA, NSA, and the Department of Commerce.
By the close of 2024, the pressure mounted further. In the US, the Office of Management and Budget (OMB) set a due date requiring all federal agencies to comply with the Secure Development Framework (SSDF), effectively reinforcing SBOM usage as part of secure software development. Meanwhile, across the Atlantic, the EU CRA officially became law, cementing SBOMs as a cornerstone of modern software security. This constant pressure ensures that SBOM adoption will only continue to grow. It won’t be long until SBOMs become table stakes for anyone operating an online business. We expect the steady march forward of SBOMs to continue in 2025.
In fact, this regulatory push has been noticed by the foundational ecosystems of the software industry and they are reacting accordingly.
Software Ecosystems Trial Build-Native SBOM Support
Until now, SBOM generation has been relegated to afterthought in software ecosystems. Businesses scan their internal supply chains with software composition analysis (SCA) tools; trying to piece together a picture of their dependencies. But as SBOM adoption continues its upward momentum, this model is evolving. In 2025, we expect that leading software ecosystems will promote SBOMs to a first-class citizen and integrate them natively into their build tools.
Industry experts have recently begun advocating for this change. Brandon Lum, the SBOM Lead at Google, notes, “The software industry needs to improve build tools propagating software metadata.” Rather than forcing downstream consumers to infer the software’s composition after the fact, producers will generate SBOMs as part of standard build pipelines. This approach reduces friction, makes application composition discoverable, and ensures that software supply chain security is not left behind.
We are already seeing early examples:
- Linux Ecosystem (Yocto): The Yocto Project’s OpenEmbedded build system now includes native SBOM generation. This demonstrates the feasibility of integrating SBOM creation directly into the developer toolchain, establishing a blueprint for other ecosystems to follow.
- Python Ecosystem: In 2024, Python maintainers explored proposals for build-native SBOM support, motivated by the regulations such as, the Secure Software Development Framework (SSDF) and the EU’s CRA. They’ve envisioned a future where projects, package maintainers, and contributors can easily annotate their code with software dependency metadata that will automatically propagate at build time.
- Perl Ecosystem: The Perl Security Working Group has also begun exploring internal proposals for SBOM generation, again driven by the CRA’s regulatory changes. Their goal: ensure that Perl packages have SBOM data baked into their ecosystems so that compliance and security requirements can be met more effortlessly.
- Java Ecosystem: The Eclipse Foundation and VMware’s Spring Boot team have introduced plug-ins for Java build tools like Maven or Gradle that streamline SBOM generation. While not fully native to the compiler or interpreter, these integrations lower the barrier to SBOM adoption within mainstream Java development workflows.
In 2025 we won’t just be talking about build-native SBOMs in abstract terms—we’ll have experimental support for them from the most forward thinking ecosystems. This shift is still in its infancy but it foreshadows the central role that SBOMs will play in the future of cybersecurity and software development as a whole.
Closing Remarks
The writing on the wall is clear: supply chain attacks aren’t slowing down—they are accelerating. In a world of complex, interconnected dependencies, every organization must know what’s inside its software to quickly spot and respond to risk. As SBOMs move from a nice-to-have to a fundamental part of building secure software, teams can finally gain the transparency they need over every component they use, whether open source or proprietary. This clarity is what will help them respond to the next Log4j or XZ Utils issue before it spreads, putting security team’s back in the driver’s seat and ensuring that software innovation doesn’t come at the cost of increased vulnerability.
Learn about the role that SBOMs for the security of your organization in this white paper.

---
*检索时间: 2026-07-24 15:24:16*
*搜索来源: DuckDuckGo*
