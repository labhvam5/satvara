import models
from fastapi import FastAPI
from routers.posts import router as post_router
from routers.users import router as user_router
from routers.auth import router as auth_router
from db import engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(post_router)
app.include_router(user_router)

@app.get("/healthcheck")
async def root():
    return {"message": "Hello World"}
