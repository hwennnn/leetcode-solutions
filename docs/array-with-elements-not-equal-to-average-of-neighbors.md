---
id: array-with-elements-not-equal-to-average-of-neighbors
title: Array With Elements Not Equal to Average of Neighbors
description: Problem Description and Solution for Array With Elements Not Equal to Average of Neighbors
sidebar_label: 1968. Array With Elements Not Equal to Average of Neighbors
sidebar_position: 1968
---

# [1968. Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/)

```py title=array-with-elements-not-equal-to-average-of-neighbors.py
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        
        return nums
```


