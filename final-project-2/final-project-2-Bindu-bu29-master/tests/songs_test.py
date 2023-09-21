"""test for songs"""
import logging
from pprint import pprint

from sqlalchemy import func

from app import db
from app.db.models import User, Song


# testing links for songs only appear for logged-in users
def test_request_main_menu_links_authenticated(client_authenticated):
    """This makes the index page"""
    response = client_authenticated.get("/songs")
    assert response.status_code == 200
    assert b'href="/songs/upload"' in response.data, "songs/upload is not in response data"
    assert b'href="/songs"' in response.data, "songs is not in response data"


# testing that an authenticated user can access songs
def test_browse_songs_authenticated(client_authenticated):
    """Tests browse songs authenticated"""
    response = client_authenticated.get("/songs")
    assert response.status_code == 200, "status code is not successful"


# testing that uploads require an authenticated users
def test_upload_authenticated(client_authenticated):
    """Tests uploads require an authenticated"""
    response = client_authenticated.get("/songs/upload")
    assert response.status_code == 200, "status code is not successful"


# testing that songs is not accessible by unauthenticated users
def test_browse_songs_unauthenticated(client):
    """Tests browse songs an authenticated"""
    response = client.get("/songs")
    assert response.status_code == 302, "redirection is not successful"


# testing that upload is not accessible by unauthenticated users
def test_upload_unauthenticated(client):
    """Tests upload songs unauthenticated"""
    response = client.get("/songs/upload")
    assert response.status_code == 302, "redirection is not successful"


# testing that songs can be added in the database directly
def test_adding_song(application):
    """Tests adding songs"""
    logging.getLogger("myApp")
    with application.app_context():
        # pylint:disable=no-member
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        song = Song.query.filter_by(artist="Keith").first()
        # asserting that the user retrieved is correct
        assert song.title == 'Great song'
        # this is how you get a related record ready for insert


def test_deleting_song(application):
    """testing that songs can be deleted"""
    logging.getLogger("myApp")
    with application.app_context():
        # pylint:disable=no-member
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        song = Song.query.filter_by(artist="Keith").first()
        # asserting that the user retrieved is correct
        assert song.title == 'Great song'
        # this is how you delete the song
        db.session.delete(song)
        assert db.session.query(Song).count() == 0


def test_relate_song_to_user(application, add_user):
    """testing that songs can be related to a users"""
    # pylint: disable=invalid-name, unused-argument
    with application.app_context():
        # pylint:disable=no-member
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        user = User.query.filter_by(email='test@test.com').first()
        user.songs.append(song)
        db.session.add(user)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        assert len(user.songs) == 1
        # asserting that the user retrieved is correct
        # this is how you delete the song


def test_update_song(application, add_user):
    """testing update of a song title"""
    # pylint: disable=invalid-name, unused-argument
    with application.app_context():
        # pylint:disable=no-member
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()

        # just update the title and add it again.
        song.title = "Updated Great Song"
        db.session.add(song)
        db.session.commit()
        song_from_query = Song.query.filter_by(artist="Keith").first()
        assert song_from_query.title == "Updated Great Song"


def test_song_artist_count(application, upload_music_response):
    """A count of songs by artists"""
    # pylint: disable=invalid-name, unused-argument

    with application.app_context():
        # pylint:disable=no-member
        result = db.session.query(func.count(
            Song.artist), Song.artist).group_by(Song.artist).all()
    pprint(result)
