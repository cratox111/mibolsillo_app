from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.services.auth_services import service_register, service_login, service_me
from app.schemas.user_schema import UserCreate, UserResponse
from app.core.security import oauth
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

@router.post('/login', status_code=201)
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    return service_login(
        email=form.username, 
        password=form.password,
        db=db
    )


@router.get("/me", response_model=UserResponse, status_code=200)
async def me(token: str = Depends(oauth), db: Session = Depends(get_db)):
    return service_me(token=token, db=db)
