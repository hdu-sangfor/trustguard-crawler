# TrickBot Ditches HTTP for DNS Tunneling in Latest Variant

### 来源信息
- **URL**: https://www.infosecurity-magazine.com/news/trickbot-dns-tunneling-c2/
- **来源站点**: Infosecurity Magazine
- **页面抓取**: 成功

### 页面正文
A TrickBot variant has been observed swapping the HTTP command-and-control (C2) channel the malware has used for the better part of a decade for a bespoke DNS tunneling scheme that hides beacons and payloads inside malformed DNS queries.
According to new research from Fortinet's FortiGuard Labs published on July 22, the samples reveal a modular architecture consistent with earlier TrickBot campaigns but with the transport layer redesigned around encrypted data smuggled through DNS packets to a public resolver.
The redesign is significant given the family's history. Microsoft coordinated a court-ordered takedown of the TrickBot botnet in 2020 after infections exceeded one million devices, and public reporting had largely written the family off. This variant shows operators still iterating on the platform.
John Bambenek, president at cybersecurity consultancy Bambenek Consulting, said the malware family's survival came down to operator adaptation.
"TrickBot has been a long-running malware family that has survived because the adversary adapts," he said, adding that passive DNS analysis of the C2 identified in the report showed extensive exploitation activity and reinforced the case for enterprises controlling their own DNS resolution.
Encoded Commands Inside DNS Queries
Once launched, the malware disguised outbound C2 messages as ordinary domain-name lookups and read the responses back from what looked like ordinary IP addresses.
The outbound channel encrypted each command with a single-byte XOR key, hex-encoded the result, then broke it into 63-character chunks separated by periods to mimic a valid domain, before prepending the whole string to a hardcoded C2 domain.
Three packet types carried the traffic: 0x30 for command requests, 0x31 for size queries and 0x32 for response data.
Inbound traffic exploited the DNS specification's allowance for multiple IPv4 addresses per reply. TrickBot treated the first byte of each returned "address" as an ordering index so it could re-sort the resolver's shuffled reply, and read the remaining three bytes as raw payload.
FortiGuard measured throughput at around 30.7 KB per second in its lab, moving a 1.2 MB file in 40 seconds.
Persistence and Modular Execution
Persistence relied on the Windows Task Scheduler. TrickBot generated a task name by combining a randomly picked %AppData% folder name, the string "autoupdate #" and a random number, producing entries such as "Wireshark autoupdate #72784" that ran every five minutes.
It stored the task name and executable path in two NTFS Alternate Data Streams (ADS) so subsequent executions rebuilt the same scheduled task rather than creating duplicates.
Command handling stayed close to the HTTP-era design. FortiGuard documented 12 response commands, including downloading and executing EXE modules, running DLLs through rundll32.exe, injecting into processes via process hollowing or process doppelganging, executing PowerShell through anonymous pipes to cmd.exe and running raw shellcode in memory.
Runtime-decrypted strings and hash-based Windows API resolution were designed to defeat static analysis. The DNS tunneling shift preserved the modular capabilities that have made TrickBot a persistent threat.

---
*爬取时间: 2026-07-24 15:48:24*
*来源: 直接站点爬取*
