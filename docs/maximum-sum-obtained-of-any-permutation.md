---
id: maximum-sum-obtained-of-any-permutation
title: Maximum Sum Obtained of Any Permutation
description: Problem Description and Solution for Maximum Sum Obtained of Any Permutation
sidebar_label: 1589. Maximum Sum Obtained of Any Permutation
sidebar_position: 1589
---

# [1589. Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/)

```py title=maximum-sum-obtained-of-any-permutation.py
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        p = [0] * (n+1)

        for s,e in requests:
            p[s] += 1
            p[e+1] -= 1
        
        for i in range(1, n+1):
            p[i] += p[i-1]
        
        nums.sort(reverse = True)
        p.sort(reverse = True)
        res = 0
        for i,x in enumerate(nums):
            res += x * p[i]
            res %= M
        
        return res
```


