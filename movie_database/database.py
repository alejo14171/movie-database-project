import json
from movie_database.models import Movie

class MovieDatabase:
    def __init__(self, filepath):
        self.filepath = filepath
        self.movies = []

    def load_data(self):
        """Load movie data from a JSON file and create Movie objects."""
        with open(self.filepath, "r") as file:
            data = json.load(file)
            for movie_data in data:
                movie = Movie(
                    title=movie_data["title"],
                    year=movie_data["year"],
                    genres=movie_data["genres"],
                    ratings=movie_data["ratings"],
                    viewer_count=movie_data["viewerCount"],
                    storyline=movie_data["storyline"],
                    actors=movie_data["actors"],
                    duration=movie_data["duration"],
                    release_date=movie_data["releaseDate"],
                    content_rating=movie_data["contentRating"],
                    poster_image=movie_data["posterImage"]
                )
                self.movies.append(movie)

    def get_all_movies(self):
        """Return all movies."""
        return self.movies
