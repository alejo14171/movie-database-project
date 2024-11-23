from movie_database.playlists import Playlist
from movie_database.strategies import (
    PopularityStrategy,
    DurationStrategy,
    YearStrategy,
    ActorStrategy,
    SimilarMoviesStrategy
)

class PlaylistFactory:
    def __init__(self, db):
        self.db = db

    def create_playlist(self, classification_type, **kwargs):
        """Create a Playlist based on the given classification type."""
        strategy = None

        if classification_type == "popularity":
            strategy = PopularityStrategy()
        elif classification_type == "duration":
            strategy = DurationStrategy()
        elif classification_type == "year":
            strategy = YearStrategy()
        elif classification_type == "actor":
            actor_name = kwargs.get("actor_name")
            strategy = ActorStrategy(actor_name)
        elif classification_type == "similar":
            movie_title = kwargs.get("movie_title")
            strategy = SimilarMoviesStrategy(movie_title)
        else:
            raise ValueError(f"Unknown classification type: {classification_type}")

        # Apply the selected strategy to the database
        movies = strategy.classify(self.db)
        return Playlist(movies)
