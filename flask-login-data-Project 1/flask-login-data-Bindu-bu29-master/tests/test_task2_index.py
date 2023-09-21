""" Tests that the correct information is displayed on the index page"""


def test_task2_index_correct_information(client):
    """
    Make tests that the correct information is displayed on the index page
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Let's get connected" in response.data
    assert b"Contact Me" in response.data
