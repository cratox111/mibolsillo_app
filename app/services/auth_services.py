from fastapi import HTTPException, status
from datetime import datetime
from uuid import uuid4
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.repositories.user_repositories import UserRepository

pwd_hash = PasswordHash.recommended()


def service_register(name: str, last_name: str, email: str, password: str, db: Session) -> dict:
    repo = UserRepository(db)

    existing = repo.get_by_email(email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    password_hashed = pwd_hash.hash(password)

    user_data = {
        "id": str(uuid4()),
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password_hashed,
        "is_activate": True,
        "is_verified": False,
        "created_at": datetime.utcnow().isoformat(),
    }

    repo.create(user_data)

    return {"msg": "Usuario creado correctamente"}

