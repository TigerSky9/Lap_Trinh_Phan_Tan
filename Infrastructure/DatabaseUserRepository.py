from .UserRepository import UserRepository
from .models import UserModel
from sqlalchemy.orm import Session
from Entities.User import User

class DatabaseUserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_email(self, email):
        user_model = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user_model:
            return User(email=user_model.email, password=user_model.hashed_password)
        return None

    def save(self, user):
        hashed_password = user.hashed_password
        user_model = UserModel(email=user.email, hashed_password=hashed_password)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model
