import yfinance as yf


class InsiderScanner:

    def __init__(self):
        pass

    def has_insider_buying(self, ticker):
        try:
            stock = yf.Ticker(ticker)

            insiders = stock.insider_transactions

            if insiders is None:
                return False

            if len(insiders) == 0:
                return False

            buy_count = 0

            for _, row in insiders.iterrows():

                text = str(row).lower()

                if (
                    "buy" in text
                    or "purchase" in text
                    or "+" in text
                ):
                    buy_count += 1

            return buy_count > 0

        except Exception:
            return False