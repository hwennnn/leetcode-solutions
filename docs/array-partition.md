---
id: array-partition
title: Array Partition
description: Problem Description and Solution for Array Partition
sidebar_label: 561. Array Partition
sidebar_position: 561
---

# [561. Array Partition](https://leetcode.com/problems/array-partition/)

```py title=array-partition.py
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        ans = 0
        
        for i in range(0,len(nums),2):
            ans+=nums[i]
            
        return ans
```


