from sqlmodel import Session, select
from sqlalchemy import func
from app.models import Link

def get_total_count(session: Session) -> int:
    return session.exec(select(func.count(Link.id))).one()

def get_links(session: Session, offset: int, limit: int):
    statement = select(Link).offset(offset).limit(limit)
    return session.exec(statement).all()

def get_link_by_id(session: Session, link_id: int):
    return session.get(Link, link_id)

def get_link_by_short_name(session: Session, short_name: str):
    statement = select(Link).where(Link.short_name == short_name)
    return session.exec(statement).first()

def save_link(session: Session, link: Link):
    session.add(link)
    session.commit()
    session.refresh(link)
    return link

def delete_link(session: Session, link: Link):
    session.delete(link)
    session.commit()