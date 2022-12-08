---
id: minimum-moves-to-equal-array-elements-ii
title: Minimum Moves to Equal Array Elements II
description: Problem Description and Solution for Minimum Moves to Equal Array Elements II
sidebar_label: 462. Minimum Moves to Equal Array Elements II
sidebar_position: 462
---

# [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

```py title=minimum-moves-to-equal-array-elements-ii.py
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n // 2]
        res = 0
        
        for x in nums:
            res += abs(mid - x)
        
        return res
```


