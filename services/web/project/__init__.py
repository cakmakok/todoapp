from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(128), unique=FileExistsError, nullable=False)
    status = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


@app.route("/")
def hello_world():
    return jsonify(hello="world")
