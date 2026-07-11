from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class School(Base):
    __tablename__ = "schools"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True)

    tenant_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tenants.id")
    )

    name: Mapped[str] = mapped_column(String(255))

    address: Mapped[str] = mapped_column(Text)

    phone: Mapped[str] = mapped_column(String(50))

    created_at: Mapped[DateTime]
