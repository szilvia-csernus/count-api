from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# Pydantic model
class Visit(BaseModel):
    page: str
    count: int
    last_visit: str


def get_db_session() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# CORS configuration
origins = [
    "http://localhost:3000",
    os.getenv('MY_APP_HOST_1'),
]

# Add the CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/visit/")
async def increment_page_visit(
        request: Request, db: Session = Depends(get_db_session)):
    try:
        referer_url = request.headers.get("Referer")
        print(referer_url)
        current_date = date.today()

        page = db.query(models.Visits).filter_by(page=referer_url).first()

        if page:
            last_visit_month = None
            last_visit = page.last_visit
            if last_visit is not None:
                last_visit_month = last_visit.month
            current_month = current_date.month

            if last_visit_month != current_month:
                page.count = 1
            else:
                page.count += 1

            page.last_visit = current_date
            db.commit()

            return JSONResponse(content={"count": page.count}, status_code=200)

        else:
            return JSONResponse(
                content={"message": f"{referer_url}  not found in database"},
                status_code=404)

    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(content={"message": "Internal Server Error"},
                            status_code=500)
