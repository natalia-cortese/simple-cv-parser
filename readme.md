## SIMPLE RESUME PARSER
## Challenge
You're building a lightweight API that takes in PDF or image resumes (curriculum vitae),
runs OCR + LLM, and returns a structured JSON schema with name, contact info, experience, and skills.
The goal is to design and implement a small, functional prototype that reflects the core data flow.
# 💻 What They'll Do:
* Set up a REST API (can be FastAPI/Flask/Nest/etc or Cloud Function-style).
Accept file uploads (PDF, PNG, or JPG).
* Call a mock OCR function (or real OCR lib like Tesseract or GCP Vision).
* Simulate a call to Gemini/GPT with an LLM prompt to extract structured data.
* Return structured JSON (e.g., {"name": ..., "email": ..., "skills": [...], "experience": [...]}).
# Rules:
Take 5min to think the solution. Decide what architecture attributes are desirable for this kind of project and implement accordingly as
much as possible.
Tell your plan before prompting/seraching for anything.
You can use LLMs to vibe code and also ask about concepts or design strategies. Even paste this README if you like after telling your plan.
You can use as many artifacts/services as you need.
Always express verbally your steps and your thoughts on the LLM responses.
You have 60 min to implement as much as posible.

## Work Flow

Client
  ↓
POST /parse-resume
  ↓
File validation
  ↓
OCR (mock or real)
  ↓
LLM prompt → structured JSON
  ↓
Response

## Requisitos / Setup (importante)

Este proyecto **no es compatible con Python 3.14** todavía (depencias como `pydantic-core` / `Pillow` no tienen wheels estables y pip intenta compilar).

- **Python recomendado**: 3.11.x (también debería funcionar 3.12.x)
- **Mac (Homebrew)**:

```bash
brew install python@3.11
brew install poppler tesseract
rm -rf .venv
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

- **Run API**:

```bash
source .venv/bin/activate
uvicorn main:app --reload
```

## Qué usa mi solucion?

🔹 pytesseract

Wrapper de Tesseract OCR.

Convierte imágenes → texto

Fácil de mockear

Muy usado en prototipos

🔹 Pillow

Procesamiento de imágenes.
Necesario para que Tesseract lea JPG/PNG.

🔹 pdf2image

Convierte PDFs a imágenes antes del OCR.

👉 En producción podría cambiarse por:

AWS Textract

GCP Vision

🔹 pydantic

Validación del schema de salida.
Evita respuestas mal formadas.

🔹 python-multipart

Necesario para manejar UploadFile en FastAPI.

🔹 pytest

Testing básico del endpoint.
Muestra mentalidad profesional.
