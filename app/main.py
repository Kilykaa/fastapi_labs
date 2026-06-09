from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="Lab 3 CRUD API")

app.include_router(api_router, prefix="/api/v1")