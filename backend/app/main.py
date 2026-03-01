# backend/app/main.py
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .database import Base, SessionLocal, engine
from .routers import guestbook


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Körs vid uppstart

    db = SessionLocal()

    db.close()

    yield  # startup done


# Skapa databastabeller om de inte redan finns.
Base.metadata.create_all(bind=engine)

# Skapa FastAPI appen
app = FastAPI(lifespan=lifespan, title="Race Timing Backend API")

# Sätt på CORS för dev om frontend körs separat
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inkludera routrar. Smidigt att dela upp i flera filer.
app.include_router(guestbook.router)


# 'Mounta' frontend dist mappen (efter build)
if os.path.exists("../frontend/dist"):
    print("Mounting static files from ../frontend/dist")
    app.mount(
        "/assets",
        StaticFiles(directory="../frontend/dist/assets"),
        name="assets",
    )

    @app.get("/{_:path}")
    async def spa_fallback(_: str):
        return FileResponse("../frontend/dist/index.html")
else:
    print("No frontend dist folder found, not serving static files.")
    print("Make sure to build the frontend with 'deno task build' in the frontend directory.")


# Tillåter att starta appen med "python -m app.main"
# istället för att alltid använda "uvicorn app.main:app --reload"
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
