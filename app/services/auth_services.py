from fastapi import HTTPException, status
from datetime import datetime
from uuid import uuid4
from jose import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from datetime import timedelta, datetime, timezone

from app.repositories.user_repositories import UserRepository

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

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


def service_login(email: str, password: str, db: Session):
    repo = UserRepository(db)

    existing = repo.get_by_email(email=email)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already not registered"
        )

    if not pwd_hash.verify(password, existing.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password"
        )

    return {
        "access_token": jwt.encode({
            "iss": "auth/login",
            "sub": existing.id,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }, key=SECRET_KEY, algorithm=ALGORITHM),
        "token_type": "bearer",
    }

def token_decode(token):
    token_de = jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)

    return token_de

def service_me(token, db: Session):
    repo = UserRepository(db=db)
    token_de = token_decode(token=token)

    existing = repo.get_by_id(user_id=token_de["sub"])

    if not existing:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not token"
        )

    return existing


    


