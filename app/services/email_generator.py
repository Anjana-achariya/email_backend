from openai import OpenAI
from app.core.config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_email(resume_text: str, jd_text: str, matching_skills: list, key_strengths: list, tone: str = "formal"):
    """
    Generates a personalized job application email based on resume, JD, and strengths.
    """
    if not resume_text or not jd_text:
        return "Unable to generate email — missing resume or job description."


    prompt = f"""
Write a job application email based on the following details.

Tone: {tone}

Resume Summary:
{resume_text}

Job Description:
{jd_text}

Matching Skills:
{matching_skills}

Key Strengths:
{key_strengths}

Requirements for the email:
- 100% professional and personalized
- Clear, confident, and concise
- Mention relevant strengths
- Show interest in the role
- NO placeholders like {{Company Name}}
- NO overly long paragraphs
- Should feel written by a real human

Return ONLY the email text without quotes.
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7   )

    return response.choices[0].message.content.strip()
