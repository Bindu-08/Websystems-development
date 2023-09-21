"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data, "about is not in response data"
    assert b'href="/welcome"' in response.data, "welcome is not in response data"
    assert b'href="/login"' in response.data, "login is not in response data"
    assert b'href="/register"' in response.data, "register is not in response data"


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200, "status code is not successful"
    assert b"Index" in response.data, "Index string is not in response data"


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200, "status code is not successful"
    assert b"About" in response.data, "About string is not in response data"


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200, "status code is not successful"
    assert b"welcome" in response.data, "welcome string is not in response data"


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404, "page exists, someone might created"
