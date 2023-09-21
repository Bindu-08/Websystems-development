"""tests for file upload"""

from app import db
from app.db.models import User
from app.db.models import Song


def test_upload_textfile(application, upload_music_response):
    """Tests upload textfile"""
    assert upload_music_response.status_code == 302

    user = User('keith@webizly.com', 'testtest')
    # add it to get ready to be committed
    # pylint: disable=invalid-name, unused-argument, no-member
    db.session.add(user)

    # check that the songs were added to the database
    with application.app_context():
        songs = Song.query.all()
        assert len(songs) == 411, "Songs count is not equal to 411"
