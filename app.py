import os
from movie_database.database import MovieDatabase
from movie_database.playlist_factory import PlaylistFactory

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def navigate_playlist(playlist):
    """Navigate through a playlist."""
    while True:
        clear_console()
        current_movies = playlist.current_page_movies()
        if not current_movies:
            print("Playlist is empty.")
            return

        print("=== Current Playlist ===")
        for i, movie in enumerate(current_movies, start=1):
            print(f"{i}. {playlist.format_movie(movie)}")
        print(f"\n{playlist.display_progress()}")
        print("Options: [N]ext page, [P]revious page, [R]eset, [E]xit navigation")
        action = input("Choose an option: ").strip().upper()

        if action == "N":
            playlist.next_page()
        elif action == "P":
            playlist.previous_page()
        elif action == "R":
            playlist.reset()
        elif action == "E":
            break
        else:
            print("Invalid option. Try again.")

def main():
    db = MovieDatabase("data/movies.json")
    db.load_data()
    factory = PlaylistFactory(db)

    while True:
        clear_console()
        print("=== Movie Database Menu ===")
        print("1. Classify by Popularity")
        print("2. Classify by Duration")
        print("3. Classify by Year")
        print("4. Classify by Actor")
        print("5. Find Similar Movies")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "6":
                print("Goodbye!")
                break

            classification_type = {
                "1": "popularity",
                "2": "duration",
                "3": "year",
                "4": "actor",
                "5": "similar"
            }.get(choice)

            if not classification_type:
                raise ValueError("Invalid choice")

            kwargs = {}
            if classification_type == "actor":
                kwargs["actor_name"] = input("Enter actor's name: ").strip()
            elif classification_type == "similar":
                kwargs["movie_title"] = input("Enter movie title: ").strip()

            playlist = factory.create_playlist(classification_type, **kwargs)
            playlist.context = classification_type  # Set the playlist context

            if len(playlist) == 0:
                print("No movies found.")
                input("Press Enter to continue...")
                continue

            navigate_playlist(playlist)
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
