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
