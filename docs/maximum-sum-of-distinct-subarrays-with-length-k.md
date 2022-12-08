---
id: maximum-sum-of-distinct-subarrays-with-length-k
title: Maximum Sum of Distinct Subarrays With Length K
description: Problem Description and Solution for Maximum Sum of Distinct Subarrays With Length K
sidebar_label: 2461. Maximum Sum of Distinct Subarrays With Length K
sidebar_position: 2461
---

# [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)

```py title=maximum-sum-of-distinct-subarrays-with-length-k.py
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        i = 0
        curr = set()
        currSum = 0
        res = 0
        
        for j, x in enumerate(nums):
            while j - i + 1 > k or x in curr:
                curr.remove(nums[i])
                currSum -= nums[i]
                i += 1
            
            curr.add(x)
            currSum += x
            if j - i + 1 == k:
                res = max(res, currSum)
        
        return res
```


