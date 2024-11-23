from movie_database.playlists import Playlist
from movie_database.models import Movie
import unittest


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        """Create a sample playlist with movies."""
        self.movies = [
            Movie("Movie 1", 2020, ["Action"], [5], 1000, "Storyline 1", ["Actor A"], "PT90M", "2020-01-01", "PG", ""),
            Movie("Movie 2", 2019, ["Drama"], [4], 500, "Storyline 2", ["Actor B"], "PT110M", "2019-01-01", "PG", ""),
        ]
        self.playlist = Playlist(self.movies)

    def test_current_page_movies(self):
        """Test that the current page shows the correct movies."""
        self.assertEqual(len(self.playlist.current_page_movies()), 2)

    def test_navigation(self):
        """Test playlist navigation."""
        self.playlist.next_page()
        self.assertEqual(self.playlist.current_page, 0)  # No next page
        self.playlist.previous_page()
        self.assertEqual(self.playlist.current_page, 0)  # No previous page

    def test_display_progress(self):
        """Test display progress."""
        self.assertEqual(self.playlist.display_progress(), "Page 1/1")
