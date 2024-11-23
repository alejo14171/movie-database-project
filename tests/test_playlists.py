from movie_database.models import Movie
from movie_database.playlists import Playlist

def test_playlist_navigation():
    movies = [
        Movie("Movie 1", 2022, ["Drama"], [], 1000, "", [], "PT120M", "2022-01-01", "PG", ""),
        Movie("Movie 2", 2021, ["Action"], [], 2000, "", [], "PT90M", "2021-01-01", "PG-13", ""),
        Movie("Movie 3", 2020, ["Comedy"], [], 3000, "", [], "PT110M", "2020-01-01", "R", "")
    ]
    playlist = Playlist(movies)

    assert playlist.current().title == "Movie 1"
    assert playlist.next().title == "Movie 2"
    assert playlist.next().title == "Movie 3"
    assert playlist.previous().title == "Movie 2"
    playlist.reset()
    assert playlist.current().title == "Movie 1"
    assert len(playlist) == 3
