from app import db
import json
from ..models import Task
from .factories import TaskFactory


def test_tasks_list(app, client, db_session):
    task = TaskFactory()
    db_session.commit()

    response = client.get("/tasks/")
    assert len(response.json) > 0


def test_tasks_create(app, client, db_session):
    title = "my_test"
    # Ensure no task persist with this title
    Task.query.filter_by(title=title).delete()
    data = json.dumps({"title": "my_test"})
    response = client.post("/tasks/", data=data, content_type="application/json")
    assert response.status_code == 201

    response = client.post("/tasks/", data=data, content_type="application/json")
    assert response.status_code == 400


def test_tasks_get_one(app, client, db_session):
    task = TaskFactory()
    db_session.commit()
    task = Task.query.filter_by(title=task.title).first()
    response = client.get(f"/tasks/{task.id}")
    assert response.status_code == 200


def test_tasks_update_one(app, client, db_session):
    new_title = "new_title"
    # Ensure no task persist with this title
    Task.query.filter_by(title=new_title).delete()

    task = TaskFactory()
    db_session.commit()
    task2 = Task.query.filter_by(title=task.title).first()
    print(task2.id)
    response = client.put(
        f"/tasks/{task2.id}",
        data=json.dumps({"title": new_title}),
        content_type="application/json",
    )
    print(response.get_data())
    assert response.status_code == 200

    print(Task.query.filter_by(title=new_title).all())

    Task.query.filter_by(title="already_existing").delete()
    db_session.commit()
    TaskFactory(title="already_existing")
    db_session.commit()
    task3 = Task.query.filter_by(title=new_title).first()
    print(task3)
    print(Task.query.filter_by(title=new_title).all())

    response = client.put(
        f"/tasks/{task3.id}",
        data=json.dumps({"title": "already_existing"}),
        content_type="application/json"
    )
    print(Task.query.filter_by(title=new_title).all())

    assert response.status_code == 400


def test_tasks_delete_one(app, client, db_session):
    task = TaskFactory()
    db_session.commit()

    task = Task.query.filter_by(title=task.title).first()
    response = client.delete(f"/tasks/{task.id}")
    assert response.status_code == 204
