from app.models import ToDo
from app import db

def create_todo(title, info):
    todo = ToDo(title, info)
    print("==> Created new To-do object")
    
    db.session.add(todo)
    db.session.commit()
    
    todos = ToDo.query.all()
    print(todos)