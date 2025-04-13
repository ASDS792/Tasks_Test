from sqlalchemy import select
from shemas import STask, STaskAdd
from database import TasksORM, new_sesion


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_sesion() as session:
            task_dict = task.model_dump()
            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_sesion() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_shemas = [STask.model_validate() for task in task_models]
            return task_shemas
