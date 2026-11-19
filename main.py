from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

import models
from database import engine
from routers import employees


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Auto-create tables on startup if not present
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Database tables verified / created successfully.")
    except Exception as exc:
        print(f"Warning: Could not connect to database on startup: {exc}")
        print("Ensure MySQL is running and your .env credentials are correct.")

    yield


app = FastAPI(
    title="Employee Management System API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)


@app.get("/", tags=["Root"], summary="API Health and Welcome Endpoint")
def root():
    return {
        "status": "healthy",
        "message": "Welcome to the Employee Management System REST API",
        "documentation": "/docs"
    }


@app.exception_handler(SQLAlchemyError)
def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An internal database error occurred.",
            "error_type": exc.__class__.__name__
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
