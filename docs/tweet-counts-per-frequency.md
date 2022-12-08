---
id: tweet-counts-per-frequency
title: Tweet Counts Per Frequency
description: Problem Description and Solution for Tweet Counts Per Frequency
sidebar_label: 1348. Tweet Counts Per Frequency
sidebar_position: 1348
---

# [1348. Tweet Counts Per Frequency](https://leetcode.com/problems/tweet-counts-per-frequency/)

```py title=tweet-counts-per-frequency.py
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute": seconds = 60 
        elif freq == "hour": seconds = 3600
        else: seconds = 86400
            
        ans = [0] * ((endTime-startTime)//seconds + 1)
        
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                ans[(t-startTime)//seconds] += 1
        
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```


