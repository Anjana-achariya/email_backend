from openai import OpenAI
from app.core.config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_key_strengths(resume_text: str, jd_text: str, matched_skills: list):
    """
    Uses the LLM to extract the candidate's strongest job-relevant strengths.
    Returns a list of bullet points.
    """

    if not resume_text or not jd_text:
        return ["Unable to identify strengths — missing resume or job description."]

    prompt = f"""
You are an expert career analyst.
Based on the Resume and Job Description below, identify the candidate's TOP key strengths that make them a good fit.

Return the output as a clean JSON list of short bullet points.

Resume:
{resume_text}

Job Description:
{jd_text}

Matching Skills:
{matched_skills}

Example output:
[
  "Strong proficiency in Python and SQL",
  "Experience with FastAPI and backend development",
  "Hands-on exposure to cloud technologies",
  "Excellent problem-solving and analytical skills"
]
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    raw = response.choices[0].message.content

    
    try:
        import json
        strengths = json.loads(raw)

        if isinstance(strengths, list):
            return strengths
        else:
            return ["AI returned unexpected format for strengths."]
    except Exception:
        
        return ["Unable to parse strengths from AI response."]