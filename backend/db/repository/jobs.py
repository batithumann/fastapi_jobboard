from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job
from db.models.users import User


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id = owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_job_by_id(id:int, db:Session):
    job = db.query(Job).filter(Job.id==id).first()
    return job


def get_active_jobs(db:Session):
    jobs = db.query(Job).filter(Job.is_active==True).all()
    return jobs

