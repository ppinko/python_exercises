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