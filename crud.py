from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserLogin

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, login_data: UserLogin):
    user = get_user_by_email(db, login_data.email)
    if not user:
        return None

    if user.password != login_data.password:
        return None

    return user

def get_users(db: Session):
    return db.query(User).all()