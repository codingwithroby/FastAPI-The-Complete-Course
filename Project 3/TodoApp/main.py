from fastapi import Depends, FastAPI, Path, HTTPException
from fastapi import status


from typing import Annotated

from pydantic import BaseModel, Field
from database import SessionLocal, engine
from sqlalchemy.orm import Session


import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@app.get("/")
def read_all(db: db_dependency):
    return db.query(models.Todos).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
def read_todos_by_id(
    db: db_dependency, todo_id: int = Path(title="The ID of the item to get", gt=0)
):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is not None:
        return todo_model

    else:
        raise HTTPException(status_code=400, detail="Todo Not Found")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(db: db_dependency, todo: TodoRequest):
    todo_model = models.Todos(**todo.model_dump())

    db.add(todo_model)
    db.commit()


@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(
    db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)
):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not Found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not Found")

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    db.commit()
