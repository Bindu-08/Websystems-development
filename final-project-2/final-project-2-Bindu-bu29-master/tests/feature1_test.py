"""Test duplicate song entries"""


import os


def test_duplicate_song_entries(application, add_user, client_authenticated):
    """Test for duplicate song entries"""
    # pylint: disable=invalid-name, unused-argument, line-too-long
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(BASE_DIR, "test_data", "my_music_dup.csv")
    data = {}
    with open(file_path, "rb") as file:  # Use file to refer to the file object
        data = {
            'file': (file, file_path)
        }

        client_authenticated.post(
            '/songs/upload', data=data, follow_redirects=True)

    with open(file_path, "rb") as file:  # Use file to refer to the file object
        data = {
            'file': (file, file_path)
        }

        response2 = client_authenticated.post(
            '/songs/upload', data=data, follow_redirects=True)
    assert b"Skipped some of the duplicate entries" in response2.data
