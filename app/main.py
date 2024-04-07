from fastapi import Depends, FastAPI
from . import models
from .database import engine
from .routers import user, tax_calc, auth
import psycopg2, time
from psycopg2.extras import RealDictCursor
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

from pydantic import BaseModel
from .schemas import *
app = FastAPI()

# CORS middleware configuration. Adjust as necessary
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Adjust this to actual url when in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get rid of this later on, very not secure but works rn
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='taxapi', user='postgres', 
                                password='password123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successfully connected to Database")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)



app.include_router(user.router)
app.include_router(tax_calc.router)
app.include_router(auth.router)
