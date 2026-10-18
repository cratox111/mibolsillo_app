from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from core.db import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String, 
        unique=True, 
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    is_activate: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    is_verified: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    created_at: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )
