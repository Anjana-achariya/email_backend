from openai import OpenAI
from app.core.config import OPENAI_API_KEY, LLM_MODEL
client= OpenAI(api_key=OPENAI_API_KEY)
def extract_skills_from_text(text: str):
    if not text or text.strip() == "":
        return []
    
    prompt = f"""
You are a professional skill extraction engine.

Extract ONLY the skills from the following text. 
Return the result strictly as a JSON list of strings.

Do NOT include explanations, formatting, notes, or sentences.

Text:
{text}

Example output:
["Python", "Machine Learning", "Teamwork"]
    
    """
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )
    
    raw = response.choices[0].message.content.strip()
    try:
        import json
        skills = json.loads(raw)
        return skills if isinstance(skills, list) else []
    except Exception:
        
        return []
    
    