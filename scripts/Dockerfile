FROM google/cloud-sdk:alpine

# Instalar kubectl
RUN gcloud components install kubectl --quiet

# Instalar Python y pyyaml (usando paquetes de Alpine)
RUN apk add --no-cache python3 py3-yaml

# Crear directorio de trabajo
WORKDIR /app

# Copiar los scripts
COPY snapshot.sh /app/snapshot.sh
COPY generate_cluster_doc.py /app/generate_cluster_doc.py
COPY generate_diagram.py /app/generate_diagram.py
COPY inject_diagram_into_cluster_doc.py /app/inject_diagram_into_cluster_doc.py

# Dar permisos de ejecución
RUN chmod +x /app/snapshot.sh

# Configurar el entrypoint
ENTRYPOINT ["/app/snapshot.sh"]

