"""
Web Scraper for Latest News

Write a Python program that scrapes the latest news headlines from a news
website and saves them to a file.

Your Task:
- Fetch the HTML content of a news website (e.g., BBC, CNN, or any news site).
- Extract the latest headlines using BeautifulSoup.
- Save the headlines to a text file (news_headlines.txt).
- Print the headlines to the console in a clean format.

Example Output (news_headlines.txt):
Latest News Headlines:
1. Scientists Discover New Exoplanet with Water
2. Global Markets Show Signs of Recovery
3. AI Revolution: How It’s Changing Everyday Life
4. New Study Links Sleep Patterns to Productivity

Constraints:
✅ Use BeautifulSoup for parsing HTML.
✅ Handle network errors gracefully.
✅ Extract only clean text (remove unnecessary HTML tags).
"""

from bs4 import BeautifulSoup
import requests

def fetch_news_headlines_from_sky_news() -> list:
    '''
    Fetches the latest news headlines from Sky news.
    '''
    try:
        response = requests.get('https://news.sky.com/', timeout=10)
        if response.status_code != 200:
            print("Error fetching data:", response.text)
            return []
        with open("news_headlines.txt", "w") as f:
            f.write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        headline_tags = soup.find_all('a', class_='ui-story-headline')
        return [headline_tag.get('data-title') for headline_tag in headline_tags if headline_tag.get('data-title').strip() != ""] 
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

def tee_headlines(headlines: list) -> None:
    '''
    Saves the headlines to a file and prints them to the console.
    '''
    with open("news_headlines.txt", "w") as f:
        f.write("Latest News Headlines:\n")
        print("Latest News Headlines:\n")
        for i, headline in enumerate(headlines):
            f.write(f"{i+1}. {headline}\n")
            print(f"{i+1}. {headline}")

def main():
    headlines = fetch_news_headlines_from_sky_news()
    if headlines:
        tee_headlines(headlines)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()