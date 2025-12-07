from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.email_generator import generate_email
from app.services.cover_letter import generate_cover_letter
from app.services.resume_improvements import generate_resume_improvements

router = APIRouter()


class EmailRequest(BaseModel):
    resume_text: str
    jd_text: str
    matching_skills: List[str] = []
    key_strengths: List[str] = []
    tone: str = "formal"  


class CoverLetterRequest(BaseModel):
    resume_text: str
    jd_text: str
    matching_skills: List[str] = []
    key_strengths: List[str] = []
    tone: str = "professional"


class SuggestionsRequest(BaseModel):
    resume_text: str
    jd_text: str
    missing_skills: List[str] = []
    match_score: float


@router.post("/generate-email")
async def generate_email_endpoint(payload: EmailRequest):
    """
    Generate a personalized job application email
    from resume, JD, skills, and key strengths.
    """
    email_text = generate_email(
        resume_text=payload.resume_text,
        jd_text=payload.jd_text,
        matching_skills=payload.matching_skills,
        key_strengths=payload.key_strengths,
        tone=payload.tone,
    )
    return {"email": email_text}


@router.post("/generate-cover-letter")
async def generate_cover_letter_endpoint(payload: CoverLetterRequest):
    """
    Generate a full cover letter from resume, JD, and strengths.
    """
    cover_letter_text = generate_cover_letter(
        resume_text=payload.resume_text,
        jd_text=payload.jd_text,
        matching_skills=payload.matching_skills,
        key_strengths=payload.key_strengths,
        tone=payload.tone,
    )
    return {"cover_letter": cover_letter_text}


@router.post("/resume-suggestions")
async def resume_suggestions_endpoint(payload: SuggestionsRequest):
    """
    Generate resume improvement suggestions from resume, JD,
    missing skills, and the match score.
    """
    suggestions = generate_resume_improvements(
        resume_text=payload.resume_text,
        jd_text=payload.jd_text,
        missing_skills=payload.missing_skills,
        match_score=payload.match_score,
    )
    return {"suggestions": suggestions}
