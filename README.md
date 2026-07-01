# Demo: R2RML/RML + Morph-KGC con Northwind

Este proyecto muestra cómo transformar datos a un grafo de conocimiento RDF utilizando RML y Morph-KGC.

A diferencia de R2RML, que únicamente permite mapear bases de datos relacionales, RML permite transformar distintas fuentes de datos (CSV, JSON, XML, bases de datos relacionales, etc.) a RDF mediante un único lenguaje de mapeo.

Se trabaja con un subconjunto del modelo Northwind:

- Customers  
- Orders  
- OrderDetails  
- Products  
- Categories  
- Suppliers  


## Archivos del proyecto

```
demo/
│
├── config.ini # Configuración de Morph-KGC
├── demo.py # Script principal de materialización RDF
├── northwind_mapeo.r2rml.ttl # Mapeos r2RML (SQL → RDF)
├── northwind_mapeo.rml.ttl # Mapeos RML (CSV → RDF)
├── northwind.sql 
└── README.md
```


## Paso 1 — Instalar dependencias Python

Abrí una terminal y ejecutá:

```bash
pip install morph-kgc psycopg2-binary
```

## Paso 2 - Crear la base de datos

Crear una base de datos llamada `northwind`:

```bash
createdb -U postgres northwind
```

Si `createdb` no está disponible en el PATH de Windows, puede utilizarse:

```bash
"C:\Program Files\PostgreSQL\<VERSION>\bin\createdb.exe" -U postgres northwind
```

### 2.1 Descargar el script SQL

Descargar el archivo que contiene el esquema y datos del modelo northwind:

👉 https://github.com/pthom/northwind_psql/blob/master/northwind.sql

(Botón **Raw** en la página → Ctrl+S para guardar)


### 2.2 Cargar Northwind

Importar el archivo SQL incluido en el proyecto:

```bash
psql -U postgres -d northwind -f northwind.sql
```

Si el archivo SQL se encuentra en otra carpeta, indicar la ruta completa:

```bash
psql -U postgres -d northwind -f "C:\ruta\northwind.sql"
```

---

## Paso 3 — Editar `config.ini`

Para el mapeo R2RML -> RDF, el archivo `config.ini` debe contener las siguientes líneas:

```ini
[CONFIGURATION]
output_file: northwind.nt
output_format: N-TRIPLES

[DataSource1]
mappings: northwind_mapeo.r2rml.ttl
db_url: postgresql+psycopg2://usuario:contraseña@localhost:5432/northwind
```
Reemplazar usuario:contraseña por el usuario y contraseña correspondientes.


Para el mapeo R2RML -> RDF, el archivo `config.ini` debe contener las siguientes líneas:

```ini
[CONFIGURATION]
output_file = knowledge-graph.nt
output_format = N-TRIPLES

[DataSource1]
mappings = northwind_mapeo.rml.ttl
```


## Paso 4 — Ejecutar la demo

Desde la carpeta del proyecto:

```bash
python demo.py
```

o 
```bash
python3 -m morph_kgc config.ini
```

### Salida esperada en consola

```
Materializando grafo RDF desde Northwind...
INFO | 2026-06-28 21:09:54,110 | Parallelization is not supported for win32 when running as a library. If you need to speed up your data integration pipeline, please run through the command line.
INFO | 2026-06-28 21:09:55,730 | 39 mapping rules retrieved.
INFO | 2026-06-28 21:09:55,765 | Mapping partition with 39 groups generated.
INFO | 2026-06-28 21:09:55,770 | Maximum number of rules within mapping group: 1.
INFO | 2026-06-28 21:09:55,775 | Mappings processed in 1.652 seconds.
INFO | 2026-06-28 21:09:59,219 | Number of triples generated in total: 20228.
Grafo generado con 20228 triples
```

### Archivos generados

| Archivo | Descripción |
|---|---|
| `northwind_kg.nt` | Grafo RDF en formato N-Triples |
| `northwind_kg.ttl` | Grafo RDF en formato Turtle (más legible) |
