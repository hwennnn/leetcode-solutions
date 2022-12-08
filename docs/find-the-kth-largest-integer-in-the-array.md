---
id: find-the-kth-largest-integer-in-the-array
title: Find the Kth Largest Integer in the Array
description: Problem Description and Solution for Find the Kth Largest Integer in the Array
sidebar_label: 1985. Find the Kth Largest Integer in the Array
sidebar_position: 1985
---

# [1985. Find the Kth Largest Integer in the Array](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/)

```py title=find-the-kth-largest-integer-in-the-array.py
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda x : int(x))

        return nums[len(nums) - k]
```


