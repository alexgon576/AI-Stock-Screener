import praw
from config.settings import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USERNAME,
    REDDIT_PASSWORD,
    WATCHLIST_SUBREDDITS,
)


class RedditScanner:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD,
            user_agent="AI Stock Screener by u/" + REDDIT_USERNAME,
        )

    def test_connection(self):
        try:
            print("Connecting to Reddit...")
            print("Logged in as:", self.reddit.user.me())
            print("Connection successful!")
        except Exception as e:
            print("Connection failed!")
            print(e)