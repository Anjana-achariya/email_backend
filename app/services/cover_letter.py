from openai import OpenAI
from app.core.config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_cover_letter(
    resume_text: str, 
    jd_text: str, 
    matching_skills: list, 
    key_strengths: list, 
    tone: str = "professional"
):
    """
    Generates a complete job-specific cover letter based on resume and JD.
    """
    if not resume_text or not jd_text:
        return "Unable to generate cover letter — missing resume or job description."

    prompt = f"""
Write a polished, professional cover letter tailored to the following resume and job description.

Tone: {tone}

Resume:
{resume_text}

Job Description:
{jd_text}

Matching Skills:
{matching_skills}

Key Strengths:
{key_strengths}

Requirements:
- Should be 3–5 paragraphs
- Include an engaging opening
- Highlight the most relevant skills and strengths
- Show enthusiasm for the job/company
- Clearly communicate why the candidate is a strong fit
- End with a confident closing paragraph
- No placeholders like {{Company}}, {{Role}}, or {{Hiring Manager}}
- Do NOT include brackets, instructions, or notes
- Return ONLY the cover letter as plain text (no quotes)
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.65,
    )

    return response.choices[0].message.content.strip()
