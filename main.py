from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.match import router as match_router
from app.api.v1.generate import router as generate_router

app = FastAPI(
    title="SkillSculpt AI Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {"status": "backend running"}

app.include_router(match_router, prefix="/api/v1")

app.include_router(generate_router, prefix="/api/v1")
