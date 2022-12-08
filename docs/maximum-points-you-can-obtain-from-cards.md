---
id: maximum-points-you-can-obtain-from-cards
title: Maximum Points You Can Obtain from Cards
description: Problem Description and Solution for Maximum Points You Can Obtain from Cards
sidebar_label: 1423. Maximum Points You Can Obtain from Cards
sidebar_position: 1423
---

# [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

```py title=maximum-points-you-can-obtain-from-cards.py
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int: 
        n = len(cardPoints)
        t = n - k
        total = sum(cardPoints)
        prefix = [0] + list(accumulate(cardPoints))
        res = float('inf')

        for i in range(t, n + 1):
            res = min(res, prefix[i] - prefix[i - t])

        return total - res
        
```


