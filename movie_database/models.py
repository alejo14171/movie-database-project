import statistics


class Movie:
    """
    Represents a movie with various attributes such as title, year, genres,
    ratings, viewer count, and other metadata.

    Methods:
        calculate_popularity: Calculates a popularity score based on ratings
        and viewer count.
    """

    def __init__(
        self,
        title,
        year,
        genres,
        ratings,
        viewer_count,
        storyline,
        actors,
        duration,
        release_date,
        content_rating,
        poster_image,
    ):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(year, str) or not year.isdigit():
            raise ValueError("Year must be an integer or a string of digits.")
        if not isinstance(genres, list):
            raise ValueError("Genres must be a list.")
        if not isinstance(ratings, list) or not all(
            isinstance(r, (int, float)) for r in ratings
        ):
            raise ValueError("Ratings must be a list of numbers.")
        if not isinstance(viewer_count, int):
            raise ValueError("Viewer count must be an integer.")
        if not storyline or not isinstance(storyline, str):
            raise ValueError("Storyline must be a non-empty string.")
        if not actors or not isinstance(actors, list):
            raise ValueError("Actors must be a list.")
        if not duration or not isinstance(duration, str):
            raise ValueError("Duration must be a string.")
        if not release_date or not isinstance(release_date, str):
            raise ValueError("Release date must be a string.")
        if not content_rating or not isinstance(content_rating, str):
            raise ValueError("Content rating must be a string.")
        if not poster_image or not isinstance(poster_image, str):
            raise ValueError("Poster image must be a string.")

        self.title = title
        self.year = year
        self.genres = genres
        self.ratings = ratings
        self.viewer_count = viewer_count
        self.storyline = storyline
        self.actors = actors
        self.duration = self._parse_duration(duration)
        self.release_date = release_date
        self.content_rating = content_rating
        self.poster_image = poster_image

    @staticmethod
    def _parse_duration(duration_str):
        """Parse ISO 8601 duration format into minutes."""
        if duration_str.startswith("PT") and "M" in duration_str:
            return int(duration_str[2:-1])  # Strip 'PT' and 'M' to get minutes
        return 0

    def calculate_popularity(self):
        """
        Calculate a popularity score for the movie.

        Popularity is computed as a weighted average of the mean rating
        (70%) and viewer count (scaled down) (30%).

        Returns:
            float: The popularity score.
        """
        if not self.ratings:
            return 0
        average_rating = statistics.mean(self.ratings)
        return average_rating * 0.7 + (self.viewer_count / 1_000_000) * 0.3

    def __repr__(self):
        return f"<Movie {self.title} ({self.year})>"
