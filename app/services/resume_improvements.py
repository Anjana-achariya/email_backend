from openai import OpenAI
from app.core.config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_resume_improvements(resume_text: str, jd_text: str, missing_skills: list, match_score: float):
    """
    Provides resume improvement suggestions tailored to the job description.
    Returns a JSON list of actionable bullet points.
    """
    if not resume_text or not jd_text:
        return []

    prompt = f"""
You are an expert ATS resume analyst.

Your job is to give highly actionable resume improvement suggestions
based on the candidate's resume, the job description, the missing skills,
and the current match score.

Resume:
{resume_text}

Job Description:
{jd_text}

Missing Skills:
{missing_skills}

Current Match Score: {match_score}

Return output STRICTLY as a JSON list of short bullet points.

Each point should:
- Be direct and actionable
- Improve hiring chances
- Optimized for ATS + human hiring managers
- Focused on clarity, strength, and alignment with the JD
- Show what to add/remove/rephrase
- Help increase alignment with the JD

Example output:
[
  "Add a dedicated Skills section with more HR-focused tools.",
  "Include measurable achievements to make resume more impactful.",
  "Highlight experience in compliance and reporting if applicable."
]
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4  
    )

    raw = response.choices[0].message.content.strip()

    try:
        import json
        suggestions = json.loads(raw)
        return suggestions if isinstance(suggestions, list) else []
    except:
        return []
