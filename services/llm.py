import re
from schemas.resume import ResumeResponse, Experience

async def parse_resume_with_llm(text: str) -> ResumeResponse:
    # Simulación de prompt + respuesta estructurada

    return ResumeResponse(
        name="John Doe",
        email="john.doe@email.com",
        skills=["Python", "Django", "AWS", "Docker"],
        experience=[
            {
                "role": "Backend Developer",
                "company": "X Company",
                "years": "2019-2024"
            }
        ]
    )


async def parse_cv_with_llm(text: str) -> ResumeResponse:
    """
    Simulates an LLM extracting structured data from OCR text.
    """

    name = extract_name(text)
    email = extract_email(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    return ResumeResponse(
        name=name,
        email=email,
        skills=skills,
        experience=experience
    )


def extract_name(text: str) -> str:
    lines = text.strip().split("\n")
    return lines[0].strip()


def extract_email(text: str) -> str:
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match.group(0) if match else ""


def extract_skills(text: str) -> list[str]:
    match = re.search(r"Skills?:\s*(.*)", text, re.IGNORECASE)
    if not match:
        return []

    skills_raw = match.group(1)
    return [s.strip() for s in skills_raw.split(",")]


def extract_experience(text: str) -> list:
    if "Experience" not in text:
        return []

    return [
        {
            "role": "Backend Developer",
            "company": "ACME",
            "years": "2019-2024"
        }
    ]
