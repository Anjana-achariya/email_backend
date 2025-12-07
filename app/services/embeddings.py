from openai import OpenAI
import numpy as np
from app.core.config import OPENAI_API_KEY,EMBED_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text: str):
    if not text or text.strip() == "":
        return [0.0] * 1536
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input = text
    )
    return response.data[0].embedding

def cosine_similarity(a,b):
    a=np.array(a)
    b=np.array(b)
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0

    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def get_match_score(resume_text: str,jd_text :str):
    resume_vec = get_embedding(resume_text)
    jd_vec =get_embedding(jd_text)
    similarity = cosine_similarity(resume_vec,jd_vec)
    match_score = round(similarity*100 ,2)
    
    return match_score