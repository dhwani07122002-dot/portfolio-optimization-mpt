import yfinance as yf

# Define the stock ticker symbols
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Download the daily closing prices for the last few years
print("Downloading stock data...")
data = yf.download(stocks, start="2020-01-01", end="2025-01-01")["Close"]

# Display the first 5 rows of the downloaded data
print("Data downloaded successfully!")
print(data.head())
