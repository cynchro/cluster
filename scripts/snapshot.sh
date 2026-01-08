#!/usr/bin/env bash
set -e

# Variables de entorno con valores por defecto
PROJECT_ID="${PROJECT_ID:-kuepa-datos}"
CLUSTER="${CLUSTER:-kuepa-cluster}"
ZONE="${ZONE:-us-central1-c}"
OUTPUT_DIR="${OUTPUT_DIR:-.}"

# Crear directorios de salida
mkdir -p "${OUTPUT_DIR}/infra" "${OUTPUT_DIR}/network" "${OUTPUT_DIR}/iam" "${OUTPUT_DIR}/k8s"

echo "🔍 Infra GKE"
gcloud container clusters describe "$CLUSTER" \
  --zone "$ZONE" \
  --project "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/infra/cluster.json"

gcloud container node-pools list \
  --cluster "$CLUSTER" \
  --zone "$ZONE" \
  --project "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/infra/node-pools.json"

echo "🌐 Network"
gcloud compute networks list \
  --project "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/network/networks.json"

gcloud compute networks subnets list \
  --project "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/network/subnets.json"

gcloud compute firewall-rules list \
  --project "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/network/firewalls.json"

echo "🔐 IAM"
gcloud projects get-iam-policy "$PROJECT_ID" \
  --format=json > "${OUTPUT_DIR}/iam/project-iam.json"

echo "☸️ Kubernetes"
kubectl get namespaces -o yaml > "${OUTPUT_DIR}/k8s/namespaces.yaml"
kubectl get deploy,sts,ds,job,cronjob -A -o yaml > "${OUTPUT_DIR}/k8s/workloads.yaml"
kubectl get svc,cm,secret -A -o yaml > "${OUTPUT_DIR}/k8s/config.yaml"
kubectl get ingress -A -o yaml > "${OUTPUT_DIR}/k8s/ingress.yaml"
kubectl get pvc,pv,storageclass -A -o yaml > "${OUTPUT_DIR}/k8s/storage.yaml"
kubectl get role,rolebinding,clusterrole,clusterrolebinding -A -o yaml > "${OUTPUT_DIR}/k8s/rbac.yaml"

echo "✅ Snapshot completo"

# Generar documentación
echo "📝 Generando documentación..."
export OUTPUT_DIR CLUSTER ZONE
python3 /app/generate_cluster_doc.py

# Generar diagrama
echo "📊 Generando diagrama..."
python3 /app/generate_diagram.py

echo "✅ Proceso completado"
