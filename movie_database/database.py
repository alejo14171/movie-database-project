import json
import os
from movie_database.models import Movie


class MovieDatabase:
    """
    Handles loading and retrieving movies from a JSON file.

    Attributes:
        filepath (str): Path to the JSON file containing movie data.
        movies (list): List of Movie objects.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.movies = []

    def load_data(self):
        """Load movie data from a JSON file and create Movie objects."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The file '{self.filepath}' does not exist.")

        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON file: {e}")

        for movie_data in data:
            try:
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
                    poster_image=movie_data["posterImage"],
                )
                self.movies.append(movie)
            except KeyError as e:
                print(f"Missing expected field in movie data: {e}")

    def get_all_movies(self):
        """Return all movies."""
        return self.movies
