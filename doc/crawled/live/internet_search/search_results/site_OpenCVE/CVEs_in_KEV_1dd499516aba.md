# CVEs in KEV

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=kev:true
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | An issue was discovered in router/upnp/src/ssdp.c in DD-WRT before 45724. An unsafe strcpy in the UPnP handling functionality allows an unauthenticated remote attacker to send a request that would overflow an internal fixed buffer. Exploitation requires the DD-WRT user to enable UPnP (which is off by default, and only listens on internal interfaces by default). This occurs in ssdp_msearch (reachable by an M-SEARCH request). | 
  
  
  
  | Joomla Extension - joomlack.fr - Unauthenticated file upload in Page Builder CK extension < 3.6.0 - The Joomla extension Page Builder CK is vulnerable to an unauthenticated arbitrary file upload that allows uploading executable files and leads to full RCE. | 
  
  
  
  | Joomla Extension - balbooa.com - Unauthenticated file upload in Balbooa Forms extension < 2.4.1 - The Joomla extension Balbooa Forms is vulnerable to an unauthenticated arbitrary file upload that allows uploading executable files and leads to full RCE. | 
  
  
  
  | Post-authentication improper control of generation of code ('Code Injection') vulnerability has been identified in the SMA1000 Appliance Management Console (AMC) which in specific conditions could potentially enable a remote authenticated attacker as administrator to execute arbitrary OS commands. | 
  
  
  
  | Deserialization of untrusted data in Microsoft Office SharePoint allows an unauthorized attacker to execute code over a network. | 
  
  
  
  | An authentication bypass vulnerability in the Check Point SmartConsole login process allows an unauthenticated remote attacker to obtain an application login token and use it to authenticate with full administrative privileges. Successful exploitation allows the attacker to modify security policies and security configurations. Remote exploitation requires internet access to the Management Server IP address and a configuration that does not restrict Trusted Clients. Check Point is aware that this vulnerability is being exploited and has affected a very small number of customers. | 
  
  
  
  | A Server-side request forgery (SSRF) vulnerability has been identified in the SMA1000 Appliance Work Place interface. A remote unauthenticated attacker could potentially cause the appliance to make requests to unintended location. | 
  
  
  
  | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Payments.  Successful attacks of this vulnerability can result in takeover of Oracle Payments. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H). | 
  
  
  
  | A vulnerability in the CLI of Cisco Catalyst SD-WAN Controller, formerly SD-WAN vSmart, Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, and Cisco Catalyst SD-WAN Validator, formerly SD-WAN vBond, could allow an authenticated, local attacker to execute arbitrary commands as root by supplying a crafted file to the affected system.
This vulnerability is due to insufficient validation of user-supplied input. An attacker could exploit this vulnerability by uploading a crafted file to the affected system. A successful exploit could allow the attacker to perform command injection attacks on an affected system and elevate their privileges as the root user.
To exploit this vulnerability, the attacker must have netadmin privileges on the affected system. This would require valid credentials or exploitation of  or . Cisco is not aware of successful exploitation by other methods. Cisco has observed limited cases where the exploitation of this bug resulted in a configuration change pushed to edge devices.
Cisco recommends that customers upgrade to the fixed software that is documented in the  that was published on May 14, 2026, and verify the configuration of the edge devices. | 
  
  
  
  | Langflow exec_globals Inclusion of Functionality from Untrusted Control Sphere Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Authentication is not required to exploit this vulnerability.
The specific flaw exists within the handling of the exec_globals parameter provided to the validate endpoint. The issue results from the inclusion of a resource from an untrusted control sphere. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-27325. | 
  
  
  
  | WordPress 6.9.x before 6.9.5 and 7.0.x before 7.0.2 is affected by a REST API batch endpoint route confusion issue which, combined with the author__not_in WP_Query SQL Injection (CVE-2026-60137), could allow an attacker to perform SQL Injection and achieve Remote Code Execution. | 
  
  
  
  | WordPress 6.8.x before 6.8.6, 6.9.x before 6.9.5, and 7.0.x before 7.0.2 does not properly sanitise the author__not_in parameter of WP_Query, which could allow SQL Injection when a plugin or theme passes untrusted input to the parameter. | 
  
  
  
  | Windows Kernel-Mode Driver Elevation of Privilege Vulnerability | 
  
  
  
  | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet FortiSandbox 4.4.0 through 4.4.8 may allow attacker to execute unauthorized code or commands via <insert attack vector here> | 
  
  
  
  | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet FortiSandbox 5.0.0 through 5.0.5, FortiSandbox 4.4.0 through 4.4.8, FortiSandbox 4.2 all versions, FortiSandbox Cloud 5.0.4 through 5.0.5, FortiSandbox PaaS 5.0.4 through 5.0.5 may allow an unauthenticated attacker to execute unauthorized commands via specifically crafted HTTP requests | 
  
  
  
  | Deserialization of untrusted data in Microsoft Office SharePoint allows an unauthorized attacker to execute code over a network. | 
  
  
  
  | KNX devices that use KNX Connection Authorization and support Option 1 are, depending on the implementation, vulnerable to being locked and users being unable to reset them to gain access to the device. The BCU key feature on the devices can be used to create a password for the device, but this password can often not be reset without entering the current password. If the device is configured to interface with a network, an attacker with access to that network could interface with the KNX installation, purge all devices without additional security options enabled, and set a BCU key, locking the device. Even if a device is not connected to a network, an attacker with physical access to the device could also exploit this vulnerability in the same way. | 
  
  
  
  | SimpleHelp versions 5.5.15 and prior and 6.0 pre-release versions contain an authentication bypass vulnerability in the OIDC authentication flow. When OIDC authentication is configured, identity tokens submitted during login are accepted without verifying their cryptographic signature. In a vulnerable configuration, a remote, unauthenticated attacker can submit a forged token containing arbitrary identity claims to obtain a fully authenticated technician session. In some configurations, this may also allow bypass of multi-factor authentication. No user interaction is required. | 
  
  
  
  | Missing authentication for critical function in Microsoft Office SharePoint allows an unauthorized attacker to elevate privileges over a network. | 
  
  
  
  | Insufficient granularity of access control in Active Directory Federation Services (AD FS) allows an authorized attacker to elevate privileges locally. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
