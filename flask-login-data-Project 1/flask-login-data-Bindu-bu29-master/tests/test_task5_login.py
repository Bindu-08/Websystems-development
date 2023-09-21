"""
Make a test that the login form displays and that
you can log in to the site with a post request.
"""


def test_task5_login_page_post_request(client):
    """
    Make a test that the login form displays and
    that you can log in to the site with a post request.
    """
    # pylint: disable=fixme
    # FIXME: the show contacts page fails due to `contact_logs.log` being empty,
    # we will have to seed it first
    # FIXME: This needs to fixed!!
    client.post("/contact/", data=dict(
        name="Johny Bravo",
        email="johnybravo@gmail.com",
        message="This is a test message"
    ), follow_redirects=True)

    response = client.get("/login/")
    # This test will fail if the login page doesn't load
    assert response.status_code == 200
    # This test will fail if the login page doesn't have the correct text
    assert b"Login" in response.data
    # Lets test if login form is displayed
    assert b"<form" in response.data
    assert b"<input" in response.data
    # Lets test if we can log in to the site with a post request
    response = client.post("/login/", data=dict(
        username="admin",
        password="password"
    ), follow_redirects=True)

    assert response.status_code == 200
    # "Logout" should be in the response data as we have logged in in the previous test
    assert b"Logout" in response.data
