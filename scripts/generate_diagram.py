import yaml
import json
import os
import re

# Usar variable de entorno o valor por defecto
BASE = os.getenv("OUTPUT_DIR", "kuepa-cluster-doc")
OUT = os.path.join(BASE, "DIAGRAM.md")

# Función para limpiar IDs (Mermaid no acepta ciertos caracteres especiales)
def clean_id(text):
    # Reemplazar caracteres especiales por guiones bajos
    cleaned = re.sub(r'[^a-zA-Z0-9_]', '_', str(text))
    # Limitar longitud y eliminar guiones bajos múltiples
    cleaned = re.sub(r'_+', '_', cleaned)
    return cleaned.strip('_')

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

# Agrupar aplicaciones por namespace y limitar para hacer el diagrama más legible
ns_apps = {}
for w in workloads:
    ns = w["metadata"]["namespace"]
    app = w["metadata"]["name"]
    ns_apps.setdefault(ns, []).append(app)

# Limitar número de aplicaciones por namespace para hacer el diagrama más legible
# Mostrar solo los primeros 10 y agregar un contador
MAX_APPS_PER_NS = 10
for ns in ns_apps:
    total = len(ns_apps[ns])
    if total > MAX_APPS_PER_NS:
        ns_apps[ns] = ns_apps[ns][:MAX_APPS_PER_NS] + [f"... y {total - MAX_APPS_PER_NS} más aplicaciones"]

with open(OUT, "w") as f:
    f.write("```mermaid\n")
    f.write("flowchart TB\n\n")  # Usar flowchart TB para mejor control del layout
    
    # Nivel 1: Infraestructura
    f.write("subgraph INFRA[\"Infraestructura GCP\"]\n")
    f.write(f"  GCP[\"GCP Project\"]\n")
    f.write(f"  VPC[\"VPC: {network}\"]\n")
    f.write("end\n\n")
    
    # Nivel 2: Cluster
    f.write(f"CLUSTER[\"GKE Cluster<br/>{cluster_name}<br/>{zone}\"]\n\n")
    
    # Conexiones infraestructura
    f.write("GCP --> VPC\n")
    f.write("VPC --> CLUSTER\n\n")
    
    # Nivel 3: Node Pools
    pools_list = node_pools if isinstance(node_pools, list) else (node_pools if node_pools else [])
    if pools_list:
        f.write("subgraph NODES[\"Node Pools\"]\n")
        for np in pools_list:
            np_name = np["name"]
            np_id = clean_id(f"NP_{np_name}")
            f.write(f"  {np_id}[\"NodePool: {np_name}\"]\n")
        f.write("end\n\n")
        f.write("CLUSTER --> NODES\n\n")
    
    # Nivel 4: Namespaces con subgrafos para mejor organización vertical
    for ns, apps in ns_apps.items():
        ns_id = clean_id(f"NS_{ns}")
        ns_label = ns.replace('"', '\\"')
        f.write(f"subgraph {ns_id}[\"Namespace: {ns_label}\"]\n")
        for app in apps:
            app_id = clean_id(f"APP_{ns}_{app}")
            app_label = str(app).replace('"', '\\"')
            f.write(f"  {app_id}[\"{app_label}\"]\n")
        f.write("end\n\n")
        f.write(f"CLUSTER --> {ns_id}\n\n")
    
    # Nivel 5: Ingress
    if ingress:
        f.write("subgraph INGRESS[\"Ingress Resources\"]\n")
        for i in ingress:
            name = i["metadata"]["name"]
            ing_id = clean_id(f"ING_{name}")
            ing_label = name.replace('"', '\\"')
            f.write(f"  {ing_id}[\"Ingress: {ing_label}\"]\n")
        f.write("end\n\n")
        
        # Conectar ingress a namespaces e internet
        for i in ingress:
            ns = i["metadata"]["namespace"]
            name = i["metadata"]["name"]
            ing_id = clean_id(f"ING_{name}")
            ns_id = clean_id(f"NS_{ns}")
            f.write(f"{ns_id} --> {ing_id}\n")
            f.write(f"{ing_id} --> Internet\n")
        f.write("\n")
    
    # Internet al final
    f.write("Internet((Internet))\n")
    f.write("```\n")

print("✅ Diagrama Mermaid generado")
