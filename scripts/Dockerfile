FROM google/cloud-sdk:alpine

# Instalar kubectl
RUN gcloud components install kubectl --quiet

# Instalar Python, pyyaml y Node.js (para mermaid-cli)
RUN apk add --no-cache python3 py3-yaml nodejs npm

# Instalar dependencias necesarias para Puppeteer/Chrome en Alpine (headless)
RUN apk add --no-cache \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    font-noto-emoji \
    glib \
    dbus \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    libxrandr \
    libxrender \
    libxtst \
    pango \
    gdk-pixbuf

# Configurar variables de entorno para Puppeteer
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Instalar mermaid-cli globalmente
RUN npm install -g @mermaid-js/mermaid-cli

# Crear directorio de trabajo
WORKDIR /app

# Copiar los scripts
COPY snapshot.sh /app/snapshot.sh
COPY generate_cluster_doc.py /app/generate_cluster_doc.py
COPY generate_costs.py /app/generate_costs.py
COPY generate_diagram.py /app/generate_diagram.py
COPY generate_diagram_svg.py /app/generate_diagram_svg.py
COPY inject_diagram_into_cluster_doc.py /app/inject_diagram_into_cluster_doc.py
COPY puppeteer-config.json /app/puppeteer-config.json

# Dar permisos de ejecución
RUN chmod +x /app/snapshot.sh /app/generate_diagram_svg.py /app/generate_costs.py

# Configurar el entrypoint
ENTRYPOINT ["/app/snapshot.sh"]

