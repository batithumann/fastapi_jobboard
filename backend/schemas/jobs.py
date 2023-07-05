from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobBase(BaseModel):
    title : Optional[str] = None
    company : Optional[str] = None
    company_url : Optional[str] = None
    location : Optional[str] = None
    description : Optional[str] = None
    date : Optional[str] = datetime.now().date()


class JobCreate(JobBase):
    title : str
    company : str
    location : str
    description : str


class ShowJob(JobBase):
    title : str
    company : str
    company_url : Optional[str]
    location : str
    description : Optional[str]
    date : date

    class Config():
        orm_mode  = True