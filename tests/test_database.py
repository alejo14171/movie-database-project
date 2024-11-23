from movie_database.database import MovieDatabase


def test_load_data():
    db = MovieDatabase("data/movies.json")
    db.load_data()

    assert len(db.movies) > 0, "No movies were loaded"
    assert db.movies[0].title == "Multi-lateral optimal synergy"
    assert db.movies[0].calculate_popularity() > 0
