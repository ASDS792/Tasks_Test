from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends

from repository import TaskRepository
from shemas import STask, STaskAdd, STaskId

router = APIRouter(prefix="/tasks")


@router.post(
    "",
    tags=["ЗАДАЧИ"],
)
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("", tags=["ЗАДАЧИ"])
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
