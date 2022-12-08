---
id: find-the-most-competitive-subsequence
title: Find the Most Competitive Subsequence
description: Problem Description and Solution for Find the Most Competitive Subsequence
sidebar_label: 1673. Find the Most Competitive Subsequence
sidebar_position: 1673
---

# [1673. Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/)

```py title=find-the-most-competitive-subsequence.py
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        
        for i,x in enumerate(nums):
            while res and len(res) + (n-i) > k and x < res[-1]:
                res.pop()
            
            if len(res) < k:
                res.append(x)
        
        return res
        
```


