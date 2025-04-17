from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ViewLogCreate(BaseModel):
    username: str
    ip_address: str
    user_agent: str
    country: Optional[str]
    city: Optional[str]
    referrer: Optional[str]

class ViewLogResponse(ViewLogCreate):
    timestamp: datetime