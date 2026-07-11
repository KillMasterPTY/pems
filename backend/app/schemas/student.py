from pydantic import BaseModel
from datetime import date, datetime


class StudentResponse(BaseModel):
    id: str
    tenant_id: str
    student_number: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None
    active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
