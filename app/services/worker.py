import asyncio
from datetime import datetime
from typing import Union, List

import nest_asyncio

from app.core.schemas.task import Task, TaskOut


# to fix "asyncio.run() cannot be called from a running event loop"
nest_asyncio.apply()

tasks = []
tasks_info = []
result_numbers = []
new_task_id = 1


async def add_task(new_task: Task):
    global new_task_id
    new_task_id += 1
    task = TaskOut(
        id=new_task_id,
        num=new_task.num,
        timeout=new_task.timeout,
        timestamp=datetime.now()
    )
    tasks_info.append(task)
    tasks.append(asyncio.create_task(do_task(task)))


async def main():
    await asyncio.gather(*tasks)


async def do_task(task: Union[TaskOut, Task]):
    await asyncio.sleep(task.timeout)
    result_numbers.append(task.num)
    tasks_info.remove(task)


def get_results() -> List[int]:
    return result_numbers


def get_tasks_info() -> List[TaskOut]:
    return tasks_info


asyncio.run(main())
