# Software Supply Chain Security in 2026 — SBOM, SLSA, and Sigstore

### 来源信息
- **URL**: https://blog.rajpoot.dev/posts/devops/software-supply-chain-security-sbom-slsa-sigstore/
- **域名**: blog.rajpoot.dev
- **检索关键词**: software supply chain security SBOM 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Software supply chain security explained — SBOM (CycloneDX/SPDX), SLSA levels, signing builds with Sigstore, attestations, and how to wire the whole thing into your CI without theatre.

### 页面正文
In 2026, “supply chain security” has stopped being a regulatory checkbox and become an actual engineering discipline. Three things drove it: log4shell, the SolarWinds breach, and the steady drip of npm/PyPI typosquats. The tooling has caught up. This post is the working knowledge a backend or platform engineer needs.
What we mean by “supply chain”
Every artifact you ship has a chain:
sources (Git) → dependencies (PyPI/npm/cargo) →
build (CI) → image (registry) → deploy (cluster) → runtime
Each step is a link. Each link can be tampered with. Supply chain security is the discipline of making each link verifiable.
The five attack patterns to defend against:
- Typosquat — requestsvsrequestvsrequesys.
- Dependency confusion — internal package name resolves to a public registry.
- Build hijack — attacker modifies build pipeline to inject code.
- Tampered artifact — bytes between build and registry differ from what was built.
- Runtime substitution — image at deploy time isn’t what was tested.
Modern tools address each. Let’s walk through them.
SBOM — your bill of materials
An SBOM (Software Bill of Materials) lists every component in your artifact. Two formats matter in 2026:
- CycloneDX — OWASP, terser, vulnerability-focused.
- SPDX — Linux Foundation, more verbose, license-focused.
Both work. Most tools emit either. Generate from your project:
# Python
syft -o cyclonedx-json . > sbom.cdx.json
# Go
syft -o cyclonedx-json target=./ . > sbom.cdx.json
# Node
syft -o cyclonedx-json . > sbom.cdx.json
# Container image
syft -o cyclonedx-json my-image:1.4.2 > sbom.cdx.json
Or directly from package managers:
pip-audit --format=cyclonedx-json > sbom.cdx.json
cargo cyclonedx
npm sbom --sbom-format=cyclonedx
What an SBOM gets you:
- Inventory — what’s actually shipped, including transitive deps.
- Vulnerability checking — feed the SBOM into Grype/Trivy/Dependency-Track and get a CVE list.
- License compliance — surfaces the GPL transitively pulled in by some chart you didn’t read.
Continuous SBOM scanning
grype sbom:./sbom.cdx.json --fail-on high
Wire that into CI. New high CVE in a transitive dep tomorrow → CI fails the next build. Without SBOM scanning, the same CVE goes unnoticed for months.
Signing — Sigstore and cosign
Signing artifacts proves “the bytes you have are the bytes I built.” Old way: maintain a PGP key, hope you don’t lose it, manually distribute the public key, hope nobody substitutes it.
Sigstore’s insight: use short-lived signing certificates issued by an OIDC identity (your GitHub/Google/email account) and log every signature to a public transparency log (Rekor). No long-lived keys to lose.
# Sign a container image. Browser pops up for OIDC; cert is issued; signature is logged.
cosign sign ghcr.io/example/orders-api@sha256:abcd...
# Verify
cosign verify ghcr.io/example/orders-api@sha256:abcd... \
=[email protected] \
=https://token.actions.githubusercontent.com
In CI it’s better. Use keyless signing with the workflow’s identity:
# .github/workflows/build.yml
permissions:
  id-token: write
  contents: read
  packages: write
jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: docker/login-action@v3
  - uses: docker/build-push-action@v6
  with: { push: true, tags: ghcr.io/${{ github.repository }}:${{ github.sha }} }
  id: build
  - uses: sigstore/cosign-installer@v3
  - run: |
  cosign sign --yes \
  ghcr.io/${{ github.repository }}@${{ steps.build.outputs.digest }}
The signing identity is [email protected]:org/repo:.github/workflows/build.yml@<branch>. To verify, you assert the expected identity. An attacker would need to compromise GitHub OIDC + Rekor to forge — orders of magnitude harder than stealing a PGP key.
Attestations — claims, signed
A signature says “I signed this image.” An attestation says “I signed this image and here’s a structured claim about it.” The most common claim: an SBOM.
cosign attest --predicate sbom.cdx.json --type cyclonedx \
Other useful predicate types:
- slsaprovenance— how this artifact was built (see SLSA below)
- vuln— vulnerability scan results at build time
- cyclonedx/- spdx— SBOM
At deploy/admission time, your cluster can require: “this image must have a signed CycloneDX SBOM and an SLSA L3 provenance attestation, both signed by the expected GitHub workflow.”
That’s a lot more than “trust me.”
SLSA — leveling up the build
SLSA (Supply-chain Levels for Software Artifacts) is a framework for build-pipeline integrity. Levels 1–4. Each level adds requirements.
| Level | What it requires | 
|---|---|
| L1 | Documented build process, automated build | 
| L2 | Hosted build service, signed provenance | 
| L3 | Source/build platforms isolated, ephemeral, non-falsifiable provenance | 
| L4 | Two-person review, hermetic builds | 
In practice in 2026:
- GitHub Actions + sigstore gets you to SLSA L2 with reasonable work.
- GitHub Actions reusable workflow + slsa-github-generator gets you to L3.
- L4 is a goal for projects with a 30-person platform team. Aim for L3.
Generate SLSA provenance:
# Use the SLSA reusable workflow
jobs:
  build:
  # ... build the image, capture digest as output
  provenance:
  needs: [build]
  permissions:
  actions: read
  id-token: write
  contents: write
  uses: slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@v2
  with:
  image: ghcr.io/example/orders-api
  digest: ${{ needs.build.outputs.digest }}
  registry-username: ${{ github.actor }}
  secrets:
  registry-password: ${{ secrets.GITHUB_TOKEN }}
The output is a signed in-toto attestation describing exactly what built the image. At deploy time, you verify that.
Dependency vetting
The most common compromise isn’t your code — it’s a dep your code transitively pulls in.
Lock files everywhere
# Python
uv lock  # uv.lock — exact versions
pip-compile --generate-hashes  # requirements.txt with hashes
# Node
npm ci  # only installs from package-lock.json
# Go
go.sum  # already a hash
# Cargo
Cargo.lock  # already a hash
Hashes pin you to exact bytes, not just versions. A typosquat replacing v1.0.4 with malicious v1.0.4 fails hash verification.
Allow-listed registries
For internal packages, configure your toolchain to refuse fetching from public registries:
# pip.conf — internal namespace pinned to internal index
[global]
index-url = https://internal.pypi.example.com/simple/
extra-index-url = https://pypi.org/simple/
Or better: use a single repository proxy (Artifactory, Nexus, GCP Artifact Registry) that fronts public registries and refuses anything that hasn’t been vetted.
Dependency review in CI
GitHub’s dependency-review-action:
- uses: actions/dependency-review-action@v4
  with:
  fail-on-severity: high
  deny-licenses: GPL-3.0
Blocks PRs that introduce vulnerable or wrong-licensed deps. Free signal.
Sigstore-backed package verification
Many ecosystems now publish Sigstore signatures alongside packages:
- PyPI — sigstore.org-signed releases for many top packages.
- npm — provenance attestations enforced for new releases.
- Crates.io — work in progress.
Verify on install where you can. At least audit which of your deps are signed.
Admission control — the cluster gate
Verifying signatures at deploy time is what closes the loop. A signed image is useless if the cluster runs unsigned ones happily.
Sigstore Policy Controller or Kyverno:
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-signed-images
spec:
  validationFailureAction: enforce
  rules:
  - name: verify-signatures
  match:
  any:
  - resources: { kinds: [Pod] }
  verifyImages:
  - imageReferences: ["ghcr.io/example/*"]
  attestors:
  - entries:
  - keyless:
  issuer: https://token.actions.githubusercontent.com
  subject: https://github.com/example/*/.github/workflows/*
Result: an image not signed by your CI’s identity won’t run in the cluster. Period.
Putting it together — a real CI pipeline
name: build-and-attest
on:
  push:
  branches: [main]
  tags: ["v*"]
permissions:
  id-token: write
  contents: read
  packages: write
jobs:
  build:
  runs-on: ubuntu-latest
  outputs:
  digest: ${{ steps.build.outputs.digest }}
  steps:
  - uses: actions/checkout@v4
  - uses: actions/dependency-review-action@v4
  if: github.event_name == 'pull_request'
  with: { fail-on-severity: high }
  - uses: docker/login-action@v3
  with:
  registry: ghcr.io
  username: ${{ github.actor }}
  password: ${{ secrets.GITHUB_TOKEN }}
  - id: build
  uses: docker/build-push-action@v6
  with:
  push: true
  tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
  - uses: anchore/sbom-action@v0
  with:
  image: ghcr.io/${{ github.repository }}@${{ steps.build.outputs.digest }}
  format: cyclonedx-json
  output-file: sbom.cdx.json
  - uses: aquasecurity/trivy-action@master
  with:
  image-ref: ghcr.io/${{ github.repository }}@${{ steps.build.outputs.digest }}
  severity: HIGH,CRITICAL
  exit-code: 1
  - uses: sigstore/cosign-installer@v3
  - run: |
  IMAGE=ghcr.io/${{ github.repository }}@${{ steps.build.outputs.digest }}
  cosign sign --yes "$IMAGE"
  cosign attest --yes --predicate sbom.cdx.json --type cyclonedx "$IMAGE"
  provenance:
  needs: [build]
  permissions: { actions: read, id-token: write, contents: write }
  uses: slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@v2
  with:
  image: ghcr.io/${{ github.repository }}
  digest: ${{ needs.build.outputs.digest }}
  registry-username: ${{ github.actor }}
  secrets:
  registry-password: ${{ secrets.GITHUB_TOKEN }}
This pipeline:
- Reviews dependencies on PRs.
- Builds an image.
- Generates an SBOM, scans for high CVEs.
- Signs the image (keyless).
- Attests the SBOM (linked to the image digest).
- Generates SLSA L3 provenance.
The cluster’s Kyverno policy then verifies the signature before scheduling. End-to-end provenance.
What I’d do first if I were starting today
- Lock files with hashes. Free, immediate.
- SBOM in every build, scanned in CI. A few hours of work.
- Keyless sign images with cosign. A day.
- Admission policy: require signatures. A day.
- Add SBOM attestations. Weekend.
- Add SLSA L3 provenance via the reusable workflow. Half a day.
That’s a week of work for a normal-sized backend, and it covers the realistic 95th-percentile attack surface.
What’s still hard
- Open-source dependencies you don’t control. SBOM scanning catches knowns; novel attacks slip through.
- Internal artifacts between teams in a monorepo. Same patterns apply, but tooling assumes external pipelines.
- Long-lived images. Your “stable” base image from 2024 has 60 unpatched CVEs. Rebase regularly.
- Cultural drift. Once the policies are in, the temptation to add --insecure“just for now” is constant. Hold the line.
Read this next
- The SLSA spec — short and clear.
- Sigstore docs — start with cosign, get into Rekor / Fulcio later.
- The OWASP Software Component Verification Standard.
- Platform Engineering and IDPs — supply chain security is a platform feature, not an app feature.
If you want a working build-and-attest reusable workflow you can drop into any service, it’s on rajpoot.dev
.
Building something AI-, backend-, or data-heavy and want a second pair of eyes? I do consulting and freelance work — see my projects and ways to reach me at rajpoot.dev .

---
*检索时间: 2026-07-24 15:24:52*
*搜索来源: DuckDuckGo*
