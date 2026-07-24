# How Quantum Computing Affects Cryptography

### 来源信息
- **URL**: https://thequantuminsider.com/2026/04/06/how-quantum-computing-affects-cryptography/
- **域名**: thequantuminsider.com
- **检索关键词**: quantum computing cryptography threat
- **页面抓取**: 成功

### 搜索摘要
April 6, 2026 - Quantum computing poses a fundamental threat to widely used encryption systems including RSA, elliptic curve cryptography, and Diffie-Hellman key exchange, which secure everything from online banking to government communications, with algorithms ...

### 页面正文
Insider Brief
- Quantum computing poses a fundamental threat to widely used encryption systems including RSA, elliptic curve cryptography, and Diffie-Hellman key exchange, which secure everything from online banking to government communications, with algorithms like Shor’s algorithm capable of breaking these schemes exponentially faster than classical computers.
- The National Institute of Standards and Technology (NIST) has standardized post-quantum cryptographic algorithms designed to resist quantum attacks, and organizations worldwide are beginning the complex process of migrating critical systems to these new encryption methods.
- The “harvest now, decrypt later” threat – where adversaries collect encrypted data today to decrypt once quantum computers become available – creates urgency for organizations handling sensitive long-term data, even though large-scale quantum computers capable of breaking encryption remain years away.
- The cryptographic landscape is splitting between post-quantum cryptography (mathematical algorithms resistant to quantum attacks) and quantum key distribution (physics-based security using quantum networking), with governments, financial institutions, and technology companies investing billions in both approaches.
The relationship between quantum computing and cryptography represents one of the most consequential technological races of the coming decade. On one side stands the promise of quantum computers powerful enough to break the encryption protecting global commerce, government secrets, and personal privacy. On the other stands the effort to develop and deploy new cryptographic systems that can withstand quantum attacks.
Intelligence agencies are already harvesting encrypted communications with the intention of decrypting them once quantum computers become available. Governments have designated post-quantum cryptography as a national security priority. Technology companies are rewriting the cryptographic foundations of their products. Financial institutions are planning multi-year migrations to quantum-resistant systems.
The stakes are extraordinary. Modern digital infrastructure depends on encryption to secure transactions, authenticate identities, and protect sensitive information. If quantum computers can break these systems before alternatives are deployed, the consequences could range from compromised financial systems to exposed state secrets to undermined trust in digital communications.
However, the threat timeline remains uncertain. Estimates for when quantum computers will achieve the scale and reliability needed to break widely used encryption range from a decade to several decades, depending on who makes the projection and what assumptions they apply. This uncertainty creates a challenging planning problem: organizations must invest in quantum-resistant cryptography without knowing precisely when quantum computers will arrive or which systems will be most at risk.
What’s clear is that cryptographic transitions take years or decades to complete. Standards must be developed, software must be rewritten, hardware must be upgraded, and users must adopt new systems. The migration to quantum-resistant cryptography is already underway, driven by the knowledge that once quantum computers arrive, it will be too late to prepare.
What Is the Quantum Threat to Cryptography?
The quantum threat to cryptography stems from algorithms that quantum computers can execute exponentially faster than classical computers for specific mathematical problems. These algorithms would allow a sufficiently powerful quantum computer to break encryption schemes that currently protect sensitive data across governments, corporations, and individuals.
The threat is not that quantum computers will be better at all forms of computation. The danger lies in quantum computers’ ability to solve a narrow set of problems – specifically, factoring large numbers and computing discrete logarithms – that underpin widely used encryption systems.
Shor’s Algorithm: The Foundation of the Threat
In 1994, mathematician Peter Shor developed a quantum algorithm that can factor large numbers exponentially faster than the best-known classical algorithms. This breakthrough demonstrated that quantum computers, if built at sufficient scale, could break RSA encryption – one of the most widely used cryptographic systems in the world.
RSA encryption relies on the difficulty of factoring the product of two large prime numbers. A classical computer attempting to factor a 2048-bit RSA key would require computational resources and time scales that make the attack impractical – estimates range from thousands to millions of years using current technology, but Shor’s algorithm changes that.
Recent estimates suggest the resource requirements for breaking widely used cryptographic systems may be lower than previously thought. Earlier projections placed RSA-2048 factoring at around 20 million physical qubits on a fault-tolerant quantum computer.
More recent work has revised that significantly. A 2025 result by Craig Gidney reduced the estimate to under one million physical qubits under similar assumptions. Additional research, including work on QLDPC codes, has suggested that further optimizations could bring this number even lower in specific architectures.
Separately, Google indicated in a 2026 whitepaper that elliptic-curve cryptography (such as secp256k1) could be vulnerable with roughly 1,200 logical qubits, translating to fewer than 500,000 physical qubits on a sufficiently advanced fault-tolerant system.
Grover’s Algorithm: A More Subtle Threat
Another quantum algorithm, developed by Lov Grover in 1996, provides a quadratic speedup for searching unsorted databases. In cryptographic terms, Grover’s algorithm could accelerate brute-force attacks on symmetric encryption schemes like AES (Advanced Encryption Standard).
The impact is less severe than Shor’s algorithm. While Shor’s algorithm provides an exponential speedup (turning infeasible problems into tractable ones), Grover’s algorithm provides only a quadratic speedup. This means that doubling the key length restores security against quantum attacks.
For example, AES-128 (128-bit keys) would have roughly the security of a 64-bit key against a quantum computer running Grover’s algorithm – weak but not catastrophically broken. AES-256, by contrast, would maintain roughly 128-bit security against quantum attacks, which remains strong by current standards.
As a result, symmetric encryption can be defended against quantum computers relatively easily by increasing key lengths and continuing using existing algorithms. The real threat concentrates on asymmetric encryption – the public-key cryptography systems that underpin digital signatures, key exchange, and authentication.
| Cryptographic System | Classical Security Basis | Quantum Algorithm | Impact of Quantum Attack | 
| RSA Encryption | Factoring large numbers | Shor’s Algorithm | Exponential speedup, security completely broken | 
| Elliptic Curve Cryptography (ECC) | Discrete logarithm problem | Shor’s Algorithm | Exponential speedup, security completely broken | 
| Diffie-Hellman Key Exchange | Discrete logarithm problem | Shor’s Algorithm | Exponential speedup, security completely broken | 
| AES Symmetric Encryption | Brute-force search | Grover’s Algorithm | Quadratic speedup, mitigated by doubling key length | 
| SHA-256/SHA-3 Hashing | Collision resistance | Grover’s Algorithm | Quadratic speedup, mitigated by using longer hashes | 
The table illustrates that the quantum threat is highly asymmetric. Public-key cryptography faces an existential challenge, while symmetric encryption and hash functions require only modest adjustments to remain secure.
Which Cryptographic Systems Are Vulnerable to Quantum Attacks?
Not all encryption is equally at risk from quantum computers. The threat concentrates on specific algorithms and protocols that depend on mathematical problems quantum computers can solve efficiently.
Highly Vulnerable: Public-Key Systems
RSA encryption, used in secure email (PGP/GPG), VPNs, secure web connections (HTTPS), and software signing, is completely vulnerable to Shor’s algorithm. RSA keys of any practical length – 1024-bit, 2048-bit, or 4096-bit – can be broken by a sufficiently large quantum computer.
Elliptic Curve Cryptography (ECC), including algorithms like ECDSA (Elliptic Curve Digital Signature Algorithm) and ECDH (Elliptic Curve Diffie-Hellman), is similarly vulnerable. ECC is widely used in mobile applications, blockchain systems like Bitcoin and Ethereum, and modern TLS implementations. Shor’s algorithm breaks ECC more efficiently than RSA, requiring fewer qubits for equivalent key sizes.
Diffie-Hellman and its elliptic curve variant (ECDH), which establish shared secrets for encrypting communications, are vulnerable to quantum attacks. An adversary with a quantum computer could retroactively decrypt recorded communications by breaking the key exchange.
This retroactive decryption threat is particularly serious for protocols like TLS 1.2 and earlier, which rely entirely on Diffie-Hellman or RSA for key exchange. Even if the session encryption uses AES (which is quantum-resistant with longer keys), compromising the key exchange exposes the session keys and allows decryption of the entire communication.
Moderately Vulnerable: Symmetric Encryption and Hash Functions
AES-128 provides reduced security against quantum computers (equivalent to ~64-bit security), which is considered weak by modern standards. Organizations should migrate to AES-256, which maintains ~128-bit security against quantum attacks – still considered strong.
SHA-256 and other hash functions experience a quadratic speedup in collision attacks but remain reasonably secure. Using longer hash functions like SHA-384 or SHA-512 provides additional margin.
Real-World Impact: What Gets Broken
The concentration of vulnerabilities in public-key cryptography has wide-ranging implications:
- Online banking and e-commerce rely on HTTPS connections secured with RSA or ECC. Quantum computers could impersonate banks, intercept transactions, or steal credentials.
- Government communications protected by RSA or ECC encryption could be decrypted retroactively if adversaries record encrypted traffic today.
- Blockchain systems like Bitcoin use ECDSA for digital signatures. Quantum computers could forge signatures, allowing theft of cryptocurrency from exposed public keys.
- Software distribution depends on digital signatures to verify authenticity. Quantum computers could forge signatures, enabling malware distribution.
- VPNs and secure messaging using RSA or ECC for key establishment could be compromised, exposing corporate networks and private communications.
- PKI (Public Key Infrastructure) systems that issue digital certificates rely on RSA or ECC. Quantum computers could undermine trust in the entire certificate ecosystem.
The breadth of vulnerable systems underscores why post-quantum cryptography migration is a global infrastructure challenge, not merely a technical upgrade.
What Is Post-Quantum Cryptography?
Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to run on classical computers but resist attacks from both classical and quantum computers. Unlike quantum cryptography (which uses quantum mechanics for security), post-quantum cryptography relies on mathematical problems that researchers believe are hard for quantum computers to solve.
The goal is to replace vulnerable public-key algorithms like RSA and ECC with new algorithms that provide equivalent functionality – encryption, digital signatures, key exchange – while remaining secure against quantum attacks.
The NIST Post-Quantum Cryptography Standardization Process
In 2016, the National Institute of Standards and Technology (NIST) initiated a multi-year process to evaluate and standardize post-quantum cryptographic algorithms. After multiple rounds of evaluation, testing, and cryptanalysis involving 82 initial candidates, NIST announced the first set of standardized post-quantum algorithms in 2024:
CRYSTALS-Kyber (now standardized as ML-KEM, Module-Lattice-Based Key-Encapsulation Mechanism) for key establishment. Kyber allows two parties to securely establish a shared secret key, replacing protocols like Diffie-Hellman and RSA key exchange.
CRYSTALS-Dilithium (now standardized as ML-DSA, Module-Lattice-Based Digital Signature Algorithm) for digital signatures. Dilithium provides authentication and integrity verification, replacing RSA and ECDSA signatures.
SPHINCS+ (now standardized as SLH-DSA, Stateless Hash-Based Digital Signature Algorithm) as an alternative signature scheme based on hash functions rather than lattices, providing diversity in case lattice-based cryptography proves vulnerable.
FALCON (Fast Fourier Lattice-based Compact Signatures over NTRU) as another lattice-based signature scheme optimized for applications with size and bandwidth constraints.
These algorithms represent the first wave of standardized post-quantum cryptography. NIST continues evaluating additional candidates, particularly for specific use cases and alternative mathematical foundations.
Mathematical Foundations: Hard Problems for Quantum Computers
Post-quantum cryptographic algorithms rely on mathematical problems that appear resistant to quantum algorithms:
Lattice-based cryptography (used in Kyber, Dilithium, and FALCON) relies on the difficulty of finding short vectors in high-dimensional lattices – a problem for which no efficient quantum algorithm is known. Lattice problems have been studied extensively, and researchers believe they remain hard even for quantum computers.
Hash-based cryptography (used in SPHINCS+) derives security from the collision resistance of cryptographic hash functions. While Grover’s algorithm provides a quadratic speedup in finding collisions, using sufficiently long hashes maintains security.
Code-based cryptography relies on the difficulty of decoding random linear codes, a problem that has resisted both classical and quantum attacks for decades.
Multivariate polynomial cryptography relies on the difficulty of solving systems of multivariate polynomial equations over finite fields.
Isogeny-based cryptography uses the structure of elliptic curve isogenies, though recent cryptanalytic advances have broken some isogeny-based schemes, raising concerns about the long-term security of this approach.
The diversity of mathematical foundations is intentional. If a breakthrough algorithm emerges that breaks lattice-based cryptography, systems can fall back on hash-based or code-based alternatives.
Trade-offs: Security, Performance, and Key Sizes
Post-quantum algorithms involve trade-offs compared to current cryptographic systems. Key sizes are generally larger – while a 256-bit ECC key provides strong security today, a Kyber-768 public key uses approximately 1,184 bytes. Computational performance varies by algorithm, with Kyber and Dilithium being reasonably efficient while hash-based signatures like SPHINCS+ are slower and produce larger signatures. Signature sizes tend to be larger than current ECDSA signatures, impacting applications with bandwidth constraints.
Despite these trade-offs, post-quantum algorithms are practical for deployment. Software implementations have been optimized, hardware accelerators are under development, and integration into existing protocols (TLS, SSH, VPNs) is underway.
| Algorithm | Type | Security Basis | Public Key Size | Signature/Ciphertext Size | Performance | 
| ML-KEM (Kyber) | Key Encapsulation | Lattice problems | ~1,184 bytes | ~1,088 bytes | Fast | 
| ML-DSA (Dilithium) | Digital Signature | Lattice problems | ~1,952 bytes | ~3,293 bytes | Fast | 
| SLH-DSA (SPHINCS+) | Digital Signature | Hash functions | ~64 bytes | ~29,792 bytes | Slow, large | 
| FALCON | Digital Signature | Lattice (NTRU) | ~1,793 bytes | ~1,261 bytes | Moderate | 
| RSA-3072 (current) | Encryption/Signature | Factoring | ~384 bytes | ~384 bytes | Moderate | 
| ECDSA P-256 (current) | Digital Signature | Discrete log | ~64 bytes | ~64 bytes | Fast, small | 
How Does Quantum Key Distribution Provide Security?
While post-quantum cryptography uses mathematics to resist quantum attacks, quantum key distribution (QKD) takes a fundamentally different approach – using the laws of quantum mechanics to detect eavesdropping and distribute encryption keys with information-theoretic security.
QKD does not encrypt data directly. Instead, it establishes a shared secret key between two parties in such a way that any attempt by an eavesdropper to intercept the key leaves detectable traces. Once the key is established and verified as secure, the parties use it with a classical encryption algorithm like AES to encrypt their communication.
The BB84 Protocol
The most widely used QKD protocol, BB84 (proposed in 1984), operates by having Alice send single photons to Bob, encoding each photon in one of four possible quantum states. Bob randomly selects measurement bases for each incoming photon. After transmission, Alice and Bob communicate over a classical channel to compare their basis choices, keeping only measurements where bases matched. They then compare a subset of their remaining bits to estimate the error rate – if too high, they abort assuming an eavesdropper is present. If acceptable, they use privacy amplification to distill a fully secure shared key.
The security of QKD derives from the no-cloning theorem and the observer effect in quantum mechanics. If an eavesdropper tries to intercept and measure the photons, she necessarily disturbs them, introducing errors that Alice and Bob detect. Even an eavesdropper with a quantum computer cannot break QKD’s security, as it relies on physical laws rather than computational complexity.
Limitations of QKD
Despite its theoretical security, QKD faces practical limitations:
- Distance constraints: Photons traveling through optical fiber are absorbed or scattered, limiting QKD range to roughly 100 kilometers without trusted repeater nodes. Quantum repeaters could extend range but remain in early development.
- Infrastructure requirements: QKD requires dedicated quantum channels, single-photon sources, and detectors. This infrastructure is expensive and not compatible with existing classical networks.
- Key distribution only: QKD only establishes keys. It does not encrypt data, authenticate parties, or provide digital signatures.
- Trusted nodes: Long-distance QKD networks currently rely on trusted nodes that break the quantum link into segments, reintroducing some vulnerabilities.
- Point-to-point only: QKD links are inherently point-to-point, limiting scalability for multi-party communications.
QKD Deployment Status
Despite limitations, QKD networks are operational in several regions. China has deployed the world’s most extensive QKD infrastructure, including a 2,000-kilometer ground network connecting Beijing and Shanghai and the Micius satellite demonstrating intercontinental QKD. Europe is building the European Quantum Communication Infrastructure (EuroQCI), linking member states with QKD networks. South Korea, Japan, and Singapore operate metropolitan-scale QKD networks for government and financial sector use.
| Approach | Security Basis | Quantum Resistance | Deployment Status | Key Limitation | 
| Post-Quantum Cryptography | Mathematical hardness | Believed secure (not proven) | Standardized, early deployment | Relies on unproven assumptions | 
| Quantum Key Distribution | Quantum mechanics | Provably secure (physics-based) | Limited operational networks | Distance, cost, infrastructure | 
Both approaches have roles to play. Post-quantum cryptography will protect most digital infrastructure due to its compatibility with existing systems and global scalability. QKD will secure high-value communications where the cost and complexity of quantum infrastructure can be justified.
What Is “Harvest Now, Decrypt Later” and Why Does It Matter?
One of the most immediate and concerning implications of quantum computing for cryptography is the “harvest now, decrypt later” threat. Adversaries with the foresight and resources to do so are collecting encrypted communications today with the intention of storing them until quantum computers become powerful enough to decrypt them.
This threat creates urgency even though large-scale quantum computers do not yet exist. Data encrypted today using RSA or ECC may remain sensitive for years or decades. Medical records, government secrets, corporate intellectual property, and personal communications could all be vulnerable to future decryption.
Why Harvest Now, Decrypt Later Is Feasible
Modern digital communications leave extensive traces. Internet traffic passes through routers, undersea cables, and data centers where it can be intercepted and stored. State-level actors with access to network infrastructure can collect vast quantities of encrypted data at relatively low cost.
Storage costs have fallen exponentially over the past decades. Storing petabytes or exabytes of encrypted traffic is economically feasible for well-resourced adversaries, particularly intelligence agencies and nation-states. Encrypted data has a long shelf life – unlike perishable intelligence that loses value quickly, encrypted communications retain their value as long as the underlying information remains sensitive.
Who Is At Risk?
The harvest now, decrypt later threat disproportionately affects organizations and individuals handling information with long-term sensitivity:
- Government agencies communicating classified information face risks that intercepted communications could be decrypted years later, exposing state secrets, diplomatic negotiations, or intelligence sources.
- Healthcare organizations storing patient records encrypted with current algorithms may see those records decrypted in the future, violating patient privacy.
- Financial institutions handling long-term investment strategies, mergers and acquisitions, or proprietary trading algorithms could see competitive advantages eroded.
- Legal firms communicating privileged attorney-client information could face breaches of confidentiality if encrypted emails are decrypted retroactively.
- Research institutions developing intellectual property in fields with long development cycles could lose competitive advantages if adversaries decrypt communications revealing trade secrets.
- Individuals with access to sensitive information – government officials, corporate executives, journalists, activists – may face personal risks if private communications are exposed.
Mitigating the Threat
Organizations concerned about harvest now, decrypt later attacks have several mitigation options:
Migrate to post-quantum cryptography immediately for communications containing information that must remain confidential for 10+ years. Even though standardized algorithms only became available in 2024, early adopters can begin deploying them for high-value data.
Use hybrid cryptography that combines current algorithms (RSA, ECC) with post-quantum algorithms. This provides security even if one approach is broken, offering defense-in-depth during the transition period.
Minimize data retention by deleting sensitive communications after they are no longer needed. Data that does not exist cannot be decrypted, regardless of future quantum computing advances.
Deploy quantum key distribution for the most sensitive communications where the cost and complexity can be justified.
Implement perfect forward secrecy in communication protocols, ensuring that even if long-term keys are compromised, past communications remain secure.
Timeline Considerations
Estimates for when quantum computers will be powerful enough to break RSA-2048 range from 10 to 30+ years. However, the uncertainty itself drives action. An organization protecting 30-year secrets cannot wait until quantum computers are imminent to begin migration – by then, adversaries will already possess years or decades of harvestable data.
This creates a decision-making challenge – invest in post-quantum migration now at significant cost and complexity, or risk that sensitive data will be decrypted in the future. For many organizations, particularly those handling classified information or long-term trade secrets, the solution lies in early migration.
Who Is Leading Post-Quantum Cryptography Development?
The development and deployment of post-quantum cryptography involves government agencies, standards organizations, technology companies, and specialized startups.
Government and Standards Bodies
NIST (National Institute of Standards and Technology) in the United States has led the global standardization effort, evaluating submissions from international cryptographers and publishing the first standardized post-quantum algorithms in 2024.
NSA (National Security Agency) designated post-quantum cryptography as a priority and requires U.S. national security systems to begin transitioning to quantum-resistant algorithms.
CISA (Cybersecurity and Infrastructure Security Agency) coordinates quantum cryptography migration across critical infrastructure sectors, providing resources and timelines for organizations to assess and upgrade systems.
European Union Agency for Cybersecurity (ENISA) coordinates post-quantum cryptography efforts across EU member states, publishing guidelines and supporting research initiatives.
China’s State Cryptography Administration is developing national post-quantum cryptographic standards, with Chinese researchers contributing significantly to international standardization efforts.
Technology Giants
IBM has been a leader in post-quantum cryptography research, with researchers contributing to algorithms like Dilithium and FALCON. The company has integrated post-quantum algorithms into its products and cloud services.
Microsoft provides post-quantum cryptography libraries and has begun integrating quantum-resistant algorithms into Azure services.
Google has conducted experiments with post-quantum key exchange in Chrome and HTTPS connections, testing hybrid approaches that combine classical and post-quantum algorithms.
Amazon Web Services (AWS) offers post-quantum TLS options in some services and provides cryptographic libraries implementing NIST-standardized algorithms.
Apple has begun integrating post-quantum cryptography into iMessage, representing one of the first large-scale deployments in consumer applications.
Cloudflare has experimented with post-quantum TLS on its edge network, measuring performance and identifying deployment challenges.
Quantum Computing and Cryptography Companies
SEALSQ, a Swiss semiconductor company, develops post-quantum cryptographic chips for IoT devices, automotive systems, and secure hardware roots of trust.
BTQ Technologies focuses on post-quantum security for blockchain and distributed ledger systems, offering quantum-resistant digital signatures.
01 Communique (IronCAP) licenses post-quantum encryption software for enterprise applications.
PQShield, a U.K.-based startup, develops post-quantum cryptographic implementations optimized for embedded systems, IoT devices, and automotive applications.
QuSecure offers a post-quantum cybersecurity platform that integrates quantum-resistant encryption, quantum key distribution, and quantum random number generation.
Financial Institutions and Critical Infrastructure
JPMorgan Chase, Bank of America, and other major banks have established quantum cryptography research programs, assessing vulnerabilities in payment systems and secure communications.
SWIFT, the global financial messaging network, is evaluating post-quantum cryptography for securing interbank communications and transaction authentication.
Telecommunications providers including AT&T, Verizon, and BT Group are researching post-quantum security for 5G networks and fiber optic infrastructure.
When Will Quantum Computers Break Current Encryption?
The timeline for when quantum computers will achieve the scale and reliability needed to break widely used encryption remains one of the most debated questions in the field.
Optimistic (For Attackers) Projections: 10-15 Years
Some researchers and quantum computing companies project that fault-tolerant quantum computers capable of running Shor’s algorithm to break RSA-2048 could emerge within 10 to 15 years. This timeline assumes continued exponential growth in physical qubit counts, successful implementation of quantum error correction at scale, optimization of algorithms to reduce qubit requirements, and adequate classical computing resources for real-time error syndrome decoding.
Companies like IBM and Google have roadmaps targeting fault-tolerant systems within this timeframe, though the commercial viability of cryptographic attacks remains uncertain.
Moderate Projections: 15-25 Years
The broader research community tends toward more conservative estimates, suggesting that breaking RSA-2048 or equivalent elliptic curve systems will require 15 to 25 years of continued development. This view acknowledges the enormous engineering challenge of scaling from today’s hundreds of qubits to the millions required, the likelihood of unforeseen technical obstacles, the resource intensity of maintaining million-qubit quantum computers, and the possibility that classical cryptanalytic advances could extend the useful life of current systems.
This timeline aligns with expert surveys and government planning documents, which often cite the mid-2040s as a plausible horizon for cryptographically relevant quantum computers.
Pessimistic (For Attackers) Projections: 25+ Years or Never
Some skeptics argue that practical quantum computers capable of breaking encryption may take significantly longer than 25 years or may never be realized at the scale required. This perspective emphasizes the gap between current physical error rates and the rates needed for efficient error correction, the overhead of error correction codes (potentially requiring 10,000+ physical qubits per logical qubit), the possibility that fundamental physical limits will prevent scaling beyond certain thresholds, and the potential for classical computing advances to maintain parity with quantum computing.
What We Know With Certainty
Regardless of timeline uncertainty, several facts are clear:
The threat is real: Shor’s algorithm is mathematically proven to break RSA, ECC, and Diffie-Hellman if implemented on a sufficiently large quantum computer. The question is “when,” not “if.”
Cryptographic transitions take decades: Even with standardized algorithms available today, migrating global infrastructure to post-quantum cryptography will require 10-20 years of coordinated effort.
Harvest now, decrypt later is happening now: Adversaries do not need to wait for quantum computers to begin collecting encrypted data. The vulnerability exists today for any data that will remain sensitive when quantum computers arrive.
No organization can afford to wait: By the time quantum computers powerful enough to break encryption become publicly known, it will be too late for organizations to protect data that has already been collected.
| Estimate Source | Timeframe | Key Assumptions | 
| Optimistic QC Companies | 10-15 years | Continued exponential qubit scaling, breakthrough in error correction | 
| Academic Consensus | 15-25 years | Steady progress but unforeseen challenges expected | 
| Government Planning | ~2040-2045 | Conservative timeline for policy and infrastructure planning | 
| Skeptics | 25+ years or uncertain | Fundamental physical limits may prevent scaling | 
For planning purposes, most organizations use a 15-20 year horizon as a reasonable middle ground, recognizing that even if this estimate proves pessimistic, the time required for migration justifies beginning immediately.
Frequently Asked Questions
What is the quantum threat to cryptography?
The quantum threat refers to the ability of sufficiently powerful quantum computers to break widely used encryption systems including RSA, elliptic curve cryptography (ECC), and Diffie-Hellman key exchange. Shor’s algorithm, running on a fault-tolerant quantum computer with thousands of logical qubits, could factor large numbers and compute discrete logarithms exponentially faster than classical computers, undermining the mathematical hardness assumptions that protect these cryptographic systems.
When will quantum computers be able to break encryption?
Estimates range from 10 to 30+ years depending on assumptions about quantum hardware progress, error correction advances, and algorithmic optimization. Most experts and government agencies use timelines of 15-25 years for planning purposes. However, the “harvest now, decrypt later” threat means that adversaries are already collecting encrypted data to decrypt once quantum computers become available, creating urgency even though the timeline is uncertain.
What is post-quantum cryptography?
Post-quantum cryptography consists of mathematical algorithms designed to run on classical computers while resisting attacks from both classical and quantum computers. Unlike quantum cryptography (which uses quantum mechanics for security), post-quantum algorithms rely on mathematical problems believed to be hard even for quantum computers, such as lattice problems, hash function security, and code-based cryptography. NIST standardized the first post-quantum algorithms in 2024, including ML-KEM (Kyber) for key exchange and ML-DSA (Dilithium) for digital signatures.
Is quantum key distribution better than post-quantum cryptography?
Each approach has advantages and limitations. Quantum key distribution (QKD) provides security based on the laws of physics and is provably secure against quantum attacks, but requires expensive dedicated infrastructure and is limited to point-to-point connections over ~100 km without trusted nodes. Post-quantum cryptography uses mathematical security (which is not provably unbreakable) but works with existing internet infrastructure and scales globally. Most organizations will rely primarily on post-quantum cryptography, with QKD reserved for high-value communications where specialized infrastructure can be justified.
Which encryption systems are vulnerable to quantum attacks?
Public-key cryptography systems including RSA encryption, elliptic curve cryptography (ECC/ECDSA), and Diffie-Hellman key exchange are highly vulnerable to Shor’s algorithm. Digital signatures based on these systems are equally vulnerable. Symmetric encryption like AES remains reasonably secure if key lengths are doubled (e.g., using AES-256 instead of AES-128). Hash functions like SHA-256 experience only modest quantum advantages and remain secure with sufficient output lengths.
What is “harvest now, decrypt later” and why should I care?
“Harvest now, decrypt later” describes the practice of adversaries collecting encrypted communications today to store and decrypt once quantum computers become powerful enough to break the encryption. This creates immediate risk for organizations handling data that will remain sensitive for 10+ years, including government secrets, healthcare records, financial strategies, and intellectual property. Even though quantum computers cannot break encryption today, the data being collected now could be vulnerable in the future, making post-quantum migration urgent for long-term sensitive information.
How do I prepare my organization for post-quantum cryptography?
Organizations should begin by conducting a cryptographic inventory to identify where RSA, ECC, and other vulnerable algorithms are used. Prioritize systems handling long-term sensitive data and begin migrating to NIST-standardized post-quantum algorithms (ML-KEM, ML-DSA) where feasible. Consider hybrid approaches that combine current and post-quantum algorithms during the transition. Update procurement requirements to specify quantum-resistant cryptography for new systems. Develop a multi-year migration roadmap recognizing that full transition will take 5-10 years for most organizations.

---
*检索时间: 2026-07-24 15:30:47*
*搜索来源: DuckDuckGo*
