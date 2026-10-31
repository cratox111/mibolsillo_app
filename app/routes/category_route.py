from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import oauth
from app.core.db import get_db
from app.core.security import get_user_of_token
from app.services.category_services import service_add_category, service_get_all_categories, service_get_category, service_delete_category


router = APIRouter(prefix="/category", tags=["category"])


@router.get(path="/get")
async def get_all_categories(token: str = Depends(oauth), db: Session = Depends(get_db)):
    return service_get_all_categories(db=db)


@router.get(path="/get_by_name")
async def get_category(category_name: str, token: str = Depends(oauth), db: Session = Depends(get_db)):
    return service_get_category(category_name=category_name, db=db)


@router.post(path="/add")
async def add_category(category_name: str, color: str, token: str = Depends(oauth), db: Session = Depends(get_db)):
    return service_add_category(
        category_name=category_name,
        color=color,
        user_id=get_user_of_token(token=token),
        db=db
    )


@router.delete(path="/delete")
async def add_category(category_name: str, token: str = Depends(oauth), db: Session = Depends(get_db)):
    return service_delete_category(category_name=category_name, db=db)