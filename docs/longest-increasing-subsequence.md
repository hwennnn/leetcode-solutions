---
id: longest-increasing-subsequence
title: Longest Increasing Subsequence
description: Problem Description and Solution for Longest Increasing Subsequence
sidebar_label: 300. Longest Increasing Subsequence
sidebar_position: 300
---

# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

```py title=longest-increasing-subsequence.py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        A = []
        
        for x in nums:
            index = bisect_left(A, x)
            
            if index < len(A):
                A[index] = x
            else:
                A.append(x)
        
        return len(A)
```


