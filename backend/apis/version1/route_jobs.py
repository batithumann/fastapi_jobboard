from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.jobs import JobCreate, ShowJob
from db.models.jobs import Job
from db.session import get_db
from db.repository.jobs import create_new_job, get_job_by_id, get_active_jobs, update_job_by_id

router = APIRouter()

@router.post("/create_job", response_model=ShowJob)
def create_job(job:JobCreate, db:Session=Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get("/details/{id}", response_model=ShowJob)
def get_job(id:int, db:Session=Depends(get_db)):
    job = get_job_by_id(id, db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return job

@router.get("/all", response_model=List[ShowJob])
def get_all_jobs(db:Session=Depends(get_db)):
    jobs = get_active_jobs(db)
    return jobs


@router.put("/update/{id}")
def update_job(id:int, job:JobCreate, db:Session=Depends(get_db)):
    owner_id = 1
    message = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return {"detail":"Job successfully updated"}