---
id: two-sum-ii-input-array-is-sorted
title: Two Sum II - Input Array Is Sorted
description: Problem Description and Solution for Two Sum II - Input Array Is Sorted
sidebar_label: 167. Two Sum II - Input Array Is Sorted
sidebar_position: 167
---

# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

```py title=two-sum-ii-input-array-is-sorted.py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]
```


