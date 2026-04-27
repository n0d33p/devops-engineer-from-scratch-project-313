import sentry_sdk
import os
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response, status, Query
from database import engine, get_session
from models import Link
from sqlmodel import Session, select, SQLModel
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from sqlalchemy import func

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
router = APIRouter()

@app.get('/ping')
async def pong():
    return {"ping": "pong"}

@router.post('/api/links', status_code=201)
async def create_link(link_data: Link, session: Session = Depends(get_session)):
    session.add(link_data)
    try:
        session.commit()
        session.refresh(link_data)
        return link_data
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail="Short url already exists")

@router.get('/api/links')
async def get_links(response: Response, session: Session = Depends(get_session), range: str = Query(None)):
    if range:
        indices = [int(i) for i in range.strip("[]").split(",")]
        start = indices[0]
        end = indices[1]
    else:
        start, end = 0, 9
    limit = end - start + 1
    total = session.exec(select(func.count(Link.id))).one()
    statement = select(Link).offset(start).limit(limit)
    links = session.exec(statement).all()
    response.headers["Content-Range"] = f"links {start}-{end}/{total}"
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    return links


@router.get('/api/links/{id}')
async def get_one_link(id: int, session: Session = Depends(get_session)):
    link = session.get(Link, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@router.put('/api/links/{id}')
async def update_link(id: int, link_data: Link, session: Session = Depends(get_session)):
    db_link = session.get(Link, id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db_link.original_url = link_data.original_url
    db_link.short_name = link_data.short_name

    session.add(db_link)
    session.commit()
    session.refresh(db_link)
    return db_link

@router.delete("/api/links/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(id: int, session: Session = Depends(get_session)):
    link = session.get(Link, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    session.delete(link)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

app.include_router(router)