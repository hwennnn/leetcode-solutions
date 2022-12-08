---
id: sum-of-subarray-ranges
title: Sum of Subarray Ranges
description: Problem Description and Solution for Sum of Subarray Ranges
sidebar_label: 2104. Sum of Subarray Ranges
sidebar_position: 2104
---

# [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)

```py title=sum-of-subarray-ranges.py
from sortedcontainers import SortedList

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            smallest = largest = nums[i]
            for j in range(i + 1, n):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                
                res += largest - smallest
        
        return res
```


