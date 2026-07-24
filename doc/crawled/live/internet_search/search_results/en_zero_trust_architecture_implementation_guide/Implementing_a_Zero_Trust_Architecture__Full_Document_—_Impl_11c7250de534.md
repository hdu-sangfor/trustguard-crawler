# Implementing a Zero Trust Architecture: Full Document — Implementing a Zero Trust Architecture Project documentation

### 来源信息
- **URL**: https://pages.nist.gov/zero-trust-architecture/
- **域名**: pages.nist.gov
- **检索关键词**: zero trust architecture implementation guide
- **页面抓取**: 成功

### 搜索摘要
The Guide also summarizes best practices and lessons learned from the implementations and integrations to make it easier and more cost-effective to implement ZTA. This guide also includes mappings of ZTA principles and technologies to commonly used security standards and guidelines. ... enhanced identity governance (EIG); identity, credential, and access management (ICAM); microsegmentation; secure access service edge (SASE); software-defined perimeter (SDP); zero trust; zero trust architecture (ZTA).

### 页面正文
NIST SPECIAL PUBLICATION 1800-35
Implementing a Zero Trust Architecture: Full Document#
| Oliver Borchert Gema Howell Alper Kerman Scott Rose Murugiah Souppaya National Institute of Standards and Technology Jason Ajmo Yemi Fashina Parisa Grayeli Joseph Hunt Jason Hurlburt Nedu Irrechukwu Joshua Klosterman Oksana Slivina Susan Symington Allen Tan The MITRE Corporation Karen Scarfone Scarfone Cybersecurity William Barker Dakota Consulting Peter Gallagher Aaron Palermo Appgate Madhu Balaji Adam Cerini Rajarshi Das AWS (Amazon Web Services) Jacob Barosin Kyle Black Scott Gordon Jerry Haskins Keith Luck Dale McKay Sunjeet Randhawa Broadcom | Brian Butler Mike Delaguardia Matthew Hyatt Randy Martin Peter Romness Cisco Corey Bonnell Dean Coclin DigiCert Ryan Johnson Dung Lam Darwin Tolbert F5 Tim Jones Tom May Forescout Christopher Altman Alex Bauer Marco Genovese Google Cloud Andrew Campagna John Dombroski Adam Frank Nalini Kannan Priti Patil Harmeet Singh Mike Spisak Krishna Yellepeddy IBM Nicholas Herrmann Corey Lund Farhan Saifudin Ivanti | Madhu Dodda Tim LeMaster Lookout Ken Durbin James Elliott Earl Matthews David Pricer Mandiant Joey Cruz Tarek Dawoud Carmichael Patton Alex Pavlovsky Brandon Stephenson Clay Taylor Microsoft Bob Lyons Vinu Panicker Okta Peter Bjork Hans Drolshagen Omnissa Imran Bashir Ali Haider Nishit Kothari Sean Morgan Seetal Patel Norman Wong Palo Alto Networks Zack Austin Shawn Higgins Rob Woodworth PC Matic Mitchell Lewars Bryan Rosensteel Ping Identity Bill Baz Don Coltrain Wade Ellery Deborah McGinn Radiant Logic | Frank Briguglio Ryan Tighe SailPoint Chris Jensen Joshua Moll Tenable Jason White Trellix, Public Sector Joe Brown Gary Bradt Zimperium Jeffrey Adorno Syed Ali Bob Smith Zscaler | 
June 2025
FINAL
DISCLAIMER
Certain commercial entities, equipment, products, or materials may be identified by name or company logo or other insignia in order to acknowledge their participation in this collaboration or to describe an experimental procedure or concept adequately. Such identification is not intended to imply special status or relationship with NIST or recommendation or endorsement by NIST or NCCoE; neither is it intended to imply that the entities, equipment, products, or materials are necessarily the best available for the purpose.
While NIST and the NCCoE address goals of improving management of cybersecurity and privacy risk through outreach and application of standards and best practices, it is the stakeholderâs responsibility to fully perform a risk assessment to include the current threat, vulnerabilities, likelihood of a compromise, and the impact should the threat be realized before adopting cybersecurity measures such as this recommendation.
National Institute of Standards and Technology Special Publication 1800-35, Natl. Inst. Stand. Technol. Spec. Publ. 1800-35, (June 2025), CODEN: NSPUE2
NIST TECHNICAL SERIES POLICIES
AUTHOR ORCID IDS
Oliver Borchert: 0009-0006-1880-0542
Gema Howell: 0000-0002-0428-5045
Alper Kerman: 0009-0000-5880-8369
Scott Rose: 0000-0002-3105-7427
Murugiah Souppaya: 0000-0002-8055-8527
Karen Scarfone: 0000-0001-6334-9486
William Barker: 0000-0002-4113-8861
FEEDBACK
You can view or download the final guide at the NCCoE ZTA project page.
Comments on this publication may be submitted to: nccoe-zta-project@list.nist.gov.
All comments are subject to release under the Freedom of Information Act.
NATIONAL CYBERSECURITY CENTER OF EXCELLENCE
The National Cybersecurity Center of Excellence (NCCoE), a part of the National Institute of Standards and Technology (NIST), is a collaborative hub where industry organizations, government agencies, and academic institutions work together to address businesses â most pressing cybersecurity issues. This public-private partnership enables the creation of practical cybersecurity solutions for specific industries, as well as for broad, cross-sector technology challenges. Through consortia under Cooperative Research and Development Agreements (CRADAs), including technology partnersâfrom Fortune 50 market leaders to smaller companies specializing in information technology securityâthe NCCoE applies standards and best practices to develop modular, adaptable example cybersecurity solutions using commercially available technology. The NCCoE documents these example solutions in the NIST Special Publication 1800 series, which maps capabilities to the NIST Cybersecurity Framework (CSF) and details the steps needed for another entity to re-create the example solution. The NCCoE was established in 2012 by NIST in partnership with the State of Maryland and Montgomery County, Maryland.
To learn more about the NCCoE, visit https://www.nccoe.nist.gov/. To learn more about NIST, visit https://www.nist.gov.
NIST CYBERSECURITY PRACTICE GUIDES
NIST Cybersecurity Practice Guides (Special Publication 1800 series) target specific cybersecurity challenges in the public and private sectors. They are practical, user-friendly guides that facilitate the adoption of standards-based approaches to cybersecurity. They show members of the information security community how to implement example solutions that help them align with relevant standards and best practices, and provide users with the materials lists, configuration files, and other information they need to implement a similar approach.
The documents in this series describe example implementations of cybersecurity practices that businesses and other organizations may voluntarily adopt. These documents do not describe regulations or mandatory practices, nor do they carry statutory authority.
ABSTRACT
A zero trust architecture (ZTA) enables secure authorized access to enterprise resources that are distributed across on-premises and multiple cloud environments, while enabling a hybrid workforce and partners to access resources from anywhere, at any time, from any device in support of the organizationâs mission.
This NIST Cybersecurity Practice Guide explains how organizations can implement ZTA consistent with the concepts and principles outlined in NIST Special Publication (SP) 800-207, Zero Trust Architecture. The NCCoE worked with 24 collaborators under Cooperative Research and Development Agreements (CRADAs) to integrate commercially available technology to build 19 ZTA example implementations and demonstrate a number of common use cases. The guide includes detailed technical information on each example ZTA implementation, providing models that organizations can emulate. The Guide also summarizes best practices and lessons learned from the implementations and integrations to make it easier and more cost-effective to implement ZTA. This guide also includes mappings of ZTA principles and technologies to commonly used security standards and guidelines.
KEYWORDS
enhanced identity governance (EIG); identity, credential, and access management (ICAM); microsegmentation; secure access service edge (SASE); software-defined perimeter (SDP); zero trust; zero trust architecture (ZTA).
ACKNOWLEDGMENTS
We are grateful to the following individuals for their generous contributions of expertise and time.
- Appgate: Jason Garbis, Adam Rose, Jonathan Roy 
- AWS (Amazon Web Services): Conrad Fernandes*, Harrison Holstein, Quint Van Deman 
- Broadcom: Andrew Babakian*, Genc Domi*, Paul Mancuso, Eric Michael, Dennis Moreau*, Wayne Pauley*, Jacob Rapp*, Lewis Shepherd 
- Cisco: Ken Andrews, Robert Bui, Leo Lebel, Tom Oast, Aaron Rodriguez, Kelly Sennett, Steve Vetter, Micah Wilson 
- F5: Daniel Cayer, David Clark, Jay Kelley, Darrell Pierson 
- Forescout: Yejin Jang*, Neal Lucier* 
- Google Cloud: Tim Knudson* 
- IBM: Nilesh Atal, Himanshu Gupta, Lakshmeesh Hegde, Sharath Math, Naveen Murthy, Nikhil Shah, Deepa Shetty, Harishkumar Somashekaraiah 
- IT Coalition: Aaron Cook, Vahid Esfahani*, Jeff Laclair, Ebadullah Siddiqui*, Musumani Woods* 
- Ivanti: Patty Arcano, Jeffery Burton, Jay Dineshkumar 
- Lookout: Tyler Croak, Jeff Gilhool, Hashim Khan* 
- Microsoft: Thomas Detzner, Ehud Itshaki, Janet Jones, Hemma Prafullchandra*, Enrique Saggese, Sarah Young 
- MITRE: Eileen Division*, Spike E. Dog*, Sallie Edwards*, Ayayidjin Gabiam, Jolene Loveless*, Karri Meldorf, Kenneth Sandlin, Lauren Swan, Jessica Walton* 
- NIST: Mike Bartock, Julia Chua, Douglas Montgomery, Cherilyn Pascoe, Michael Powell, Kevin Stine 
- Okta: Brian Dack, Sean Frazier, Naveed Mirza, Kelsey Nelson, Ron Wilson 
- Omnissa: Keith Luck* 
- PC Matic: Andy Tuch 
- Ping Identity: Ivan Anderson, Aubrey Turner 
- Radiant Logic: Rusty Deaton, John Petrutiu, Lauren Selby 
- SailPoint: Peter Amaral, Jim Russell, Esteban Soto 
- Tenable: Jeremiah Stallcup 
- Zimperium: Dan Butzer, Jim Kovach*, Kern Smith 
- Zscaler: Jeremy James, Lisa Lorenzin*, Matt Moulton, Patrick Perry 
* Former employee; all work for this publication was done while at that organization
Special thanks to all who reviewed and provided feedback on this document.
The Technology Collaborators who participated in this project submitted their capabilities in response to a notice in the Federal Register. Respondents with relevant capabilities or product components were invited to sign a Cooperative Research and Development Agreement (CRADA) with NIST, allowing them to participate in a consortium to build this example solution. We worked with:
Note that after the VMware End User Computing division products were implemented at the NCCoE, VMware was acquired by Broadcom, then the VMware End User Computing Division was divested and reformed under a new entity, Omnissa LLC. Symantec was also previously acquired by Broadcom.
DOCUMENT CONVENTIONS
The terms âshallâ and âshall notâ indicate requirements to be followed strictly to conform to the publication and from which no deviation is permitted. The terms âshouldâ and âshould notâ indicate that among several possibilities, one is recommended as particularly suitable without mentioning or excluding others, or that a certain course of action is preferred but not necessarily required, or that (in the negative form) a certain possibility or course of action is discouraged but not prohibited. The terms âmayâ and âneed notâ indicate a course of action permissible within the limits of the publication. The terms âcanâ and âcannotâ indicate a possibility and capability, whether material, physical, or causal.
PATENT DISCLOSURE NOTICE
NOTICE: The Information Technology Laboratory (ITL) has requested that holders of patent claims whose use may be required for compliance with the guidance or requirements of this publication disclose such patent claims to ITL. However, holders of patents are not obligated to respond to ITL calls for patents and ITL has not undertaken a patent search in order to identify which, if any, patents may apply to this publication.
As of the date of publication and following call(s) for the identification of patent claims whose use may be required for compliance with the guidance or requirements of this publication, no such patent claims have been identified to ITL.
No representation is made or implied by ITL that licenses are not required to avoid patent infringement in the use of this publication.

---
*检索时间: 2026-07-24 15:20:02*
*搜索来源: DuckDuckGo*
