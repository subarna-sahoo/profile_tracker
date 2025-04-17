from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class ViewLog(Base):
    __tablename__ = "view_logs"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    ip_address = Column(String)
    user_agent = Column(String)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    referrer = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)