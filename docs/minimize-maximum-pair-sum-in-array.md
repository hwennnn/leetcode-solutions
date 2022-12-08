---
id: minimize-maximum-pair-sum-in-array
title: Minimize Maximum Pair Sum in Array
description: Problem Description and Solution for Minimize Maximum Pair Sum in Array
sidebar_label: 1877. Minimize Maximum Pair Sum in Array
sidebar_position: 1877
---

# [1877. Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)

```py title=minimize-maximum-pair-sum-in-array.py
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n // 2):
            res.append(nums[i] + nums[n - i - 1])
        
        return max(res)
```


