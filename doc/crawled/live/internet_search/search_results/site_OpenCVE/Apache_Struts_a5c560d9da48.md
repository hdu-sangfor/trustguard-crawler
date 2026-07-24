# Apache Struts

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=vendor:apache+AND+product:struts
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | ParametersInterceptor in OpenSymphony XWork 2.0.x before 2.0.6 and 2.1.x before 2.1.2, as used in Apache Struts and other products, does not properly restrict # (pound sign) references to context objects, which allows remote attackers to execute Object-Graph Navigation Language (OGNL) statements and modify server-side context objects, as demonstrated by use of a \u0023 representation for the # character. | 
  
  
  
  | Cross-site scripting (XSS) vulnerability in Apache Struts before 1.2.9-162.31.1 on SUSE Linux Enterprise (SLE) 11, before 1.2.9-108.2 on SUSE openSUSE 10.3, before 1.2.9-198.2 on SUSE openSUSE 11.0, and before 1.2.9-162.163.2 on SUSE openSUSE 11.1 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors related to "insufficient quoting of parameters." | 
  
  
  
  | Multiple directory traversal vulnerabilities in Apache Struts 2.0.x before 2.0.12 and 2.1.x before 2.1.3 allow remote attackers to read arbitrary files via a ..%252f (encoded dot dot slash) in a URI with a /struts/ path, related to (1) FilterDispatcher in 2.0.x and (2) DefaultStaticContentLoader in 2.1.x. | 
  
  
  
  | Apache Tiles 2.1 before 2.1.2, as used in Apache Struts and other products, evaluates Expression Language (EL) expressions twice in certain circumstances, which allows remote attackers to conduct cross-site scripting (XSS) attacks or obtain sensitive information via unspecified vectors, related to the (1) tiles:putAttribute and (2) tiles:insertTemplate JSP tags. | 
  
  
  
  | Multiple cross-site scripting (XSS) vulnerabilities in Apache Struts 2.0.x before 2.0.11.1 and 2.1.x before 2.1.1 allow remote attackers to inject arbitrary web script or HTML via vectors associated with improper handling of (1) " (double quote) characters in the href attribute of an s:a tag and (2) parameters in the action attribute of an s:url tag. | 
  
  
  
  | Multiple cross-site scripting (XSS) vulnerabilities in Dojo 0.4.1 and 0.4.2, as used in Apache Struts and other products, allow remote attackers to inject arbitrary web script or HTML via unspecified vectors involving (1) xip_client.html and (2) xip_server.html in src/io/. | 
  
  
  
  | Apache Struts 2.0.0 through 2.3.15 allows remote attackers to execute arbitrary OGNL expressions via a parameter with a crafted (1) action:, (2) redirect:, or (3) redirectAction: prefix. | 
  
  
  
  | The ExceptionDelegator component in Apache Struts before 2.2.3.1 interprets parameter values as OGNL expressions during certain exception handling for mismatched data types of properties, which allows remote attackers to execute arbitrary Java code via a crafted parameter. | 
  
  
  
  | The Jakarta Multipart parser in Apache Struts 2 2.3.x before 2.3.32 and 2.5.x before 2.5.10.1 has incorrect exception handling and error-message generation during file-upload attempts, which allows remote attackers to execute arbitrary commands via a crafted Content-Type, Content-Disposition, or Content-Length HTTP header, as exploited in the wild in March 2017 with a Content-Type header containing a #cmd= string. | 
  
  
  
  | The Struts 1 plugin in Apache Struts 2.1.x and 2.3.x might allow remote code execution via a malicious field value passed in a raw message to the ActionMessage. | 
  
  
  
  | The REST Plugin in Apache Struts 2.1.1 through 2.3.x before 2.3.34 and 2.5.x before 2.5.13 uses an XStreamHandler with an instance of XStream for deserialization without any type filtering, which can lead to Remote Code Execution when deserializing XML payloads. | 
  
  
  
  | ActionForm in Apache Software Foundation (ASF) Struts before 1.2.9 with BeanUtils 1.7 allows remote attackers to cause a denial of service via a multipart/form-data encoded form with a parameter name that references the public getMultipartRequestHandler method, which provides further access to elements in the CommonsMultipartRequestHandler implementation and BeanUtils. | 
  
  
  
  | Cross-site scripting (XSS) vulnerability in Apache Struts 1.2.7, and possibly other versions allows remote attackers to inject arbitrary web script or HTML via the query string, which is not properly quoted or filtered when the request handler generates an error message. | 
  
  
  
  | Apache Software Foundation (ASF) Struts before 1.2.9 allows remote attackers to bypass validation via a request with a 'org.apache.struts.taglib.html.Constants.CANCEL' parameter, which causes the action to be canceled but would not be detected from applications that do not use the isCancelled check. | 
  
  
  
  | Cross-site scripting (XSS) vulnerability in (1) LookupDispatchAction and possibly (2) DispatchAction and (3) ActionDispatcher in Apache Software Foundation (ASF) Struts before 1.2.9 allows remote attackers to inject arbitrary web script or HTML via the parameter name, which is not filtered in the resulting error message. | 
  
  
  
  | Missing XML Validation vulnerability in Apache Struts, Apache Struts.
This issue affects Apache Struts: from 2.0.0 before 2.2.1; Apache Struts: from 2.2.1 through 6.1.0.
Users are recommended to upgrade to version 6.1.1, which fixes the issue. | 
  
  
  
  | Denial of Service vulnerability in Apache Struts, file leak in multipart request processing causes disk exhaustion.
This issue affects Apache Struts: from 2.0.0 through 6.7.0, from 7.0.0 through 7.0.3.
Users are recommended to upgrade to version 6.8.0 or 7.1.1, which fixes the issue. | 
  
  
  
  | Denial of Service vulnerability in Apache Struts, file leak in multipart request processing causes disk exhaustion.
This issue affects Apache Struts: from 2.0.0 through 6.7.4, from 7.0.0 through 7.0.3.
Users are recommended to upgrade to version 6.8.0 or 7.1.1, which fixes the issue.
It's related to  https://cve.org/CVERecord?id=CVE-2025-64775  - this CVE addresses missing affected version 6.7.4 | 
  
  
  
  | ** UNSUPPORTED WHEN ASSIGNED ** Improper Output Neutralization for Logs vulnerability in Apache Struts.
This issue affects Apache Struts Extras: before 2.
When using LookupDispatchAction, in some cases, Struts may print untrusted input to the logs without any filtering. Specially-crafted input may lead to log output where part of the message masquerades as a separate log line, confusing consumers of the logs (either human or automated). 
As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.
NOTE: This vulnerability only affects products that are no longer supported by the maintainer. | 
  
  
  
  | When a Multipart request is performed but some of the fields exceed the maxStringLength  limit, the upload files will remain in struts.multipart.saveDir  even if the request has been denied.
Users are recommended to upgrade to versions Struts 2.5.32 or 6.1.2.2 or Struts 6.3.0.1 or greater, which fixe this issue. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
