---
id: longest-consecutive-sequence
title: Longest Consecutive Sequence
description: Problem Description and Solution for Longest Consecutive Sequence
sidebar_label: 128. Longest Consecutive Sequence
sidebar_position: 128
---

# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

```py title=longest-consecutive-sequence.py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        while s:
            first = last = s.pop()
            
            while first - 1 in s:
                s.remove(first - 1)
                first -= 1
            
            while last + 1 in s:
                s.remove(last + 1)
                last += 1
            
            res = max(res, last - first + 1)
        
        return res
```


