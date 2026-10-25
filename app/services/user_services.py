from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repositories import UserRepository

def services_user_delete(email: str, db: Session):
    repo = UserRepository(db=db)

    existing = repo.get_by_email(email)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already not registered"
        )

    UserRepository.delete(email)

    return {"msg": "Usuario eliminado correctamente"}
    