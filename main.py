import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker not in self.portfolio:
            self.portfolio[ticker] = {'shares': shares, 'purchase_price': self.get_current_price(ticker)}
            print(f"Added {shares} shares of {ticker} to your portfolio.")
        else:
            print(f"{ticker} is already in your portfolio.")

    def remove_stock(self, ticker):
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from your portfolio.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def track_performance(self):
        current_prices = {}
        for ticker in self.portfolio:
            current_prices[ticker] = self.get_current_price(ticker)

        portfolio_value = 0
        for ticker, data in self.portfolio.items():
            shares = data['shares']
            purchase_price = data['purchase_price']
            current_price = current_prices[ticker]
            profit_loss = (current_price - purchase_price) * shares
            portfolio_value += current_price * shares
            print(f"{ticker}:")
            print(f"  Shares: {shares}")
            print(f"  Purchase Price: {purchase_price}")
            print(f"  Current Price: {current_price}")
            print(f"  Profit/Loss: {profit_loss}")

        print("\nTotal Portfolio Value:", portfolio_value)

    def get_current_price(self, ticker):
        try:
            ticker_data = yf.Ticker(ticker)
            current_price = ticker_data.history(period="1d")['Close'][0]
            return current_price
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def visualize_performance(self):
        # Assuming you have a DataFrame of historical prices for each stock
        # (you can fetch this using yfinance or from a CSV)
        historical_data = pd.DataFrame(index=pd.date_range(start='2023-01-01', end='2024-08-27'))
        for ticker in self.portfolio:
            historical_data[ticker] = yf.download(ticker, start='2023-01-01', end='2024-08-27')['Close']

        # Plot the historical prices
        plt.figure(figsize=(12, 6))
        plt.plot(historical_data)
        plt.title("Stock Portfolio Performance")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend(historical_data.columns)
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    tracker = StockPortfolioTracker()

    # Example usage:
    tracker.add_stock("AAPL", 100)
    tracker.add_stock("GOOGL", 50)
    tracker.track_performance()
    tracker.visualize_performance()

