import datetime

from pydantic import BaseModel


class Task(BaseModel):
    num: int
    timeout: int  # seconds


class TaskOut(Task):
    id: int
    timestamp: datetime.datetime
