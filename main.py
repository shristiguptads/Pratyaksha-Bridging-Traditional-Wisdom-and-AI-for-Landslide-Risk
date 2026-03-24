from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, risk_predictor
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pratyaksha API")

# Risk prediction
@app.post("/predict-risk/")
def get_risk_prediction(features: dict):
    return risk_predictor.predict_risk(features)

# Observation endpoints
@app.post("/observations/", response_model=schemas.Observation)
def create_observation(obs: schemas.ObservationCreate, db: Session = Depends(get_db)):
    return crud.create_observation(db, obs)

@app.get("/observations/", response_model=list[schemas.Observation])
def read_observations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_observations(db, skip=skip, limit=limit)

@app.get("/")
def root():
    return {"message": "Pratyaksha Backend is running"}