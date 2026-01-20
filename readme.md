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

## Requirements / Setup (Important)

This project **is not compatible with Python 3.14** yet (dependencies like `pydantic-core` / `Pillow` do not have stable wheels and pip tries to compile them).

- **Recommended Python**: 3.11.x (should also work with 3.12.x)
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

## What does my solution use?

🔹 pytesseract

Wrapper for Tesseract OCR.

Converts images → text.

Easy to mock.

Widely used in prototypes.

🔹 Pillow

Image processing.
Necessary for Tesseract to read JPG/PNG files.

🔹 pdf2image

Converts PDFs to images before OCR.

👉 For production, you could replace with:

AWS Textract

GCP Vision

🔹 pydantic

Validates the output schema.
Prevents badly formed responses.

🔹 python-multipart

Required to handle UploadFile in FastAPI.

🔹 pytest

Basic endpoint testing.
Shows professional mindset.
