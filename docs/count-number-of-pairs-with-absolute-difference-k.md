---
id: count-number-of-pairs-with-absolute-difference-k
title: Count Number of Pairs With Absolute Difference K
description: Problem Description and Solution for Count Number of Pairs With Absolute Difference K
sidebar_label: 2006. Count Number of Pairs With Absolute Difference K
sidebar_position: 2006
---

# [2006. Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)

```py title=count-number-of-pairs-with-absolute-difference-k.py
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
    
        return res
```


