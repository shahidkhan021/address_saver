from sqlalchemy.orm import Session
import models, schemas


def get_address(db: Session):
    return db.query(models.Address).all()

def get_address_by_lat_long(db:Session, lat:float, long: float):
    return db.query(models.Address).filter(models.Address.lat==lat,models.Address.long==long).all()

def get_address_by_email(db:Session,email:str):
    return db.query(models.Address).filter(models.Address.email== email).all()

def save_address(db:Session,address:schemas.Address):
    address_qry = models.Address(email=address.email,address=address.address,lat=address.lat,long=address.long)
    db.add(address_qry)
    db.commit()
    db.refresh(address_qry)
    return address_qry