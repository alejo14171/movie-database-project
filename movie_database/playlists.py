class Playlist:
    def __init__(self, movies, page_size=10, context="default"):
        self.movies = movies
        self.page_size = page_size
        self.current_page = 0
        self.context = context

    def current_page_movies(self):
        """Get the movies on the current page."""
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.movies[start:end]

    def next_page(self):
        """Move to the next page."""
        if (self.current_page + 1) * self.page_size < len(self.movies):
            self.current_page += 1
        else:
            print("You are on the last page.")

    def previous_page(self):
        """Move to the previous page."""
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("You are on the first page.")

    def reset(self):
        """Reset the playlist to the first page."""
        self.current_page = 0

    def display_progress(self):
        """Display the current progress in the playlist."""
        total_pages = (len(self.movies) + self.page_size - 1) // self.page_size
        return f"Page {self.current_page + 1}/{total_pages}"

    def format_movie(self, movie):
        """Format the movie display based on the playlist context."""
        if self.context == "popularity":
            return f"{movie.title} ({movie.year}) - Popularity: {movie.calculate_popularity():.2f}"
        elif self.context == "duration":
            return f"{movie.title} ({movie.year}) - Duration: {movie.duration} minutes"
        elif self.context == "year":
            return f"{movie.title} - Year: {movie.year}"
        elif self.context == "actor":
            actors = ", ".join(movie.actors[:3])  # Show first 3 actors
            return f"{movie.title} ({movie.year}) - Actors: {actors}"
        elif self.context == "similar":
            genres = ", ".join(movie.genres[:3])  # Show first 3 genres
            return f"{movie.title} ({movie.year}) - Genres: {genres}"
        else:
            return f"{movie.title} ({movie.year})"

    def __len__(self):
        return len(self.movies)
