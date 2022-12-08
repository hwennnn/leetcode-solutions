---
id: longest-subarray-with-maximum-bitwise-and
title: Longest Subarray With Maximum Bitwise AND
description: Problem Description and Solution for Longest Subarray With Maximum Bitwise AND
sidebar_label: 2419. Longest Subarray With Maximum Bitwise AND
sidebar_position: 2419
---

# [2419. Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)

```py title=longest-subarray-with-maximum-bitwise-and.py
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        mmax = max(nums)
        curr = res = 0

        for x in nums:
            if x == mmax:
                curr += 1
            else:
                curr = 0
            
            res = max(res, curr)
        
        return res
            
```


