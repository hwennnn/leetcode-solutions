---
id: count-number-of-maximum-bitwise-or-subsets
title: Count Number of Maximum Bitwise-OR Subsets
description: Problem Description and Solution for Count Number of Maximum Bitwise-OR Subsets
sidebar_label: 2044. Count Number of Maximum Bitwise-OR Subsets
sidebar_position: 2044
---

# [2044. Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)

```py title=count-number-of-maximum-bitwise-or-subsets.py
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mmax = 0
        
        for x in nums: mmax |= x
        
        for mask in range(1, 1 << n):
            s = 0
            for j in range(n):
                if (mask >> j) & 1:
                    s |= nums[j]

            mp[s] += 1

        return mp[mmax]
```


