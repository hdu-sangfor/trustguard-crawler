# Europe's Multilingual Reality Exposes AI Security Gaps

### 来源信息
- **URL**: https://www.darkreading.com/cybersecurity-operations/europes-multilingual-reality-exposes-ai-security-gaps
- **来源站点**: Dark Reading
- **页面抓取**: 成功

### 页面正文
Breaking cybersecurity news, news analysis, commentary, and other content from around the world, with an initial focus on the Middle East & Africa, the Asia Pacific, Europe, and Latin America.
Europe's Multilingual Reality Exposes AI Security Gaps
The AI security layer and guardrails for many AI products don't evenly protect against jailbreaking and unsafe actions in every single language.
Not all languages are treated equally when it comes to AI model function and safety, and European organizations face a particular risk when it comes to this reality.
The modern large language model (LLM) ecosystem relies heavily on natural language, whether a user is speaking to a chatbot, issuing specific instructions for software development, generating emails, or performing large-scale data analysis. This reliance is further illustrated through the wide range of prompt injection attacks that rely on language-based trickery.
While leading models can process text in dozens to hundreds of languages, performance and safety capabilities vary dramatically between languages.
Many of the less-supported languages, such as Welsh and Swahili, can answer only basic prompts and may make grammatical errors. Mainstream models like OpenAI's GPT, Google's Gemini, and Anthropic's Claude demonstrate strong performance in around 30 to 40 languages such as English, Arabic, Spanish, French, German, Japanese, Simplified Chinese, and Hindi.
English is by far the language best supported by many AI models. English benefits both from disproportionate training data and from tokenization schemes that often represent English more efficiently than many other languages.
Academic research shows that many LLMs perform logic, reasoning, coding, and math tasks best when prompted in English language, and many major AI labs conduct safety tuning, behavior alignment, and reinforcement using English-speaking annotators.
There are exceptions to this rule. Chinese models like Qwen and DeepSeek outperform Western models when handling Chinese text and cultural context, and certain initiatives are in place to further support languages in Europe and the Middle East. But it would not be a stretch to call the modern AI landscape English-centric.
From a global perspective, this is not just a comprehension or AI function problem but a security issue as well. On July 22, AI security vendor DeepKeep published a blog post titled, "Your AI Speaks 100 Languages. Your AI Security Layer Doesn't."
As DeepKeep explained, the AI security layer and guardrails that exist on top of so many AI products don't necessarily protect against jailbreaking and unsafe actions equally in every single language.
"Security intent can shift during translation. A jailbreak may become less explicit. A prompt injection may lose some of its command structure," the blog post read. "A culturally specific phrase may be flattened into harmless text. A sensitive term may be translated poorly or mapped into language that no longer matches the security policy. Mixed-language inputs can preserve the malicious instruction in one language while surrounding it with benign context in another."
This becomes particularly problematic when many organizations collaborate and use AI tools across multiple languages. This is the case at any globally operating company, but particularly one based somewhere like Europe, Asia, or Africa.
Europe provides one of the clearest examples of the challenges described. Yossi Altevet, chief technology officer (CTO) and co-founder at AI security vendor DeepKeep, tells Dark Reading that dozens of languages sit inside one regulatory and economic bloc, and cross-border operations are the norm rather than the exception.
"That density means Europe is more exposed by design, simply because the odds of hitting a language gap in daily operations are so much higher," he says. "Every multilingual enterprise, anywhere, carries the same underlying risk the moment it processes a non-English prompt."
The Unique Place Europe Sits In
The European Union recognizes 24 official languages, and there are many more regional and minority languages an employee could easily use predominantly.
Paolo Palumbo, VP of strategic threat intelligence and research for WithSecure (a vendor that specializes in European cybersecurity), tells Dark Reading that Europe is not uniquely affected by the security and safety inconsistencies across lower-resourced AI languages, but Europe faces a particularly complex operational challenge "because organizations commonly deploy the same product across multiple linguistic and environments."
"A product may appear to converse competently in a particular language even though its moderation, prompt-injection detection, data-loss prevention, or incident-monitoring controls have not been validated to the same standard in that language," he says.
Palumbo says multilingual security could become an overlooked part of AI governance, and argues organizations should require evidence of multilingual safety from vendors, rather than inferring it from claims of support.
"The EU AI Act does not impose a general requirement that every AI product must achieve identical safety performance in every supported language, and an ordinary chatbot is not automatically a high-risk system," he explains. "For high-risk systems, however, the act requires continuous risk management and appropriate levels of accuracy, robustness, and cybersecurity throughout the system's life cycle. Providers must also address foreseeable misuse and test whether the measures they have implemented are effective. Where linguistic differences materially affect those controls, language-specific testing may become part of the evidence needed to demonstrate compliance."
In DeepKeep's benchmark testing, German, Spanish, French, and Italian all showed meaningful accuracy drops for translation-based personally identifiable information (PII) detection compared to native language analysis. "Europe's multilingual reality just means this gap gets exposed constantly, across nearly every one of its major markets at once," Altevet adds.
That being said, Europe has some advantages over other parts of the world in this respect. Filip Mazán, senior manager of AI research at ESET, points out that many European languages share similarities.
"English and German, for example, have overlapping vocabulary, and large language models can often leverage that common ground. The same applies to many Slavic languages, which share linguistic structures and vocabulary," he says.
The Security Question Behind Multilingual AI Support
One must distinguish between language capability, safety alignment, and downstream security controls, which may not perform equally across languages, even when the model itself appears highly capable. In other words, even if a model speaks and understands German or Spanish well, it does not mean security guardrails will necessarily perform equally as well.
Altevet explains that the risks behind AI multi-language support are not theoretical; attackers repeat malicious commands across multiple languages specifically to slip past filters tuned primarily for English.
The vendor cited Brown University research from 2023 and 2024, which found that OpenAI's GPT-4 provided harmful and actionable responses to unsafe prompts 79% of the time when translated into low-resource languages. The original English prompts generated similar harmful responses less than 1% of the time.
Pete Bryan, technical lead of Microsoft's AI red team, tells Dark Reading that the tech giant has been testing its AI systems for years across a range of different languages specifically because "model safety and behavioral profile can change depending on the language it is prompted in, as well as which it responds in."
"Language is just one dimension of the safety story, and a safe response for a user in a particular language may be unsafe in the same language if that user is in a different cultural context — for example an American in California speaking Korean versus a Korean in Seoul speaking Korean," he says.
Similarly, major AI vendors like OpenAI, Anthropic, and Google also test their models against multilingual issues, though the battle continues.
Addressing Multilingual AI Issues
There are different ways organizations attempt to address the issues posed by multilingual inconsistencies across LLMs in Europe and beyond.
A standard option is translation-first security filtering, where an organization's security layer translates content into English, applies guardrails, and chooses whether to allow or block the output. There are also native language guardrails, where instead of translating everything into English, the security layer evaluates prompts and meaning in the original language.
Vendors like DeepKeep and Lakera advertise this capability as superior to the blind spots introduced by translation-based guardrails, as intent is accounted for and policy is, ideally, better preserved.
Many AI-focused red teaming firms offer multilingual evaluation. Microsoft's internal AI Red Team tests across multiple languages, different modalities including text and audio, as well as the various cultural contexts that come with different languages.
"We aren't just doing direct translation of English to another language in our scenarios. In addition, we often mix and combine languages in order to test systems, with scenarios incorporating multiple languages at once to see what effect that may have on the safety of the systems under test," he says.
Finally, runtime AI firewalls and policy enforcement tools cover the bigger risks posed by threat actors. AI firewalls block suspicious tool calls, prevent sensitive data exfiltration, attempt to block prompt-injected actions, and log suspicious incidents for investigation.

---
*爬取时间: 2026-07-24 21:42:39*
*来源: 直接站点爬取*
