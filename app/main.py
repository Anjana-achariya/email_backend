from fastapi import FastAPI
from app.api.v1.match import router as match_router
from fastapi.middleware.cors import CORSMiddleware

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
