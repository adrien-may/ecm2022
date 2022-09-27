import pytest

from app import create_app, db


@pytest.fixture(scope="session")
def app(request):
    app = create_app()
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session")
def _db(app):
    db.create_all()
    return db