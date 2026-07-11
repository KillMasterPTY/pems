from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.students import router as students_router

app = FastAPI(
    title="PEMS API",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(students_router)

@app.get("/")
def root():
    return {
        "application": "PEMS",
        "status": "online",
        "version": "0.1.0"
    }
