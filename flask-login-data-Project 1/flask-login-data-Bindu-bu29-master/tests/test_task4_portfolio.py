"""Make a test that the portfolio page loads (just a word will be sufficient)"""


def test_task4_about_page_loads(client):
    """
    Make a test that the portfolio page loads (just a word will be sufficient)
    """
    response = client.get("/portfolio/")
    # This test will fail if the portfolio page doesn't load
    assert response.status_code == 200
    # This test will fail if the about page doesn't have the correct text
    assert b"Portfolio" in response.data
