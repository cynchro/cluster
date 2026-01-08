# GKE Snapshot Tool

Herramienta para crear snapshots de la infraestructura GKE, incluyendo información del cluster, red, IAM y recursos de Kubernetes.

## Requisitos

- Docker y Docker Compose instalados
- Credenciales de Google Cloud configuradas en `~/.config/gcloud`
- Configuración de kubectl en `~/.kube` (opcional, si se usa kubeconfig local)

## Uso

### Opción 1: Usar valores por defecto

```bash
docker-compose up
```

### Opción 2: Personalizar variables de entorno

```bash
PROJECT_ID=mi-proyecto CLUSTER=mi-cluster ZONE=us-east1-a docker-compose up
```

O crear un archivo `.env`:

```env
PROJECT_ID=mi-proyecto
CLUSTER=mi-cluster
ZONE=us-east1-a
```

Y luego ejecutar:

```bash
docker-compose up
```

## Salida

Los archivos de snapshot se generan en el directorio `./output/` con la siguiente estructura:

```
output/
├── infra/
│   ├── cluster.json
│   └── node-pools.json
├── network/
│   ├── networks.json
│   ├── subnets.json
│   └── firewalls.json
├── iam/
│   └── project-iam.json
├── k8s/
│   ├── namespaces.yaml
│   ├── workloads.yaml
│   ├── config.yaml
│   ├── ingress.yaml
│   ├── storage.yaml
│   └── rbac.yaml
├── CLUSTER.md          # Documentación generada automáticamente
└── DIAGRAM.md          # Diagrama Mermaid generado automáticamente
```

Además de los archivos de snapshot, se generan automáticamente:
- `CLUSTER.md`: Documentación completa del cluster en formato Markdown
- `DIAGRAM.md`: Diagrama Mermaid con la arquitectura del cluster

## Variables de Entorno

- `PROJECT_ID`: ID del proyecto de Google Cloud (default: `kuepa-datos`)
- `CLUSTER`: Nombre del cluster GKE (default: `kuepa-cluster`)
- `ZONE`: Zona del cluster (default: `us-central1-c`)
- `OUTPUT_DIR`: Directorio de salida (default: `/app/output` en el contenedor)

## Notas

- El contenedor se ejecuta una vez y luego sale (no se reinicia automáticamente)
- Las credenciales de gcloud se montan con permisos de escritura (necesario para archivos temporales)
- El kubeconfig se monta como solo lectura
- Asegúrate de tener los permisos necesarios en GCP para ejecutar los comandos
- Después del snapshot, se generan automáticamente:
  - `CLUSTER.md`: Documentación completa del cluster
  - `DIAGRAM.md`: Diagrama Mermaid de la arquitectura

