# Nobody was checking the drives that encrypt your laptop

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/21/hdd-self-encrypting-drive-security/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
Nobody was checking the drives that encrypt your laptop
A drive ships with a label promising hardware encryption. You plug it in, set a password, and trust the chip inside to handle the rest. Millions of laptops and workstations run this way, on solid-state drives built to the TCG Opal2 standard.
Milan Brož and three colleagues bought 38 of those drives and ran them through a test bench. Brož maintains cryptsetup, the tool that configures disk encryption on most Linux systems. The drives came from Samsung, Western Digital, Micron, Kioxia, and others, a mix of new stock and secondhand units pulled from laptops. The team treated each one as a black box and sent it only the commands the Opal2 documentation defines.
Several drives failed on basic points.
What the drives got wrong
Two Lenovo OEM drives encrypt every sector with the same tweak value. AES-XTS relies on that value to make identical data look different depending on where it sits on the disk. With one value across the whole drive, identical content written to two locations produces identical ciphertext. A pattern in your files survives into the encrypted data.
The same two drives ship a random number generator that returns a predictable counting sequence on every call. A SanDisk SATA drive leans toward one byte value, 0x8B. The drive emits it roughly double the expected frequency. Opal2 requires every drive to expose this generator and leaves its quality unspecified.
The tweak flaw exposes residual pattern information about data a key change was meant to erase, and the researchers rate real exploitation as very limited. The weak generator matters for software that pulls keys from it, and the team searched for a product that does and came up empty. The encryption key itself lives on the drive and stays there.
The reset tokens have their own problem. Every Opal2 drive carries a PSID, a code printed on the label that wipes the drive back to factory state. One batch of SanDisk drives generated those codes in sequence, sharing a prefix and a suffix. Recovering one drive’s PSID hands you its neighbors’ by counting up. Six other drives accept any garbage appended to a valid PSID and treat it as correct.
Vendors buy hardware encryption, and no one checks it
Companies deploy Opal2 drives to satisfy a data-at-rest requirement. A purchasing officer sees “hardware encryption” on a spec sheet and marks the box. The gap between that label and the chip’s behavior went years unmeasured by any independent party.
This is the first cross-vendor security comparison of Opal2 drives. The last major public work on self-encrypting SSDs landed in 2019. The Samsung generator bias sat undetected across a drive that researchers had already reverse-engineered. The method that surfaced all of it: buy used SSDs and run a script.
The marketing muddies things further. The team began with more than fifty drives and set aside a dozen that support only Pyrite2, a related standard that checks a password and leaves the data in plaintext. Vendors sell those drives with hardware encryption in the copy.
The disclosure went nowhere
Brož and his team reported every security issue to the affected vendors. Micron shipped a firmware fix for a sector-size bug on its Crucial T500. Every other report came back as already known and unpatched, out of support, or met with silence. Several vendors answer broken encryption firmware by marking the feature dead and pointing customers to software encryption.
Firmware updates stay hard to get. Many require a vendor’s Windows-only tool or a bootable image. The Linux Vendor Firmware Service covers a slice of OEM drives, and the rest depend on whichever support site still exists.
What got fixed
The project shipped code. Opal2 support landed in cryptsetup. Single-user mode is staged for a coming release, along with the Linux kernel changes it needs. The team released the Opal Test Suite so anyone can point the same checks at their own drives.
Three of the tested drives turned out unusable for real disk encryption. Single-user mode, the feature that keeps a drive administrator from unlocking a user’s data, tells a similar story. Twenty-four drives advertise it. Fourteen support it well enough to use.
Cryptsetup now checks a drive’s single-user-mode firmware before trusting it and drops to a safer configuration when the check fails. The practical guidance runs opposite to the original sales pitch. Layer software encryption over the drive’s own, and let the hardware serve as a second wall.
A drive that claims to encrypt your data deserves the same scrutiny as any other security control. The tools to apply that scrutiny are open source now, and the first pass through them found broken firmware in production on machines storing real data.
Download: The ultimate guide to network operations management

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
