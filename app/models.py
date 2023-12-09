from app import db
from uuid import uuid4
from datetime import datetime


class ToDo(db.Model):
    __tablename__ = "todos"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    info = db.Column(db.String)
    done = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime, default=None, nullable=True)
    
    def __init__(self, title, info):
        self.id = str(uuid4())
        self.title = title
        self.info = info
        self.done = 0
        self.created_at = datetime.now()
        self.completed_at = datetime.now()
    