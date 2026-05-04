import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session

load_dotenv()
DEFAULT_DB_URL = "postgresql://user:password@db:5432/shortener_db"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)
print(f"Connecting to: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session