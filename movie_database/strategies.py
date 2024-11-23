import statistics


class ClassificationStrategy:
    """Base class for all classification strategies."""

    def classify(self, db):
        raise NotImplementedError("Subclasses must implement classify()")


class PopularityStrategy(ClassificationStrategy):
    """
    Classify movies by their calculated popularity score.

    Methods:
        classify: Sorts movies in descending order of popularity.
    """

    def classify(self, db):
        return sorted(
            db.get_all_movies(),
            key=lambda m: m.calculate_popularity(),
            reverse=True,
        )


class DurationStrategy(ClassificationStrategy):
    def classify(self, db):
        return sorted(db.get_all_movies(), key=lambda m: m.duration, reverse=True)


class YearStrategy(ClassificationStrategy):
    """
    Classify movies by their release year.
    """

    def classify(self, db):
        return sorted(db.get_all_movies(), key=lambda m: m.year, reverse=True)


class ActorStrategy(ClassificationStrategy):
    def __init__(self, actor_name):
        self.actor_name = actor_name

    def classify(self, db):
        return [
            movie for movie in db.get_all_movies() if self.actor_name in movie.actors
        ]


class SimilarMoviesStrategy(ClassificationStrategy):
    """
    Classify movies by similarity to a given movie.
    """

    def __init__(self, movie_title):
        self.movie_title = movie_title

    def classify(self, db):
        target_movie = next(
            (m for m in db.get_all_movies() if m.title == self.movie_title),
            None,
        )
        if not target_movie:
            return []

        def similarity_score(movie):
            genre_match = len(set(movie.genres) & set(target_movie.genres))
            actor_match = len(set(movie.actors) & set(target_movie.actors))
            rating_diff = abs(
                statistics.mean(movie.ratings) - statistics.mean(target_movie.ratings)
            )
            return genre_match * 2 + actor_match - rating_diff

        similar_movies = sorted(
            [m for m in db.get_all_movies() if m.title != self.movie_title],
            key=similarity_score,
            reverse=True,
        )
        return similar_movies[:10]  # Top 10 similar movies
