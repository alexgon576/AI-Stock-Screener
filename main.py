import yfinance as yf
from scanner_folder.reddit_scanner import RedditScanner

tickers = [
    "COSM", "MBRX", "LRMR", "CRIS", "VNTG", "ADTX", "LABT", "SNOA", "BIVI", "ATNF",
    "HSDT", "CTMX", "PRFX", "SXTP", "SPRC", "AKAN", "SINT", "SABS", "GNS", "CYN",
    "APVO", "SONN", "VERB", "INBS", "CNSP", "REVB", "RNAZ", "TIVC", "HOOK", "MGRX",
    "AREB", "ICCT", "CDT", "XCUR", "ONCO", "DTIL", "BNRG", "CERO", "MIRA", "MULN",
    "KAVL", "FFIE", "WINT", "ALLR", "PHIO", "BPTS", "IMNN", "KWE", "OCX", "BTAI"
]

print("Scanning for stocks up 15% to 30%, under $5, with volume over 500,000...\n")

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="10d", auto_adjust=False)

        if data.empty or len(data) < 2:
            continue

        previous_close = data["Close"].iloc[-2]
        current_close = data["Close"].iloc[-1]
        volume = data["Volume"].iloc[-1]

        percent_change = ((current_close - previous_close) / previous_close) * 100

        if 15 <= percent_change <= 30 and current_close < 5 and volume > 500000:
            print(
                "🚀",
                ticker,
                "Price:",
                round(current_close, 2),
                "Change:",
                round(percent_change, 2),
                "%",
                "Volume:",
                volume
            )

    except Exception:
        continue

print("\nReddit scanner is ready, but connection test is paused until API access is approved.")