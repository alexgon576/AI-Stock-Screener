import yfinance as yf


class NewsScanner:
    def __init__(self):
        pass

    def get_news(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            news = stock.news

            print(f"\n========== {ticker} ==========")

            if not news:
                print("No recent news found.")
                return

            for article in news[:5]:
                title = article.get("title", "No Title")
                publisher = article.get("publisher", "Unknown")
                print(f"- {title}")
                print(f"  Source: {publisher}")
                print()

        except Exception as e:
            print(f"Error getting news for {ticker}: {e}")