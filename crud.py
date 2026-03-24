from sqlalchemy.orm import Session
from . import models, schemas

def create_observation(db: Session, obs: schemas.ObservationCreate):
    db_obs = models.Observation(**obs.model_dump())
    db.add(db_obs)
    db.commit()
    db.refresh(db_obs)
    return db_obs

def get_observations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Observation).offset(skip).limit(limit).all()