---
id: find-all-good-indices
title: Find All Good Indices
description: Problem Description and Solution for Find All Good Indices
sidebar_label: 2420. Find All Good Indices
sidebar_position: 2420
---

# [2420. Find All Good Indices](https://leetcode.com/problems/find-all-good-indices/)

```py title=find-all-good-indices.py
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        left = [0] * N
        right = [0] * N
        res = []
        
        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                left[i] = 1
        
            if nums[i] >= nums[i - 1]:
                right[i] = 1

        left = list(accumulate(left))
        right = list(accumulate(right))

        for i in range(k, N - k):
            L = left[i - 1] - left[i - k]
            R = right[i + k] - right[i + 1]

            if L == R == k - 1:
                res.append(i)
        
        return res
```


