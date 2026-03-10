import uvicorn
from fastapi import FastAPI
from src.app.core.database import engine
from src.app.models.user_model import Base
from src.app.routers.user_router import router as user_router

app = FastAPI(
    title="FastAPI GitHub PR Practice",
    description="User CRUD API using FastAPI",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "FastAPI application is running"}


# Register routers
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )