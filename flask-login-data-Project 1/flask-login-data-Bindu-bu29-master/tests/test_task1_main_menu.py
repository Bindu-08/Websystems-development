""" Do not change these tests, or I will fail you for cheating"""


# pylint: disable=redefined-outer-name, unused-argument, line-too-long

# This is not the correct test but is an example
def test_task1_pages_exist(client):
    """This tests that the pages load"""
    response = client.get("/")
    assert response.status_code == 200
    response = client.get("/about/")
    assert response.status_code == 200
    response = client.get("/portfolio/")
    assert response.status_code == 200
    response = client.get("/contact/")
    assert response.status_code == 200
    response = client.get("/thanks/")
    assert response.status_code == 200
