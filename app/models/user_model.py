from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime
from datetime import datetime

from app.core.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String, primary_key=True)

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    is_activate: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )