"""Make a test to show that you can log in and that after log in it shows the show contact page"""


def test_task6_show_contacts_page(client):
    """
    Make a test to show that you can log in and that after log in it shows the show contact page
    """
    # pylint: disable=fixme
    # FIXME: the show contacts page fails due to `contact_logs.log` being empty,
    # we will have to seed it first
    # FIXME: This needs to fixed!!
    client.post("/contact/", data=dict(
        name="Johny Sins",
        email="johnysins@gmail.com",
        message="This is a test message"
    ), follow_redirects=True)

    response = client.get("/login/")
    # This test will fail if the login page doesn't load
    assert response.status_code == 200
    # Lets test if we can log in to the site with a post request
    response = client.post("/login/", data=dict(
        username="admin",
        password="password"
    ), follow_redirects=True)
    assert response.status_code == 200
    # check if show contacts page is displayed
    assert b"List of Contacts" in response.data
    assert b"<table" in response.data
