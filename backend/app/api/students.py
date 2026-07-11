from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students(db: Session = Depends(get_db)):

    result = db.execute(
        text("SELECT * FROM students")
    )

    students = [dict(row._mapping) for row in result]

    return students
