import statistics

class Movie:
    def __init__(self, title, year, genres, ratings, viewer_count, storyline, actors, 
                 duration, release_date, content_rating, poster_image):
        self.title = title
        self.year = int(year) if isinstance(year, str) else year
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
        """Calculate a popularity score based on ratings and viewer count."""
        if not self.ratings:
            return 0
        average_rating = statistics.mean(self.ratings)
        return average_rating * 0.7 + (self.viewer_count / 1_000_000) * 0.3

    def __repr__(self):
        return f"<Movie {self.title} ({self.year})>"
