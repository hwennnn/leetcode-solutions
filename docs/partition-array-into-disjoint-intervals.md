---
id: partition-array-into-disjoint-intervals
title: Partition Array into Disjoint Intervals
description: Problem Description and Solution for Partition Array into Disjoint Intervals
sidebar_label: 915. Partition Array into Disjoint Intervals
sidebar_position: 915
---

# [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)

```py title=partition-array-into-disjoint-intervals.py
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        localMax = mmax = nums[0]
        partitionIndex = 0
        
        for i, x in enumerate(nums):
            if x < localMax:
                localMax = mmax
                partitionIndex = i
            else:
                mmax = max(mmax, x)
        
        return partitionIndex + 1
```


