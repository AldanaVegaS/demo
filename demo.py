"""
demo_northwind.py
Ejecuta Morph-KGC sobre Northwind y hace algunas queries SPARQL de ejemplo.

Instalación previa:
    pip install morph-kgc psycopg2-binary
"""

import morph_kgc

print("Materializando grafo RDF desde Northwind...")

g = morph_kgc.materialize("config.ini")

print(f"Grafo generado con {len(g)} triples")

g.serialize("northwind.ttl", format="turtle")
g.serialize("northwind.nt", format="nt")
