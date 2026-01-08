#!/usr/bin/env python3
"""
Extrae el contenido Mermaid de DIAGRAM.md y genera diagram.svg usando mermaid-cli
"""
import os
import re
from pathlib import Path
import subprocess

OUTPUT_DIR = os.getenv("OUTPUT_DIR", ".")
DIAGRAM_MD = Path(OUTPUT_DIR) / "DIAGRAM.md"
DIAGRAM_MMD = Path(OUTPUT_DIR) / "diagram.mmd"
DIAGRAM_SVG = Path(OUTPUT_DIR) / "diagram.svg"

# Leer DIAGRAM.md
diagram_content = DIAGRAM_MD.read_text()

# Extraer el contenido Mermaid (sin los ```mermaid y ```)
mermaid_match = re.search(r'```mermaid\n(.*?)\n```', diagram_content, re.DOTALL)
if not mermaid_match:
    raise Exception("No se encontró contenido Mermaid válido en DIAGRAM.md")

mermaid_code = mermaid_match.group(1).strip()

# Escribir diagram.mmd (sin los backticks)
DIAGRAM_MMD.write_text(mermaid_code)

# Generar SVG usando mermaid-cli con configuración para Alpine/Chromium
print(f"🖼️  Generando diagram.svg desde diagram.mmd...")

# Configurar entorno para usar Chromium de Alpine
env = os.environ.copy()
env["PUPPETEER_EXECUTABLE_PATH"] = "/usr/bin/chromium-browser"
env["PUPPETEER_SKIP_CHROMIUM_DOWNLOAD"] = "true"
env["CHROME_BIN"] = "/usr/bin/chromium-browser"
env["CHROMIUM_PATH"] = "/usr/bin/chromium-browser"

result = subprocess.run(
    [
        "mmdc",
        "-i", str(DIAGRAM_MMD),
        "-o", str(DIAGRAM_SVG),
        "-t", "default",
        "-b", "transparent",
        "--puppeteerConfigFile", "/app/puppeteer-config.json"
    ],
    capture_output=True,
    text=True,
    env=env
)

if result.returncode != 0:
    raise Exception(f"Error al generar SVG: {result.stderr}")

print(f"✅ diagram.svg generado correctamente en {OUTPUT_DIR}/")

