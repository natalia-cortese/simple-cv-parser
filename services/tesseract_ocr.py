from utils.file_utils import is_pdf, is_image
from services.ocr import extract_text as mock_extract_text


async def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from a PDF or image using Tesseract OCR.
    """
    # NOTE: We import OCR deps lazily to avoid import-time crashes on unsupported Python
    # versions (e.g., Python 3.14 + older pytesseract).
    try:
        import pytesseract  # type: ignore
        from PIL import Image  # type: ignore
        from pdf2image import convert_from_path  # type: ignore
    except Exception:
        # Fallback to mock OCR so the API remains usable even if Tesseract deps are missing.
        return await mock_extract_text(file_path)

    if is_pdf(file_path):
        return _extract_from_pdf(file_path, pytesseract=pytesseract, convert_from_path=convert_from_path)
    elif is_image(file_path):
        return _extract_from_image(file_path, pytesseract=pytesseract, Image=Image)
    else:
        raise ValueError("Unsupported file type for OCR")


def _extract_from_pdf(path: str, *, pytesseract, convert_from_path) -> str:
    pages = convert_from_path(path)
    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)

    return text


def _extract_from_image(path: str, *, pytesseract, Image) -> str:
    image = Image.open(path)
    return pytesseract.image_to_string(image)
