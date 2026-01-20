from pydantic import BaseModel  # this is a parser for files.
from typing import List

class Experience(BaseModel):
    role: str
    company: str
    years: str

class ResumeResponse(BaseModel):
    name: str
    email: str
    skills: List[str]
    experience: List[Experience]
