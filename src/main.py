"""
This main.py file creates a basic FastAPI application for the User Data Storage API.
The primary goal of this API is to manage the interaction between a user, data providers,
and Spike integration,storing the relevant user data within a Google Spreadsheet for future use.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.api_router import router as api_router_v1

app = FastAPI(
    title="Spike API Integration",
    description="""
        This is an API to facilitate the interaction between users, data providers, and Spike integration.
        It stores user-specific data in a Google Spreadsheet for easy tracking and future use.
        """,
    version="0.0.1",
)

# Setting up CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router_v1, prefix="")

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, port=port, host="0.0.0.0")
