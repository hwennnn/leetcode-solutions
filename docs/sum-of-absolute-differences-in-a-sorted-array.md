---
id: sum-of-absolute-differences-in-a-sorted-array
title: Sum of Absolute Differences in a Sorted Array
description: Problem Description and Solution for Sum of Absolute Differences in a Sorted Array
sidebar_label: 1685. Sum of Absolute Differences in a Sorted Array
sidebar_position: 1685
---

# [1685. Sum of Absolute Differences in a Sorted Array](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/)

```py title=sum-of-absolute-differences-in-a-sorted-array.py
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i,x in enumerate(nums):
            left = prefix[i]
            right = prefix[-1] - prefix[i+1]

            ans = (x*i - left) + (-x*(n-i-1) + right)
            res.append(ans)
        
        return res
```


