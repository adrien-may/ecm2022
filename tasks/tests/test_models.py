from .factories import TaskFactory


def test_task_repr(db_session):
    task = TaskFactory()
    db_session.commit()
    assert repr(task) == task.title