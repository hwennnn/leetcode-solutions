class Tweet:
    timestamp = 0
    
    def __init__(self, tweet):
        self.time = Tweet.timestamp
        self.tweet = tweet
        self.next = None
        Tweet.timestamp += 1

class User:
    def __init__(self, uid):
        self.uid = uid
        self.follows = set([uid])
        self.tweet_head = None

    def follow(self, uid):
        self.follows.add(uid)

    def unfollow(self, uid):
        if uid in self.follows:
            self.follows.remove(uid)

    def post(self, tweetId):
        tweet = Tweet(tweetId)
        tweet.next = self.tweet_head
        self.tweet_head = tweet
            
class Twitter:  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        users = self.users
        if userId not in users:
            users[userId] = User(userId)
        
        users[userId].post(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        if userId not in self.users: return res
        
        people = self.users[userId].follows
        heap = []
        for p in people:
            t = self.users[p].tweet_head
            
            if t:
                heap.append((-t.time, t))
        
        heapq.heapify(heap)
        
        read = 0
        while heap and read < 10:
            _, t = heapq.heappop(heap)
            res.append(t.tweet)
            
            if t.next:
                heapq.heappush(heap, (-t.next.time, t.next))
            
            read += 1
            
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
            
        self.users[followerId].follow(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users or followerId == followeeId: return
        
        self.users[followerId].unfollow(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)