from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="CV Parser API")

app.include_router(router)
