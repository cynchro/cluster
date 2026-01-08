# 📘 Clúster GKE – kuepa-cluster

## 1. Información general

- **Proveedor:** Google Cloud Platform
- **Servicio:** Google Kubernetes Engine (GKE)
- **Tipo:** Zonal
- **Zona:** us-central1-c
- **Modo:** Standard
- **Versión Kubernetes:** 1.33.5-gke.1162000
- **Fecha del relevamiento:** 2026-01-08

## 2. Infraestructura GKE

- **Red:** default
- **Subred:** default

### Node Pools

| Node Pool | Machine Type | Autoscaling | Min | Max |
|---|---|---|---|---|
| kuepa-pool | e2-standard-4 | Sí | 1 | 6 |

## 3. Namespaces

| Namespace | Propósito |
|---|---|
| default | No documentado |
| dev | No documentado |
| gke-managed-system | No documentado |
| gke-managed-volumepopulator | No documentado |
| kube-node-lease | No documentado |
| kube-public | No documentado |
| kube-system | No documentado |
| kuepa | No documentado |
| kuepa-infra | No documentado |

## 4. Aplicaciones desplegadas

| Namespace | Aplicación | Tipo | Réplicas |
|---|---|---|---|
| dev | leadhub | Deployment | 1 |
| dev | leadhub-agent | Deployment | 1 |
| dev | leadhub-campaign-execution | Deployment | 2 |
| dev | leadhub-client | Deployment | 1 |
| dev | leadhub-connect | Deployment | 1 |
| dev | leadhub-copilot | Deployment | 1 |
| dev | leadhub-landing | Deployment | 1 |
| dev | leadhub-pinecone | Deployment | 1 |
| dev | leadhub-trigger-execution | Deployment | 1 |
| dev | lookeye-nexus | Deployment | 0 |
| dev | lookeye-openai | Deployment | 0 |
| dev | lookeye-stage1 | Deployment | 0 |
| dev | lookeye-stage2 | Deployment | 0 |
| dev | lookeye-stage3 | Deployment | 0 |
| dev | mongodb | Deployment | 1 |
| dev | realtime-agent | Deployment | 1 |
| dev | twilio-agentic-voice | Deployment | 1 |
| dev | uk-chatbot-student | Deployment | 0 |
| dev | uk-clacciari | Deployment | 1 |
| dev | uk-cleverclass | Deployment | 1 |
| dev | uk-elelem | Deployment | 1 |
| dev | uk-emipago | Deployment | 0 |
| dev | uk-portal-prepa | Deployment | 1 |
| dev | uk-promptgrounds | Deployment | 1 |
| dev | uk-qa-content | Deployment | 1 |
| dev | uk-qa-emiforce | Deployment | 1 |
| dev | uk-qa-emipago | Deployment | 1 |
| dev | uk-qa-leads | Deployment | 1 |
| dev | uk-qa-platform | Deployment | 1 |
| dev | uk-rex | Deployment | 0 |
| dev | uk-rex-client | Deployment | 0 |
| dev | uk-soyalumno | Deployment | 0 |
| dev | uk-streaming | Deployment | 1 |
| dev | uk-test | Deployment | 0 |
| dev | uk-twilio-tooling | Deployment | 1 |
| kube-system | event-exporter-gke | Deployment | 1 |
| kube-system | konnectivity-agent | Deployment | 5 |
| kube-system | konnectivity-agent-autoscaler | Deployment | 1 |
| kube-system | kube-dns | Deployment | 2 |
| kube-system | kube-dns-autoscaler | Deployment | 1 |
| kube-system | l7-default-backend | Deployment | 1 |
| kube-system | metrics-server-v1.33.0 | Deployment | 1 |
| kuepa-infra | langfuse | Deployment | 0 |
| kuepa-infra | wireguard | Deployment | 1 |
| kuepa | ex-cannid | Deployment | 1 |
| kuepa | ex-cannid-front | Deployment | 1 |
| kuepa | flexchat-nest | Deployment | 0 |
| kuepa | flexchat-ui | Deployment | 0 |
| kuepa | flexmobile | Deployment | 0 |
| kuepa | grafana-k8s-monitoring-kube-state-metrics | Deployment | 1 |
| kuepa | grafana-k8s-monitoring-opencost | Deployment | 1 |
| kuepa | mongodb-emi | Deployment | 1 |
| kuepa | my-mc-deployment | Deployment | 1 |
| kuepa | plugin-update-lead | Deployment | 1 |
| kuepa | react-flexmobile | Deployment | 0 |
| kuepa | redirect-notfound | Deployment | 1 |
| kuepa | uk-analytic | Deployment | 1 |
| kuepa | uk-broker | Deployment | 0 |
| kuepa | uk-care-bot-api | Deployment | 1 |
| kuepa | uk-care-bot-worker | Deployment | 1 |
| kuepa | uk-certificate | Deployment | 1 |
| kuepa | uk-chatbot | Deployment | 0 |
| kuepa | uk-chatbot-student | Deployment | 0 |
| kuepa | uk-chatbot-student-demo | Deployment | 0 |
| kuepa | uk-cloud-client | Deployment | 0 |
| kuepa | uk-comodin | Deployment | 1 |
| kuepa | uk-content | Deployment | 1 |
| kuepa | uk-course-gen-api | Deployment | 1 |
| kuepa | uk-course-gen-nest-api | Deployment | 1 |
| kuepa | uk-course-gen-nest-workers | Deployment | 1 |
| kuepa | uk-deluca | Deployment | 1 |
| kuepa | uk-demo-lead | Deployment | 1 |
| kuepa | uk-elelem | Deployment | 1 |
| kuepa | uk-embeddings | Deployment | 1 |
| kuepa | uk-emiconnect | Deployment | 1 |
| kuepa | uk-emidrive | Deployment | 1 |
| kuepa | uk-emiforce | Deployment | 1 |
| kuepa | uk-emipago | Deployment | 1 |
| kuepa | uk-emiportal | Deployment | 1 |
| kuepa | uk-emisign | Deployment | 1 |
| kuepa | uk-ensamble | Deployment | 1 |
| kuepa | uk-event | Deployment | 0 |
| kuepa | uk-facturapi | Deployment | 0 |
| kuepa | uk-fee | Deployment | 1 |
| kuepa | uk-lead | Deployment | 2 |
| kuepa | uk-lead-checkout | Deployment | 1 |
| kuepa | uk-lead-client | Deployment | 1 |
| kuepa | uk-lead-client-qa | Deployment | 1 |
| kuepa | uk-leadhub | Deployment | 1 |
| kuepa | uk-learnix | Deployment | 1 |
| kuepa | uk-luka | Deployment | 1 |
| kuepa | uk-luzbelito | Deployment | 1 |
| kuepa | uk-marketing-backend | Deployment | 1 |
| kuepa | uk-marketing-frontend | Deployment | 1 |
| kuepa | uk-platform | Deployment | 1 |
| kuepa | uk-player | Deployment | 1 |
| kuepa | uk-power-dialer | Deployment | 1 |
| kuepa | uk-prepa | Deployment | 1 |
| kuepa | uk-prepa-client | Deployment | 1 |
| kuepa | uk-prepa-webchat | Deployment | 1 |
| kuepa | uk-prepa-webchat-client | Deployment | 1 |
| kuepa | uk-quantico | Deployment | 1 |
| kuepa | uk-realtime-agents | Deployment | 1 |
| kuepa | uk-reddit-comments | Deployment | 1 |
| kuepa | uk-report-api | Deployment | 1 |
| kuepa | uk-report-redis | Deployment | 1 |
| kuepa | uk-report-worker | Deployment | 1 |
| kuepa | uk-soyalumno | Deployment | 1 |
| kuepa | uk-storage | Deployment | 1 |
| kuepa | uk-subscriptions | Deployment | 0 |
| kuepa | uk-teachers | Deployment | 1 |
| kuepa | uk-twiliano | Deployment | 1 |
| kuepa | uk-twiliano-dev | Deployment | 0 |
| kuepa | uk-voice-plugin | Deployment | 1 |
| kuepa | uk-webchat | Deployment | 1 |
| kuepa | uk-webchat-client | Deployment | 1 |
| kuepa | uk-witte | Deployment | 1 |
| dev | redis-dev-master | StatefulSet | 1 |
| dev | redis-dev-replicas | StatefulSet | 1 |
| kuepa-infra | langfuse-pgsql-postgresql | StatefulSet | 0 |
| kuepa | grafana-k8s-monitoring-grafana-agent | StatefulSet | 1 |
| kuepa | leadhub-campaign-redis | StatefulSet | 1 |
| kuepa | leadhub-redis-master | StatefulSet | 1 |
| kuepa | leadhub-redis-replica | StatefulSet | 1 |
| kuepa | redis-master | StatefulSet | 1 |
| kuepa | redis-replicas | StatefulSet | 1 |
| kuepa | uk-care-redis | StatefulSet | 1 |
| kube-system | efficiency-daemon | DaemonSet | - |
| kube-system | fluentbit-gke | DaemonSet | - |
| kube-system | fluentbit-gke-256pd | DaemonSet | - |
| kube-system | fluentbit-gke-managed-node-big | DaemonSet | - |
| kube-system | fluentbit-gke-managed-node-small | DaemonSet | - |
| kube-system | fluentbit-gke-max | DaemonSet | - |
| kube-system | gke-metrics-agent | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-10 | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-100 | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-20 | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-200 | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-50 | DaemonSet | - |
| kube-system | gke-metrics-agent-scaling-500 | DaemonSet | - |
| kube-system | gke-metrics-agent-windows | DaemonSet | - |
| kube-system | kube-proxy | DaemonSet | - |
| kube-system | maintenance-handler | DaemonSet | - |
| kube-system | metadata-proxy-v0.1 | DaemonSet | - |
| kube-system | nccl-fastsocket-installer | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-large-cos | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-large-ubuntu | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-medium-cos | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-medium-ubuntu | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-small-cos | DaemonSet | - |
| kube-system | nvidia-gpu-device-plugin-small-ubuntu | DaemonSet | - |
| kube-system | pdcsi-node | DaemonSet | - |
| kube-system | pdcsi-node-windows | DaemonSet | - |
| kube-system | runsc-metric-server | DaemonSet | - |
| kube-system | tpu-device-plugin | DaemonSet | - |
| kuepa | grafana-k8s-monitoring-grafana-agent-logs | DaemonSet | - |
| kuepa | grafana-k8s-monitoring-prometheus-node-exporter | DaemonSet | - |
| kuepa | lead-future-contact-afternoon-29263155 | Job | - |
| kuepa | lead-reassign-massive-29464500 | Job | - |
| kuepa | reddit-search-bot-weekly-29329020 | Job | - |
| kuepa | reddit-search-bot-weekly-29449980 | Job | - |
| kuepa | reddit-search-bot-weekly-29460060 | Job | - |
| kuepa | uk-copilot-segment-29461200 | Job | - |
| kuepa | uk-copilot-segment-29464080 | Job | - |
| kuepa | uk-emiconnect-classroom-28506960 | Job | - |
| kuepa | uk-emiconnect-classroom-29464560 | Job | - |
| kuepa | uk-emiconnect-cleverclass-classroom-29453760 | Job | - |
| kuepa | uk-emiconnect-emipago-payments-29162560 | Job | - |
| kuepa | uk-emiconnect-emipago-payments-29464600 | Job | - |
| kuepa | uk-emiconnect-salesforce-contacts-29326515 | Job | - |
| kuepa | uk-emiconnect-salesforce-contacts-29464575 | Job | - |
| kuepa | uk-emiconnect-twilio-calls-29326590 | Job | - |
| kuepa | uk-emiconnect-twilio-calls-29464590 | Job | - |
| kuepa | uk-emiconnect-twilio-messages-29326590 | Job | - |
| kuepa | uk-emiconnect-twilio-messages-29464590 | Job | - |
| kuepa | uk-ensamble-massive-analysis-29232480 | Job | - |
| kuepa | uk-ensamble-massive-analysis-29464320 | Job | - |
| kuepa | uk-soyalumno-conversations-29464200 | Job | - |
| kuepa | uk-subscriptions-debit-28736160 | Job | - |
| kuepa | uk-subscriptions-debit-28788000 | Job | - |
| kuepa | uk-subscriptions-debit-manual | Job | - |
| kuepa | uk-task-comments-29464080 | Job | - |
| kuepa | youtube-search-bot-weekly-29449980 | Job | - |
| kuepa | youtube-search-bot-weekly-29460060 | Job | - |
| kuepa | lead-future-contact-afternoon | CronJob | - |
| kuepa | lead-future-contact-night | CronJob | - |
| kuepa | lead-reassign-massive | CronJob | - |
| kuepa | reddit-search-bot-weekly | CronJob | - |
| kuepa | uk-copilot-segment | CronJob | - |
| kuepa | uk-emiconnect-classroom | CronJob | - |
| kuepa | uk-emiconnect-cleverclass-classroom | CronJob | - |
| kuepa | uk-emiconnect-emipago-payments | CronJob | - |
| kuepa | uk-emiconnect-salesforce-contacts | CronJob | - |
| kuepa | uk-emiconnect-twilio-calls | CronJob | - |
| kuepa | uk-emiconnect-twilio-messages | CronJob | - |
| kuepa | uk-ensamble-massive-analysis | CronJob | - |
| kuepa | uk-soyalumno-conversations | CronJob | - |
| kuepa | uk-subscriptions-debit | CronJob | - |
| kuepa | uk-task-comments | CronJob | - |
| kuepa | youtube-search-bot-weekly | CronJob | - |

## 5. Exposición (Ingress)

| Namespace | Ingress | Host | Público |
|---|---|---|---|
| dev | nexus-ingress | dev.universidaduk.com | Sí |
| kuepa | client-ingress-rules | chat.universidaduk.com | Sí |
| kuepa | uk-chatbot-ingress | chatbot.universidaduk.com | Sí |
| kuepa | uk-course-gen-api-ingress | uk-course-gen-api.kuepa.io | Sí |
| kuepa | uk-course-gen-ingress | uk-course-gen.kuepa.io | Sí |
| kuepa | uk-course-gen-nest-api-ingress | uk-course-gen-nest.kuepa.io | Sí |

## 6. Secrets

| Secret | Namespace | Usado por |
|---|---|---|
| google-cloud-credentials | default | No identificado |
| ranchi-cfg | default | No identificado |
| google-ads-client-secret | dev | No identificado |
| google-ads-token-secret | dev | No identificado |
| google-cloud-credentials | dev | No identificado |
| leadhub-agent-secret | dev | No identificado |
| leadhub-campaign-secret | dev | No identificado |
| leadhub-connect-secret | dev | No identificado |
| leadhub-copilot-secret | dev | No identificado |
| leadhub-pinecone-secret | dev | No identificado |
| leadhub-secret | dev | No identificado |
| lookeye-nexus-acc | dev | No identificado |
| mongodb | dev | No identificado |
| ranchi-cfg | dev | No identificado |
| realtime-agent-secret | dev | No identificado |
| sh.helm.release.v1.mongodb.v1 | dev | No identificado |
| sh.helm.release.v1.redis-dev.v1 | dev | No identificado |
| sub.universidaduk.com | dev | No identificado |
| uk-clacciari-cfg | dev | No identificado |
| uk-cleverclass-cfg | dev | No identificado |
| uk-emiconnect-cfg | dev | No identificado |
| uk-emipago-cfg | dev | No identificado |
| uk-promptgrounds-cfg | dev | No identificado |
| uk-qa-emiforce-cfg | dev | No identificado |
| uk-qa-emipago-cfg | dev | No identificado |
| uk-qa-leads-cfg | dev | No identificado |
| uk-qa-platform-cfg | dev | No identificado |
| uk-rex-cfg | dev | No identificado |
| uk-soyalumno-cfg | dev | No identificado |
| uk-test-secret | dev | No identificado |
| langfuse-pgsql-postgresql | kuepa-infra | No identificado |
| lead-next-secret | kuepa-infra | No identificado |
| prepagratis-secret | kuepa-infra | No identificado |
| sh.helm.release.v1.langfuse-pgsql.v1 | kuepa-infra | No identificado |
| sub.universidaduk.com | kuepa-infra | No identificado |
| tls-secret | kuepa-infra | No identificado |
| ex-cannid-cfg | kuepa | No identificado |
| flexchat-gcp-sac | kuepa | No identificado |
| flexchat-ui-cfg | kuepa | No identificado |
| gcp-credentials | kuepa | No identificado |
| google-credentials | kuepa | No identificado |
| google-credentials-nest | kuepa | No identificado |
| google-credentials-test | kuepa | No identificado |
| loki-k8s-monitoring | kuepa | No identificado |
| mongodb-emi | kuepa | No identificado |
| plugin-update-lead-cfg | kuepa | No identificado |
| prometheus-k8s-monitoring | kuepa | No identificado |
| reddit-search-bot | kuepa | No identificado |
| sh.helm.release.v1.grafana-k8s-monitoring.v1 | kuepa | No identificado |
| sh.helm.release.v1.mongodb-emi.v1 | kuepa | No identificado |
| sh.helm.release.v1.redis.v1 | kuepa | No identificado |
| sub.universidaduk.com | kuepa | No identificado |
| sub.universidaduk.com.temp | kuepa | No identificado |
| tempo-k8s-monitoring | kuepa | No identificado |
| uk-analytic-cfg | kuepa | No identificado |
| uk-broker-cfg | kuepa | No identificado |
| uk-care-bot-secrets | kuepa | No identificado |
| uk-certificate-cfg | kuepa | No identificado |
| uk-comodin-cfg | kuepa | No identificado |
| uk-course-gen-cfg | kuepa | No identificado |
| uk-course-gen-nest-secrets | kuepa | No identificado |
| uk-course-gen-secrets | kuepa | No identificado |
| uk-course-gen-secrets-test | kuepa | No identificado |
| uk-emiconnect-cfg | kuepa | No identificado |
| uk-emidrive-cfg | kuepa | No identificado |
| uk-emiforce-cfg | kuepa | No identificado |
| uk-emipago-cfg | kuepa | No identificado |
| uk-emiportal-cfg | kuepa | No identificado |
| uk-emisign-cfg | kuepa | No identificado |
| uk-ensamble-cfg | kuepa | No identificado |
| uk-event-cfg | kuepa | No identificado |
| uk-fee-cfg | kuepa | No identificado |
| uk-lead-cfg | kuepa | No identificado |
| uk-leadhub-cfg | kuepa | No identificado |
| uk-learnix-cfg | kuepa | No identificado |
| uk-luka-cfg | kuepa | No identificado |
| uk-luzbelito-cfg | kuepa | No identificado |
| uk-luzbelito-secrets | kuepa | No identificado |
| uk-marketing-secrets | kuepa | No identificado |
| uk-platform-cfg | kuepa | No identificado |
| uk-prepa-cfg | kuepa | No identificado |
| uk-prepa-webchat-cfg | kuepa | No identificado |
| uk-quantico-cfg | kuepa | No identificado |
| uk-reddit-comments-creds | kuepa | No identificado |
| uk-report-secrets | kuepa | No identificado |
| uk-soyalumno-cfg | kuepa | No identificado |
| uk-storage-cfg | kuepa | No identificado |
| uk-subscriptions-cfg | kuepa | No identificado |
| uk-twiliano-cfg | kuepa | No identificado |
| uk-twiliano-dev-cfg | kuepa | No identificado |
| uk-voice-plugin-cfg | kuepa | No identificado |
| uk-webchat-cfg | kuepa | No identificado |
| uk-witte-cfg | kuepa | No identificado |
| youtube-search-bot | kuepa | No identificado |

## 7. Persistencia

| PVC | Namespace | Tamaño | Uso |
|---|---|---|---|
| mongodb | dev | 16Gi | No documentado |
| redis-data-redis-dev-master-0 | dev | 8Gi | No documentado |
| redis-data-redis-dev-replicas-0 | dev | 8Gi | No documentado |
| data-langfuse-pgsql-postgresql-0 | kuepa-infra | 200Gi | No documentado |
| pv-claim-wireguard | kuepa-infra | 10M | No documentado |
| mongodb-emi | kuepa | 8Gi | No documentado |
| redis-data-leadhub-campaign-redis-0 | kuepa | 20Gi | No documentado |
| redis-data-leadhub-redis-master-0 | kuepa | 20Gi | No documentado |
| redis-data-leadhub-redis-replica-0 | kuepa | 20Gi | No documentado |
| redis-data-redis-master-0 | kuepa | 30Gi | No documentado |
| redis-data-redis-replicas-0 | kuepa | 30Gi | No documentado |
| redis-data-uk-care-redis-0 | kuepa | 2Gi | No documentado |

## 8. Anexos

- Snapshot completo en `/app/output/`
- Relevamiento 100% read-only


## Diagrama de arquitectura

```mermaid
graph TD

GCP[GCP Project]
VPC[VPC: default]
CLUSTER[GKE: kuepa-cluster\nus-central1-c]

GCP --> VPC --> CLUSTER

CLUSTER --> NP_kuepa-pool[NodePool: kuepa-pool]

CLUSTER --> NS_dev[Namespace: dev]
NS_dev --> APP_dev_leadhub[leadhub]
NS_dev --> APP_dev_leadhub-agent[leadhub-agent]
NS_dev --> APP_dev_leadhub-campaign-execution[leadhub-campaign-execution]
NS_dev --> APP_dev_leadhub-client[leadhub-client]
NS_dev --> APP_dev_leadhub-connect[leadhub-connect]
NS_dev --> APP_dev_leadhub-copilot[leadhub-copilot]
NS_dev --> APP_dev_leadhub-landing[leadhub-landing]
NS_dev --> APP_dev_leadhub-pinecone[leadhub-pinecone]
NS_dev --> APP_dev_leadhub-trigger-execution[leadhub-trigger-execution]
NS_dev --> APP_dev_lookeye-nexus[lookeye-nexus]
NS_dev --> APP_dev_lookeye-openai[lookeye-openai]
NS_dev --> APP_dev_lookeye-stage1[lookeye-stage1]
NS_dev --> APP_dev_lookeye-stage2[lookeye-stage2]
NS_dev --> APP_dev_lookeye-stage3[lookeye-stage3]
NS_dev --> APP_dev_mongodb[mongodb]
NS_dev --> APP_dev_realtime-agent[realtime-agent]
NS_dev --> APP_dev_twilio-agentic-voice[twilio-agentic-voice]
NS_dev --> APP_dev_uk-chatbot-student[uk-chatbot-student]
NS_dev --> APP_dev_uk-clacciari[uk-clacciari]
NS_dev --> APP_dev_uk-cleverclass[uk-cleverclass]
NS_dev --> APP_dev_uk-elelem[uk-elelem]
NS_dev --> APP_dev_uk-emipago[uk-emipago]
NS_dev --> APP_dev_uk-portal-prepa[uk-portal-prepa]
NS_dev --> APP_dev_uk-promptgrounds[uk-promptgrounds]
NS_dev --> APP_dev_uk-qa-content[uk-qa-content]
NS_dev --> APP_dev_uk-qa-emiforce[uk-qa-emiforce]
NS_dev --> APP_dev_uk-qa-emipago[uk-qa-emipago]
NS_dev --> APP_dev_uk-qa-leads[uk-qa-leads]
NS_dev --> APP_dev_uk-qa-platform[uk-qa-platform]
NS_dev --> APP_dev_uk-rex[uk-rex]
NS_dev --> APP_dev_uk-rex-client[uk-rex-client]
NS_dev --> APP_dev_uk-soyalumno[uk-soyalumno]
NS_dev --> APP_dev_uk-streaming[uk-streaming]
NS_dev --> APP_dev_uk-test[uk-test]
NS_dev --> APP_dev_uk-twilio-tooling[uk-twilio-tooling]
NS_dev --> APP_dev_redis-dev-master[redis-dev-master]
NS_dev --> APP_dev_redis-dev-replicas[redis-dev-replicas]
CLUSTER --> NS_kube-system[Namespace: kube-system]
NS_kube-system --> APP_kube-system_event-exporter-gke[event-exporter-gke]
NS_kube-system --> APP_kube-system_konnectivity-agent[konnectivity-agent]
NS_kube-system --> APP_kube-system_konnectivity-agent-autoscaler[konnectivity-agent-autoscaler]
NS_kube-system --> APP_kube-system_kube-dns[kube-dns]
NS_kube-system --> APP_kube-system_kube-dns-autoscaler[kube-dns-autoscaler]
NS_kube-system --> APP_kube-system_l7-default-backend[l7-default-backend]
NS_kube-system --> APP_kube-system_metrics-server-v1.33.0[metrics-server-v1.33.0]
NS_kube-system --> APP_kube-system_efficiency-daemon[efficiency-daemon]
NS_kube-system --> APP_kube-system_fluentbit-gke[fluentbit-gke]
NS_kube-system --> APP_kube-system_fluentbit-gke-256pd[fluentbit-gke-256pd]
NS_kube-system --> APP_kube-system_fluentbit-gke-managed-node-big[fluentbit-gke-managed-node-big]
NS_kube-system --> APP_kube-system_fluentbit-gke-managed-node-small[fluentbit-gke-managed-node-small]
NS_kube-system --> APP_kube-system_fluentbit-gke-max[fluentbit-gke-max]
NS_kube-system --> APP_kube-system_gke-metrics-agent[gke-metrics-agent]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-10[gke-metrics-agent-scaling-10]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-100[gke-metrics-agent-scaling-100]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-20[gke-metrics-agent-scaling-20]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-200[gke-metrics-agent-scaling-200]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-50[gke-metrics-agent-scaling-50]
NS_kube-system --> APP_kube-system_gke-metrics-agent-scaling-500[gke-metrics-agent-scaling-500]
NS_kube-system --> APP_kube-system_gke-metrics-agent-windows[gke-metrics-agent-windows]
NS_kube-system --> APP_kube-system_kube-proxy[kube-proxy]
NS_kube-system --> APP_kube-system_maintenance-handler[maintenance-handler]
NS_kube-system --> APP_kube-system_metadata-proxy-v0.1[metadata-proxy-v0.1]
NS_kube-system --> APP_kube-system_nccl-fastsocket-installer[nccl-fastsocket-installer]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-large-cos[nvidia-gpu-device-plugin-large-cos]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-large-ubuntu[nvidia-gpu-device-plugin-large-ubuntu]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-medium-cos[nvidia-gpu-device-plugin-medium-cos]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-medium-ubuntu[nvidia-gpu-device-plugin-medium-ubuntu]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-small-cos[nvidia-gpu-device-plugin-small-cos]
NS_kube-system --> APP_kube-system_nvidia-gpu-device-plugin-small-ubuntu[nvidia-gpu-device-plugin-small-ubuntu]
NS_kube-system --> APP_kube-system_pdcsi-node[pdcsi-node]
NS_kube-system --> APP_kube-system_pdcsi-node-windows[pdcsi-node-windows]
NS_kube-system --> APP_kube-system_runsc-metric-server[runsc-metric-server]
NS_kube-system --> APP_kube-system_tpu-device-plugin[tpu-device-plugin]
CLUSTER --> NS_kuepa-infra[Namespace: kuepa-infra]
NS_kuepa-infra --> APP_kuepa-infra_langfuse[langfuse]
NS_kuepa-infra --> APP_kuepa-infra_wireguard[wireguard]
NS_kuepa-infra --> APP_kuepa-infra_langfuse-pgsql-postgresql[langfuse-pgsql-postgresql]
CLUSTER --> NS_kuepa[Namespace: kuepa]
NS_kuepa --> APP_kuepa_ex-cannid[ex-cannid]
NS_kuepa --> APP_kuepa_ex-cannid-front[ex-cannid-front]
NS_kuepa --> APP_kuepa_flexchat-nest[flexchat-nest]
NS_kuepa --> APP_kuepa_flexchat-ui[flexchat-ui]
NS_kuepa --> APP_kuepa_flexmobile[flexmobile]
NS_kuepa --> APP_kuepa_grafana-k8s-monitoring-kube-state-metrics[grafana-k8s-monitoring-kube-state-metrics]
NS_kuepa --> APP_kuepa_grafana-k8s-monitoring-opencost[grafana-k8s-monitoring-opencost]
NS_kuepa --> APP_kuepa_mongodb-emi[mongodb-emi]
NS_kuepa --> APP_kuepa_my-mc-deployment[my-mc-deployment]
NS_kuepa --> APP_kuepa_plugin-update-lead[plugin-update-lead]
NS_kuepa --> APP_kuepa_react-flexmobile[react-flexmobile]
NS_kuepa --> APP_kuepa_redirect-notfound[redirect-notfound]
NS_kuepa --> APP_kuepa_uk-analytic[uk-analytic]
NS_kuepa --> APP_kuepa_uk-broker[uk-broker]
NS_kuepa --> APP_kuepa_uk-care-bot-api[uk-care-bot-api]
NS_kuepa --> APP_kuepa_uk-care-bot-worker[uk-care-bot-worker]
NS_kuepa --> APP_kuepa_uk-certificate[uk-certificate]
NS_kuepa --> APP_kuepa_uk-chatbot[uk-chatbot]
NS_kuepa --> APP_kuepa_uk-chatbot-student[uk-chatbot-student]
NS_kuepa --> APP_kuepa_uk-chatbot-student-demo[uk-chatbot-student-demo]
NS_kuepa --> APP_kuepa_uk-cloud-client[uk-cloud-client]
NS_kuepa --> APP_kuepa_uk-comodin[uk-comodin]
NS_kuepa --> APP_kuepa_uk-content[uk-content]
NS_kuepa --> APP_kuepa_uk-course-gen-api[uk-course-gen-api]
NS_kuepa --> APP_kuepa_uk-course-gen-nest-api[uk-course-gen-nest-api]
NS_kuepa --> APP_kuepa_uk-course-gen-nest-workers[uk-course-gen-nest-workers]
NS_kuepa --> APP_kuepa_uk-deluca[uk-deluca]
NS_kuepa --> APP_kuepa_uk-demo-lead[uk-demo-lead]
NS_kuepa --> APP_kuepa_uk-elelem[uk-elelem]
NS_kuepa --> APP_kuepa_uk-embeddings[uk-embeddings]
NS_kuepa --> APP_kuepa_uk-emiconnect[uk-emiconnect]
NS_kuepa --> APP_kuepa_uk-emidrive[uk-emidrive]
NS_kuepa --> APP_kuepa_uk-emiforce[uk-emiforce]
NS_kuepa --> APP_kuepa_uk-emipago[uk-emipago]
NS_kuepa --> APP_kuepa_uk-emiportal[uk-emiportal]
NS_kuepa --> APP_kuepa_uk-emisign[uk-emisign]
NS_kuepa --> APP_kuepa_uk-ensamble[uk-ensamble]
NS_kuepa --> APP_kuepa_uk-event[uk-event]
NS_kuepa --> APP_kuepa_uk-facturapi[uk-facturapi]
NS_kuepa --> APP_kuepa_uk-fee[uk-fee]
NS_kuepa --> APP_kuepa_uk-lead[uk-lead]
NS_kuepa --> APP_kuepa_uk-lead-checkout[uk-lead-checkout]
NS_kuepa --> APP_kuepa_uk-lead-client[uk-lead-client]
NS_kuepa --> APP_kuepa_uk-lead-client-qa[uk-lead-client-qa]
NS_kuepa --> APP_kuepa_uk-leadhub[uk-leadhub]
NS_kuepa --> APP_kuepa_uk-learnix[uk-learnix]
NS_kuepa --> APP_kuepa_uk-luka[uk-luka]
NS_kuepa --> APP_kuepa_uk-luzbelito[uk-luzbelito]
NS_kuepa --> APP_kuepa_uk-marketing-backend[uk-marketing-backend]
NS_kuepa --> APP_kuepa_uk-marketing-frontend[uk-marketing-frontend]
NS_kuepa --> APP_kuepa_uk-platform[uk-platform]
NS_kuepa --> APP_kuepa_uk-player[uk-player]
NS_kuepa --> APP_kuepa_uk-power-dialer[uk-power-dialer]
NS_kuepa --> APP_kuepa_uk-prepa[uk-prepa]
NS_kuepa --> APP_kuepa_uk-prepa-client[uk-prepa-client]
NS_kuepa --> APP_kuepa_uk-prepa-webchat[uk-prepa-webchat]
NS_kuepa --> APP_kuepa_uk-prepa-webchat-client[uk-prepa-webchat-client]
NS_kuepa --> APP_kuepa_uk-quantico[uk-quantico]
NS_kuepa --> APP_kuepa_uk-realtime-agents[uk-realtime-agents]
NS_kuepa --> APP_kuepa_uk-reddit-comments[uk-reddit-comments]
NS_kuepa --> APP_kuepa_uk-report-api[uk-report-api]
NS_kuepa --> APP_kuepa_uk-report-redis[uk-report-redis]
NS_kuepa --> APP_kuepa_uk-report-worker[uk-report-worker]
NS_kuepa --> APP_kuepa_uk-soyalumno[uk-soyalumno]
NS_kuepa --> APP_kuepa_uk-storage[uk-storage]
NS_kuepa --> APP_kuepa_uk-subscriptions[uk-subscriptions]
NS_kuepa --> APP_kuepa_uk-teachers[uk-teachers]
NS_kuepa --> APP_kuepa_uk-twiliano[uk-twiliano]
NS_kuepa --> APP_kuepa_uk-twiliano-dev[uk-twiliano-dev]
NS_kuepa --> APP_kuepa_uk-voice-plugin[uk-voice-plugin]
NS_kuepa --> APP_kuepa_uk-webchat[uk-webchat]
NS_kuepa --> APP_kuepa_uk-webchat-client[uk-webchat-client]
NS_kuepa --> APP_kuepa_uk-witte[uk-witte]
NS_kuepa --> APP_kuepa_grafana-k8s-monitoring-grafana-agent[grafana-k8s-monitoring-grafana-agent]
NS_kuepa --> APP_kuepa_leadhub-campaign-redis[leadhub-campaign-redis]
NS_kuepa --> APP_kuepa_leadhub-redis-master[leadhub-redis-master]
NS_kuepa --> APP_kuepa_leadhub-redis-replica[leadhub-redis-replica]
NS_kuepa --> APP_kuepa_redis-master[redis-master]
NS_kuepa --> APP_kuepa_redis-replicas[redis-replicas]
NS_kuepa --> APP_kuepa_uk-care-redis[uk-care-redis]
NS_kuepa --> APP_kuepa_grafana-k8s-monitoring-grafana-agent-logs[grafana-k8s-monitoring-grafana-agent-logs]
NS_kuepa --> APP_kuepa_grafana-k8s-monitoring-prometheus-node-exporter[grafana-k8s-monitoring-prometheus-node-exporter]
NS_kuepa --> APP_kuepa_lead-future-contact-afternoon-29263155[lead-future-contact-afternoon-29263155]
NS_kuepa --> APP_kuepa_lead-reassign-massive-29464500[lead-reassign-massive-29464500]
NS_kuepa --> APP_kuepa_reddit-search-bot-weekly-29329020[reddit-search-bot-weekly-29329020]
NS_kuepa --> APP_kuepa_reddit-search-bot-weekly-29449980[reddit-search-bot-weekly-29449980]
NS_kuepa --> APP_kuepa_reddit-search-bot-weekly-29460060[reddit-search-bot-weekly-29460060]
NS_kuepa --> APP_kuepa_uk-copilot-segment-29461200[uk-copilot-segment-29461200]
NS_kuepa --> APP_kuepa_uk-copilot-segment-29464080[uk-copilot-segment-29464080]
NS_kuepa --> APP_kuepa_uk-emiconnect-classroom-28506960[uk-emiconnect-classroom-28506960]
NS_kuepa --> APP_kuepa_uk-emiconnect-classroom-29464560[uk-emiconnect-classroom-29464560]
NS_kuepa --> APP_kuepa_uk-emiconnect-cleverclass-classroom-29453760[uk-emiconnect-cleverclass-classroom-29453760]
NS_kuepa --> APP_kuepa_uk-emiconnect-emipago-payments-29162560[uk-emiconnect-emipago-payments-29162560]
NS_kuepa --> APP_kuepa_uk-emiconnect-emipago-payments-29464600[uk-emiconnect-emipago-payments-29464600]
NS_kuepa --> APP_kuepa_uk-emiconnect-salesforce-contacts-29326515[uk-emiconnect-salesforce-contacts-29326515]
NS_kuepa --> APP_kuepa_uk-emiconnect-salesforce-contacts-29464575[uk-emiconnect-salesforce-contacts-29464575]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-calls-29326590[uk-emiconnect-twilio-calls-29326590]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-calls-29464590[uk-emiconnect-twilio-calls-29464590]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-messages-29326590[uk-emiconnect-twilio-messages-29326590]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-messages-29464590[uk-emiconnect-twilio-messages-29464590]
NS_kuepa --> APP_kuepa_uk-ensamble-massive-analysis-29232480[uk-ensamble-massive-analysis-29232480]
NS_kuepa --> APP_kuepa_uk-ensamble-massive-analysis-29464320[uk-ensamble-massive-analysis-29464320]
NS_kuepa --> APP_kuepa_uk-soyalumno-conversations-29464200[uk-soyalumno-conversations-29464200]
NS_kuepa --> APP_kuepa_uk-subscriptions-debit-28736160[uk-subscriptions-debit-28736160]
NS_kuepa --> APP_kuepa_uk-subscriptions-debit-28788000[uk-subscriptions-debit-28788000]
NS_kuepa --> APP_kuepa_uk-subscriptions-debit-manual[uk-subscriptions-debit-manual]
NS_kuepa --> APP_kuepa_uk-task-comments-29464080[uk-task-comments-29464080]
NS_kuepa --> APP_kuepa_youtube-search-bot-weekly-29449980[youtube-search-bot-weekly-29449980]
NS_kuepa --> APP_kuepa_youtube-search-bot-weekly-29460060[youtube-search-bot-weekly-29460060]
NS_kuepa --> APP_kuepa_lead-future-contact-afternoon[lead-future-contact-afternoon]
NS_kuepa --> APP_kuepa_lead-future-contact-night[lead-future-contact-night]
NS_kuepa --> APP_kuepa_lead-reassign-massive[lead-reassign-massive]
NS_kuepa --> APP_kuepa_reddit-search-bot-weekly[reddit-search-bot-weekly]
NS_kuepa --> APP_kuepa_uk-copilot-segment[uk-copilot-segment]
NS_kuepa --> APP_kuepa_uk-emiconnect-classroom[uk-emiconnect-classroom]
NS_kuepa --> APP_kuepa_uk-emiconnect-cleverclass-classroom[uk-emiconnect-cleverclass-classroom]
NS_kuepa --> APP_kuepa_uk-emiconnect-emipago-payments[uk-emiconnect-emipago-payments]
NS_kuepa --> APP_kuepa_uk-emiconnect-salesforce-contacts[uk-emiconnect-salesforce-contacts]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-calls[uk-emiconnect-twilio-calls]
NS_kuepa --> APP_kuepa_uk-emiconnect-twilio-messages[uk-emiconnect-twilio-messages]
NS_kuepa --> APP_kuepa_uk-ensamble-massive-analysis[uk-ensamble-massive-analysis]
NS_kuepa --> APP_kuepa_uk-soyalumno-conversations[uk-soyalumno-conversations]
NS_kuepa --> APP_kuepa_uk-subscriptions-debit[uk-subscriptions-debit]
NS_kuepa --> APP_kuepa_uk-task-comments[uk-task-comments]
NS_kuepa --> APP_kuepa_youtube-search-bot-weekly[youtube-search-bot-weekly]

ING_nexus-ingress[Ingress: nexus-ingress]
ING_nexus-ingress --> Internet
NS_dev --> ING_nexus-ingress
ING_client-ingress-rules[Ingress: client-ingress-rules]
ING_client-ingress-rules --> Internet
NS_kuepa --> ING_client-ingress-rules
ING_uk-chatbot-ingress[Ingress: uk-chatbot-ingress]
ING_uk-chatbot-ingress --> Internet
NS_kuepa --> ING_uk-chatbot-ingress
ING_uk-course-gen-api-ingress[Ingress: uk-course-gen-api-ingress]
ING_uk-course-gen-api-ingress --> Internet
NS_kuepa --> ING_uk-course-gen-api-ingress
ING_uk-course-gen-ingress[Ingress: uk-course-gen-ingress]
ING_uk-course-gen-ingress --> Internet
NS_kuepa --> ING_uk-course-gen-ingress
ING_uk-course-gen-nest-api-ingress[Ingress: uk-course-gen-nest-api-ingress]
ING_uk-course-gen-nest-api-ingress --> Internet
NS_kuepa --> ING_uk-course-gen-nest-api-ingress

Internet((Internet))
```
