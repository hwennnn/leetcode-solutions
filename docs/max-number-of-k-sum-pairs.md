---
id: max-number-of-k-sum-pairs
title: Max Number of K-Sum Pairs
description: Problem Description and Solution for Max Number of K-Sum Pairs
sidebar_label: 1679. Max Number of K-Sum Pairs
sidebar_position: 1679
---

# [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

```py title=max-number-of-k-sum-pairs.py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        keys = sorted(counter.keys())
        
        for x in keys:
            if x > k: break
                
            target = k - x
            
            d = min(counter[target], counter[x])
            res += d
        
        return res // 2
```


