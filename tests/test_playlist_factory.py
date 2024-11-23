from movie_database.database import MovieDatabase
from movie_database.playlist_factory import PlaylistFactory
import unittest


class TestPlaylistFactory(unittest.TestCase):

    def setUp(self):
        """Set up a test factory and database."""
        self.db = MovieDatabase("data/movies.json")
        self.db.load_data()
        self.factory = PlaylistFactory(self.db)

    def test_create_popularity_playlist(self):
        """Test creating a playlist by popularity."""
        playlist = self.factory.create_playlist("popularity")
        self.assertGreater(len(playlist), 0)

    def test_create_duration_playlist(self):
        """Test creating a playlist by duration."""
        playlist = self.factory.create_playlist("duration")
        self.assertGreater(len(playlist), 0)

    def test_create_year_playlist(self):
        """Test creating a playlist by year."""
        playlist = self.factory.create_playlist("year")
        self.assertGreater(len(playlist), 0)

    def test_create_actor_playlist(self):
        """Test creating a playlist by actor."""
        playlist = self.factory.create_playlist("actor", actor_name="Actor A")
        self.assertTrue(all("Actor A" in m.actors for m in playlist.movies))

    def test_create_similar_playlist(self):
        """Test creating a playlist by similar movies."""
        playlist = self.factory.create_playlist("similar", movie_title="Test Movie")
        self.assertLessEqual(len(playlist.movies), 10)
