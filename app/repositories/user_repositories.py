from typing import Optional
from sqlalchemy.orm import Session
from app.models.user_model import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: dict) -> User:
        db_user = User(**user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: str, update_data: dict) -> Optional[User]:
        db_user = self.get_by_id(user_id)

        if not db_user:
            return None
        
        for field, value in update_data.items():
            setattr(db_user, field, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_email: str) -> bool:
        db_user = self.get_by_email(user_email)

        if not db_user:
            return False
        
        self.db.delete(db_user)
        self.db.commit()
        return True