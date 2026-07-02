class ScoreCalculator:

    def __init__(self):
        pass

    def calculate_score(
        self,
        percent_change,
        volume,
        reddit_mentions=0,
        positive_news=0,
        insider_buying=False,
        catalyst=False
    ):

        score = 0
        reasons = []

        # Price Movement
        if percent_change >= 15:
            score += 20
            reasons.append("Strong price momentum")

        if percent_change >= 25:
            score += 10
            reasons.append("Large breakout")

        # Volume
        if volume >= 500000:
            score += 20
            reasons.append("High trading volume")

        if volume >= 2000000:
            score += 10
            reasons.append("Exceptional volume")

        # Reddit
        score += min(reddit_mentions * 2, 20)

        if reddit_mentions:
            reasons.append(f"{reddit_mentions} Reddit mentions")

        # News
        score += min(positive_news * 5, 20)

        if positive_news:
            reasons.append(f"{positive_news} positive news articles")

        # Insider Buying
        if insider_buying:
            score += 10
            reasons.append("Insider buying")

        # Catalyst
        if catalyst:
            score += 10
            reasons.append("Upcoming catalyst")

        score = min(score, 100)

        return {
            "score": score,
            "reasons": reasons
        }