""" Make a test that the about page loads (just a word will be sufficient) """


def test_task3_about_page_loads(client):
    """
    Make a test that the about page loads (just a word will be sufficient)
    """
    response = client.get("/about/")
    # This test will fail if the about page doesn't load
    assert response.status_code == 200
    # This test will fail if the about page doesn't have the correct text
    assert b"About" in response.data
    assert b"Sidebar" in response.data
