from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, crud, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/taxCalcs",
    tags=['taxCalcs']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.taxCalc)
def create_taxCalc(taxCalc: schemas.taxCalcCreate, current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):

    # Not sure about checks for now

    return crud.create_taxCalc(taxCalc = taxCalc, user_id = current_user.id, db = db)



@router.get("/", response_model=list[schemas.taxCalc])
def get_taxCalcs(current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):

    return crud.get_taxCalc_by_user(current_user.id, db)


@router.post("/{taxCalc_id}", response_model=schemas.taxCalc)
def update_taxCalc(taxCalc_id : int, updated_taxCalc: schemas.taxCalcUpdate, db: Session = Depends(get_db)):

    db_taxCalc = crud.update_taxCalc(taxCalc_id, updated_taxCalc, db)

    if db_taxCalc is None:
        raise HTTPException(status_code=404, detail="Tax Calculation not found")
    
    return db_taxCalc


# Finish later
# @router.get("/{post_id}", response_model=list[schemas.taxCalc])
# def get_taxCalcs(user_id: int, get_current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):

#     return crud.get_taxCalc_by_user(user_id, db)
