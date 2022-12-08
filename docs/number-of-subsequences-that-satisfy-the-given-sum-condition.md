---
id: number-of-subsequences-that-satisfy-the-given-sum-condition
title: Number of Subsequences That Satisfy the Given Sum Condition
description: Problem Description and Solution for Number of Subsequences That Satisfy the Given Sum Condition
sidebar_label: 1498. Number of Subsequences That Satisfy the Given Sum Condition
sidebar_position: 1498
---

# [1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

```py title=number-of-subsequences-that-satisfy-the-given-sum-condition.py
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7
        res = 0
        nums.sort()

        for i, x in enumerate(nums):
            index = bisect.bisect_right(nums, target - x) - 1
            
            if index >= i and x + nums[index] <= target:
                diff = index - i
                res += pow(2, diff, M)
        
        return res % M
```


