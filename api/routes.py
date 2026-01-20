from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.file_utils import validate_file, save_temp_file
from services.ocr import extract_text
from services.tesseract_ocr import extract_text_from_file
from services.llm import parse_resume_with_llm, parse_cv_with_llm
from schemas.resume import ResumeResponse

router = APIRouter()


@router.post("/parse-resume", response_model=ResumeResponse)
async def parse_resume(file: UploadFile = File(...)):
    """
    Main endpoint to receive a resume file, run OCR + LLM, and return structured data.
    """
    try:
        # Validate content type and basic constraints
        validate_file(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Persist file to a temp path for the OCR layer
    path = await save_temp_file(file)

    # Run (mock) OCR on the saved file
    text = await extract_text(path)

    # Run (mock) LLM to parse the text into a structured schema
    structured_data = await parse_resume_with_llm(text)

    return structured_data


@router.post("/parse-cv", response_model=ResumeResponse)
async def parse_cv(file: UploadFile = File(...)):
    """
    Second Main endpoint to receive a resume file, run OCR + LLM, and return structured data.
    This endpoint is actually using our OCR and not the mocking one.
    """
    try:
        # Validate content type and basic constraints
        validate_file(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Persist file to a temp path for the OCR layer
    path = await save_temp_file(file)

    # Run Tesseract OCR (falls back to mock OCR if deps are unavailable)
    text = await extract_text_from_file(path)

    # Run (mock) LLM to parse the text into a structured schema
    structured_data = await parse_cv_with_llm(text)

    return structured_data
