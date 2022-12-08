---
id: maximum-alternating-subsequence-sum
title: Maximum Alternating Subsequence Sum
description: Problem Description and Solution for Maximum Alternating Subsequence Sum
sidebar_label: 1911. Maximum Alternating Subsequence Sum
sidebar_position: 1911
---

# [1911. Maximum Alternating Subsequence Sum](https://leetcode.com/problems/maximum-alternating-subsequence-sum/)

```py title=maximum-alternating-subsequence-sum.py
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def go(isPos, i):
            if i >= len(nums): return 0
            
            curr = nums[i] if isPos else -nums[i]
            
            return max(curr + go(not isPos, i + 1), go(isPos, i + 1))
        
        return go(True, 0)
```


