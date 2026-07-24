# Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's ServersJul 24, 2026Vulnerability / Web Securit

### 来源信息
- **URL**: https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
- **来源站点**: The Hacker News
- **页面抓取**: 成功

### 页面正文
A crafted SVG submitted to Bing's image search ran commands as NT AUTHORITY\SYSTEM on Microsoft's production image-processing workers, and as root on the Linux machines in the same fleet.
XBOW's testing got the same result on workers across different hosts and network ranges, so the problem sat in Bing's image tier, not on one bad machine. Microsoft issued two critical CVEs, CVE-2026-32194 and CVE-2026-32191, and rated both 9.8 on the CVSS scale.
XBOW, the autonomous offensive security startup, found both and reported them privately. Bing users have no patch or mitigation to apply: Microsoft fixed both server-side before the advisories went out in March, and the records state there is "no customer action to resolve."
Neither advisory recorded exploitation or public disclosure when they went up on March 19. XBOW published the exploit mechanics on July 23, after holding them back at Microsoft's request until the remediation had landed.
What outlives the fix is the shape of the bug. The application believed it was handling an image; the helper underneath read part of that image as a command.
If your own stack pipes uploads or server-fetched URLs through ImageMagick or anything ImageMagick-compatible, your exposure turns on whether attacker-controlled content can still reach a delegate-enabled path. Deny the delegates, cut the formats you accept, and keep the worker off the network, and the same SVG does nothing.
Bing's reverse image search fetches an image URL from the backend, because that is what the feature does. On its own, that is a blind SSRF: nothing comes back to the client. The tell was the error. Some workers returned a 500 to the browser and still fetched and parsed what they retrieved, which pointed at something downstream doing the parsing.
SVG answered that question. It is XML, not pixels: it can reference other images, and a renderer that follows those references goes and gets them. Underneath, conversion suites hand formats they do not process themselves to a delegate, an external program invoked through a shell.
On the path XBOW reached, that layer was still enabled, so an image reference beginning with a pipe character went to the shell rather than being read as a filename. The payload was a one-pixel SVG whose reference ran a command on the worker and curled the output back to a collector XBOW controlled.
That gave two routes into the same conversion tier and two CVEs.
- CVE-2026-32194, filed as command injection under CWE-77, is the public "Search by Image" upload, with the SVG going in base64 as the imageBinfield to/images/kblob.
- CVE-2026-32191, filed as OS command injection under CWE-78, is the crawler route: host the SVG anywhere, hand its URL to the search through the imgurlparameter, andbingbot/2.0fetches it into the same pipeline. Neither needs authentication, cookies, session state or a click.
The Hacker News checked both CVE records on July 24. Both still carry Microsoft's March status of no public disclosure, which XBOW's writeup has overtaken, and Microsoft still lists them as not exploited.
The proof had to come out of band. The frontend could return an error while the worker executed anyway. Linux workers returned uid=0 and gid=0. On Windows, systeminfo named Windows Server 2022 Datacenter, whoami /all showed SeImpersonatePrivilege and SeDebugPrivilege enabled, and directory listings put execution inside Bing's multimedia image-processing components. The firm says it ran only benign read-only commands and touched no customer data.
Narrowing it to that path took dozens of probes. ImageMagick pseudo-protocols came back differently depending on the coder: label: rendered text and xc: produced a color image, while text:, caption: and direct file reads failed. Shell metacharacters inside label: rendered as text rather than executing, which ruled that coder out. The path that did reach a delegate was the image reference inside the SVG itself.
Turn the delegates off
An image-processing worker handling untrusted files should not reach a shell, run as SYSTEM, or have a way out to the internet. Bing's pipeline did all three.
ImageMagick's own guidance is explicit that the default policy is open and meant for sandboxed or firewalled use, not a public website. For anything touching untrusted images, deny delegates outright in policy.xml:
<policy domain="delegate" rights="none" pattern="*" />
Then, in order of what buys you most:
- Cut the formats you accept. SVG, MVG and EPS are among those that carry references and interpreters.
- Review delegates.xmland disable anything enabled that you do not need.
- Run conversion sandboxed and with reduced privileges.
- Block outbound network from the worker, which is the leg that turned a blind bug into a proven one.
- Allowlist the destinations a server-side fetch may reach, and keep the worker off internal addresses.
ImageMagick's guidance is to test after any policy change, and magick identify -list policy prints what is actually loaded.
ImageTragick, the 2016 delegate command injection tracked as CVE-2016-3714, is the same class of failure, and it keeps resurfacing because nobody counts the converter as part of the attack surface. XBOW CISO Nico Waisman, who wrote the disclosure, put it this way: "Applications treat image helpers as plumbing. Attackers treat them as parsers."
The fetch was reachable, returned nothing, and looked like a dead end. What turned it into a SYSTEM shell was the parser behind it, and nothing in the response would have told you so.

---
*爬取时间: 2026-07-24 21:40:12*
*来源: 直接站点爬取*
