from typing import List

from fastapi import APIRouter

from app.core.schemas.task import Task, TaskOut
from app.services.worker import add_task, get_tasks_info, get_results


router = APIRouter()


@router.post('', response_model=dict)
async def create_task(task: Task):
    await add_task(task)
    return {'success': True}


@router.get('', response_model=List[TaskOut])
def get_current_tasks():
    return get_tasks_info()


@router.get('/results', response_model=List[int])
def get_tasks_results():
    return get_results()
