# Kubernetes Architecture. Kubernetes may be a container | FAUN.dev()

### 来源信息
- **URL**: https://faun.pub/kubernetes-architecture-85ad2999882a
- **域名**: faun.pub
- **检索关键词**: container kubernetes security 2025 2026
- **页面抓取**: 成功

### 搜索摘要
Kubernetes may be a container deployment and management platform that aims to strengthen the Linux container orchestration tools. the…

### 页面正文
Kubernetes may be a container deployment and management platform that aims to strengthen the Linux container orchestration tools.
The expansion of Kubernetes comes from its long experience journey, led by Google for several years before offering it to the open-source community together of the fastest-growing container-based application platforms.
Kubernetes is full of several overwhelming features, including scaling, auto-deployment, and resource management across multiple clusters of hosts.
If you want to Gain In-depth Knowledge of Kubernetes please go through this link Kubernetes Online Training
Magnum makes Kubernetes available within the OpenStack ecosystem. Like Swarm, users can use the Magnum API to manage and operate Kubernetes clusters, objects, and services. Here’s a summary of the main player components within the Kubernetes architecture:
The Kubernetes architecture is modular and exposes several services which will be spread across multiple nodes. Unlike Swarm, Kubernetes uses different terminologies as follows:
Get sindhuja cynixit’s stories in your inbox
Join Medium for free to get updates from this writer.
Get More Info From Kubernetes Certification.
- Pods: a set of containers forming the appliance unit and sharing the networking configuration, namespaces, and storage
- Service: A Kubernetes abstraction layer exposing a group of pods as a service, typically, through a load balancer
From an architectural perspective, Kubernetes essentially defines the subsequent components:
- Master node: This controls and orchestrates the Kubernetes cluster. A master node can run the subsequent services:
- API-server: This provides API endpoints to process RESTful API calls to regulate and manage the cluster
- Controller manager: This embeds several management services including
- Replication controller: This manages pods within the cluster by creating and removing failed pods.
- Endpoint controller: It joins pods by providing cluster endpoints.
- Node controller: This manages node initialization and discovery information within the cloud provider.
- Service controller: This maintains service backends in Kubernetes running behind load balancers. The service controller configures load balancers supported the service state update.
- Scheduler: This decides the pod on which the service deployment should happen. supported the node resource capacity, the scheduler makes sure that the specified service would run onto the nodes belonging to an equivalent pod or across different ones.
- Key-value store: This stores REST API objects like node and pod states, scheduled jobs, service deployment information, and namespaces. Kubernetes utilizes etcd as its main key-value store to share configuration information across the cluster.
- Worker node: It handles the Kubernetes pods and containers runtime environment. Each worker node runs the subsequent components:
- Kubelet: This is often a primary node agent that takes care of containers running in their associated pods. The kubelet process reports the health status of pods and nodes to the master node periodically.
- Docker: This is often the default container runtime engine employed by Kubernetes.
- Kube-proxy: This is often a network proxy to forward requests to the proper container. Kube-proxy routes traffic across pods within an equivalent service.
Follow us on Twitter 🐦 and Facebook 👥 and Instagram 📷 and join our Facebook and Linkedin Groups 💬.
To join our community Slack team chat 🗣️ read our weekly Faun topics 🗞️, and connect with the community 📣 click here⬇

---
*检索时间: 2026-07-24 15:38:17*
*搜索来源: DuckDuckGo*
