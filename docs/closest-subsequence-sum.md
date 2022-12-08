---
id: closest-subsequence-sum
title: Closest Subsequence Sum
description: Problem Description and Solution for Closest Subsequence Sum
sidebar_label: 1755. Closest Subsequence Sum
sidebar_position: 1755
---

# [1755. Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/)

```py title=closest-subsequence-sum.py
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def construct(A):
            s = set()
            
            for k in range(len(A) + 1):
                for comb in combinations(A, k):
                    s.add(sum(comb))
            
            return s
        
        n = len(nums) // 2
        s1, s2 = construct(nums[:n]), construct(nums[n:])
        s2 = sorted(s2)
        res = float('inf')
        
        for x in s1:
            target = goal - x
            index = bisect.bisect_left(s2, target)
            
            for p in (index, index - 1):
                if 0 <= p < len(s2):
                    res = min(res, abs(x + s2[p] - goal))
        
        return res
```


