from task_flow_api import repository
from task_flow_api.model import Task, TaskStatus


def create_task(task: Task):
    assert task.id is None, f"Task already exists with id: {task.id}"
    return repository.save(task)


def get_task(task_id: int):
    return repository.get(task_id)


def update_task(task_id: int, title: str, description: str, status: TaskStatus):
    task = repository.get(task_id)
    task.title = title
    task.description = description
    task.status = TaskStatus(status)
    if task.status == TaskStatus.DONE:
        task.completed = True
    return repository.save(task)


def delete_task(task_id: int):
    return repository.delete(task_id)


def list_tasks() -> list[Task]:
    return repository.find_all()
