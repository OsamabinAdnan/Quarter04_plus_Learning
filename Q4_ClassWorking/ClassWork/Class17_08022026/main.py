from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from model import Task
from database import create_db_and_tables, get_session

app = FastAPI(title="Task API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/tasks", status_code=201)
def create_task(task: Task, session: Session = Depends(get_session)): # Dependency injection
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.get("/tasks")
def list_tasks(session: Session = Depends(get_session)):
    return session.exec(select(Task)).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: Task,
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = task_update.title
    task.description = task_update.description
    task.status = task_update.status

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()