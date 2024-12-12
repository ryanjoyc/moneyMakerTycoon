import yfinance as yf

# Fetch data for a specific ticker
ticker = "AAPL"  # Example: Apple Inc.
data = yf.Ticker(ticker)

# Get historical market data
historical_data = data.history(period="1mo")
print(historical_data)

# Get today's market data
info = data.info
print(info["currentPrice"])
