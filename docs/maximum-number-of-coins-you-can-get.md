---
id: maximum-number-of-coins-you-can-get
title: Maximum Number of Coins You Can Get
description: Problem Description and Solution for Maximum Number of Coins You Can Get
sidebar_label: 1561. Maximum Number of Coins You Can Get
sidebar_position: 1561
---

# [1561. Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)

```py title=maximum-number-of-coins-you-can-get.py
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        i = 0
        j = n-1
        res = 0
        rounds = n//3
        
        while i < rounds:
            res += piles[j-1]
            i+=1
            j-=2
        
        return res
```


