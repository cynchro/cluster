import yaml
import json
import os

# Usar variable de entorno o valor por defecto
BASE = os.getenv("OUTPUT_DIR", "kuepa-cluster-doc")
OUT = os.path.join(BASE, "DIAGRAM.md")

# Manejar archivos que pueden estar vacíos o no tener items
def get_yaml_items(path):
    data = yaml.safe_load(open(path))
    return data.get("items", []) if data else []

cluster = json.load(open(f"{BASE}/infra/cluster.json"))
node_pools = json.load(open(f"{BASE}/infra/node-pools.json"))
namespaces = get_yaml_items(f"{BASE}/k8s/namespaces.yaml")
workloads = get_yaml_items(f"{BASE}/k8s/workloads.yaml")
ingress = get_yaml_items(f"{BASE}/k8s/ingress.yaml")

cluster_name = cluster["name"]
zone = cluster["location"]
network = cluster["network"].split("/")[-1]

ns_apps = {}
for w in workloads:
    ns = w["metadata"]["namespace"]
    app = w["metadata"]["name"]
    ns_apps.setdefault(ns, []).append(app)

with open(OUT, "w") as f:
    f.write("```mermaid\n")
    f.write("graph TD\n\n")
    f.write(f"GCP[GCP Project]\n")
    f.write(f"VPC[VPC: {network}]\n")
    f.write(f"CLUSTER[GKE: {cluster_name}\\n{zone}]\n\n")

    f.write("GCP --> VPC --> CLUSTER\n\n")

    # node_pools puede ser una lista o un objeto con items
    pools_list = node_pools if isinstance(node_pools, list) else (node_pools if node_pools else [])
    for np in pools_list:
        np_name = np["name"]
        f.write(f"CLUSTER --> NP_{np_name}[NodePool: {np_name}]\n")

    f.write("\n")

    for ns, apps in ns_apps.items():
        f.write(f"CLUSTER --> NS_{ns}[Namespace: {ns}]\n")
        for app in apps:
            f.write(f"NS_{ns} --> APP_{ns}_{app}[{app}]\n")

    f.write("\n")

    for i in ingress:
        ns = i["metadata"]["namespace"]
        name = i["metadata"]["name"]
        f.write(f"ING_{name}[Ingress: {name}]\n")
        f.write(f"ING_{name} --> Internet\n")
        f.write(f"NS_{ns} --> ING_{name}\n")

    f.write("\nInternet((Internet))\n")
    f.write("```\n")

print("✅ Diagrama Mermaid generado")
