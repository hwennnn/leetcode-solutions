---
id: maximum-number-of-pairs-in-array
title: Maximum Number of Pairs in Array
description: Problem Description and Solution for Maximum Number of Pairs in Array
sidebar_label: 2341. Maximum Number of Pairs in Array
sidebar_position: 2341
---

# [2341. Maximum Number of Pairs in Array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/)

```py title=maximum-number-of-pairs-in-array.py
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        removed = 0
        
        for x in Counter(nums).values():
            removed += x // 2
        
        return [removed, n - removed * 2]
```


