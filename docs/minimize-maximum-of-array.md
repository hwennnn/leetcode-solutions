---
id: minimize-maximum-of-array
title: Minimize Maximum of Array
description: Problem Description and Solution for Minimize Maximum of Array
sidebar_label: 2439. Minimize Maximum of Array
sidebar_position: 2439
---

# [2439. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array/)

```py title=minimize-maximum-of-array.py
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = min(nums), max(nums)
        
        def good(k):
            A = nums[:]

            for i in range(N - 1, 0, -1):
                if A[i] <= k: continue

                deduct = A[i] - k
                A[i] -= deduct
                A[i - 1] += deduct

            return max(A) <= k
        
        while left < right:
            mid = (left + right) >> 1
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


