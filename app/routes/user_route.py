from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_services import services_user_delete
from app.core.db import get_db

router = APIRouter(prefix="/user", tags=["user"])


@router.delete(path="/", status_code=status.HTTP_200_OK)
async def route_user_delete(email: str, db: Session = Depends(get_db)):
    return services_user_delete(
        db=db,
        email=email
    )