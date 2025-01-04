---
title: 355. Design Twitter
draft: false
tags: 
  - leetcode-medium
  - hash-table
  - linked-list
  - design
  - heap-priority-queue
date: 2021-04-09
---

[Problem Link](https://leetcode.com/problems/design-twitter/)

## Description

---
<p>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user&#39;s news feed.</p>

<p>Implement the <code>Twitter</code> class:</p>

<ul>
	<li><code>Twitter()</code> Initializes your twitter object.</li>
	<li><code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.</li>
	<li><code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user&#39;s news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be <strong>ordered from most recent to least recent</strong>.</li>
	<li><code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.</li>
	<li><code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Twitter&quot;, &quot;postTweet&quot;, &quot;getNewsFeed&quot;, &quot;follow&quot;, &quot;postTweet&quot;, &quot;getNewsFeed&quot;, &quot;unfollow&quot;, &quot;getNewsFeed&quot;]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
<strong>Output</strong>
[null, null, [5], null, null, [6, 5], null, [5]]

<strong>Explanation</strong>
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 1 tweet id -&gt; [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 2 tweet ids -&gt; [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 1 tweet id -&gt; [5], since user 1 is no longer following user 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId, followerId, followeeId &lt;= 500</code></li>
	<li><code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code></li>
	<li>All the tweets have <strong>unique</strong> IDs.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>postTweet</code>, <code>getNewsFeed</code>, <code>follow</code>, and <code>unfollow</code>.</li>
	<li>A user cannot follow himself.</li>
</ul>


## Solution

---
### Python3
``` py title='design-twitter'
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
```

