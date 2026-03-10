from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.clickhouse.init_db_script import create_tables
from app.clickhouse.router import clickhouse_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def root():
    return {"message": "Ok"}

app.include_router(clickhouse_router)
