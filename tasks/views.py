import json
from turtle import update
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app import db
from .models import Task
from .serializers import TaskSchema


task_blueprint = Blueprint(
    "tasks", "tasks", url_prefix="/tasks", description="Operations on tasks"
)


@task_blueprint.route("/")
class Tasks(MethodView):
    @task_blueprint.response(200, TaskSchema(many=True))
    def get(self):
        """List tasks"""
        return Task.query.all()

    @task_blueprint.arguments(TaskSchema(only=["title"]))
    @task_blueprint.response(201, TaskSchema)
    def post(self, new_data):
        """Creates a new task"""
        try:
            task = Task(**new_data)
            db.session.add(task)
            db.session.commit()
            return task
        except Exception as e:
            print(e)
            db.session.rollback()
            abort(400, message="An error occurred")


@task_blueprint.route("/<task_id>")
class TasksById(MethodView):
    @task_blueprint.response(200, TaskSchema)
    def get(self, task_id):
        """Get task by ID"""
        return Task.query.get_or_404(task_id)

    @task_blueprint.arguments(TaskSchema(only=["title", "done"]))
    @task_blueprint.response(200, TaskSchema)
    def put(self, update_data, task_id):
        """Update existing task"""
        print(update_data)
        try:
            task = Task.query.get_or_404(task_id)
            print(update_data)
            print(update_data["title"])
            task.title = update_data["title"]
            db.session.commit()
        except Exception as e:
            print(e)
            print('execption')
            db.session.rollback()
            abort(400, message="An error occurred")
        return task

    @task_blueprint.response(204)
    def delete(self, task_id):
        """Delete task"""
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
