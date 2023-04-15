from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from . import validations
from fastapi.encoders import jsonable_encoder


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# no authentication done usually jwt tokens will be used
@app.post("/save_address/", response_model=schemas.Address)
def create_user(address: schemas.Address, db: Session = Depends(get_db)):
    db_user = crud.get_address_by_email(db, email=address.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    ok = validations.validate_address(address)
    if not ok:
        raise HTTPException(status_code=400, detail="Lattitude and Longitude Should be in correct format")
    return crud.create_user(db=db, user=address)


@app.post("/get_address_by_email/", response_model=schemas.Address)
def get_address_by_email(address: schemas.Address, db: Session = Depends(get_db)):
    db_user = crud.get_address_by_email(db, email=address.email)
    return jsonable_encoder(list(db_user))


@app.post("/get_address_by_lat_long/", response_model=schemas.Address)
def get_address_by_email(lat: schemas.Address.lat,long=schemas.Address.long, db: Session = Depends(get_db)):
    db_user = crud.get_address_by_lat_long(db, lat=lat,long=long)
    return jsonable_encoder(list(db_user))


@app.post("/get_address_by_lat_long/", response_model=schemas.Address)
def get_all_address(address: schemas.Address, db: Session = Depends(get_db)):
    address = crud.get_address(db)
    return jsonable_encoder(list(address))