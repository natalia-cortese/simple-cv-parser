from typing import Tuple
from fastapi import UploadFile
import os
import tempfile


ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "image/png",
    "image/jpeg"
}


def validate_file(file: UploadFile) -> None:
    """
    Validates file type and basic constraints.
    """
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise ValueError(f"Unsupported file type: {file.content_type}")


async def save_temp_file(file: UploadFile) -> str:
    """
    Saves uploaded file to a temporary location and returns its path.
    """
    suffix = os.path.splitext(file.filename)[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        return tmp.name


def is_pdf(file_path: str) -> bool:
    return file_path.lower().endswith(".pdf")


def is_image(file_path: str) -> bool:
    return file_path.lower().endswith((".png", ".jpg", ".jpeg"))
