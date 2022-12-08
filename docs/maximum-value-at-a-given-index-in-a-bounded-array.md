---
id: maximum-value-at-a-given-index-in-a-bounded-array
title: Maximum Value at a Given Index in a Bounded Array
description: Problem Description and Solution for Maximum Value at a Given Index in a Bounded Array
sidebar_label: 1802. Maximum Value at a Given Index in a Bounded Array
sidebar_position: 1802
---

# [1802. Maximum Value at a Given Index in a Bounded Array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/)

```py title=maximum-value-at-a-given-index-in-a-bounded-array.py
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def good(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a
        
        maxSum -= n
        left, right = 0, maxSum
        
        while left < right:
            mid = (left + right + 1) // 2
            if good(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left + 1
```


