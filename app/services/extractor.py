import fitz
import docx2txt
from fastapi import UploadFile
import tempfile
import os


def extract_text_from_pdf(path: str) -> str:
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"PDF extraction error: {e}"


def extract_text_from_docx(path: str) -> str:
    try:
        text = docx2txt.process(path)
        return text.strip()
    except Exception as e:
        return f"DOCX extraction error: {e}"


def extract_text_from_txt(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().strip()
    except Exception as e:
        return f"TXT extraction error: {e}"


def extract_from_textarea(text: str) -> str:
    if not text:
        return ""
    return text.strip()


def extract_text(file: UploadFile) -> str:
    suffix = os.path.splitext(file.filename)[1].lower()

    
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    
    if suffix == ".pdf":
        text = extract_text_from_pdf(tmp_path)
    elif suffix == ".docx":
        text = extract_text_from_docx(tmp_path)
    elif suffix == ".txt":
        text = extract_text_from_txt(tmp_path)
    else:
        text = f"Unsupported file type: {suffix}"

    os.remove(tmp_path)
    return text.strip()


def extract_text_from_path(path: str) -> str:
    suffix = os.path.splitext(path)[1].lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(path)
    elif suffix == ".docx":
        return extract_text_from_docx(path)
    elif suffix == ".txt":
        return extract_text_from_txt(path)
    else:
        return f"Unsupported file type: {suffix}"
