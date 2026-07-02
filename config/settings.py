import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME", "")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD", "")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "")

WATCHLIST_SUBREDDITS = [
    "pennystocks",
    "stocks",
    "Shortsqueeze",
    "RobinHood",
    "StockMarket",
    "wallstreetbets",
]

MIN_PRICE = 0.01
MAX_PRICE = 5.00
MIN_VOLUME = 500_000
MIN_PERCENT_CHANGE = 15
MAX_PERCENT_CHANGE = 30