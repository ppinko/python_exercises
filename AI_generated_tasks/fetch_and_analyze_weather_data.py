"""
Fetch and Analyze Weather Data

Your task is to fetch real-time weather data from an API, process it, and
generate a simple summary report.

Steps:
- Fetch weather data from the OpenWeatherMap API (or any public API of your choice).
- Extract relevant information (e.g., temperature, humidity, wind speed).
- Process the data (e.g., convert temperatures from Kelvin to Celsius/Fahrenheit).
- Save the processed data to a report file (weather_report.txt).

Example API Request:

You can use OpenWeatherMap’s API (you’ll need a free API key).

Example request to get weather for London:
https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY

Expected Output (weather_report.txt):
Weather Report for London:
Temperature: 18.5°C
Humidity: 65%
Wind Speed: 3.6 m/s
Condition: Clear Sky

Constraints:
- Use requests or urllib to fetch data.
- Handle network errors gracefully (e.g., invalid API key, no internet).
- Allow the city name to be passed as a command-line argument.

Bonus Challenge:
- Format the report nicely as a table using prettytable.
- Support multiple cities in one request.
- Automatically detect the user's location and fetch weather for it.
"""

import requests


def fetch_weather_data(city: str) -> dict:
    api_key = "eb8c49f1efdd4079765d6555a58bcd2a"
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )
    if response.status_code != 200:
        print("Error fetching data:", response.text)
        return {}
    return response.json()


def process_weather_data(data: dict) -> dict:
    if not data:
        return {}
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    condition = data["weather"][0]["description"]
    return {
        "Temperature": f"{temperature - 273.15:.1f}°C",
        "Humidity": f"{humidity:.1f}%",
        "Wind Speed": f"{wind_speed:.1f} m/s",
        "Condition": condition,
    }


def save_to_report(data: dict, filename: str) -> None:
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")


def main(city: str) -> None:
    data = fetch_weather_data(city)
    processed_data = process_weather_data(data)
    save_to_report(processed_data, "weather_report.txt")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python fetch_and_analyze_weather_data.py CITY")
        sys.exit(1)
    main(sys.argv[1])
