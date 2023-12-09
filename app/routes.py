from app import app
from flask import request
import json
from app import services

@app.route("/")
@app.route("/home")
def say_hello():
    return "Hello, World!"

@app.route("/todo", methods=["POST"])
def create_todo():
    body = json.loads(request.data)
    services.create_todo(title=body["title"], info=body["info"])
    print("OK!")
    