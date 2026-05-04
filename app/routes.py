from fastapi import APIRouter, Depends, HTTPException, Response, status, Query, Request
from sqlmodel import Session, select
from app.models import Link
from app.database import get_session
from sqlalchemy import func
from fastapi.responses import RedirectResponse
import os

router = APIRouter()

def format_link(link: Link, request: Request) -> dict:
    base = os.getenv("BASE_URL", str(request.base_url)).rstrip('/')
    link_dict = link.model_dump()
    link_dict["short_url"] = f"{base}/r/{link.short_name}"
    return link_dict

@router.post('/api/links', status_code=201)
async def create_link(link_data: Link, request: Request, session: Session = Depends(get_session)):
    session.add(link_data)
    try:
        session.commit()
        session.refresh(link_data)
        return format_link(link_data, request)
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail="Short url already exists")
    
@router.get('/api/links')
async def get_links(request: Request, response: Response, session: Session = Depends(get_session), range: str = Query(None)):
    if range:
        indices = [int(i) for i in range.strip("[]").split(",")]
        start, end = indices[0], indices[1]
    else:
        start, end = 0, 9
        
    limit = end - start + 1
    total = session.exec(select(func.count(Link.id))).one()
    statement = select(Link).offset(start).limit(limit)
    links = session.exec(statement).all()
    
    result = [format_link(link, request) for link in links]

    response.headers["Content-Range"] = f"links {start}-{end}/{total}"
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    return result

@router.get('/api/links/{id}')
async def get_one_link(id: int, request: Request, session: Session = Depends(get_session)):
    link = session.get(Link, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return format_link(link, request)

@router.put('/api/links/{id}')
async def update_link(id: int, link_data: Link, request: Request, session: Session = Depends(get_session)):
    db_link = session.get(Link, id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db_link.original_url = link_data.original_url
    db_link.short_name = link_data.short_name

    session.add(db_link)
    session.commit()
    session.refresh(db_link)
    return format_link(db_link, request)

@router.delete("/api/links/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(id: int, session: Session = Depends(get_session)):
    link = session.get(Link, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    session.delete(link)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/r/{short_name}')
async def shortlink_redirect(short_name: str, session: Session = Depends(get_session)):
    statement = select(Link).where(Link.short_name == short_name)
    link = session.exec(statement).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    return RedirectResponse(url=link.original_url)