from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class ObservationBase(BaseModel):
    latitude: float
    longitude: float
    traditional_features: Dict[str, int]
    photos: Optional[List[str]] = []
    user_id: Optional[str] = None

class ObservationCreate(ObservationBase):
    pass

class Observation(ObservationBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True