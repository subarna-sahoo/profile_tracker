from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import ViewLog, Base
from schemas import ViewLogResponse
from utils.geoip import get_location
from utils.svg_generator import generate_svg
from typing import List

# Create DB tables
Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/view", response_class=Response)
async def track_view(request: Request, username: str, db: Session = Depends(get_db)):
    ip = request.client.host
    ua = request.headers.get("user-agent", "").lower()
    referrer = request.headers.get("referer", "unknown")

    # Skip bots
    if "bot" in ua or "crawl" in ua or "monitor" in ua:
        return Response(content="<!-- bot ignored -->", media_type="text/html")

    # Fetch location
    location = await get_location(ip)

    # Save log
    log = ViewLog(
        username=username,
        ip_address=ip,
        user_agent=ua,
        referrer=referrer,
        country=location.get("country"),
        city=location.get("city")
    )
    db.add(log)
    db.commit()

    # Count views
    count = db.query(ViewLog).filter_by(username=username).count()
    svg = generate_svg(count)
    return Response(content=svg, media_type="image/svg+xml")


@router.get("/logs", response_model=List[ViewLogResponse])
def get_logs(username: str, db: Session = Depends(get_db)):
    logs = db.query(ViewLog).filter_by(username=username).order_by(ViewLog.timestamp.desc()).limit(50).all()
    return logs
