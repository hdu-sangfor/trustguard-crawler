# Supply Chain Attacks in 2025/2026: What Happened and How to Prevent It | softScheck

### 来源信息
- **URL**: https://www.softscheck.com/en/blog/supply-chain-attacks/
- **域名**: www.softscheck.com
- **检索关键词**: supply chain attack 2025 2026 case study
- **页面抓取**: 成功

### 搜索摘要
May 20, 2026 - That three-hour window is the story of supply chain security in 2025/2026, in miniature. There is no zero-day. There is no buffer overflow. There is a human, a trusted account, and a registry that runs other people’s code at install time. In the past six months alone, attackers compromised axios, @bitwarden/cli, the entire @tanstack/* family, the official mistralai SDK on both npm and PyPI, Aqua Security’s Trivy scanner, the checkmarx/ast-github-action, and hundreds of others swept up by the self-replicating Shai-Hulud worm.

### 页面正文
axios is a JavaScript HTTP client with over a hundred million weekly
downloads. At 00:21 UTC on March 31, 2026, axios@1.14.1 appeared silently
on the npm registry — this version was compromised. According to the
official axios statement,
the attacker had gained access to the lead maintainer’s PC through a
targeted social engineering campaign and RAT malware, which gave them his
npm credentials. Three hours later, every build pipeline on the planet that
ran npm install against the latest release was downloading a North-Korean
RAT. The malicious version of axios sat on npm for 174 minutes before
being yanked, and whether a team escaped often came down to a single
unremarkable detail: the difference between npm install and npm ci.
That three-hour window is the story of supply chain security in 2025/2026,
in miniature. There is no zero-day. There is no buffer overflow. There is a
human, a trusted account, and a registry that runs other people’s code at
install time. In the past six months alone, attackers compromised axios,
@bitwarden/cli, the entire @tanstack/* family, the official mistralai
SDK on both npm and PyPI, Aqua Security’s Trivy scanner, the
checkmarx/ast-github-action, and hundreds of others swept up by the
self-replicating Shai-Hulud worm.
This post is the long-form version of a webinar we ran on the topic. You can watch the full recording here, and the article below covers the same ground in more depth:
With your consent, an external YouTube video (Google Ireland Limited) will be loaded here.
I agree to external content being displayed to me. This means that personal data may be transferred to third-party platforms (Google Ireland Limited). For more information, see our Privacy Policy.
Contents
- Why the supply chain is the new perimeter
- Why npm is particularly vulnerable
- The 2025/2026 wave
- How to prevent them
- Now / Soon / Later
1. Why the supply chain is the new perimeter
The mental model most teams operate under is still “we patch what’s in our repo.” But the average production Node.js application is only ~3 % first-party code and ~97 % open-source dependencies, often hundreds of packages deep. The interesting attack surface is no longer inside your repository. It is inside the trust graph that ends at your repository.
The mechanics of a modern supply chain attack are simple enough to fit in a diagram:
Each step on its own is mundane. Combined, they bypass every perimeter control your organisation has, because none of the traffic looks malicious in isolation: the developer pulled a known package from a known registry over TLS, ran a known build command, and the install completed without errors. The first signal that anything went wrong is usually a credential showing up somewhere it shouldn’t.
This is also why traditional dependency tooling fails so badly here.
npm audit and OSV-scanner are reactive: they look up known advisories. In
every 2026 incident we’ll walk through, no advisory existed for hours after
the malicious version was published. The only teams that were protected were
those who had already decided, before the fact, not to auto-execute foreign
code.
2. Why npm is particularly vulnerable
Every modern language ecosystem has some flavour of this problem. pip
runs setup.py at install time, NuGet executes MSBuild targets, Maven runs
plugins, GitHub Actions injects shell scripts into your pipeline. The following
properties make npm a particularly attractive attack target:
- 3 million+ packages, with billions of weekly downloads.
- Lifecycle scripts (preinstall,install,postinstall) run without a prompt, without a sandbox, and with the full privileges of whoever invokednpm. Often that’s a CI runner with cloud credentials.
- Floating versions by default. ^1.14.0resolves to whatever was latest at install time, including a malicious release published six minutes ago.
- Hundreds of transitive dependencies behind every direct one. Median is roughly 83 packages for a Node app (arXiv 2512.14739). Nobody reads them all, nobody can.
For comparison, Go modules made very different design choices: there are no
install-time hooks (go build only compiles), the registry is immutable
(proxy.golang.org caches versions forever, takedowns don’t rewrite
history), and a global transparency log (sum.golang.org) lets go mod verify prove that nothing was tampered with. The same package manager
problem, solved very differently. Security is a design choice, and npm
chose the opposite one.
The Sonatype Q2 2025 Open Source Malware Index counted a +188 % year-over-year increase in malicious open-source packages. That growth shows up in the 2026 headlines.
3. The 2025/2026 wave
A short timeline for context. The 2026 incidents are not isolated events, they are the current state of a multi-year development:
| Year | Incident | What was new | 
|---|---|---|
| 2020 | SolarWinds Orion / SUNBURST | ~18 000 organisations from a single signed update | 
| 2024 | XZ utils (CVE-2024-3094) | Close to three-year long-con; nearly hit OpenSSH on every major distro | 
| 2025 | Shai-Hulud waves 1 & 2 | First self-replicating npm worm | 
| 2026 | Axios, Bitwarden CLI, TanStack & Mistral AI | DPRK-grade social engineering, CI-only attack chains, AI assistant poisoning, worm hidden behind valid npm provenance | 
The rest of this section walks through what’s actually new in each 2026 incident. None of the attacks were technically sophisticated. It was the trust model, not vulnerabilities, that was exploited.
Shai-Hulud — the self-replicating npm worm
In September 2025, the group TeamPCP released what StepSecurity dubbed Shai-Hulud, the first self-replicating worm to find a foothold in the npm registry. The mechanism, once you’ve seen it once, is genuinely hard to believe nobody shipped it earlier:
Every package the victim has write access to gets a new malicious version. The worm needs no further attacker interaction after the initial infection, and revocation is genuinely painful: you have to find and pull every poisoned version, across every scope, across every maintainer.
Three named waves so far:
- Wave 1 (Sep 2025): 500+ packages compromised. CISA issued a sector-wide alert.
- Wave 2, “Second Coming” (Nov 2025): GitHub-based C2 dead-drop, ~25 000 repositories exposed (Wiz writeup).
- Wave 3, “Third Coming” (Apr 2026): first in-the-wild attack targeting AI coding assistants — landed via the Bitwarden CLI compromise below.
A fourth campaign with a different attack vector, dubbed “Mini Shai-Hulud”, hit in May 2026 (TanStack / Mistral AI). We’ll get to that one separately.
Axios — Phishing in a startup hoodie
axios is the most-used HTTP client on npm: ~100 million weekly downloads,
and it ends up as a transitive dependency in roughly 30 % of Node
applications. axios is so ubiquitous that many teams only found out they
were using it through this incident.
On March 31, 2026, the maintainer was approached on Slack by someone who appeared to be the technical co-founder of an early-stage payments startup. Branded workspace, real domain, real landing-page, weeks of low-temperature back-and-forth. After enough trust was established the contact moved the conversation to a Teams call and asked for help debugging an integration. “Could you just run this binary real quick?” The maintainer did. According to the official post-mortem, the binary was RAT malware that gained access to his PC and stole his npm credentials.
Attribution is UNC1069 / Sapphire Sleet, a DPRK-nexus group with a toolkit dating back to at least 2018 (Google GTIG). They have been running exactly this fake-recruiter/fake-startup play on LinkedIn and Slack since 2023. What’s interesting is that the attack required no technical exploit at any point. The whole chain was a relationship.
The published payload is also worth dissecting. Rather than putting the
malicious code in axios itself (where any half-decent reviewer would have
spotted it), the attacker added a brand-new “sister package” called
plain-crypto-js — a typosquat of the legitimate crypto-js — and pointed
the postinstall hook at that:
  "dependencies": {
+  "plain-crypto-js": "4.2.1",
  },
  "scripts": {
+  "postinstall": "node ./node_modules/plain-crypto-js/.bin/init"
  }
The manipulated package dropped WAVESHAPER.V2, a cross-platform RAT for macOS, Windows and Linux. Multiple vendors all published technical write-ups within 48 hours.
Who escaped? Anyone who ran npm ci against a committed lockfile, anyone
with ignore-scripts=true, and anyone behind an internal registry proxy
that quarantined fresh transitive packages. As we said in the introduction,
the boring controls did all the work.
Bitwarden CLI — when the supply chain is the attacker
Four weeks after axios, on April 22 2026, TeamPCP struck again. This
time there was no maintainer to phish. The whole attack happened inside
CI, and it is the cleanest example we have of a supply-chain-in-a-supply-
chain compromise.
The malicious release sat on npm for 90 minutes (17:57 to 19:30 ET) and
collected 334 downloads. That number sounds small, but the consumer set for
@bitwarden/cli is CI bots in SecOps pipelines — i.e. the highest-value
installs on the entire registry. To be explicit:
the Bitwarden vault was never breached. Only the npm distribution path
was affected.
The payload itself broke new ground in two ways. First, it was worm-class:
it harvested credentials across AWS, GCP, Azure, GitHub PATs, npm tokens
and kubeconfig, wrapped the loot in RSA-encrypted AES-256-GCM and
uploaded it to a GitHub dead-drop. Second — and this is the part the
industry is still digesting — it explicitly enumerated authenticated AI
coding assistants on the host and stole their credentials:
- Targets: Claude Code, Cursor, Codex CLI, Aider, Kiro, Gemini CLI, OpenCode.
- Source files: ~/.claude.json,~/.claude/mcp.json,~/.kiro/settings/mcp.jsonand similar.
- Persistence: a 3.5 KB heredoc appended to ~/.bashrcand~/.zshrc, so a fresh stealer fires on every login.
This is the first publicly-documented in-the-wild supply chain attack against AI coding assistants, and we think it deserves to be its own category. AI assistants are privileged identities. They hold API tokens. They execute shell commands. They consume repo-local instruction files that human reviewers almost never read carefully. Taking over the developer’s AI agent is more attractive than their shell, because the agent has tokens and access in addition to the shell.
TanStack, Mistral AI & UiPath — when OIDC mints a token for the attacker
Three weeks after Bitwarden, on the night of May 11 to 12 2026, TeamPCP ran the largest campaign of the year. In a single six-hour window they pushed 400+ malicious versions across 170+ npm packages and 2 PyPI packages:
- @tanstack/*— 42 packages (Router, Query, Table — used in tens of thousands of React applications), 84 malicious versions.
- Mistral AI — the official @mistralai/mistralaiSDK plus the Azure and GCP integrations, three malicious versions each, and the PyPI releasemistralai 2.4.6.
- UiPath — 65 automation packages.
- OpenSearch (1.3 M weekly npm downloads).
- Guardrails AI (PyPI).
The press dubbed the campaign after an earlier campaign “Mini Shai-Hulud”,
but the entry vector was new and is worth taking a hard look at. There was no maintainer phishing,
no stolen .npmrc, no postinstall-driven worm. Everything happened
inside the legitimate TanStack release workflow on GitHub Actions:
What makes this incident genuinely uncomfortable: the published packages
carried valid npm provenance signatures. Provenance proves that the
artefact was built by a specific GitHub Actions workflow in a specific
repository. In this case both statements were true. The artefact really
was built by the legitimate TanStack release workflow, in the legitimate
repository, from a main commit with a valid signature. The attacker had
just convinced that workflow to compile their code.
OIDC Trusted Publishing — the security model the industry is currently betting on to replace long-lived npm publish tokens — did exactly what it was designed to do. It minted a short-lived token, scoped to a workflow, on behalf of an attestable identity. The problem is that the workflow had been tricked into running attacker code first.
The PyPI half of the campaign used a different but equally simple trick.
mistralai 2.4.6 contained a one-liner injected into
mistralai/client/__init__.py that downloaded a payload to
/tmp/transformers.pyz (named to mimic Hugging Face’s Transformers) and
executed it on every import on Linux. SafeDep, Snyk, Wiz, Aikido and Orca
published parallel technical
analyses
within 24 hours.
StepSecurity researcher ashishkurmi raised the alarm publicly within 20
to 26 minutes of the first malicious publish. That is fast. It was still
long enough for several hundred CI runners worldwide to pull poisoned
tarballs.
There are three lessons from this incident specifically:
- OIDC is necessary but not sufficient. If your release workflow can be coerced into running attacker code, OIDC will sign that code into production. Provenance proves integrity after the build, not correctness of the build.
- pull_request_targetis loaded. It runs with the permissions of the base repository against code from a fork. Never check out PR head code in a- pull_request_targetworkflow without strict sandboxing.
- The GitHub Actions cache is a shared trust boundary. Almost nobody treats it as one today. The TanStack incident is the proof that you have to.
4. How to prevent them
Look across all four 2026 incidents and the same controls keep appearing in the “would have stopped it” column. Most of them are free. None of them require a new vendor. They are however genuinely unattractive, which is why nobody enables them by default.
Developer hygiene
| Do | Don’t | 
|---|---|
| Pin exact versions for direct deps | Trust ^x.y.zranges in production | 
| Commit package-lock.json | Run npm installas root | 
| Use the frozen-lockfile install in CI ( npm ci/pnpm i --frozen-lockfile/yarn install --immutable/bun install --frozen-lockfile) | Reuse publish tokens across workflows | 
| Set ignore-scripts=truein.npmrc | Ignore that “weird new transitive dep” feeling | 
| Set a minimum release age (e.g. 2 days) on every package manager | Install brand-new versions the same day they hit the registry | 
| Hardware MFA (FIDO2) on every publish-capable account | Install rarely-used deps globally | 
| Review dependency PRs like code PRs | 
A few of the entries deserve a sentence each:
- Frozen-lockfile installs in CI. Every package manager now has the same idea — “install exactly this lockfile, fail otherwise” — under a different name: - npm ci # npm pnpm install --frozen-lockfile # pnpm (also the default in CI) yarn install --immutable # Yarn Berry (v2+) bun install --frozen-lockfile # Bun 1.0+- A team building in frozen-lockfile mode against a committed lockfile was unaffected by Axios and Bitwarden. Plain - npm install/- pnpm install/- yarn addsilently resolves new versions including all malicious changes; the frozen variants do not.
- ignore-scripts=trueis the one-line- .npmrcchange that would have blocked the actual payload execution in three of the four incidents above. No-one’s stack actually needs- postinstallscripts at install time in CI. Run them explicitly later, if at all.
- Minimum release age is the single highest-leverage 2026 setting if you have no proxy registry. Every major package manager now supports refusing to install package versions younger than a configurable threshold. Every malicious release we covered above was yanked inside 48 hours; a 2-day gate would have turned all of them into non-events for any team that had it on: - # npm 11+ npm config set min-release-age 2 # pnpm 10+ — value in minutes (writes to .npmrc) pnpm config set minimumReleaseAge 2880 # Yarn Berry v4.10+ — value in minutes (writes to .yarnrc.yml) yarn config set npmMinimalAgeGate 2880- Bun 1.3+ supports the same setting via - bunfig.toml(value in seconds):- [install] minimumReleaseAge = 172800- The setting gates lockfile updates, not - npm ci. A developer running- npm install <new-pkg>with- min-release-age 2cannot pull a brand-new malicious version into the lockfile, so it never reaches CI.- npm cithen installs the same vetted lockfile deterministically as before — no network-age check on already-pinned versions. The two settings compose:- min-release-agekeeps the lockfile clean;- npm cienforces it. Configure both on developer machines and CI, so a manual- npm installon a runner can’t bypass it either.- The exception list ( - minimumReleaseAgeExcludein pnpm,- npmPreapprovedPackagesin Yarn) is for internal packages you publish yourself and need to consume immediately. Add to it sparingly.
- FIDO2 doesn’t help against the TanStack attack vector, but it would have made the Axios social-engineering chain noticeably harder. Phishing defeats SMS and TOTP. It does not defeat FIDO2. 
CI/CD hardening
The TanStack incident forced the industry to take this aspect of its security seriously.
- Internal proxy registry (Verdaccio is free; Artifactory and Nexus for enterprise). One chokepoint for every install, with rules. If you already set a minimum release age on every developer machine and CI runner, the proxy is no longer the only way to enforce the quarantine — but it stays the better answer for revoking compromised versions retroactively across the org.
- 24 to 48 hour quarantine on fresh upstream versions, either at the
proxy (preferred for enforceability) or via the per-tool
min-release-age/minimumReleaseAge/npmMinimalAgeGatesettings above. Most malicious releases live and die inside that window.
- OIDC Trusted Publishing for every publish workflow. Removes long-lived npm tokens from CI secrets, full stop. Combine with the next point.
- Lock down GitHub Actions. Never check out PR head code in a
pull_request_targetworkflow. Pin Actions by commit SHA, not by floating tag. Audit who can write to the Actions cache and what those cache entries are allowed to touch.
- Behaviour-analysis scanners — Socket, Endor Labs, StepSecurity.
Their free tiers detect postinstallpatterns and suspicious lifecycle behaviour before any advisory exists, which is somethingnpm auditsimply cannot do.
- SBOM per build, diffed daily. A new transitive package, or one that silently changed maintainer, will show up in the diff before it ever executes anywhere.
AI assistant protection
The Bitwarden Wave-3 payload established this as its own category. Most organisations have no policy here today — that is likely to change in 2026. At minimum:
- Treat AI assistants as privileged identities. Rotate their API tokens
on the same cadence as service-account credentials. Don’t store them
long-lived in ~/.claude.jsonif you don’t have to.
- Source-control assistant configuration (CLAUDE.md,.cursor/rules,copilot-instructions.md) and review changes to those files in PRs, the same way you review code.
- Sandbox tool execution. No arbitrary shell without explicit human confirmation.
- Audit assistant tool calls. Log what the assistant ran, not just what the human typed at the prompt.
If you’d like a deeper walk-through, our team is happy to help. Get in touch via the contact page, or watch the full webinar at the top of this post.
Read about other interesting topics on our blog.

---
*检索时间: 2026-07-24 21:29:49*
*搜索来源: DuckDuckGo*
