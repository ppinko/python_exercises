"""
Weather Data Visualization

Write a Python program that:
1. Reads temperature data from a CSV file (weather_data.csv).
2. Plots a line chart of daily temperature changes.
3. Adds labels, title, and grid for better readability.
4. Highlights the hottest and coldest days on the graph.

Example Input (weather_data.csv)

Date,Temperature
2024-03-01,12
2024-03-02,15
2024-03-03,10
2024-03-04,18
2024-03-05,20
2024-03-06,14
2024-03-07,22
2024-03-08,19
2024-03-09,25
2024-03-10,21

Expected Plot:
📉 A line graph where:
✅ X-axis = Dates
✅ Y-axis = Temperature
✅ Markers on the hottest & coldest days
✅ A grid and labeled axes

Bonus Challenge:
⭐ Add a moving average trendline to smooth out fluctuations.
⭐ Use different colors for temperature ranges (e.g., blue for cold, red for hot).
⭐ Save the plot as an image file (weather_plot.png).
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Read temperature data from CSV file
    df: pd.DataFrame = pd.read_csv("weather_data.csv")

    # Extract dates and temperatures
    dates: pd.Series = df["Date"]
    temperatures: pd.Series = df["Temperature"]

    # Plot daily temperature changes
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, color="green", label="Temperature")
    plt.xticks(rotation=90)
    plt.title("Daily Temperature Changes")
    plt.xlabel("Date")
    plt.ylabel("Temperature [°C]")
    plt.grid(False)

    # Add moving average trendline
    moving_avg: pd.Series = temperatures.rolling(window=3, center=True).mean()
    plt.plot(dates, moving_avg, color="orange", label="Moving Average")

    # Highlght cold days (< 11°C) in blue
    cold_days: pd.Series = df[df["Temperature"] < 11]

    # Highlight hot days (> 20°C) in red
    hot_days: pd.Series = df[df["Temperature"] > 20]

    # Scatter plot for hot and cold days
    plt.scatter(
        x=hot_days["Date"],
        y=hot_days["Temperature"],
        marker="o",
        s=50,
        color="red",
        label="Hot Days",
    )
    plt.scatter(
        x=cold_days["Date"],
        y=cold_days["Temperature"],
        marker="o",
        s=50,
        color="blue",
        label="Cold Days",
    )

    plt.legend()
    plt.savefig("weather_plot.png")
    plt.show()


main()
