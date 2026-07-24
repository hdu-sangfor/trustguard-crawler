# 10 Cloud Security Best Practices

### 来源信息
- **URL**: https://www.fortinet.com/resources/cyberglossary/cloud-security-best-practices
- **域名**: www.fortinet.com
- **检索关键词**: cloud security best practices 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Organizations still struggle to find and fix security problems quickly, giving attackers more time to access sensitive data. Furthermore, hybrid and multi-cloud strategies make things more complex. Cloud Security Alliance state of cloud and AI security 2025 report highlights the growing complexity of hybrid and multi-cloud environments.

### 页面正文
11 Cloud security best practices for enterprises
  
  
  
  
  
  
  
  
   
Organizations can strengthen their cloud security posture by implementing these essential practices.
 
  
  
  
  
  
  1. Implement comprehensive identity and access management
  
  
  
  
  Strong identity and access management form the foundation of cloud security posture. Organizations should require phishing-resistant multifactor authentication for all user accounts. Moreover, access should follow zero-trust principles and continuously verify users and device posture. Decisions should be context-aware and grant access only when conditions meet security requirements.
Hardware-based authentication methods like FIDO (Fast Identity Online)/WebAuthn tokens provide better protection than SMS or app-based codes.
Key IAM practices include:
- Using secrets management tools for credential storage 
- Implementing conditional access policies based on user context 
- Requiring privileged access workstations for administrative tasks 
- Conducting regular access reviews to maintain least privilege 
Establish proper credential management practices. Never store passwords or API keys in plain text within application code or configuration files. 
Regular access reviews ensure permissions remain appropriate. Many cloud providers offer tools to identify unused privileges and help implement least privilege access.
 
  
  
  
  
  
  2. Enable network segmentation and encryption
  
  
  
  
  Network segmentation limits how far security problems can spread. The goal is to create barriers that stop attackers from moving freely between systems once they get in a core function of cloud network security that reduces lateral movement risk.
Micro-segmentation goes even further by isolating individual workloads and services. Set up cloud-native firewalls to block unnecessary traffic between network areas and protect applications running across dynamic, multi-cloud environments. This way, if one system gets compromised, it can't easily reach other parts of the infrastructure. Strengthening these defenses as part of a cloud computing security architecture ensures consistent segmentation, encryption, and access controls across hybrid and multi-cloud networks.
Essential network security measures:
- Private connectivity options to bypass the public internet 
- TLS 1.2 or higher for all web communications 
- VPN connections for administrative access 
- Flow logs for network traffic monitoring 
Cloud providers offer private connectivity options that reduce exposure to internet-based attacks. Direct network connections bypass public internet routing and provide additional security layers.
 
  
  
  
  
  
  3. Encrypt data at rest and in transit
  
  
  
  
  Data encryption protects sensitive information even if unauthorized users gain access. Encrypt all sensitive data stored in cloud environments using strong encryption algorithms.
Cloud providers typically offer multiple encryption options. Customer-managed keys provide more control over encryption processes. Hardware security modules offer the highest level of key protection for sensitive workloads.
Implement cloud encryption for data backups and archives. Many organizations focus on production data encryption but neglect backup security. Ensure backup encryption keys receive the same protection as production keys.
Use field-level encryption for highly sensitive data elements. This approach encrypts specific database fields rather than entire databases, providing granular protection.
 
  
  
  
  
  
  4. Establish secure key management practices
  
  
  
  
  Your encryption is only as strong as your key management. Poor key handling can render even the strongest encryption useless. Use dedicated key management services rather than storing encryption keys alongside encrypted data.
Automated key rotation reduces operational burden while maintaining security. Manual key rotation often gets delayed or forgotten, creating security gaps. Most cloud providers offer automated rotation features that handle this process seamlessly.
Separation of duties prevents any single person from having complete control over encryption keys. Personnel who manage encryption keys should not have access to use those keys for data operations.
 
  
  
  
  
  
  5. Secure managed service provider access
  
  
  
  
  Third-party access creates extra attack routes that many organizations miss. Managed service providers need access to do their jobs, but this access must be carefully controlled and watched.
Start by thoroughly checking MSP (managed service providers) security practices before giving any access.
Look at their security certifications, how they handle incidents, and their employee background check processes. Not all managed service providers have the same security standards.
MSP security controls should include:
- Least privilege access rules 
- Separate accounts for MSP staff 
- Complete activity logging and monitoring 
- Phishing-resistant authentication requirements 
Set clear security responsibilities in contracts. Define who handles incident alerts, response steps, and who's responsible for security breaches. Regular security checks make sure MSPs keep good security measures over time.
 
  
  
  
  
  
  6. Implement robust backup and recovery strategies
  
  
  
  
  Ransomware attacks specifically target backup systems to stop data recovery. A strong backup strategy protects against both malicious attacks and accidental data loss.
The 3-2-1 backup rule gives a solid foundation: three copies of important data, stored on two different storage types, with one copy kept off-site.
Immutable backup storage prevents modification or deletion for specified retention periods. This protection works even if attackers gain administrative access to your systems. They can't destroy backups that are technically impossible to alter.
Test your backup restoration procedures regularly. Many organizations discover backup failures only during actual emergencies, when it's too late to fix the problems.
 
  
  
  
  
  
  7. Enable comprehensive monitoring and logging
  
  
  
  
  Visibility into your cloud environment activities enables rapid threat detection and incident response. Most security breaches go undetected for months because organizations lack adequate monitoring capabilities. Leveraging specialized cloud security tools for monitoring and visibility can help enterprises quickly identify misconfigurations, anomalous access patterns, and potential threats before they escalate.
Continuous monitoring should be combined with regular security checks to identify misconfigurations and vulnerabilities in cloud services. This approach helps strengthen the overall cloud security posture.
For teams building a stronger detection baseline, these cloud security tips can help prioritize which alerts, logs, and misconfiguration signals to tune first.
Cloud providers offer centralized logging services that aggregate data from multiple sources. These services capture authentication events, resource access, configuration changes, and application activities. The key is to configure comprehensive logging before you need it.
Automated alerting (for high-risk activities) reduces response time to security incidents. Set up alerts for failed login attempts, privilege changes, unusual data access patterns, and changes to sensitive resources.
Key monitoring essentials include:
- Centralized logging for all important services 
- Cloud-native SIEM tool integration 
- Regular log review and analysis 
 
  
  
  
  
  
  8. Configure conditional access controls
  
  
  
  
  Context-based access controls add extra security layers beyond standard authentication. Set up policies that consider where users are, device status, and access patterns.
Conditional access features:
- Just-in-time access for privileged operations 
- Geographic and IP address restrictions 
- Risk-based authentication decisions 
- Device compliance requirements 
Limit administrative access to specific locations or IP address ranges. This stops access from unauthorized locations while keeping operational flexibility.
Require device compliance checks before giving access to make sure devices meet security standards.
 
  
  
  
  
  
  9. Manage certificates and PKI infrastructure
  
  
  
  
  Proper certificate management prevents authentication bypasses and man-in-the-middle attacks. Maintain an inventory of all certificates used in cloud environments.
Set up automatic certificate renewal to prevent outages from expired certificates. Many cloud providers offer managed certificate services that handle renewal automatically.
Use certificate pinning for important applications to stop certificate substitution attacks. This method makes sure applications only accept specific certificates or certificate authorities.
Watch certificate transparency logs to catch unauthorized certificate creation for domains.
 
  
  
  
  
  
  
  
  
  10. Secure cloud instance metadata services
  
  
  
  
  
  Cloud instance metadata services provide valuable information about virtual machines, but they can also expose sensitive data if misconfigured. Attackers often target these services to retrieve credentials and system information.
The latest versions of metadata services include additional security features like authentication token requirements. Upgrade to these versions and configure the strongest available protections.
Server-side request forgery attacks can abuse metadata services through vulnerable applications. Use input validation and web application firewalls (WAFs) to stop applications from making unauthorized metadata requests.
Limit access to metadata services for instances that don't need them. Many workloads don't require metadata access, so turning it off reduces potential attack points.
 
  
  
  
  
  
  11. Strengthen cloud security awareness and training
  
  
  
  
  Cloud-specific security training at regular intervals can help teams recognize potential risks and avoid common misconfigurations. It reinforces strong access practices and proper management of sensitive data. 
Continuous education ensures staff stay current with evolving threats and best practices. Most importantly, training reduces human errors, which are a leading cause of cloud security incidents. 
Therefore, prioritize awareness to create a stronger overall security posture across cloud environments in organizations.

---
*检索时间: 2026-07-24 15:19:33*
*搜索来源: DuckDuckGo*
