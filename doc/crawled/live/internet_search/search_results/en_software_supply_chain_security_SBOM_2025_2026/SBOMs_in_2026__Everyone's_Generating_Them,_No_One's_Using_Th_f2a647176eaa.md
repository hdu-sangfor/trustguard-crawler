# SBOMs in 2026: Everyone's Generating Them, No One's Using Them | Aikido Security

### 来源信息
- **URL**: https://www.aikido.dev/blog/sboms-everyones-generating-them-no-ones-using-them
- **域名**: www.aikido.dev
- **检索关键词**: software supply chain security SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
June 10, 2026 - The ENISA data points to utilization as the challenge that will define 2026. That means automated generation on every build, continuous updates across the product support period, vulnerability workflows actually tied to SBOM data, and visibility into what your suppliers ship you. That is where the survey shows the biggest gaps, and it is where the CRA will apply the most pressure. This is where Aikido Security comes in, taking supply chain transparency beyond the compliance checkbox and into your vulnerability and licensing workflows.

### 页面正文
ENISA just published its SBOM Adoption State of Play 2026, based on a survey of 334 organizations (65% EU-based, 80% directly impacted by the Cyber Resilience Act (CRA)). It is the clearest snapshot yet of where the industry stands on software supply chain transparency, and the picture is more nuanced than "everyone's on board."
Here's what stood out.
The CRA is doing the heavy lifting
Unsurprisingly, the CRA is the number one driver of SBOM adoption. 43% of organizations say the CRA has significantly accelerated their SBOM investment, with another 29% reporting a moderate influence. 78% have started their SBOM journey, and 79% expect to hit the required maturity level by the time the CRA becomes fully applicable in December 2027.
That leaves roughly 1 in 5 organizations expecting to miss the deadline, and 12% can't even estimate a timeline.
Generating SBOMs and using them are two different things
Most organizations now produce SBOMs. 39% generate them at build time, and 74% have at least partially automated per-release generation. But consumption is lagging:
- 44% report a moderate gap between generating SBOMs and actually utilizing them, and 23% report a significant gap. Only 7% have closed it.
- 20% of respondents don't know if or how SBOMs are consumed in their organization at all.
- ENISA's own conclusion is that SBOMs are used "mainly for compliance purposes" rather than active security.
An SBOM sitting unread in an artifact registry is just paperwork. SBOMs only bring value when they feed vulnerability and licensing management. That's where teams are struggling. 58% rate vulnerability matching (CPE/PURL alignment, false positives) as a major challenge, and 60% flag data quality issues like incomplete components and identifiers. Read our piece on Understanding Open-Source License Risk to learn more about how we determine risk why it's reliable.
Suppliers aren't sending SBOMs
Most organizations aren't getting SBOMs from their suppliers because most suppliers aren't sending them.
- 39% of organizations never receive SBOMs for the commercial software they buy. Another 39% only rarely do. Just 2% always receive them.
- Only 10% have mandatory SBOM clauses in supplier contracts (though 55% are working on it).
- 45% say fewer than a quarter of their suppliers meet their SBOM requirements.
- Completeness (27%), identifier accuracy (17%), and vulnerability references (12%) are the top quality gaps.
Depth compounds the quality problem. 36% of organizations need SBOMs covering all primary components and direct dependencies, but only 29% receive that. For full-depth SBOMs, the gap is 24% needed versus 14% received. And 45% don't even know what depth they're getting.
Since most real-world vulnerabilities hide in transitive dependencies, this directly caps the security value of any SBOM program.
What the data also show
The report surfaces a few more findings that reveal an industry that understands the problem and is struggling with the follow-through.
What's getting in the way
- Concern outpaces investment. Over 90% of organizations worry about supply chain security, but only 34% allocate significant resources to it. A skills gap compounds the problem, with 57% citing a lack of skills or staff as a barrier.
- Completeness is the main barrier. 62% say achieving a high degree of SBOM completeness is quite a lot or extremely difficult.
- Format wars aren't over. CycloneDX leads (44%) over SPDX (29%), but 28% still use proprietary or non-standard formats. That is a direct compliance risk, since the CRA requires a commonly used, machine-readable format and Germany's BSI guideline explicitly expects CycloneDX 1.6+ or SPDX 3.0.1+.
Who's ahead and what comes next
- Small companies are quietly ahead. 23-25% of micro and small enterprises report mature, automated SBOM implementation, versus just 4-6% of medium and large ones. Meanwhile 36% of large enterprises see SBOMs as a "mandatory burden".
- The market wants a reference implementation with ready-made pipelines (26%), tool benchmarks and a buyer's guide (22%), conformance tests (18%), and a profile defining what a "good enough" SBOM looks like (31%).
What this means in practice
The ENISA data points to utilization as the challenge that will define 2026. That means automated generation on every build, continuous updates across the product support period, vulnerability workflows actually tied to SBOM data, and visibility into what your suppliers ship you. That is where the survey shows the biggest gaps, and it is where the CRA will apply the most pressure.
How Aikido helps you get there
This is where Aikido Security comes in, taking supply chain transparency beyond the compliance checkbox and into your vulnerability and licensing workflows.
How Aikido generates SBOMs you can actually use
Automated SBOM enrichment
Aikido uses Syft to generate accurate SBOMs and automatically enriches them with precise license and copyright information to increase its overall quality.
Direct vs. transitive dependencies
Aikido’s CycloneDX export automatically separates your direct dependencies from transitive ones. This maps perfectly to the EU Cyber Resilience Act's requirement to maintain an inventory of first-level dependencies. Providing you an accurate SBOM, without having to manually trace the dependency tree yourself.
One-click SBOM generation in the right format
With one click, Aikido generates SBOMs for your repositories in CycloneDX and SPDX, the two formats the CRA and BSI guidance point to. This covers the 28% of organizations still stuck on proprietary formats and the "minimum content in machine-readable format" obligation, and exports are ready to drop into your technical documentation when a market surveillance authority comes asking.
SBOM consumption, including self-reported SBOMs
Generating your own SBOM only covers the code you write. Aikido also lets you import SBOMs you receive from vendors and suppliers (self-reported SBOMs), so third-party components get pulled into the same vulnerability monitoring as your own dependencies. Given that 39% of organizations never receive supplier SBOMs and most that do can't act on them, having a place where supplier SBOMs become monitored inventory, continuously matched against known vulnerabilities, closes the consumption gap ENISA describes.
Aikido Device Protection: visibility where SBOMs don't reach
SBOMs describe what is in your products. But your attack surface also includes the machines that build and write that software. Deploying Aikido Device Protection on build servers and developer machines extends that same inventory-and-vulnerability mindset to your development environment, covering which tools, runtimes, and packages are installed, which are outdated or vulnerable, and whether the environment producing your "trusted" builds is itself trustworthy. With supply chain attacks targeting CI pipelines and developer workstations rather than the code itself, this closes a blind spot that no SBOM will ever show you.
Together, these three capabilities let you know what you ship, know what you consume, and know the environment where it is all built. They run continuously, without adding another dashboard your team ignores. That is supply chain security that goes beyond the compliance checkbox.
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using",
      "url": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using",
      "name": "SBOMs in 2026: Everyone's generating them, no one's using them",
      "description": "ENISA's 2026 SBOM Adoption State of Play surveyed 334 organisations and found a consistent gap between generating SBOMs and actually using them. Here is what the data shows and what it means for CRA compliance.",
      "inLanguage": "en",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://www.aikido.dev",
        "url": "https://www.aikido.dev",
        "name": "Aikido Security"
      },
      "breadcrumb": {
        "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using#breadcrumb"
      },
      "mainEntity": {
        "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using#article"
      },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", "h2", ".article-summary"]
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.aikido.dev"
        },
        {
          "@type": "TechArticle",
          "position": 2,
          "name": "Blog",
          "item": "https://www.aikido.dev/blog"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "SBOMs in 2026: Everyone's generating them, no one's using them",
          "item": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using"
        }
      ]
    },
    {
      "@type": "TechArticle",
      "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using#article",
      "mainEntityOfPage": {
        "@id": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using"
      },
      "headline": "SBOMs in 2026: Everyone's generating them, no one's using them",
      "description": "ENISA's 2026 SBOM Adoption State of Play surveyed 334 organisations and found a consistent gap between generating SBOMs and actually using them. Here is what the data shows and what it means for CRA compliance.",
      "datePublished": "2026-06-10T00:00:00Z",
      "dateModified": "2026-06-10T00:00:00Z",
      "timeRequired": "PT7M",
      "inLanguage": "en",
      "url": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using",
      "canonicalUrl": "https://www.aikido.dev/blog/sboms-in-2026-everyone-generating-no-one-using",
      "author": {
        "@id": "https://www.aikido.dev/authors/nicholas-thomson#person"
      },
      "publisher": {
        "@id": "https://www.aikido.dev#organization"
      },
      "image": {
        "@type": "ImageObject",
        "url": "https://www.aikido.dev/images/blog/sboms-in-2026-cover.png",
        "width": 1200,
        "height": 630,
        "alt": "SBOMs in 2026: Everyone's generating them, no one's using them — Aikido Security"
      },
      "keywords": [
        "SBOM",
        "Software Bill of Materials",
        "Cyber Resilience Act",
        "CRA compliance",
        "software supply chain security",
        "ENISA",
        "CycloneDX",
        "SPDX",
        "SBOM adoption",
        "vulnerability management",
        "supply chain transparency",
        "open source security",
        "SCA",
        "dependency scanning",
        "Aikido Security",
        "SBOM generation",
        "SBOM consumption",
        "transitive dependencies",
        "BSI guidelines",
        "EU cybersecurity"
      ],
      "about": [
        {
          "@type": "DefinedTerm",
          "name": "Software Bill of Materials (SBOM)",
          "description": "A structured list of all components, libraries, and dependencies included in a software product, used for supply chain transparency and vulnerability management."
        },
        {
          "@type": "DefinedTerm",
          "name": "Cyber Resilience Act (CRA)",
          "description": "EU regulation requiring manufacturers of products with digital elements to ensure cybersecurity throughout the product lifecycle, including SBOM requirements, fully applicable December 2027."
        },
        {
          "@type": "DefinedTerm",
          "name": "CycloneDX",
          "description": "An OWASP-maintained SBOM standard and machine-readable format, explicitly expected by Germany's BSI guideline at version 1.6 or higher."
        },
        {
          "@type": "DefinedTerm",
          "name": "SPDX",
          "description": "A Linux Foundation SBOM standard and machine-readable format, explicitly expected by Germany's BSI guideline at version 3.0.1 or higher."
        }
      ],
      "mentions": [
        {
          "@type": "Organization",
          "name": "ENISA",
          "url": "https://www.enisa.europa.eu",
          "description": "European Union Agency for Cybersecurity, publisher of the SBOM Adoption State of Play 2026 report."
        },
        {
          "@type": "Organization",
          "name": "BSI",
          "url": "https://www.bsi.bund.de",
          "description": "Germany's Federal Office for Information Security, which has published SBOM format guidance explicitly requiring CycloneDX 1.6+ or SPDX 3.0.1+."
        },
        {
          "@type": "SoftwareApplication",
          "name": "Aikido Device Protection",
          "url": "https://www.aikido.dev/protect/device-protection",
          "applicationCategory": "SecurityApplication",
          "operatingSystem": "Cross-platform",
          "description": "Aikido Security's endpoint protection for developer devices and build servers, extending inventory and vulnerability monitoring beyond what SBOMs cover."
        },
        {
          "@type": "SoftwareApplication",
          "name": "Aikido SBOM Generator",
          "url": "https://www.aikido.dev/use-cases/sbom-generator-create-software-bill-of-materials",
          "applicationCategory": "SecurityApplication",
          "description": "One-click SBOM generation in CycloneDX and SPDX formats for software repositories, supporting CRA and BSI compliance requirements."
        }
      ],
      "citation": [
        {
          "@type": "CreativeWork",
          "name": "SBOM Adoption State of Play 2026",
          "author": {
            "@type": "Organization",
            "name": "ENISA"
          },
          "url": "https://www.enisa.europa.eu"
        }
      ],
      "articleSection": [
        "The CRA is doing the heavy lifting",
        "Generating SBOMs and using them are two different things",
        "Suppliers aren't sending SBOMs",
        "What the data also shows",
        "What this means in practice",
        "How Aikido helps you get there"
      ],
      "proficiencyLevel": "Intermediate"
    },
    {
      "@type": "Person",
      "@id": "https://www.aikido.dev/authors/nicholas-thomson#person",
      "name": "Nicholas Thomson",
      "jobTitle": "Senior SEO & Growth Lead",
      "worksFor": {
        "@id": "https://www.aikido.dev#organization"
      },
      "url": "https://www.aikido.dev/authors/nicholas-thomson",
      "sameAs": [
        "https://www.linkedin.com/",
        "https://x.com/"
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://www.aikido.dev#organization",
      "name": "Aikido Security",
      "url": "https://www.aikido.dev",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.aikido.dev/logo.png",
        "width": 200,
        "height": 60,
        "alt": "Aikido Security logo"
      },
      "sameAs": [
        "https://www.linkedin.com/company/aikido-security",
        "https://twitter.com/aikido_security",
        "https://github.com/aikido-security"
      ]
    }
  ]
}
</script>

---
*检索时间: 2026-07-24 21:33:11*
*搜索来源: DuckDuckGo*
