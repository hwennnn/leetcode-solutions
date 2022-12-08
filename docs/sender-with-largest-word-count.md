---
id: sender-with-largest-word-count
title: Sender With Largest Word Count
description: Problem Description and Solution for Sender With Largest Word Count
sidebar_label: 2284. Sender With Largest Word Count
sidebar_position: 2284
---

# [2284. Sender With Largest Word Count](https://leetcode.com/problems/sender-with-largest-word-count/)

```py title=sender-with-largest-word-count.py
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = defaultdict(int)
        
        for message, sender in zip(messages, senders):
            mp[sender] += len(message.split())

        currCount = float('-inf')
        res = ""

        for sender, count in mp.items():
            if count > currCount:
                currCount = count
                res = sender
            elif count == currCount:
                res = max(res, sender)
        
        return res
        
```


