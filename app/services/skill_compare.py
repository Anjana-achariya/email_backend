# def normalize(skill: str):
    
#     return skill.strip().lower()

# def get_missing_skills(resume_skills: list , jd_skills: list):
#     if not resume_skills or not jd_skills:
#         return []
#     resume_lower = {s.lower() for s in resume_skills}
#     jd_lower ={s.lower() for s in jd_skills}
#     missing = [skill for skill in jd_lower if skill not in resume_lower]

#     cleaned =[skill for skill in jd_skills if skill.lower() in missing]
#     return cleaned
# def get_matching_skills(resume_skills: list , jd_skills: list):
#     resume_lower = {s.lower() for s in resume_skills}
#     jd_lower ={s.lower() for s in jd_skills}
#     matched = resume_lower.intersection(jd_lower)
#     cleaned = [skill for skill in resume_skills if skill.lower() in matched]
#     return cleaned
def normalize(skill: str):
    """Clean and normalize skill names."""
    return skill.strip().lower()


def get_missing_skills(resume_skills: list, jd_skills: list):
    if not resume_skills or not jd_skills:
        return []

    resume_set = {normalize(s) for s in resume_skills}
    jd_set = {normalize(s) for s in jd_skills}

    missing_normalized = jd_set - resume_set

    cleaned = [s for s in jd_skills if normalize(s) in missing_normalized]

    return list(dict.fromkeys(cleaned))  
def get_matching_skills(resume_skills: list, jd_skills: list):
    if not resume_skills or not jd_skills:
        return []

    resume_set = {normalize(s) for s in resume_skills}
    jd_set = {normalize(s) for s in jd_skills}

    matched = resume_set & jd_set

    cleaned = [s for s in resume_skills if normalize(s) in matched]

    return list(dict.fromkeys(cleaned))  
