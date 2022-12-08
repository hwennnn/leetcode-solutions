---
id: longest-continuous-increasing-subsequence
title: Longest Continuous Increasing Subsequence
description: Problem Description and Solution for Longest Continuous Increasing Subsequence
sidebar_label: 674. Longest Continuous Increasing Subsequence
sidebar_position: 674
---

# [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)

```py title=longest-continuous-increasing-subsequence.py
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                
        return max(dp)
        
```


