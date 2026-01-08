from pathlib import Path
import os
import re

# Usar variable de entorno o valor por defecto
OUTPUT_DIR = os.getenv("OUTPUT_DIR", ".")
CLUSTER_DOC = Path(OUTPUT_DIR) / "CLUSTER.md"
DIAGRAM_DOC = Path(OUTPUT_DIR) / "DIAGRAM.md"

SECTION_TITLE = "## Diagrama de arquitectura"

diagram_content = DIAGRAM_DOC.read_text().strip()

if not diagram_content.startswith("```mermaid"):
    raise Exception("DIAGRAM.md no contiene un bloque Mermaid válido")

cluster_text = CLUSTER_DOC.read_text()

new_section = f"""
{SECTION_TITLE}

{diagram_content}
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
