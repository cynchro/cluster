#!/usr/bin/env python3
"""
Genera información de costos del cluster GKE
"""
import json
import os
import subprocess
from datetime import datetime

BASE = os.getenv("OUTPUT_DIR", "kuepa-cluster-doc")
PROJECT_ID = os.getenv("PROJECT_ID", "kuepa-datos")
OUT = os.path.join(BASE, "costs.json")

def j(path):
    with open(path) as f:
        return json.load(f)

def get_billing_account():
    """Obtener el billing account asociado al proyecto"""
    try:
        result = subprocess.run(
            ["gcloud", "billing", "projects", "describe", PROJECT_ID, "--format=json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("billingAccountName", "").split("/")[-1] if data.get("billingAccountName") else None
    except:
        pass
    return None

def get_monthly_costs(billing_account):
    """Obtener costos del mes actual usando Cloud Billing API"""
    if not billing_account:
        return None
    
    try:
        # Obtener fecha de inicio y fin del mes actual
        today = datetime.now()
        start_date = today.replace(day=1).strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")
        
        # Intentar obtener costos usando gcloud (requiere permisos)
        result = subprocess.run(
            [
                "gcloud", "billing", "budgets", "list",
                "--billing-account", billing_account,
                "--format=json"
            ],
            capture_output=True,
            text=True,
            timeout=10
        )
        # Nota: La API de billing es compleja, aquí solo intentamos obtener el billing account
        # Los costos reales requieren usar la API de Cloud Billing directamente
    except:
        pass
    
    return None

def estimate_costs():
    """Calcular costos estimados basados en los recursos"""
    import yaml
    
    cluster = j(f"{BASE}/infra/cluster.json")
    node_pools = j(f"{BASE}/infra/node-pools.json")
    
    # Leer storage YAML
    try:
        with open(f"{BASE}/k8s/storage.yaml") as f:
            storage = yaml.safe_load(f)
    except:
        storage = {"items": []}
    
    # Precios aproximados de GCP (USD por hora, actualizados aproximadamente)
    # Estos son precios de referencia, pueden variar
    machine_type_prices = {
        "e2-micro": 0.0067,
        "e2-small": 0.0169,
        "e2-medium": 0.0337,
        "e2-standard-2": 0.0675,
        "e2-standard-4": 0.135,
        "e2-standard-8": 0.27,
        "e2-standard-16": 0.54,
        "n1-standard-1": 0.0475,
        "n1-standard-2": 0.095,
        "n1-standard-4": 0.19,
        "n1-standard-8": 0.38,
    }
    
    # Precio base de GKE por nodo (aproximado)
    gke_base_cost_per_node = 0.10  # USD por hora
    
    # Precio de storage (aproximado por GB/mes)
    storage_cost_per_gb_month = 0.17
    
    total_monthly = 0
    node_costs = []
    
    # Calcular costos de node pools
    pools_list = node_pools if isinstance(node_pools, list) else (node_pools if node_pools else [])
    for np in pools_list:
        machine_type = np.get("config", {}).get("machineType", "").split("/")[-1]
        autoscaling = np.get("autoscaling", {})
        min_nodes = autoscaling.get("minNodeCount", 1) if autoscaling.get("enabled") else np.get("initialNodeCount", 1)
        max_nodes = autoscaling.get("maxNodeCount", min_nodes) if autoscaling.get("enabled") else min_nodes
        avg_nodes = (min_nodes + max_nodes) / 2
        
        # Precio de la máquina
        machine_hourly = machine_type_prices.get(machine_type, 0.10)  # Default si no está en la lista
        node_hourly = machine_hourly + gke_base_cost_per_node
        node_monthly = node_hourly * 730  # Horas en un mes aproximado
        pool_monthly = node_monthly * avg_nodes
        
        total_monthly += pool_monthly
        
        node_costs.append({
            "name": np["name"],
            "machine_type": machine_type,
            "avg_nodes": round(avg_nodes, 1),
            "monthly_cost": round(pool_monthly, 2)
        })
    
    # Calcular costos de storage
    storage_total_gb = 0
    if storage:
        if isinstance(storage, dict) and "items" in storage:
            items = storage["items"]
        elif isinstance(storage, list):
            items = storage
        else:
            items = []
    else:
        items = []
    
    for item in items:
        if item.get("kind") == "PersistentVolumeClaim":
            size_str = item.get("spec", {}).get("resources", {}).get("requests", {}).get("storage", "0Gi")
            # Convertir a GB (asumiendo formato como "10Gi", "100Gi", etc.)
            try:
                if size_str.endswith("Gi"):
                    size_gb = float(size_str[:-2])
                elif size_str.endswith("G"):
                    size_gb = float(size_str[:-1])
                else:
                    size_gb = 0
                storage_total_gb += size_gb
            except:
                pass
    
    storage_monthly = storage_total_gb * storage_cost_per_gb_month
    
    # Intentar obtener billing account
    billing_account = get_billing_account()
    
    costs_data = {
        "project_id": PROJECT_ID,
        "billing_account": billing_account,
        "estimated_monthly": {
            "compute": round(total_monthly, 2),
            "storage": round(storage_monthly, 2),
            "total": round(total_monthly + storage_monthly, 2)
        },
        "node_pools": node_costs,
        "storage_gb": round(storage_total_gb, 2),
        "currency": "USD",
        "last_updated": datetime.now().isoformat(),
        "note": "Costos estimados basados en recursos. Los costos reales pueden variar."
    }
    
    with open(OUT, "w") as f:
        json.dump(costs_data, f, indent=2)
    
    print(f"✅ Información de costos generada en {OUT}")
    return costs_data

if __name__ == "__main__":
    estimate_costs()

