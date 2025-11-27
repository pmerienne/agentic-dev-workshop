from contextlib import asynccontextmanager
from fastapi import FastAPI
from task_flow_api.api import router as tasks_router
from task_flow_api.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (add cleanup code here if needed)


app = FastAPI(lifespan=lifespan)


app.include_router(tasks_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
