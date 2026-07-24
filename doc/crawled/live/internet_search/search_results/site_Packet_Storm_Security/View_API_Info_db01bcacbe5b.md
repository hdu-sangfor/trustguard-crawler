# View API Info

### 来源信息
- **URL**: https://packetstormsecurity.com/help/view/1
- **来源站点**: Packet Storm Security
- **页面抓取**: 成功

### 页面正文
Note: This page is best viewed on a desktop browser.
Background and purpose
Packet Storm’s API provides direct programmatic access to one of the largest and most trusted archives of security advisories, exploits, and threat intelligence. With over two decades of curated content, the API enables organizations to integrate real-time security data directly into their workflows, research platforms, and defensive tools.
Differentiator
We have seen many intelligence feeds simply become data aggregators for links that point to other sources of truth. However, the Internet can be a very temporary place and that data can age out when you need it most. Packet Storm natively stores files such as advisories and exploits to ensure availability and provides direct download links for every entry.
Use Cases
Threat Intelligence Integration – Enrich SIEMs, SOAR platforms, and vulnerability scanners with timely, authoritative exploit and advisory data.
Security Research & Automation – Automate large-scale research, monitoring, and correlation across Packet Storm’s full dataset.
Compliance & Risk Assessment – Map exposures against advisories and exploits to support patch prioritization and compliance reporting.
Custom Applications – Power dashboards, alerts, and data pipelines with high-fidelity, continuously updated security intelligence.
Capabilities
Complete access to Packet Storm’s dataset of exploits, advisories, and tools, spanning 25+ years.
Persistent, stable URLs and structured metadata for reliable integration.
Query support for filtering by sections, areas, data types, searching, and more.
High-volume query tiers to support enterprise-grade automation.
Rules
If you are repackaging the API data in your own service offering, there are some simple rules to follow. As noted in the Terms of Service, you cannot resell the feed verbatim.
If you are offering feed and search interaction to our API from a service offering, we expect that you handle authentication, authorization, and accounting (AAA) for your users and that the API secret for Packet Storm MUST stay resident on your systems. It's forbidden for your secret to be shared with your customers or third parties. If we notice an uptick in traffic that indicates this behavior, your key will be disabled without refund.
Note that if you provide functionality in your service that uses your API license to search the archive, your customers will be jointly limited to the ceiling of daily query allowances. This can be annoying for them. A better idea is to make it easy for a client to onboard a license key from Packet Storm inside of your product or service and have functionality built in to use the access.
Features
The API provides telemetry for entries on the site that can be programmatically parsed to leverage for populating your own web site feeds, AI training, researching vulnerabilities, and much more. It essentially gives you database access to Packet Storm itself.
Available API requests include telemetry data-retrieval for smarter requests, normal news and file feeds, and searchable news and file feeds (with output available in both the newest and most relevant listings). You can also search via CVE number. Packet Storm is a regularly referenced datapoint in MITRE's CVE database, and we regularly sync our datasets to ensure consistency between the systems.
Available API requests do not include access to user data such as profiles, collections, favorites, etc. The only relevant data related to humans comes from the file requests when referencing a public source and links are provided back to the site for further information.
Data can be output in both JSON and XML formats to suit any programmatic parsing needs. Results are restricted to 25 items at a time, inline with how the current web site operates. This should cover all bases for an integration, but if you can think of a feature we are missing, we always like hearing new ideas. Please send us a note.
Tracking changes
As improvements, bug fixes, and/or features are added to the API, the version will change. The current API links are available at the bottom of this page. As changes may become quite frequent, we will do our best to ensure backwards compatibility to all prior releases and communicate to our customers any decommissioning. Changes for all of Packet Storm are tracked at our Changelog, including API updates. Unless unavoidable and thoroughly communicated to our clients, backwards compatibility with older API versions will remain.
API authentication
The API is inaccessible without your key. Production keys must be accessed and purchased via the API ManagerAPI Manager which needs to be accessed from a desktop browser. To gain access, the key must be passed as a header called "Apisecret".
Notice that the entry point noted on the API manager for production versus the development zone is different. The correct key must be used for the correct area in order to work.
Cost
The API has three access tiers. All tiers are 30 day recurring subscription licenses that are auto-renewed.
  
  
  
  
  
  
  
  
  
In addition to daily access limits, the rate at which requests can be made to the interface is 10 per minute.
Access to the development API for testing purposes is free and is limited to 100 queries a day. Please note that data in the development interface is restricted to December of 2023.
All payment processing is performed via Stripe. Upon payment, you will be activated within 24 hours, though usually seconds.
Request and response examples
The Packet Storm API accepts POST requests with the "Apisecret" header defined. The data submitted in the body should match the form submitted format of parameter=value with differing data being separated by an ampersand ("&"). Please review our Ruby and Python code examples for a better understanding and to see extracted data from the payloads.
Note: To show API access examples, please use a desktop browser. Example cannot be rendered on mobile due to limitations.
Please click a flow below to find out more information in order to start building your client.
 
 
 
 
 
 
 
 
Where do I start?
Please review our Ruby and Python code examples to get started.
You can head over to the API ManagerIn order to start, you will need to login and go to the API Manager from a desktop browser to get a development key.
Entry points to the respective APIs are here:
Copy Production API URL
Copy Development API URL
Having issues or a question in general? You can contact support for anything. We're super friendly and all that stuff.
  
  Background and purpose
Packet Storm’s API provides direct programmatic access to one of the largest and most trusted archives of security advisories, exploits, and threat intelligence. With over two decades of curated content, the API enables organizations to integrate real-time security data directly into their workflows, research platforms, and defensive tools.
Differentiator
We have seen many intelligence feeds simply become data aggregators for links that point to other sources of truth. However, the Internet can be a very temporary place and that data can age out when you need it most. Packet Storm natively stores files such as advisories and exploits to ensure availability and provides direct download links for every entry.
Use Cases
Threat Intelligence Integration – Enrich SIEMs, SOAR platforms, and vulnerability scanners with timely, authoritative exploit and advisory data.
Security Research & Automation – Automate large-scale research, monitoring, and correlation across Packet Storm’s full dataset.
Compliance & Risk Assessment – Map exposures against advisories and exploits to support patch prioritization and compliance reporting.
Custom Applications – Power dashboards, alerts, and data pipelines with high-fidelity, continuously updated security intelligence.
Capabilities
Complete access to Packet Storm’s dataset of exploits, advisories, and tools, spanning 25+ years.
Persistent, stable URLs and structured metadata for reliable integration.
Query support for filtering by sections, areas, data types, searching, and more.
High-volume query tiers to support enterprise-grade automation.
Rules
If you are repackaging the API data in your own service offering, there are some simple rules to follow. As noted in the Terms of Service, you cannot resell the feed verbatim.
If you are offering feed and search interaction to our API from a service offering, we expect that you handle authentication, authorization, and accounting (AAA) for your users and that the API secret for Packet Storm MUST stay resident on your systems. It's forbidden for your secret to be shared with your customers or third parties. If we notice an uptick in traffic that indicates this behavior, your key will be disabled without refund.
Note that if you provide functionality in your service that uses your API license to search the archive, your customers will be jointly limited to the ceiling of daily query allowances. This can be annoying for them. A better idea is to make it easy for a client to onboard a license key from Packet Storm inside of your product or service and have functionality built in to use the access.
Features
The API provides telemetry for entries on the site that can be programmatically parsed to leverage for populating your own web site feeds, AI training, researching vulnerabilities, and much more. It essentially gives you database access to Packet Storm itself.
Available API requests include telemetry data-retrieval for smarter requests, normal news and file feeds, and searchable news and file feeds (with output available in both the newest and most relevant listings). You can also search via CVE number. Packet Storm is a regularly referenced datapoint in MITRE's CVE database, and we regularly sync our datasets to ensure consistency between the systems.
Available API requests do not include access to user data such as profiles, collections, favorites, etc. The only relevant data related to humans comes from the file requests when referencing a public source and links are provided back to the site for further information.
Data can be output in both JSON and XML formats to suit any programmatic parsing needs. Results are restricted to 25 items at a time, inline with how the current web site operates. This should cover all bases for an integration, but if you can think of a feature we are missing, we always like hearing new ideas. Please send us a note.
Tracking changes
As improvements, bug fixes, and/or features are added to the API, the version will change. The current API links are available at the bottom of this page. As changes may become quite frequent, we will do our best to ensure backwards compatibility to all prior releases and communicate to our customers any decommissioning. Changes for all of Packet Storm are tracked at our Changelog, including API updates. Unless unavoidable and thoroughly communicated to our clients, backwards compatibility with older API versions will remain.
API authentication
The API is inaccessible without your key. Production keys must be accessed and purchased via the API ManagerAPI Manager which needs to be accessed from a desktop browser. To gain access, the key must be passed as a header called "Apisecret".
Notice that the entry point noted on the API manager for production versus the development zone is different. The correct key must be used for the correct area in order to work.
Cost
The API has three access tiers. All tiers are 30 day recurring subscription licenses that are auto-renewed.
| License | Price | Queries / Day | Organization Size | 
|---|---|---|---|
| Basic | $100 | 100 | Up to 100 | 
| Business | $500 | 500 | Up to 1,000 | 
| Enterprise | $1000 | 1000 | Over 1,000 | 
| License: Basic | |
|---|---|
| Price | $100 | 
| Queries / Day | 100 | 
| Organization Size | Up to 100 | 
| License: Business | |
|---|---|
| Price | $500 | 
| Queries / Day | 500 | 
| Organization Size | Up to 1,000 | 
| License: Enterprise | |
|---|---|
| Price | $1000 | 
| Queries / Day | 1000 | 
| Organization Size | Over 1,000 | 
In addition to daily access limits, the rate at which requests can be made to the interface is 10 per minute.
Access to the development API for testing purposes is free and is limited to 100 queries a day. Please note that data in the development interface is restricted to December of 2023.
All payment processing is performed via Stripe. Upon payment, you will be activated within 24 hours, though usually seconds.
Request and response examples
The Packet Storm API accepts POST requests with the "Apisecret" header defined. The data submitted in the body should match the form submitted format of parameter=value with differing data being separated by an ampersand ("&"). Please review our Ruby and Python code examples for a better understanding and to see extracted data from the payloads.
Note: To show API access examples, please use a desktop browser. Example cannot be rendered on mobile due to limitations.
Please click a flow below to find out more information in order to start building your client.
| List areas () | 
| List sections () | 
| List files by CVE () | 
| List single file entry () | 
| List files () | 
| Search files () | 
| List single news entry () | 
| List news () | 
| Search news () | 
Where do I start?
Please review our Ruby and Python code examples to get started.
You can head over to the API ManagerIn order to start, you will need to login and go to the API Manager from a desktop browser to get a development key.
Entry points to the respective APIs are here:
Copy Production API URL
Copy Development API URL
Having issues or a question in general? You can contact support for anything. We're super friendly and all that stuff.
Help Section

---
*爬取时间: 2026-07-24 16:10:16*
*来源: 直接站点爬取*
