# **Movie Database Application**

This is a console-based movie database application that allows users to explore a collection of movies stored in a JSON file. The application supports movie classification, playlist creation, and navigation, using clean code principles and design patterns like Factory and Strategy.

---

## **Features**
1. **Movie Classification**:
   - By **Popularity** (calculated using ratings and viewer count).
   - By **Duration** (longest movies first).
   - By **Year** (newest movies first).
   - By **Actor** (movies featuring a specified actor).
   - By **Similarity** (based on genres, ratings, and cast).

2. **Playlist Navigation**:
   - Navigate playlists with options for:
     - Moving **next** and **previous**.
     - **Resetting** to the first page.
     - Exiting navigation.

3. **Modular Design**:
   - Employs the **Factory** and **Strategy** design patterns for flexibility and scalability.

4. **Unit Tests**:
   - Comprehensive tests for database, strategies, playlists, and factory components.

---

## **Project Structure**
```plaintext
movie_database_project/
├── app.py                    # Main application entry point
├── README.md                 # Documentation
├── requirements.txt          # Dependencies
├── data/
│   └── movies.json           # Sample movie dataset
├── movie_database/
│   ├── __init__.py           # Initialization for the package
│   ├── database.py           # Movie database loader and handler
│   ├── models.py             # Movie class definition
│   ├── playlist_factory.py   # Factory for creating playlists
│   ├── playlists.py          # Playlist implementation
│   ├── strategies.py         # Classification strategies
├── tests/
│   ├── __init__.py           # Initialization for the tests package
│   ├── test_database.py      # Tests for the database module
│   ├── test_movie_database.py # Tests for the movie database
│   ├── test_playlists.py     # Tests for the playlist functionality
│   ├── test_playlist_factory.py # Tests for the playlist factory
│   ├── test_strategies.py    # Tests for the classification strategies
│   └── run_tests.py          # Custom script to run all tests
```

---

## **How to Run the Application**

### **1. Prerequisites**
- Python 3.9 or higher.
- Install dependencies from `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Running the Application**
From the project root directory, execute:
```bash
python app.py
```

### **3. Interacting with the Menu**
The console application provides the following options:
- **1. Classify by Popularity**: Displays movies ordered by popularity.
- **2. Classify by Duration**: Displays movies ordered by duration.
- **3. Classify by Year**: Displays movies ordered by release year.
- **4. Classify by Actor**: Prompts for an actor's name and displays their movies.
- **5. Find Similar Movies**: Prompts for a movie title and displays similar movies.
- **6. Exit**: Exits the application.

---

## **How to Run Tests**
Unit tests are provided to ensure the reliability of the application. To run all tests:

1. Ensure you are in the project root directory.
2. Execute:
   ```bash
   python tests/run_tests.py
   ```

3. Example output:
   ```plaintext
   test_calculate_popularity (test_movie_database.TestMovieDatabase) ... ok
   test_load_data (test_movie_database.TestMovieDatabase) ... ok
   ...
   Ran 16 tests in 0.682s
   OK
   ```

---
## **Running the Application with Docker**
After clonning the repository, and going into the main folder:
1. Build the Docker image:
   ```bash
   docker build -t movie-database-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -it movie-database-app
   ```
3. Follow the on-screen instructions to interact with the application.

---

## **Design Patterns**
1. **Factory Pattern**:
   - Used in `playlist_factory.py` to create playlists based on the selected classification type.

2. **Strategy Pattern**:
   - Implemented in `strategies.py` for different classification logic (e.g., popularity, year, actor).


---

## **Sample Dataset**
The `movies.json` file contains movie objects with the following structure:
```json
{
        "title": "Team-oriented executive installation",
        "year": "2015",
        "genres": [
            "Sci-Fi",
            "Musical",
            "Drama"
        ],
        "ratings": [
            8,
            4,
            ...,
            10
        ],
        "viewerCount": 927349,
        "storyline": "Wide determine beat employee enjoy respond. Generation during sport can purpose what and. All while within create various themselves write.",
        "actors": [
            "Peyton Sage",
            "Taylor Morgan"
        ],
        "duration": "PT131M",
        "releaseDate": "2015-04-02",
        "contentRating": "PG",
        "posterImage": "https://dummyimage.com/250x400?text=Team-oriented%20executive%20installation"
    },
```

---
## Code Quality and Linters

This project uses `flake8` to ensure code quality and compliance with the PEP 8 style guide. Below are the instructions for running the linter and fixing style issues.

### Linter: `flake8`

To check for style issues:

1. Ensure `flake8` is installed:
   ```bash
   pip install flake8
   ```
2. Run the linter:
   ```bash
   flake8 movie_database tests
   ```
### Auto-formatting with `black`
To automatically fix style issues:

1. Ensure `black` is installed:
   ```bash
   pip install black
   ```
2. Run the formatter:
   ```bash
   black movie_database tests
   ```

---
