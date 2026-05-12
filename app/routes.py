from fastapi import APIRouter, Depends, HTTPException, Response, status, Query, Request
from sqlmodel import Session
from app.models import Link
from app.database import get_session
from fastapi.responses import RedirectResponse
import os
from app import repository

router = APIRouter()

def format_link(link: Link, request: Request) -> dict:
    base = os.getenv("BASE_URL", str(request.base_url)).rstrip('/')
    link_dict = link.model_dump()
    link_dict["short_url"] = f"{base}/r/{link.short_name}"
    return link_dict

@router.post('/api/links', status_code=201)
async def create_link(link_data: Link, request: Request, session: Session = Depends(get_session)):
    try:
        saved_link = repository.save_link(session, link_data)
        return format_link(saved_link, request)
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail="Short url already exists")
    
@router.get('/api/links')
async def get_links(request: Request, response: Response, session: Session = Depends(get_session), range: str = Query(None)):
    start, end = 0, 9
    if range:
        indices = [int(i) for i in range.strip("[]").split(",")]
        start, end = indices[0], indices[1]
        
    total = repository.get_total_count(session)
    links = repository.get_links(session, offset=start, limit=end - start + 1)
    
    response.headers["Content-Range"] = f"links {start}-{end}/{total}"
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    return [format_link(link, request) for link in links]

@router.get('/api/links/{id}')
async def get_one_link(id: int, request: Request, session: Session = Depends(get_session)):
    link = repository.get_link_by_id(session, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return format_link(link, request)

@router.put('/api/links/{id}')
async def update_link(id: int, link_data: Link, request: Request, session: Session = Depends(get_session)):
    db_link = repository.get_link_by_id(session, id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db_link.original_url = link_data.original_url
    db_link.short_name = link_data.short_name

    updated_link = repository.save_link(session, db_link)
    return format_link(updated_link, request)

@router.delete("/api/links/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(id: int, session: Session = Depends(get_session)):
    link = repository.get_link_by_id(session, id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    repository.delete_link(session, link)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/r/{short_name}')
async def shortlink_redirect(short_name: str, session: Session = Depends(get_session)):
    link = repository.get_link_by_short_name(session, short_name)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return RedirectResponse(url=link.original_url)