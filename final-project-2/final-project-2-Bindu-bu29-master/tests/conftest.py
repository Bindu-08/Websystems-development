"""This makes the test for configuration setup"""
# pylint: disable=redefined-outer-name, line-too-long
import os

import pytest
from app import create_app, User
from app.db import db


# this is a good tutorial I used to fix this code to do datbase testing.
# https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/

@pytest.fixture()
def application():
    """This makes the app"""
    # you need this one if you want to see whats in the database
    # os.environ['FLASK_ENV'] = 'development'
    # you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.drop_all()
        db.create_all()
        yield application
        db.session.remove()
        # drops the database tables after the test runs
        # db.drop_all()


@pytest.fixture()
def add_user(application):
    """This makes the app user"""
    with application.app_context():
        # new record
        user = User('test@test.com', 'testtest')
        # pylint: disable=no-member
        # The error is thrown by Pylint which is a static code checker,
        # it can introduce false positives at times,
        # it does not mean that your code does not work.
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    testing_client = application.test_client()
    ctx = application.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture()
def client_authenticated(add_user, client):
    """This makes the http client authenticated"""
    # pylint: disable=unused-argument
    client.post(
        "/login",
        data=dict(email='test@test.com', password='testtest'),
        follow_redirects=True
    )
    return client


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()


@pytest.fixture()
def upload_music_response(client_authenticated):
    """Upload music.csv and return the reponse"""
    # pylint: disable=invalid-name, unused-argument
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file = os.path.join(BASE_DIR, "test_data", "my_music.csv")
    with open(file, "rb") as f:
        data = {
            'file': (f, file)
        }

        # add it to get ready to be committed
        response = client_authenticated.post('/songs/upload', data=data)
        return response
