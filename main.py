
# This file sets up the FastAPI application and includes all routes for the CV Parser API.

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="CV Parser API")

app.include_router(router)
