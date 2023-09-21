"""Make a test that the thanks page displays after filling out the contact form"""


def test_task7_thanks_displayed_after_contact(client):
    """
    Make a test that the thanks page displays after filling out the contact form
    """
    response = client.get("/contact/")
    # This test will fail if the contact page doesn't load
    assert response.status_code == 200
    # Lets test if we can submit a contact form with a post request
    response = client.post("/contact/", data=dict(
        name="Johny Sins",
        email="johnysins@gmail.com",
        message="This is a test message"
    ), follow_redirects=True)
    assert response.status_code == 200
    # "Thanks" should be in the response data as we have submitted the contact form
    assert b"thank you" in response.data
    assert b"I will return your message as soon as possible." in response.data
