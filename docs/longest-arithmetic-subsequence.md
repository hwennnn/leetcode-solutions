---
id: longest-arithmetic-subsequence
title: Longest Arithmetic Subsequence
description: Problem Description and Solution for Longest Arithmetic Subsequence
sidebar_label: 1027. Longest Arithmetic Subsequence
sidebar_position: 1027
---

# [1027. Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/)

```py title=longest-arithmetic-subsequence.py
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                dp[(j, nums[j] - nums[i])] = dp.get((i, nums[j] - nums[i]), 1) + 1
        
        return max(dp.values())
```


