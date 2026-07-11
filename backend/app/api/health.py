from fastapi import APIRouter
from sqlalchemy import text
from app.db.database import engine

router = APIRouter()

@router.get("/health/db")
def health_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "ok"}
