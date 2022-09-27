from app import ma

from .models import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
