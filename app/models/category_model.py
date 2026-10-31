from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from datetime import datetime

from app.core.db import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[str] = mapped_column(String, primary_key=True)

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    color: Mapped[str] = mapped_column(
        String,
        nullable=True,
        unique=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    parent: Mapped["User"] = relationship(back_populates="category")



