from typing import Optional
from sqlalchemy.orm import Session
from app.models.category_model import Category


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db


    def get_categories(self):
        return self.db.query(Category).all()
    

    def get_by_id(self, category_id: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()


    def get_by_name(self, category_name: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.name == category_name).first()


    def create(self, category_data: dict) -> Category:
        db_user = Category(**category_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def update(self, category_id: str, update_data: dict) -> Optional[Category]:
        db_category = self.get_by_id(category_id=category_id)

        if not db_category:
            return None
        
        for field, value in update_data.items():
            setattr(db_category, field, value)

        self.db.commit()
        self.db.refresh(db_category)
        return db_category


    def delete(self, category_name: str) -> bool:
        db_category = self.get_by_name(category_name=category_name)

        if not db_category:
            return False
        
        self.db.delete(db_category)
        self.db.commit()
        return True