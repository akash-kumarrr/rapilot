from schemas.user import UserBase, UserCreate, UserResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User
from core.security import hash_password

def create(user_payload : UserCreate, db : Session)  :
    user_payload.password = hash_password(user_payload.password)
    stmt = select(User).where(User.email == user_payload.email)
    user = db.scalars(stmt).first()

    if user :
        raise Exception(
            "user laready exists"
        )

    db_user = User(**user_payload.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

def read(userid : str, db : Session):
    return db.scalars(select(User).where(User.userid == userid)).first()

def delete(user_id : str, db : Session):
    stmt = select(User).where(User.id == user_id)
    user = db.scalars(stmt).first()
    
    if not user : 
        raise Exception(
            "Not found"
        )
    
    db.delete(user)
    db.commit()
    
    return {
        "message" : "user deleted"
    }