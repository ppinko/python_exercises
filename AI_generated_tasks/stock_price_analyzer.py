'''
Stock Price Analyzer

Write a Python program that fetches real-time stock prices from a financial API, 
analyzes them, and saves the results to a file.

Your Task:
1.	Fetch stock price data for a given company (e.g., Apple, Tesla, Google).
2.	Extract key details: 
o	Current stock price
o	Opening price
o	Highest & lowest prices of the day
o	Percentage change
3.	Analyze the trend (e.g., rising or falling).
4.	Save the analysis to a file (stock_report.txt)

Example Output (stock_report.txt)":
Stock Report for AAPL:
Current Price: $185.32
Opening Price: $182.50
High: $187.20
Low: $181.75
Change: +1.55% 📈 (Rising Trend)

Constraints:
✅ Use a financial API (e.g., Yahoo Finance, Alpha Vantage, IEX Cloud).
✅ Handle network errors gracefully.
✅ Allow the stock ticker to be passed as a command-line argument.

Bonus Challenge:
⭐ Support multiple stock tickers at once.
⭐ Save the report as a CSV file instead of text.
⭐ Plot stock price history using matplotlib.
'''

import requests
import csv
import sys

ALPHA_VANTAGE_KEY = 'AI10GJUNG3GPLO2A'
OUT_FILE = "stock_report.csv"

def fetch_stock_price(ticker: str) -> dict:
    '''
    Fetches stock price data for a given company.
    '''
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={ALPHA_VANTAGE_KEY}'
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("Error fetching data:", response.text)
            return {}
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return {}
    
def analyze_stock_price(data: dict) -> dict:
    '''
    Analyzes the stock price data and returns key details.
    '''
    if not data:
        return {}
    time_series = data.get('Time Series (5min)', {})
    if not time_series:
        return {}
    latest_timestamp = list(time_series.keys())[0]
    latest_data = time_series.get(latest_timestamp, {})
    opening_price = float(latest_data.get('1. open', 0))
    high_price = float(latest_data.get('2. high', 0))
    low_price = float(latest_data.get('3. low', 0))
    current_price = float(latest_data.get('4. close', 0))
    change_percent = round(((current_price - opening_price) / opening_price) * 100, 2)
    trend = "Rising" if change_percent > 0 else "Falling"
    return {
        "Current Price": current_price,
        "Opening Price": opening_price,
        "High": high_price,
        "Low": low_price,
        "Change": change_percent,
        "Trend": trend
    }
    
def save_stock_report(ticker: str, analysis: dict, writer) -> None:
    '''
    Saves the stock price analysis to a file.
    '''
    writer.writerow([ticker, analysis["Current Price"], analysis["Opening Price"], analysis["High"], analysis["Low"], analysis["Change"], analysis["Trend"]])
    
    print(f"Stock Report for {ticker}:")
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print()
        
def main():
    if len(sys.argv) < 2:
        print("Please provide at least one stock ticker.")
        return
    tickers = sys.argv[1:]  # Get stock tickers from command-line arguments
    
    headers = ["Ticker", "Current Price", "Opening Price", "High", "Low", "Change", "Trend"]
    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for ticker in tickers:
            data = fetch_stock_price(ticker)
            analysis = analyze_stock_price(data)
            if analysis:
                save_stock_report(ticker, analysis, writer)
            else:
                print(f"No data found for {ticker}.")   
            
if __name__ == "__main__":
    main()  # Run the program