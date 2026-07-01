import feedparser
from finvizfinance.screener.overview import Overview


def get_news(ticker):
    try:
        url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
        feed = feedparser.parse(url)

        if len(feed.entries) == 0:
            return "No recent news found."

        return feed.entries[0].title

    except Exception:
        return "Unable to retrieve news."


print("Scanning Finviz for possible momentum runners...\n")

filters = {
    "Price": "Under $5",
    "Average Volume": "Over 500K",
    "Change": "Up 15%"
}

overview = Overview()
overview.set_filter(filters_dict=filters)

stocks = overview.screener_view()
stocks = stocks[["Ticker", "Company", "Sector", "Price", "Change", "Volume"]]

stocks = stocks[
    ~stocks["Company"].str.contains(
        "ETF|Fund|Trust|2X|3X|Daily",
        case=False,
        na=False
    )
]


def calculate_score(change, volume, price):
    score = 0

    if change >= 0.50:
        score += 40
    elif change >= 0.30:
        score += 30
    elif change >= 0.15:
        score += 20

    if volume >= 50_000_000:
        score += 40
    elif volume >= 10_000_000:
        score += 30
    elif volume >= 1_000_000:
        score += 20

    if price < 1:
        score += 20
    elif price < 3:
        score += 15
    elif price < 5:
        score += 10

    return score


def get_reasons(change, volume, price):
    reasons = []

    if change >= 0.50:
        reasons.append("Explosive momentum")
    elif change >= 0.30:
        reasons.append("Very strong momentum")
    elif change >= 0.15:
        reasons.append("Strong momentum")

    if volume >= 50_000_000:
        reasons.append("Massive volume")
    elif volume >= 10_000_000:
        reasons.append("Very high volume")
    elif volume >= 1_000_000:
        reasons.append("High volume")

    if price < 1:
        reasons.append("Low-priced penny stock")
    elif price < 3:
        reasons.append("Small-cap price range")

    return reasons


stocks["AI Score"] = stocks.apply(
    lambda row: calculate_score(row["Change"], row["Volume"], row["Price"]),
    axis=1
)

stocks = stocks.sort_values(by="AI Score", ascending=False)

for index, row in stocks.head(10).iterrows():
    score = row["AI Score"]
    ticker = row["Ticker"]
    reasons = get_reasons(row["Change"], row["Volume"], row["Price"])
    headline = get_news(ticker)

    if score >= 85:
        rating = "🔥 Strong Momentum"
    elif score >= 65:
        rating = "⚠️ Good but Risky"
    else:
        rating = "👀 Watch Only"

    news_link = f"https://finance.yahoo.com/quote/{ticker}/news"

    print("=" * 50)
    print("🚀", ticker)
    print("Company:", row["Company"])
    print("Sector:", row["Sector"])
    print("Price: $", row["Price"])
    print("Change:", round(row["Change"] * 100, 2), "%")
    print("Volume:", int(row["Volume"]))
    print("AI Score:", score, "/ 100")
    print("Rating:", rating)
    print("Reasons:", ", ".join(reasons))
    print("Latest Headline:", headline)
    print("News:", news_link)
    print("=" * 50)
    print()