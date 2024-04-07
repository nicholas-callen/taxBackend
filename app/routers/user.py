from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, crud, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user : schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id : int, db: Session = Depends(get_db)):


    db_user = crud.get_user(db, user_id = user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@router.post("/{user_id}", response_model=schemas.User)
def update_user(user_id : int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db)):

    db_user = crud.update_user(user_id, updated_user, db)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


# def delete_user(email: str, db: Session):
#     user = db.query(models.User).filter(models.User.email == email)

#     if user.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with email {email} was not found")
    
#     user.delete(synchronize_session=False)
#     db.commit()

#     return user
