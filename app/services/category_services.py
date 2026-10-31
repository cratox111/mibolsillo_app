from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import uuid4

from app.repositories.category_repositories import CategoryRepository


def service_get_all_categories(db: Session):
    repo = CategoryRepository(db=db)

    return repo.get_categories()


def service_get_category(category_name: str, db: Session):
    repo = CategoryRepository(db=db)

    return repo.get_by_name(category_name=category_name)


def service_add_category(category_name: str, color: str, user_id: str, db: Session):
    repo = CategoryRepository(db=db)

    if repo.get_by_name(category_name=category_name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Existing category"
        )

    category = {
        "id": str(uuid4()),
        "user_id": user_id,
        "name": category_name,
        "color": color, 
    }

    repo.create(category_data=category)
    
    
    return {"msg": "Category created successfully"}
    

def service_delete_category(category_name: str, db: Session):
    repo = CategoryRepository(db=db)

    repo.delete(category_name=category_name)

    return {"msg": "Category deleted successfully"}