import unittest
from movie_database.models import Movie
from movie_database.database import MovieDatabase

class TestMovieDatabase(unittest.TestCase):

    def setUp(self):
        """Create a sample movie object and a test database."""
        self.movie = Movie(
            title="Test Movie",
            year="2020",
            genres=["Action", "Adventure"],
            ratings=[5, 4, 3],
            viewer_count=1000000,
            storyline="An exciting test movie.",
            actors=["Actor A", "Actor B"],
            duration="PT120M",
            release_date="2020-01-01",
            content_rating="PG-13",
            poster_image="https://example.com/poster.jpg"
        )
        self.db = MovieDatabase("data/movies.json")

    def test_movie_attributes(self):
        """Test that the movie attributes are set correctly."""
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.year, 2020)
        self.assertEqual(self.movie.genres, ["Action", "Adventure"])
        self.assertEqual(self.movie.duration, 120)

    def test_calculate_popularity(self):
        """Test the popularity calculation."""
        average_rating = sum(self.movie.ratings) / len(self.movie.ratings)
        viewer_score = self.movie.viewer_count / 1_000_000
        expected_popularity = (average_rating * 0.7) + (viewer_score * 0.3)
        popularity = self.movie.calculate_popularity()
        self.assertAlmostEqual(popularity, expected_popularity)


    def test_load_data(self):
        """Test that data is loaded into the database."""
        self.db.load_data()
        self.assertGreater(len(self.db.get_all_movies()), 0)
