from sqlalchemy import String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True)

    tenant_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tenants.id")
    )

    student_number: Mapped[str] = mapped_column(String(50))

    first_name: Mapped[str] = mapped_column(String(100))

    last_name: Mapped[str] = mapped_column(String(100))

    birth_date: Mapped[Date]

    active: Mapped[bool] = mapped_column(Boolean)

    created_at: Mapped[DateTime]
