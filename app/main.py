import sentry_sdk
import os
from fastapi import FastAPI
from app.database import engine
from sqlmodel import SQLModel
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as links_router

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(links_router)