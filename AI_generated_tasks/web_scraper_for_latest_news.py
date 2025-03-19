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
    try:
        response = requests.get('https://news.sky.com/')
        if response.status_code != 200:
            print("Error fetching data:", response.text)
            return []
        with open("news_headlines.txt", "w") as f:
            f.write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        headline_tags = soup.find_all('a', class_='ui-story-headline')
        return [headline_tag.get('data-title') for headline_tag in headline_tags]
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

print(fetch_news_headlines_from_sky_news())