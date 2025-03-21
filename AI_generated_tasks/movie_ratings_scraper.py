"""
Challenge: Movie Ratings Scraper

Write a Python program that scrapes movie ratings from IMDb (or another movie
database) and saves the results to a file.

Your Task:
1) Fetch movie ratings for a given search term (e.g., "Inception").
2) Extract key details:
* Movie title
* IMDb rating
* Year of release
* Genre
3) Save the results to a text file (movies.txt).
4) Print the top-rated movie to the console.

Example Output (movies.txt)
Search Results for "Inception":
1. Inception (2010) - 8.8/10 - Sci-Fi, Thriller
2. Inception: The Cobol Job (2010) - 7.8/10 - Animation, Short

Console Output:
Top-rated movie: Inception (2010) - 8.8/10

Constraints:
✅ Use BeautifulSoup or an API like OMDB.
✅ Handle network errors gracefully.
✅ Allow the search term to be passed as a command-line argument.

Bonus Challenge:
⭐ Save the results as a CSV file instead of text.
⭐ Allow the user to search multiple movies at once.
⭐ Fetch Rotten Tomatoes ratings along with IMDb ratings.
"""

import requests

_OMDB_API_KEY = "f86594"


def fetch_movie_ratings(movie_title: str) -> dict:
    """
    Fetches movie ratings from IMDb for a given search term.
    """
    request: requests.Response = requests.get(
        f"http://www.omdbapi.com/?apikey={_OMDB_API_KEY}&t={movie_title}"
    )
    if request.status_code != 200:
        print("Error fetching data:", request.text)
        return []
    movie_data: dict = request.json()
    ratings: dict = {
        "Metacritic": movie_data.get("Metascore"),
        "IMDb": movie_data.get("imdbRating"),
    }
    for rating in movie_data.get("Ratings"):
        if rating["Source"] == "Rotten Tomatoes":
            ratings["Rotten Tomatoes"] = rating["Value"]
    return ratings


def tee_movie_ratings(output_file: str, movie_title: str, movie_ratings: dict) -> None:
    """
    Saves the movie ratings to a file and prints the top-rated movie to the console.
    """
    with open(output_file, "w") as f:
        f.write(f"Movie title: {movie_title}\n")
        print(f"Movie title: {movie_title}")
        for source, rating in movie_ratings.items():
            f.write(f"{source}: {rating}\n")
            print(f"{source}: {rating}")


def main(output_file: str, movie_title: str) -> None:
    movie_data: dict = fetch_movie_ratings(movie_title)
    tee_movie_ratings(output_file, movie_title, movie_data)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python movie_ratings_scraper.py <output_file> <movie_title>")
        sys.exit(1)
    output_file = sys.argv[1]
    movie_title = sys.argv[2]
    main(output_file, movie_title)
