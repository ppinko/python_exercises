import yfinance as yf
import sys

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")  # Get today's data

        if data.empty:
            print(f"Error: No data found for {ticker}")
            return None

        current_price = stock.info.get("regularMarketPrice", None)  # Live price
        open_price = data["Open"].iloc[0]
        high_price = data["High"].iloc[0]
        low_price = data["Low"].iloc[0]
        change_percent = ((current_price - open_price) / open_price) * 100

        return {
            "ticker": ticker.upper(),
            "current_price": current_price,
            "open_price": open_price,
            "high_price": high_price,
            "low_price": low_price,
            "change_percent": round(change_percent, 2),
            "trend": "📈 Rising" if change_percent >= 0 else "📉 Falling",
        }

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def save_to_file(report, filename="stock_report_v2.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    print(f"Stock report saved to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python stock_analyzer.py <stock_ticker>")
        return

    ticker = sys.argv[1]
    stock_data = get_stock_data(ticker)

    if stock_data:
        report = (
            f"Stock Report for {stock_data['ticker']}:\n"
            f"Current Price: ${stock_data['current_price']:.2f}\n"
            f"Opening Price: ${stock_data['open_price']:.2f}\n"
            f"High: ${stock_data['high_price']:.2f}\n"
            f"Low: ${stock_data['low_price']:.2f}\n"
            f"Change: {stock_data['change_percent']}% {stock_data['trend']}\n"
        )
        print(report)
        save_to_file(report)

# Run the script
if __name__ == "__main__":
    main()
