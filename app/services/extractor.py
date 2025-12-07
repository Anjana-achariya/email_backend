from pypdf import PdfReader
import docx2txt
from fastapi import UploadFile
import tempfile
import os

def extract_text_from_pdf(path: str) -> str:
    try:
        reader = PdfReader(path)
        text = "".join(page.extract_text() or "" for page in reader.pages)
        return text.strip()
    except Exception:
        return ""

def extract_text_from_docx(path: str) -> str:
    try:
        text = docx2txt.process(path)
        return text.strip() if text else ""
    except Exception:
        return ""

def extract_text_from_txt(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().strip()
    except Exception:
        return ""

def extract_from_textarea(text: str) -> str:
    return text.strip() if text else ""

def extract_text(file: UploadFile) -> str:
    """
    Handles all uploaded files. Supports PDF, DOCX, TXT.
    Safely writes the uploaded file to a temporary location.
    """

    suffix = os.path.splitext(file.filename)[1].lower()

    contents = file.file.read()
    if not contents:
        return ""

    file.file.seek(0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    if suffix == ".pdf":
        text = extract_text_from_pdf(tmp_path)
    elif suffix == ".docx":
        text = extract_text_from_docx(tmp_path)
    elif suffix == ".txt":
        text = extract_text_from_txt(tmp_path)
    else:
        text = ""

    try:
        os.remove(tmp_path)
    except Exception:
        pass

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
        return ""
