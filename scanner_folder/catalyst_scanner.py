class CatalystScanner:

    def __init__(self):
        self.keywords = [
            "FDA",
            "approval",
            "phase 1",
            "phase 2",
            "phase 3",
            "clinical trial",
            "earnings",
            "merger",
            "acquisition",
            "buyout",
            "partnership",
            "contract",
            "share repurchase",
            "buyback",
            "insider buying",
            "patent",
            "breakthrough",
            "fast track",
            "orphan drug",
            "NASDAQ compliance",
            "extension"
        ]

    def find_catalysts(self, news_titles):

        found = []

        for title in news_titles:

            lower_title = title.lower()

            for keyword in self.keywords:

                if keyword.lower() in lower_title:
                    found.append(keyword)

        return list(set(found))