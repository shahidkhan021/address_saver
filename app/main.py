from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
import validations
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
    ok = validations.validate_address(address.lat,address.long)
    if not ok:
        raise HTTPException(status_code=400, detail="Lattitude and Longitude Should be in correct format")
    return crud.save_address(db=db, address=address)


@app.post("/get_address_by_email/", response_model=list[schemas.Address])
def get_address_by_email(email: schemas.Email, db: Session = Depends(get_db)):
    db_user = crud.get_address_by_email(db, email=email.email)
    print(db_user)
    return db_user


@app.post("/get_address_by_lat_long/", response_model=list[schemas.Address])
def get_address_by_email(lat: schemas.Latitude,long: schemas.Longitude, db: Session = Depends(get_db)):
    db_user = crud.get_address_by_lat_long(db, lat=lat.lat,long=long.long)
    return jsonable_encoder(list(db_user))


@app.post("/get_address_all/", response_model=list[schemas.Address])
def get_all_address(db: Session = Depends(get_db)):
    address = crud.get_address(db)
    return jsonable_encoder(list(address))