from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.jobs import JobCreate, ShowJob
from db.models.jobs import Job
from db.session import get_db
from db.repository.jobs import create_new_job

router = APIRouter()

@router.post("/create_job", response_model=ShowJob)
def create_job(job:JobCreate, db:Session=Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job