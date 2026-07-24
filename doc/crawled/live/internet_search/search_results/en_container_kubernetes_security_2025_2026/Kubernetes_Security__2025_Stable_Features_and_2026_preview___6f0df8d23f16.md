# Kubernetes Security: 2025 Stable Features and 2026 preview | CNCF

### 来源信息
- **URL**: https://www.cncf.io/blog/2025/12/15/kubernetes-security-2025-stable-features-and-2026-preview/
- **域名**: www.cncf.io
- **检索关键词**: container kubernetes security 2025 2026
- **页面抓取**: 成功

### 搜索摘要
December 15, 2025 - 2025 marked important progress in Kubernetes security, with key features graduating to stable status between versions 1.32 and 1.35. These advancements enhance authentication, authorization, workload isolation, and overall hardening for production ...

### 页面正文
It’s time to recap the key Kubernetes security highlights from 2025 and outline features likely to graduate to stable in early 2026.
From a DevSecOps perspective, 2025 brought several meaningful security improvements that directly influenced day-2 operations and production hardening efforts.
With Kubernetes v1.35 scheduled for release on December 17, now is an ideal moment to review the past year’s progress and prepare for what’s ahead.
2025 Kubernetes security: Stable graduates
2025 marked important progress in Kubernetes security, with key features graduating to stable status between versions 1.32 and 1.35. These advancements enhance authentication, authorization, workload isolation, and overall hardening for production cloud-native environments. Here are the most impactful stable graduates from 2025:
| Feature | Stable in | Description | Documentation | 
| Bound ServiceAccount token improvements | v1.33 | Adds unique token IDs and node binding to ServiceAccount tokens, improving validation, auditability, and limiting token reuse or node impersonation. | https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/ | 
| Sidecar containers | v1.33 | Native sidecar containers become a stable Pod lifecycle primitive, making it safer and more reliable to run security agents, proxies, and observability sidecars alongside workloads. | https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ | 
| Recursive read-only (RRO) mounts | v1.33 | Graduate to stable, allowing volumes to be mounted fully read-only (including subpaths), closing write paths that attackers could previously abuse on supposedly read-only mounts. | https://kubernetes.io/blog/2023/10/11/recursive-read-only-mounts-beta/ | 
| Finer-grained authorization using selectors | v1.34 | Authorizers (built-in and webhook) can now make decisions based on field/label selectors, so policies can restrict list/watch/deletecollection requests to, for example, only pods bound to a specific node. | https://github.com/kubernetes/enhancements/issues/4601 and https://kubernetes.io/docs/reference/access-authn-authz/authorization/ | 
| Restrict anonymous requests to specific endpoints | v1.34 | Anonymous access can be limited to an explicit allowlist of endpoints such as /healthz, /readyz, /livez, reducing the blast radius of RBAC misconfigurations that accidentally expose resources to unauthenticated users. | https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests | 
| Ordered namespace deletion | v1.34 | Namespace deletion now follows a structured order so that pods are removed before dependent resources like NetworkPolicies, mitigating gaps where workloads could continue running without the intended network controls (e.g., CVE-2024-7598). | https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/ | 
The future is now: What to expect in 2026
Looking at the alpha and beta features in Kubernetes 1.35 gives us a clear indication of what’s likely to graduate to stable in 2026. These are the advancements that will further solidify Kubernetes as a secure platform:
| Feature | Stage in v1.35 | KEP | Description | Documentation | 
| Harden kubelet serving certificate validation | Alpha new in 1.35 | KEP-4872 | Adds an API-server check that the kubelet’s serving certificate CN matches system:node:<nodename>, closing node-impersonation MitM attacks. | https://github.com/kubernetes/enhancements/issues/4872 | 
| Constrained impersonation | Alpha new in 1.35 | KEP-5284 | Tightens impersonation so that an impersonating user cannot perform actions they themselves are not allowed to do, reducing the risk of over-privileged debug or proxy workflows. | https://github.com/kubernetes/enhancements/issues/5284 | 
| User namespaces for HostNetwork Pods | Alpha new in 1.35 | KEP-5607 | Allows hostNetwork: true pods to keep hostUsers: false, so workloads can access the host network stack without also gaining host user privileges—improving containment if the pod is compromised. | https://github.com/kubernetes/enhancements/issues/5607 | 
| CSI ServiceAccount tokens via Secrets | Alpha new in 1.35 | KEP-5538 | Moves CSI driver ServiceAccount tokens out of volumeContext into a dedicated secrets field, separating sensitive credentials from non-sensitive metadata and reducing accidental leakage. | https://github.com/kubernetes/enhancements/issues/5538 | 
| Robust image pull authorization | Beta new in 1.35 | KEP-2535 | Introduces imagePullCredentialsVerificationPolicy so kubelet can re-verify registry credentials even when images are already cached, closing scenarios where pods could reuse pre-pulled images without proper auth. | https://github.com/kubernetes/enhancements/issues/2535 | 
| Pod certificates for mTLS | Beta promoted in 1.35 | KEP-4317 | The PodCertificateRequest API and PodCertificate volume source move to beta, making it easier to issue workload X.509 certificates for first-class mTLS between pods and the API server or other services. | https://github.com/kubernetes/enhancements/issues/4317 | 
| User namespaces for pods | Beta on-by-default in 1.35 | KEP-127 | Pod-level user namespaces, previously alpha/beta and opt-in, become a more mature hardening option for running root in the pod, unprivileged on the host—improving multitenant isolation. | https://github.com/kubernetes/enhancements/issues/127 | 
| Image volumes (OCI ArtifactImageVolume) | Beta promoted in 1.35 | KEP-4639 | Using OCI images as read-only volumes is now beta, enabling separation of binaries and content. From a security POV, it demands tighter policies around which registries and images may be mounted into pods. | https://github.com/kubernetes/enhancements/issues/4639 | 
Conclusion
User namespaces continue to progress, reaching beta and on-by-default status in recent releases—an important hardening capability for improving workload isolation.
Looking ahead, advancements in secrets management such as Pod certificates for mTLS (beta in v1.35, KEP-4317) and robust image pull authorization (beta, KEP-2535) are poised to strengthen credential handling and workload identity across Kubernetes environments.
Tracking the alpha-to-stable lifecycle remains a helpful practice for DevSecOps teams. Evaluating emerging features in pre-production environments can support informed adoption and help organizations stay ahead of evolving security needs.

---
*检索时间: 2026-07-24 15:38:20*
*搜索来源: DuckDuckGo*
