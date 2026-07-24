# Why Software Supply Chain Security Cannot Stop at SBOMs – Netizen Blog and News

### 来源信息
- **URL**: https://blog.netizen.net/2026/07/17/why-software-supply-chain-security-cannot-stop-at-sboms/
- **域名**: blog.netizen.net
- **检索关键词**: 软件供应链安全 SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
1 week ago - CISA describes an SBOM as a formal record of software components and their supply chain relationships, and its 2025 draft minimum elements proposed added data such as component hashes, licensing information, generation tools, and generation context.

### 页面正文
Software bills of materials have become one of the most visible controls in software supply chain security. They provide a machine-readable inventory of the libraries, packages, modules, frameworks, and other components associated with a software product. When a new vulnerability is disclosed, an SBOM can help an organization determine which applications may contain the affected component without waiting for development teams to search each codebase manually.
That visibility has real security value. CISA describes an SBOM as a formal record of software components and their supply chain relationships, and its 2025 draft minimum elements proposed added data such as component hashes, licensing information, generation tools, and generation context. These fields can make component identification and comparison more reliable.
An SBOM still answers a narrow question: What components are believed to be present?
It does not prove that the components are trustworthy, that the source repository was secure, that the build environment was uncompromised, that the published artifact matches the reviewed source, or that the software will behave safely after deployment. It may identify vulnerable code, yet it may miss malicious code that has no CVE, compromised build logic, stolen maintainer credentials, poisoned development tools, or tampering that occurred after the SBOM was generated.
Software supply chain security must extend from source creation through build, packaging, publication, deployment, and runtime. The SBOM is a valuable inventory inside that process. Treating it as the complete security control leaves the most consequential parts of the chain unverified.
An Inventory Is Not Proof of Integrity
An SBOM is commonly compared with an ingredient label. The comparison explains its purpose, but it can also obscure its limitations.
An ingredient label tells a consumer what a product is supposed to contain. It does not prove that the factory was secure, that no one altered the product after inspection, or that the label matches what is inside the package. The same distinction applies to software.
A development team can scan a source directory, container image, package manifest, lockfile, or compiled artifact and generate a detailed SBOM. The resulting document may list hundreds or thousands of dependencies. That record alone does not establish:
- Who approved each source change
- Whether the source repository was compromised
- Whether a maintainer account was taken over
- Which build system created the final artifact
- Whether the build used the reviewed source revision
- Whether an attacker modified the artifact after compilation
- Whether the SBOM itself was altered
- Whether a package executed malicious installation scripts
- Whether undeclared code was downloaded during the build
- Whether a dependency behaves maliciously despite having no known vulnerability
SLSA makes this distinction explicit. Its current specification states that source scanning and vulnerability analysis cannot prove that the reviewed code is the same code that reached the user. Code can be changed after review, during compilation, in packaging, or through distribution infrastructure. SLSA uses provenance and increasingly hardened build requirements to create evidence connecting source code to a delivered binary.
The difference is between composition and integrity.
Composition records what a product contains. Integrity provides evidence that the product was created through an expected process and has not been altered outside that process. A complete supply chain program requires both.
SBOM Accuracy Depends on How It Is Generated
An SBOM is only as reliable as the process used to create it.
Source-based generators inspect package manifests, project files, imports, lockfiles, and repository contents. They can identify declared dependencies that may never appear in the final release. They may also miss files added later by packaging scripts, compiler plugins, installation hooks, or external downloads.
Build-time generators can observe dependencies resolved during compilation and packaging. They may still miss content fetched through custom scripts, dynamically loaded modules, embedded binaries, generated code, or components copied into the artifact outside the monitored build path.
Binary and container scanners inspect the delivered artifact. They can find libraries and packages that were absent from the source manifest. Their results often depend on filenames, package metadata, hashes, language-specific markers, or database signatures. Stripped binaries, statically linked code, vendored source, modified forks, and embedded firmware can weaken that identification.
Different generation methods can produce materially different inventories for the same application. Component naming can vary across package ecosystems, operating-system repositories, source repositories, containers, and commercial scanners. A library may appear under a package URL, CPE, repository name, distribution-specific package name, or internally assigned identifier. Poor normalization can cause a vulnerable component to go unmatched or create duplicate records that look like separate components.
The SBOM may also describe the wrong lifecycle stage. A source SBOM, build SBOM, release SBOM, container SBOM, and deployed SBOM can all contain different component sets. Development tools and test libraries may appear in the repository but never reach production. Runtime plugins may be installed after the release SBOM was generated.
Security teams need to know what the SBOM represents, which artifact it covers, which tool created it, when it was produced, and which limitations apply. CISA’s 2025 draft proposal to add generation context reflects this need. A component list without context can create a false impression of completeness.
A Static SBOM Becomes Stale Quickly
Modern software is not a fixed collection of files.
Container images are rebuilt. Base images change. Packages are updated. Plugins are installed. Feature flags activate new code paths. Infrastructure definitions pull modules from registries. Applications call external services whose internal components are controlled by another organization. Serverless functions and short-lived workloads can appear and disappear between inventory scans.
An SBOM generated during an earlier release does not necessarily represent the software running today.
This problem is more severe in environments that use floating version ranges, mutable container tags, unpinned Git references, automatic dependency updates, or installation commands that resolve packages at deployment time. Two builds created from the same source revision can contain different transitive dependencies when resolution occurs on different dates.
A useful SBOM program must bind each SBOM to an immutable artifact digest and track the document through the artifact lifecycle. The SBOM for a container should correspond to the exact container-image digest being deployed, not merely to the repository name or a mutable tag such as latest.
Production inventory must also reconcile intended composition against observed deployment. A signed SBOM may accurately describe an approved release yet fail to identify an unauthorized plugin, injected library, side-loaded module, or post-deployment modification.
SBOM generation cannot be a quarterly compliance exercise. It must occur as part of each controlled build and remain connected to deployment records, asset inventory, vulnerability intelligence, and runtime telemetry.
Known Vulnerabilities Are Only One Supply Chain Risk
Most SBOM consumption workflows begin by matching components against vulnerability databases. The process typically involves mapping package names and versions to CVE records, assigning severity, and creating remediation tickets.
That workflow can identify known vulnerable dependencies. It does little against malicious packages or intentional backdoors that have no prior vulnerability record.
A newly compromised package can retain a legitimate name, version structure, maintainer identity, and registry location. At the point of publication, no CVE may exist. A vulnerability scanner can report a clean result even though the package contains credential theft, remote-access code, or a destructive installation script.
The XZ Utils compromise showed this gap. CISA described the incident as a multiyear effort in which a malicious actor gained maintainer trust and inserted a backdoor into versions 5.6.0 and 5.6.1. The backdoor was found through anomalous system behavior rather than ordinary dependency vulnerability scanning. An SBOM could identify the XZ version after the affected releases were known, but it could not establish that the release process had been socially compromised before disclosure.
A malicious component does not need a coding defect. Its harmful behavior may be intentional and function exactly as its author planned. CVE-oriented workflows are built mainly to track security weaknesses, not to determine whether a trusted maintainer has become malicious or whether a package publication account has been stolen.
Supply chain monitoring must include package reputation, maintainer changes, publication anomalies, unexpected scripts, dependency behavior, registry events, and differences between successive releases.
The Build System Can Be Compromised Without Changing the Declared Dependencies
An attacker does not need to poison an open-source library. Compromising the build pipeline can provide a cleaner route into the final product.
Build environments frequently hold high-value permissions. They can access source repositories, package registries, cloud accounts, signing services, deployment platforms, container registries, and production secrets. A malicious workflow action, compiler extension, build plugin, runner image, or CI script can steal credentials or modify artifacts without adding an obvious application dependency.
The 2025 compromise of tj-actions/changed-files demonstrated this risk. Attackers modified version tags so that workflows referencing those tags executed a malicious commit. The compromised action dumped CI/CD secrets into workflow logs and potentially affected more than 23,000 repositories. CISA reported that the incident may have been linked to the compromise of another GitHub Action.
An application SBOM might list every library inside the final product and still miss the compromised workflow action. The action may never be shipped with the application. It exists in the build control plane, where it can access secrets and influence what gets produced.
This creates a second supply chain inventory requirement: organizations need visibility into the tools that create software, not just the components included in it.
That scope includes:
- CI/CD actions and plugins
- Compilers, linkers, and build systems
- Runner and build-worker images
- Package managers
- Code generators
- Signing services
- Deployment tools
- Infrastructure modules
- Security scanners
- Artifact repositories
- External scripts invoked by the pipeline
A product SBOM describes the product. It does not automatically describe the full machinery used to create that product.
Trusted Package Names Can Hide Compromised Publishers
Package registries create a strong association between package identity and trust. Developers often assume that a familiar package name from its normal registry is safe.
That trust can fail when attackers obtain maintainer credentials, steal automation tokens, compromise a developer workstation, or abuse account-recovery procedures.
GitHub reported that the September 2025 Shai-Hulud npm attack used compromised maintainer accounts to inject malicious post-install scripts into popular packages. The worm stole multiple classes of secrets and attempted to spread through the package ecosystem. GitHub removed more than 500 compromised packages and outlined plans for stronger authentication, short-lived granular tokens, FIDO-based authentication, and trusted publishing.
An SBOM generated from an affected application could correctly record the package name and malicious version. The inventory would still provide no assurance that the publisher was authorized to release that version or that the version’s contents matched an approved source revision.
This is why identity controls and publication controls belong inside supply chain security.
Maintainers and vendors should reduce reliance on reusable registry tokens, require phishing-resistant authentication, use protected release environments, separate developer and publisher permissions, and prefer trusted-publishing systems based on short-lived workload identity. A package release should be attributable to a known repository, workflow, source revision, and build environment.
Digital Signatures Help, but Signing Alone Is Not Enough
Artifact signing can prove that an artifact was signed by a particular identity and that its contents have not changed since the signature was created. That is a major improvement over unsigned distribution.
A valid signature does not prove that the signed artifact is safe.
An attacker who steals a signing key can sign malicious code. A compromised CI workflow may request a legitimate signature for a poisoned build. A trusted insider may authorize a harmful release. A signing service may correctly sign whatever digest the pipeline submits, even when the pipeline has been altered.
Sigstore addresses several weaknesses in traditional signing through short-lived identity-bound certificates and the Rekor transparency log. Its verification flow checks the artifact signature, expected signer identity, certificate chain, and proof that the signing event was recorded in the log. The result establishes who signed an artifact and whether it changed after signing.
Those controls still need a policy that defines which identities, repositories, workflows, branches, and build systems are permitted to sign a release.
A consumer should not ask only, “Is this artifact signed?” The stronger questions are:
- Was it signed by the expected workload identity?
- Did the signature originate from the approved repository?
- Was the build triggered from a protected branch or release tag?
- Does the provenance identify the expected source commit?
- Was the build performed on an approved build service?
- Is the artifact digest the same digest recorded in the SBOM and deployment manifest?
- Does the signing event appear in the expected transparency log?
- Was the signer identity behaving consistently with prior releases?
Signatures become more valuable when they are connected to provenance, policy, and independent verification.
Provenance Connects Source Code to the Final Artifact
Build provenance records verifiable information about how an artifact was produced. Depending on the format and assurance level, it can identify the builder, build process, source repository, source revision, inputs, parameters, and output digest.
SLSA organizes build integrity into ascending levels. Lower levels establish that provenance exists. Higher levels require stronger build-service controls and greater resistance to tampering with the build, provenance, or artifact. The current SLSA specification states that its Build Track covers Levels 1 through 3.
Provenance helps answer questions an SBOM cannot:
- Was this binary built from the reviewed source commit?
- Which build platform created it?
- Which source repository supplied the input?
- Were unexpected build parameters used?
- Did the artifact originate outside the approved CI system?
- Has the artifact changed since the build completed?
An SBOM may state that a release contains a particular library version. Provenance can show that the release came from an approved build using a defined set of inputs. The two records serve separate purposes and should be cryptographically bound to the same artifact digest.
SLSA also states its own boundaries. It does not prove code quality, determine whether a producer is intentionally malicious, or automatically inherit assurance across every transitive dependency. Each dependency remains part of the trust analysis.
No single attestation can cover the entire chain. Security comes from linking several types of evidence and rejecting artifacts when required evidence is absent or inconsistent.
VEX Adds Exploitability Context
An SBOM can create a large volume of vulnerability findings. Some represent direct, reachable exposure. Others involve code that is disabled, removed during compilation, inaccessible through the product, or used in a way that does not invoke the affected function.
A component inventory by itself cannot make that distinction.
Vulnerability Exploitability eXchange, or VEX, provides a machine-readable assertion about whether a product is affected by a particular vulnerability. CISA defines minimum VEX elements covering document metadata, product information, vulnerability details, and product status.
VEX can reduce unnecessary remediation by recording why a vulnerable component is not exploitable in a particular product. It can also state that a product is affected, under investigation, or fixed.
VEX assertions require governance. A supplier should provide technical justification, update the assertion when the product changes, and bind it to the relevant product version. Consumers should not automatically accept unsupported “not affected” claims.
VEX is also not a substitute for runtime analysis. Reachability can depend on configuration, feature flags, network exposure, privilege, deployment architecture, and data flow. The same component may be unreachable in one deployment and exposed in another.
A risk decision should combine the SBOM, VEX, known-exploitation data, exploit probability, code reachability, runtime exposure, business impact, and compensating controls.
Dependency Control Must Begin Before the Build
Generating an SBOM after dependencies have entered the environment is too late to serve as the primary admission control.
Organizations need policies governing which packages may be introduced, where they may be retrieved, how versions are selected, and what evidence must accompany them.
Direct public-registry access from every developer machine and CI runner gives attackers several paths into the environment. Dependency confusion, typosquatting, namespace takeover, malicious updates, and compromised publisher accounts all rely on weak controls at dependency resolution.
A stronger model routes packages through a controlled internal repository or proxy. New components can be quarantined, scanned, and approved before broad use. Policies can block unapproved registries, newly published packages, unexpected maintainers, prohibited licenses, unsigned artifacts, and packages with dangerous installation behavior.
Version pinning should use immutable identifiers where the ecosystem supports them. GitHub Actions should be pinned to full commit hashes rather than mutable version tags. Containers should be deployed by digest rather than tag. Downloaded tools should be verified against expected hashes and signatures.
Pinning reduces surprise changes, but it does not prove that a pinned artifact is trustworthy. A malicious version remains malicious when pinned. Pinning must operate alongside review, provenance verification, signing, and update management.
Securing Source Control and Maintainer Identity
Many supply chain compromises begin before dependency resolution or compilation.
An attacker who controls a source repository, maintainer account, or code-review process can introduce malicious changes through normal-looking development activity. The change may pass through the same build and signing systems as a legitimate release.
Source control needs protections such as phishing-resistant multifactor authentication, protected branches, mandatory review, restricted administrative roles, signed changes where appropriate, review of workflow-file modifications, and alerts for unusual account or repository activity.
Changes to CI workflows, release scripts, package manifests, lockfiles, ownership files, and signing configuration deserve higher scrutiny than ordinary source changes. These files define how software is built and published. A small modification can redirect dependencies, expose secrets, alter the release artifact, or transfer package ownership.
Open-source governance also affects security. A critically used project may be maintained by one person with limited time, no backup maintainer, and no funded security support. Supplier assessments that examine only code-scanning results can miss this concentration of operational risk.
Security review should account for maintainer continuity, release authority, account protections, governance, incident-response contacts, and the project’s ability to issue fixes.
The Build Environment Must Be Treated as Privileged Infrastructure
CI/CD systems often have broader access than production applications. They may hold credentials capable of publishing packages, pushing containers, signing releases, modifying cloud resources, or deploying directly into production.
Build workers should be isolated, ephemeral, and narrowly permissioned. A build for one project should not inherit credentials or filesystem state from an unrelated project. Secrets should be issued only to the job that requires them, for the shortest possible period, and should not be exposed to untrusted pull requests or third-party actions.
Network egress should be controlled. A build that is expected to use an internal dependency mirror should not freely download executable content from arbitrary internet hosts. Hermetic or near-hermetic builds reduce the chance that undeclared inputs can enter during compilation.
Build logs also need protection. The tj-actions/changed-files incident showed that secrets written to logs can become exposed even when the malicious workflow does not directly transmit them to an attacker-controlled server.
Reproducible builds provide another form of validation. When independent builds from the same source and declared inputs produce matching outputs, defenders gain evidence that the released binary corresponds to the stated build process. Reproducibility is difficult across every language and platform, but it can provide high-value verification for critical components.
Policy Enforcement Must Occur Before Deployment
Supply chain evidence has little effect when it is collected but never enforced.
A deployment system should evaluate the artifact, SBOM, signature, provenance, vulnerability status, and approval records before admitting software into a sensitive environment.
An admission policy might require:
- An immutable artifact digest
- A valid signature from an approved identity
- Provenance from an approved build platform
- A source commit from a protected repository
- An SBOM bound to the artifact digest
- No prohibited components or licenses
- No unresolved vulnerabilities above the organization’s risk threshold
- VEX justification for accepted exceptions
- Approval for newly introduced dependencies
- No unexplained drift from the prior release
The policy engine should reject the artifact when evidence is missing, invalid, expired, or inconsistent. Recording a compliance warning without blocking deployment turns the control into documentation rather than prevention.
Exceptions need owners, expiration dates, compensating controls, and review. Permanent, untracked exceptions gradually convert an enforcement system into an approval formality.
Runtime Security Remains Necessary
A verified build can still be exploited after deployment. A trusted supplier can still contain a vulnerability. A signed application can load unapproved plugins, contact malicious infrastructure, or expose credentials through unsafe configuration.
Runtime controls provide containment after preventive controls fail.
Workloads should run with limited privileges, restricted filesystem access, controlled network egress, isolated credentials, and monitored process behavior. Container admission policies can verify image signatures and provenance before deployment, yet runtime enforcement must still restrict what the container can do.
Behavioral monitoring can identify package installation during runtime, unexpected child processes, shell execution, access to cloud metadata services, modifications to executable files, credential-store access, and outbound traffic to new destinations.
Runtime observations can also improve vulnerability prioritization. A component known to be loaded and exposed deserves different treatment from a library present in an image but never invoked. This does not make the dormant library harmless, since configuration changes may activate it later, but it provides stronger operational context than the SBOM alone.
Supplier Assurance Requires More Than Asking for an SBOM
Procurement questionnaires increasingly ask vendors whether they can provide an SBOM. A “yes” answer says little about the supplier’s wider security practices.
A meaningful supplier review should examine how the SBOM is generated, how often it is updated, whether it covers transitive dependencies, whether it is bound to specific release artifacts, and whether the supplier provides corrections when errors are found.
The review should also ask about:
- Secure development practices
- Source-code protections
- Build-environment isolation
- Artifact signing
- Build provenance
- Package publication controls
- Vulnerability disclosure
- VEX issuance
- Patch timelines
- Maintainer and administrator authentication
- Incident notification
- Dependency approval
- Subsupplier risk
- End-of-life support
- Evidence retention
NIST’s Secure Software Development Framework provides a core set of practices that can be integrated into development lifecycles and used as a common vocabulary between producers and purchasers. NIST SP 800-161 Rev. 1 takes a broader organizational view, covering identification, assessment, and mitigation of cybersecurity risk across products, services, suppliers, and multiple organizational levels.
The procurement objective is not to collect the largest number of documents. It is to determine whether the supplier can produce verifiable evidence that its development and delivery process is controlled.
A Complete Evidence Chain
A mature software supply chain program should connect several classes of evidence.
- The SBOM records component composition.
- The VEX document records supplier analysis of vulnerability applicability.
- The provenance attestation records how and where the artifact was built.
- The digital signature binds an approved identity to the artifact.
- The transparency log provides an auditable record of signing or publication events.
- The source-control record documents reviewed changes and approvals.
- The deployment record identifies which exact artifact entered each environment.
- The runtime record shows how that artifact behaved after deployment.
Each record answers a different security question. None can safely replace the rest.
These records should share stable identifiers, chiefly cryptographic digests. The artifact digest in the deployment manifest should match the digest in the signature, provenance, and SBOM. A mismatch should stop the release or trigger an investigation.
This model changes supply chain security from document collection into evidence verification.
Moving From SBOM Compliance to Supply Chain Assurance
Organizations often begin their SBOM program by selecting a generator and attaching its output to release artifacts. That is a useful starting point, not the finished program.
The next stage is consumption. SBOMs must enter a system that normalizes component identities, correlates vulnerabilities, tracks product versions, processes VEX statements, assigns ownership, and opens remediation workflows.
The stage after that is verification. The organization must determine whether the SBOM corresponds to the artifact, whether the artifact came from an approved build, and whether the build came from an approved source revision.
The final stage is enforcement. Unverified or policy-violating artifacts must be blocked from sensitive environments. Runtime controls must limit damage when a malicious or vulnerable component still passes preventive checks.
An SBOM provides visibility into software composition. Supply chain assurance requires evidence about identity, integrity, process, authorization, and behavior.
The distinction matters. Many of the most serious supply chain compromises do not depend on an old vulnerable library hiding inside an application. They target maintainer trust, developer accounts, build workflows, signing infrastructure, package registries, and distribution systems. A perfect component inventory cannot stop an attacker who controls the process that creates the inventory and the software it describes.
Software supply chain security cannot stop at SBOMs for the same reason asset inventory cannot replace endpoint protection, identity security, vulnerability management, and incident response. Knowing what exists is the foundation for control. It is not the control itself.
How Can Netizen Help?
Founded in 2013, Netizen is an award-winning technology firm that develops and leverages cutting-edge solutions to create a more secure, integrated, and automated digital environment for government, defense, and commercial clients worldwide. Our innovative solutions transform complex cybersecurity and technology challenges into strategic advantages by delivering mission-critical capabilities that safeguard and optimize clients’ digital infrastructure. One example of this is our popular “CISO-as-a-Service” offering that enables organizations of any size to access executive level cybersecurity expertise at a fraction of the cost of hiring internally.
Netizen also operates a state-of-the-art 24x7x365 Security Operations Center (SOC) that delivers comprehensive cybersecurity monitoring solutions for defense, government, and commercial clients. Our service portfolio includes cybersecurity assessments and advisory, hosted SIEM and EDR/XDR solutions, software assurance, penetration testing, cybersecurity engineering, and compliance audit support. We specialize in serving organizations that operate within some of the world’s most highly sensitive and tightly regulated environments where unwavering security, strict compliance, technical excellence, and operational maturity are non-negotiable requirements. Our proven track record in these domains positions us as the premier trusted partner for organizations where technology reliability and security cannot be compromised.
Netizen holds ISO 27001, ISO 9001, ISO 20000-1, and CMMI Level III SVC registrations demonstrating the maturity of our operations. We are a proud Service-Disabled Veteran-Owned Small Business (SDVOSB) certified by U.S. Small Business Administration (SBA) that has been named multiple times to the Inc. 5000 and Vet 100 lists of the most successful and fastest-growing private companies in the nation. Netizen has also been named a national “Best Workplace” by Inc. Magazine, a multiple awardee of the U.S. Department of Labor HIRE Vets Platinum Medallion for veteran hiring and retention, the Lehigh Valley Business of the Year and Veteran-Owned Business of the Year, and the recipient of dozens of other awards and accolades for innovation, community support, working environment, and growth.
Looking for expert guidance to secure, automate, and streamline your IT infrastructure and operations? Start the conversation today.

---
*检索时间: 2026-07-24 20:51:31*
*搜索来源: DuckDuckGo*
