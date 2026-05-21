# TP-AprendizajeAutomatico

## Paso 1

Hacer scraper de FIUBA Repos.

Guardás:

título,
materia,
PDF,
texto.

## Paso 2

Extraer texto de PDFs.

Librerías:

PyPDF2
pymupdf

## Paso 3

Chunking.

Ejemplo:

500 caracteres,
overlap de 100.

## Paso 4

Generar embeddings.

Modelo MUY usado:

all-MiniLM-L6-v2

Desde:

Sentence Transformers

## Paso 5

Guardar en ChromaDB.

Cada chunk:

texto,
embedding,
metadata.

Metadata:

materia,
autor,
PDF,
página.
Paso 6

Hacer endpoint:

POST /ask

## Paso 7

Pipeline:

pregunta
→ embedding
→ similarity search
→ top-k chunks
→ prompt
→ LLM
→ respuesta
MUY importante: citations
