---
id: minimum-swaps-to-group-all-1s-together-ii
title: Minimum Swaps to Group All 1's Together II
description: Problem Description and Solution for Minimum Swaps to Group All 1's Together II
sidebar_label: 2134. Minimum Swaps to Group All 1's Together II
sidebar_position: 2134
---

# [2134. Minimum Swaps to Group All 1's Together II](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/)

```py title=minimum-swaps-to-group-all-1s-together-ii.py
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        nums = nums + nums
        prefix = [0]
        
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        res = 0
        for i in range(n):
            res = max(res, prefix[i + ones] - prefix[i])
            
        return ones - res
```


