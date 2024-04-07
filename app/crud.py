from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.params import Body
# from sqlalchemy import Session
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import SessionLocal, engine
from .schemas import *


def create_user(user : UserCreate, db: Session):

    hashed_password = utils.hash_password(user.password)

    new_user = models.User(email = user.email, password = hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def get_user(db: Session, user_id: int):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email : str):

    user = db.query(models.User).filter(models.User.email == email).first()
    
    # if not user:
    #     raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"User with email {email} was not found"))
    
    return  user


def update_user(user_id: int, updated_user: UserUpdate, db: Session):

    user_query = db.query(models.User).filter((models.User).id == user_id)
    user = user_query.first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} was not found")

    update_data = updated_user.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)
    return user
    


# def delete_user(email: str, db: Session):
#     user = db.query(models.User).filter(models.User.email == email)

#     if user.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with email {email} was not found")
    
#     user.delete(synchronize_session=False)
#     db.commit()

#     return user

def create_taxCalc(taxCalc: taxCalc, user_id: int, db: Session):

    db_taxCalc = models.TaxCalculation(owner_id = user_id, title = taxCalc.title, description = taxCalc.description)

    db.add(db_taxCalc)
    db.commit()
    db.refresh(db_taxCalc)

    return db_taxCalc


def get_taxCalc_by_user(user_id: int, db: Session):

    taxCalc = db.query(models.TaxCalculation).filter(models.TaxCalculation.owner_id == user_id).all()

    return taxCalc


def get_taxCalcs(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.taxCalc).offset(skip).limit(limit).all()

def update_taxCalc(taxCalc_id: int, updated_taxCalc: taxCalcUpdate, db: Session):

    taxCalc_query = db.query(models.TaxCalculation).filter((models.TaxCalculation).id == taxCalc)
    taxCalc = taxCalc_query.first()
    
    if taxCalc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tax Calculation with id {taxCalc} was not found")

    update_data = updated_taxCalc.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(taxCalc, key, value)
        
    return taxCalc