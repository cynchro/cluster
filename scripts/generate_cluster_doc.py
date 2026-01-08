import json
import yaml
import os
from datetime import date
from collections import defaultdict

# Usar variable de entorno o valor por defecto
BASE = os.getenv("OUTPUT_DIR", "kuepa-cluster-doc")
CLUSTER_NAME = os.getenv("CLUSTER", "kuepa-cluster")
ZONE = os.getenv("ZONE", "us-central1-c")
OUT = os.path.join(BASE, "CLUSTER.md")

def j(path):
    with open(path) as f:
        return json.load(f)

def y(path):
    with open(path) as f:
        return yaml.safe_load(f)

def safe(val):
    return val if val else "No documentado"

cluster = j(f"{BASE}/infra/cluster.json")
node_pools = j(f"{BASE}/infra/node-pools.json")

# Manejar archivos YAML que pueden estar vacíos o no tener items
def get_yaml_items(path):
    data = y(path)
    return data.get("items", []) if data else []

namespaces = get_yaml_items(f"{BASE}/k8s/namespaces.yaml")
workloads = get_yaml_items(f"{BASE}/k8s/workloads.yaml")
config = get_yaml_items(f"{BASE}/k8s/config.yaml")
ingress = get_yaml_items(f"{BASE}/k8s/ingress.yaml")
storage = get_yaml_items(f"{BASE}/k8s/storage.yaml")

# ---- Infra ----
k8s_version = cluster.get("currentMasterVersion")
autopilot = "Autopilot" if cluster.get("autopilot", {}).get("enabled") else "Standard"
network = cluster.get("network", "").split("/")[-1]
subnet = cluster.get("subnetwork", "").split("/")[-1]

# ---- Node pools ----
np_rows = []
# node_pools puede ser una lista o un objeto con items
if isinstance(node_pools, list):
    pools_list = node_pools
else:
    pools_list = node_pools if node_pools else []
for np in pools_list:
    autoscale = "Sí" if np.get("autoscaling", {}).get("enabled") else "No"
    min_n = np.get("autoscaling", {}).get("minNodeCount", "-")
    max_n = np.get("autoscaling", {}).get("maxNodeCount", "-")
    machine = np.get("config", {}).get("machineType", "Autopilot")
    np_rows.append(f"| {np['name']} | {machine} | {autoscale} | {min_n} | {max_n} |")

# ---- Namespaces ----
ns_rows = [f"| {ns['metadata']['name']} | No documentado |" for ns in namespaces]

# ---- Apps ----
apps = []
for w in workloads:
    kind = w["kind"]
    ns = w["metadata"]["namespace"]
    name = w["metadata"]["name"]
    replicas = w.get("spec", {}).get("replicas", "-")
    apps.append(f"| {ns} | {name} | {kind} | {replicas} |")

# ---- Secrets ----
secrets = []
for c in config:
    if c["kind"] == "Secret":
        ns = c["metadata"]["namespace"]
        name = c["metadata"]["name"]
        secrets.append(f"| {name} | {ns} | No identificado |")

# ---- Ingress ----
ing_rows = []
for i in ingress:
    ns = i["metadata"]["namespace"]
    name = i["metadata"]["name"]
    hosts = []
    for rule in i.get("spec", {}).get("rules", []):
        hosts.append(rule.get("host", ""))
    ing_rows.append(f"| {ns} | {name} | {', '.join(hosts)} | Sí |")

# ---- Storage ----
stor_rows = []
for s in storage:
    if s["kind"] == "PersistentVolumeClaim":
        ns = s["metadata"]["namespace"]
        name = s["metadata"]["name"]
        size = s.get("spec", {}).get("resources", {}).get("requests", {}).get("storage", "")
        stor_rows.append(f"| {name} | {ns} | {size} | No documentado |")

# ---- Write markdown ----
with open(OUT, "w") as f:
    f.write(f"# 📘 Clúster GKE – {CLUSTER_NAME}\n\n")

    f.write("## 1. Información general\n\n")
    f.write(f"- **Proveedor:** Google Cloud Platform\n")
    f.write(f"- **Servicio:** Google Kubernetes Engine (GKE)\n")
    f.write(f"- **Tipo:** Zonal\n")
    f.write(f"- **Zona:** {ZONE}\n")
    f.write(f"- **Modo:** {autopilot}\n")
    f.write(f"- **Versión Kubernetes:** {k8s_version}\n")
    f.write(f"- **Fecha del relevamiento:** {date.today()}\n\n")

    f.write("## 2. Infraestructura GKE\n\n")
    f.write(f"- **Red:** {network}\n")
    f.write(f"- **Subred:** {subnet}\n\n")

    f.write("### Node Pools\n\n")
    f.write("| Node Pool | Machine Type | Autoscaling | Min | Max |\n")
    f.write("|---|---|---|---|---|\n")
    f.write("\n".join(np_rows) + "\n\n")

    f.write("## 3. Namespaces\n\n")
    f.write("| Namespace | Propósito |\n|---|---|\n")
    f.write("\n".join(ns_rows) + "\n\n")

    f.write("## 4. Aplicaciones desplegadas\n\n")
    f.write("| Namespace | Aplicación | Tipo | Réplicas |\n")
    f.write("|---|---|---|---|\n")
    f.write("\n".join(apps) + "\n\n")

    f.write("## 5. Exposición (Ingress)\n\n")
    f.write("| Namespace | Ingress | Host | Público |\n")
    f.write("|---|---|---|---|\n")
    f.write("\n".join(ing_rows) + "\n\n")

    f.write("## 6. Secrets\n\n")
    f.write("| Secret | Namespace | Usado por |\n")
    f.write("|---|---|---|\n")
    f.write("\n".join(secrets) + "\n\n")

    f.write("## 7. Persistencia\n\n")
    f.write("| PVC | Namespace | Tamaño | Uso |\n")
    f.write("|---|---|---|---|\n")
    f.write("\n".join(stor_rows) + "\n\n")

    f.write("## 8. Anexos\n\n")
    f.write(f"- Snapshot completo en `{BASE}/`\n")
    f.write("- Relevamiento 100% read-only\n")

print("✅ CLUSTER.md generado automáticamente")
