from movie_database.strategies import (
    PopularityStrategy, DurationStrategy, YearStrategy, ActorStrategy, SimilarMoviesStrategy
)
from movie_database.models import Movie
from movie_database.database import MovieDatabase
import unittest


class TestStrategies(unittest.TestCase):

    def setUp(self):
        """Set up a test database with movies."""
        self.db = MovieDatabase("data/movies.json")
        self.db.load_data()

    def test_popularity_strategy(self):
        """Test PopularityStrategy."""
        strategy = PopularityStrategy()
        movies = strategy.classify(self.db)
        self.assertGreater(len(movies), 0)
        self.assertGreaterEqual(movies[0].calculate_popularity(), movies[-1].calculate_popularity())

    def test_duration_strategy(self):
        """Test DurationStrategy."""
        strategy = DurationStrategy()
        movies = strategy.classify(self.db)
        self.assertGreaterEqual(movies[0].duration, movies[-1].duration)

    def test_year_strategy(self):
        """Test YearStrategy."""
        strategy = YearStrategy()
        movies = strategy.classify(self.db)
        self.assertGreaterEqual(movies[0].year, movies[-1].year)

    def test_actor_strategy(self):
        """Test ActorStrategy."""
        strategy = ActorStrategy("Actor A")
        movies = strategy.classify(self.db)
        self.assertTrue(all("Actor A" in m.actors for m in movies))

    def test_similar_movies_strategy(self):
        """Test SimilarMoviesStrategy."""
        strategy = SimilarMoviesStrategy("Test Movie")
        similar_movies = strategy.classify(self.db)
        self.assertLessEqual(len(similar_movies), 10)
