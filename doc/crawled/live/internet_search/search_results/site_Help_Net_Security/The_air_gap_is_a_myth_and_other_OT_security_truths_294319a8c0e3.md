# The air gap is a myth and other OT security truths

### 来源信息
- **URL**: https://www.helpnetsecurity.com/2026/07/21/benjamin-bachmann-bilfinger-ot-security/
- **来源站点**: Help Net Security
- **页面抓取**: 成功

### 页面正文
The air gap is a myth and other OT security truths
Benjamin Bachmann, Director Group Information Security at Bilfinger, speaks with Help Net Security about defending industrial plants. He explains why attackers want to control operations instead of stealing data, and why the air gap is mostly a myth.
Bachmann covers how containment plans get negotiated before an incident, how to build visibility on old equipment through network monitoring, and how ransomware crews price their demands on downtime. He also questions the idea that people are the weakest link in OT security.
When you walk an executive who has never set foot in a plant through your threat model, what is the one misconception you find yourself dismantling first?
That the attacker wants our data. Most executives come from a world where a breach means stolen files, and that mental model is hard to shake. But nobody breaks into an industrial environment to read the recipe for district heating. They want the button that makes things stop.
Once you reframe the threat model from “someone steals our secrets” to “someone else is operating your plant,” the conversation changes completely. Suddenly availability and physics are on the table. At Bilfinger, we operate in highly sensitive environments like refineries, chemical plants, and energy infrastructure, where this shift in perspective helps to prioritize investments where they have the most impact on resilience.
The second misconception usually dies on the same walk: “But it’s all air-gapped, right?” The air gap is the unicorn of industrial security. Everyone has heard of it; nobody has actually seen one in the wild. It typically survives until the first cabinet with a forgotten LTE dongle in it.
Engineers optimize for uptime and safety. Security teams optimize for containment. When those instincts pull against each other during a live incident, who wins in your organization, and how did you arrive at that answer?
I push back on the premise. Containment is not my goal, it is my method. The goal is the same one the engineers have: a plant that runs safely. The moment security becomes the department that stops production, I have turned myself into a second incident.
So, the honest answer is: nobody has the upper hand in this scenario at 3 a.m., because we refuse to have it at 3 a.m. Whoever “wins” a live incident won it years earlier. Plant state belongs to the people who understand the process. Network state belongs to my team. And the trigger points where one touches the other (which zone gets isolated, under which conditions, at what cost per hour) are negotiated in daylight, written down, and exercised. An incident is a terrible moment for an org chart debate.
There is also a tactical reason for this. If my containment plan requires halting production, an attacker no longer needs to break the plant. They just need to trigger my plan. A security team that can only respond by pulling the plug is not a defense. It is a free denial-of-service button. That realization shaped the architecture: containment has to be cheap enough that nobody ever has to choose between safety, uptime, and defense.
A lot of legacy equipment was never designed to authenticate anything or log anything. How do you build defensible visibility on top of protocols that predate the concept of a threat actor?
I stopped expecting the devices to testify and started treating the network as the witness. A controller from 1998 was never designed to tell you what happened. But it never lies on its own. If it starts lying, someone taught it to. It does exactly one thing, in the same rhythm, for decades. People frame that as legacy debt. I frame it as the most underrated security feature in industrial environments.
IT traffic is chaos. People browse, update, stream, join video calls. OT traffic is choreography. The same devices, the same conversations, the same cadence, every day outside of maintenance windows. Against chaos, an anomaly is a needle in a haystack. Against choreography, it is a stranger on the dance floor.
So, visibility gets built around the equipment, not on it: passive listening at a few choke points, segmentation strict enough that those choke points see every conversation that crosses a zone boundary, and a baseline that someone genuinely maintains. That last part matters, because visibility has quietly become a product category, and a sensor nobody baselines is just a screensaver with a license fee.
And note the word in the question: defensible. Defensible does not mean you saw everything. It means that when something happens, you can state with confidence what normal looked like, when it stopped, and what was within reach. That is a sentence you can defend in front of a board, a regulator, or an insurer. “We had a dashboard” is not.
Ransomware crews have learned that halting production is more lucrative than encrypting files. How has extortion against physical operations changed your calculus on segmentation and recovery?
It forced us to look closely at the economic calculation behind these attacks. Cybercriminals calculate the exact cost of operational downtime to set their demands. This means our defense strategy cannot just be about building higher walls, it must focus on disrupting their business model by making downtime as short and manageable as possible.
Once you see it that way, segmentation and recovery stop being two separate disciplines and become one question: how fast does this operation get back to a safe state without paying anyone? Segmentation defines how much of the plant can restart independently of the compromised part. Recovery defines how fast that restart actually happens, which is why we rehearse restarts, not restores. Engineering workstations, project files, controller configurations, held offline and tested.
The capability that matters most here is degraded operation. Waiting for a forensically perfect network before restarting is exactly the delay the extortion is priced on. An operation that can run safely at partial capacity while the rest is cleaned up has taken the leverage out of the negotiation.
What is a widely repeated piece of OT security advice that you think is quietly wrong?
“The human is the weakest link, so invest in awareness.” It sounds humble, it fits on a slide, and it is quietly wrong. If clicking a link can stop a turbine, the problem is not the click. It is an architecture that lets a click reach a turbine.
I sum this up as “trust is not a control”. People are part of the system, not the threat inside it, and systems get engineered. In practice, that means I stopped caring about phishing click rates and started caring about paths from a click to a controller. One number describes people. The other describes the system. Only one of them is mine to fix.
Runner-up: “Never touch OT, you will break it.” Repeat that for 20 years and it becomes “never secure OT”. Caution is a virtue. Paralysis just likes to dress up as one.
Download: The ultimate guide to network operations management

---
*爬取时间: 2026-07-24 21:48:32*
*来源: 直接站点爬取*
