from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.auth_services import service_register
from app.schemas.user_schema import UserCreate
from app.core.db import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserCreate, status_code=201)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    return service_register(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        db=db
    )
