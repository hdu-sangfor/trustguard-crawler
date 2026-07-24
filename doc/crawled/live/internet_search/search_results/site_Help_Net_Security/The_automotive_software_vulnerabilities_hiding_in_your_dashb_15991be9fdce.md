# The automotive software vulnerabilities hiding in your dashboard

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/24/car-research-automotive-software-vulnerabilities/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
The automotive software vulnerabilities hiding in your dashboard
Pop the hood on a new car and you won’t find much you can fix with a wrench. What you’ll find is software, and a lot of it. The screen in the dash probably runs Android or a flavor of Linux. The system watching the road for you might run QNX or VxWorks, the same kind of code that flies aircraft and runs factory floors.
Carmakers spent the last decade making this switch, and it bought them app stores, wireless updates, and quicker release cycles. It also handed them something less welcome: every old, publicly documented bug those platforms have collected over the years.
Researchers at Télécom SudParis decided to count that baggage. They built a scanner called VERA, aimed it at the operating systems inside current cars, and tallied up the known flaws. The pile is big. It’s also messier than the raw numbers make it look, which turns out to be the more interesting part of the story.
What’s running in your car?
First, the researchers worked out who runs what, which is harder than it sounds because carmakers treat this stuff as a trade secret. A 2023 BMW dashboard runs a Qualcomm chip loaded with Automotive Grade Linux and Android. GM and Cadillac are moving to Red Hat’s in-vehicle OS for their 2026 models. Tesla has quietly run Linux for years. Line it all up and the fleet starts to look like a rolling collection of general-purpose computers, plugged into cellular, Wi-Fi, Bluetooth, and the car’s own internal wiring.
Then they scanned it. The counts landed all over the map. Automotive Grade Linux topped the chart with 1,203 documented flaws in the version they tested. Android wasn’t far off. A leaner, safety-focused stack called Eclipse S-CORE came in with a grand total of eight. Part of that gap is just how much extra software each platform ships. Part of it is attention: popular open platforms get poked at by more researchers, so more of their flaws end up on the books. Getting looked at is its own kind of exposure.
Certified doesn’t mean bulletproof
You might expect the safety-certified systems to come out clean. They don’t. QNX Neutrino carries a respected security certification, and the tested build still logged 56 known vulnerabilities. VxWorks 7 sits at an even higher certification tier and landed in the low dozens.
Certification does real work here. It shrinks the attack surface and forces discipline into how the code gets built. What it can’t do is stop the mountain of surrounding software from sprouting new bugs that somebody has to patch.
A big number is a to-do list, not a verdict
This is where the study gets honest with itself, and where a lot of scary headlines fall apart. A logged vulnerability is a maybe. It’s a weakness that could matter under the right conditions, if the vulnerable code is even switched on, if the attacker can reach it, if the setup happens to line up. A thousand flaws means a thousand things a defender has to keep an eye on. It doesn’t mean a thousand ways into the car.
To show the difference, the team built two working attacks. One went after a bug in SQLite, a database engine buried inside all sorts of apps, running on Android Automotive. The other targeted a service discovery protocol called SOME/IP, and this one tells the whole story in miniature.
They ran the same attack against three platforms. It worked on Red Hat’s AutoSD and on Tesla’s software, letting them knock a service offline. It flopped on Android Automotive, which the researchers figure was down to the platform shuffling its port numbers around. One bug, three systems, two very different afternoons. Same severity score on paper, and the outcome came down to what defenses were actually turned on.
All of this ran inside Docker containers on a lab bench, picked because they’re easy to reproduce. That setup nails the filesystem, the installed packages, the config. It skips the vendor’s custom kernel, the firmware quirks, the hardware protections. The numbers describe what’s sitting in the software image. They stop short of what happens in a car parked in your driveway.
The scanners have a car problem
There’s a working-stiff angle here too. The everyday scanners security folks reach for assume a tidy system with a clean inventory of parts. Cars don’t play along. Trivy, one of the popular ones, coughed up more than a thousand false alarms on a single robotics image and barely anything useful on others. VERA sits on top of the existing tools and filters for the automotive reality, tossing out flaws in command-line utilities and developer tools that a locked-down car would never expose in the first place. What you get back is shorter and sharper, a list somebody can actually work through instead of drown in.
So, here’s what to walk away with. The code in your car now shares a family tree, and a rap sheet, with the rest of the computing world. The length of that rap sheet tells you how much there is to watch. The real job is sorting out which of those old bugs your particular car will ever let anyone near.
Download: The ultimate guide to network operations management

---
*爬取时间: 2026-07-24 15:54:00*
*来源: 直接站点爬取*
