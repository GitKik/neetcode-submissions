from collections import defaultdict

class Twitter:

    def __init__(self):
        self.follow_map: dict[str, list[init]] = defaultdict(set)
        self.tweet_id_map: dict[str, list[init]] = defaultdict(set)
        self.tweet_timeline: list[int] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_id_map[userId].add(tweetId)
        self.tweet_timeline.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        following_ = self.follow_map[userId]
        following_.update({userId})
        all_tweets_id = []
        for f in following_ :
            all_tweets_id += self.tweet_id_map.get(f, [])
        news_feed = [x for x in self.tweet_timeline if x in all_tweets_id]
        news_feed.reverse()
        return news_feed[0:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]: 
            self.follow_map[followerId].remove(followeeId)
