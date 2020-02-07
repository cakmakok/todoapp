from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False, server_default="false")

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = True if status == "true" else False

    def __repr__(self):
        return '<Todo %r %r %r>' % (self.title, self.description, self.status)


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = Todo


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/todo/<todo_id>", methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    return todo_schema.jsonify(todo)


@app.route("/todos", methods=['POST'])
def add_todo():
    try:
        title = request.json['title']
        description = request.json['description']
        status = request.json['status']
        new_todo = Todo(title, description, status)
        db.session.add(new_todo)
        db.session.commit()
    except Exception as e:
        print("SIÇTI:!!!!:  {}".format(e))
    return todo_schema.jsonify(new_todo)
