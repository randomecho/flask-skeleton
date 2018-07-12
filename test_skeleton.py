import pytest
import app


@pytest.fixture
def client():
    client = app.app.test_client()
    yield client


def test_homepage(client):
    rv = client.get("/")
    assert b"I'm Soon Van" in rv.data


def test_about(client):
    rv = client.get("/about/")
    assert b"web developer and writer" in rv.data


def test_author(client):
    rv = client.get("/written-by-soon-van/")
    assert b"Written works and articles" in rv.data


def test_contact(client):
    rv = client.get("/contact-soon/")
    assert b"Contact me" in rv.data


def test_repos(client):
    rv = client.get("/source/")
    assert b"Projects and code history" in rv.data


def test_websites(client):
    rv = client.get("/websites/")
    assert b"websites and web apps" in rv.data


def test_missing(client):
    rv = client.get("/page-that-does-not-exist")
    assert b"websites and web apps" in rv.data
    assert rv.status_code == 404
