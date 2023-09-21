"""Make a test that the contact form displays and a test that the contact form submit works"""


def test_task7_thanks_displayed_after_contact(client):
    """
    Make a test that the contact form displays and a test that the contact form submit works
    """
    response = client.get("/contact/")
    # This test will fail if the contact page doesn't load
    assert response.status_code == 200
    # Lets test if we can see the contact form
    assert b"<form" in response.data
    # Lets test if we can submit a contact form with a post request
    response = client.post("/contact/", data=dict(
        name="Johny Bravo",
        email="johnybravo@gmail.com",
        message="This is a test message"
    ), follow_redirects=True)
    assert response.status_code == 200
