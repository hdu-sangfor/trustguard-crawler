# Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac FilesJul 23, 2026Vulnerability / Application Securit

### 来源信息
- **URL**: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
Cybersecurity researchers have uncovered a sandbox escape vulnerability in Anthropic's Claude Cowork that makes it possible to break out of the confines of a Linux virtual machine (VM) within which the agent runs to read or write files anywhere on the Mac.
Accomplish AI, which shared details of the vulnerability with The Hacker News ahead of publication, said about 500,000 macOS users running local Cowork sessions were affected prior to it being patched. It has been codenamed SharedRoot.
"We connected a folder to a fresh Claude Cowork session, sent one short message, and watched the agent escape the sandbox," Oren Yomtov, principal security researcher at Accomplish AI, said. "From inside the VM, it reached the host Mac and read and wrote files all over it, far outside the folder we'd connected, with no permission prompt anywhere."
With this level of access, the agent can access any data stored on the Mac via the user's account, including SSH keys, cloud credentials, and other valuable information.
Following responsible disclosure, Anthropic closed the report as informative without issuing a fix. That said, the latest version of Cowork defaults to cloud execution, which addresses the issue. But users who opt to run the agent locally are still exposed to the problem.
Claude Cowork's macOS desktop app runs as the user who is logged into the system. The actual agent-related work, on the other hand, happens in a Linux VM created via Apple's Virtualization framework. Every session gets its own disposable unprivileged user, along with a Secure Computing Mode (seccomp) filter for application sandboxing. The folders connected by the user are shared into the VM by a root daemon called coworkd.
"One detail matters more than the rest: the host filesystem gets shared into that VM read-write," Yomtov explained. "The entire host '/,' mounted so that only guest-root inside the VM can see it, at /mnt/.virtiofs-root."
Because the entire host file system is mounted into the agent's VM with read-write privileges, any path to guest-root can grant the agent access to the underlying host, effectively escaping the sandbox.
This involves loading the Linux kernel's "act_pedit" Traffic Control (tc) packet editing subsystem into an unprivileged user namespace and exploiting CVE-2026-46331 in the guest kernel, a recently disclosed flaw called pedit COW, to obtain guest-root. From there, the agent can access the whole host ("/") with elevated privileges, allowing it to read or write files from and to the Mac's file system as the logged-in desktop user.
Or Hiltch, co-founder and CTO of Accomplish AI, told The Hacker News that creating user and network namespaces gives the session CAP_NET_ADMIN within its private network namespace, allowing it to perform various network-related operations.
"That capability provides access to the vulnerable tc/act_pedit kernel path used by pedit COW," Hiltch added. "The namespaces are not the exploit; they make its normally privileged prerequisite available to an ordinary user."
The development assumes significance in the face of revelations that OpenAI's models managed to break out of its sandboxed environment during a security test that resulted in the breach of Hugging Face's production infrastructure in their quest to cheat the ExploitGym benchmark they were being graded on.
"act_pedit is one bug in a category," Yomtov said. "The Linux net/sched subsystem throws off this exact shape of privilege escalation on a regular cadence: an autoloadable module, a config path an unprivileged user can reach, a memory bug at the end of it. Patch this one and you've fixed this one. The chain re-arms on the next one, with everything above the kernel untouched."
"And the next one is always coming. At any given moment there's likely a privilege-escalation bug it's still exposed to, sometimes fixed upstream but not yet in your image, sometimes not yet fixed anywhere, with a working exploit out within hours. This isn't a patch-faster problem. You're structurally one bug behind, all the time."
To mitigate the threat, it's essential to disable unprivileged user namespaces, avoid making the seccomp filter overly permissive, stop autoloading of modules, and restrict sharing of the whole host into the VM.
"Scope it to the folders that were actually connected instead of all of /, or at least mount it read-only, and run coworkd with ProtectSystem=strict in its own mount namespace so it isn't re-execing binaries a session user can poison," Accomplish said. "Then even a full guest-root has nothing to land on, the last two steps of the chain have nowhere to go."

---
*爬取时间: 2026-07-24 15:42:35*
*来源: 直接站点爬取*
