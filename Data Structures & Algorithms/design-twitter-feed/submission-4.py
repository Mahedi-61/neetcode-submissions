class Twitter:
    def __init__(self):
        self.dc_tweets = defaultdict(set)
        self.dc_following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.dc_tweets[userId].add((tweetId, self.count))

        # all followers gets the same tweet in their feed
        # for fanID in self.dc_follower:
        #     self.dc_follower[fanID].add((tweetId, self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        set_all_tweets = self.dc_tweets[userId].copy()

        for followeeId in self.dc_following[userId]:
            set_all_tweets.update(self.dc_tweets[followeeId])

        ls_tweets = list(set_all_tweets)
        ls_tweets.sort(key = lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in ls_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 
        self.dc_following[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 
        self.dc_following[followerId].discard(followeeId)
