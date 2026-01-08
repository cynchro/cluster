from pathlib import Path
import os
import re

# Usar variable de entorno o valor por defecto
OUTPUT_DIR = os.getenv("OUTPUT_DIR", ".")
CLUSTER_DOC = Path(OUTPUT_DIR) / "CLUSTER.md"
DIAGRAM_SVG = Path(OUTPUT_DIR) / "diagram.svg"

SECTION_TITLE = "## Diagrama de arquitectura"

# Verificar que el SVG existe
if not DIAGRAM_SVG.exists():
    raise Exception(f"diagram.svg no existe en {OUTPUT_DIR}/. Asegúrate de ejecutar generate_diagram_svg.py primero.")

cluster_text = CLUSTER_DOC.read_text()

# Insertar referencia a la imagen SVG en lugar del código Mermaid
new_section = f"""
{SECTION_TITLE}

![Diagrama del clúster](diagram.svg)
""".strip()

if SECTION_TITLE in cluster_text:
    # Reemplaza sección existente
    cluster_text = re.sub(
        rf"{SECTION_TITLE}[\\s\\S]*?(?=\\n## |\\Z)",
        new_section,
        cluster_text,
        flags=re.MULTILINE
    )
else:
    # Agrega al final
    cluster_text += "\n\n" + new_section + "\n"

CLUSTER_DOC.write_text(cluster_text)

print("✅ Diagrama insertado correctamente en CLUSTER.md")
