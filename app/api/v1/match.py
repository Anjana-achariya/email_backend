from fastapi import APIRouter, UploadFile, File, Form
from app.services.extractor import extract_text, extract_from_textarea
from app.services.embeddings import get_match_score
from app.services.llm import extract_skills_from_text
from app.services.skill_compare import get_missing_skills, get_matching_skills
from app.services.key_strengths import generate_key_strengths

router = APIRouter()

@router.post("/match")
async def match_resume_jd(
    resume_file: UploadFile = File(None),
    jd_file: UploadFile = File(None),
    resume_text: str = Form(None),
    jd_text: str = Form(None),
):
   
    if resume_file:
        resume_content = extract_text(resume_file)
    else:
        resume_content = extract_from_textarea(resume_text)

  
    if jd_file:
        jd_content = extract_text(jd_file)
    else:
        jd_content = extract_from_textarea(jd_text)

    
    match_score = get_match_score(resume_content, jd_content)
    resume_skills = extract_skills_from_text(resume_content)
    jd_skills = extract_skills_from_text(jd_content)

    matching_skills = get_matching_skills(resume_skills, jd_skills)
    missing_skills = get_missing_skills(resume_skills, jd_skills)


    key_strengths = generate_key_strengths(
        resume_content, jd_content, matching_skills
    )

    return {
        "resume_text": resume_content,   
        "jd_text": jd_content,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "key_strengths": key_strengths,
        "match_score": match_score,
        "message": "Match analysis completed successfully."
    }
