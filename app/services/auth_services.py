from fastapi import HTTPException, status
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Session

from app.repositories.user_repositories import UserRepository
from app.core.security import hash_password, verity_password, create_token, get_user_of_token


def service_register(name: str, last_name: str, email: str, password: str, db: Session) -> dict:
    repo = UserRepository(db)

    existing = repo.get_by_email(email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    user_data = {
        "id": str(uuid4()),
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": hash_password(password=password),
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

    verity_password(password=password, correct_password=existing.password)

    return {
        "access_token": create_token(user=existing),
        "token_type": "bearer",
    }


def service_me(token, db: Session):
    repo = UserRepository(db=db)
    
    existing = repo.get_by_id(user_id=get_user_of_token(token=token))

    if not existing:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not token"
        )

    return existing


    


