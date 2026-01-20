import asyncio


async def extract_text(file_path: str) -> str:
    """
    Mock OCR function.

    Right now we ignore the actual file contents and return a fixed sample
    resume text, but keep this async so it can later wrap real OCR calls.
    """
    # Simulate I/O-bound work (e.g. calling Tesseract / external OCR service)
    await asyncio.sleep(0)

    # En una versión real:
    # - Leer el archivo en `file_path`
    # - Tesseract / GCP Vision / AWS Textract, etc.

    return """
    John Doe
    Email: john.doe@email.com
    Backend Engineer with 5 years of experience.

    Skills:
    - Python
    - Django
    - AWS
    - Docker

    Experience:
    Backend Developer at ACME Corp (2019 - 2024)
    """
