---
id: k-concatenation-maximum-sum
title: K-Concatenation Maximum Sum
description: Problem Description and Solution for K-Concatenation Maximum Sum
sidebar_label: 1191. K-Concatenation Maximum Sum
sidebar_position: 1191
---

# [1191. K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)

```py title=k-concatenation-maximum-sum.py
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        def kadane(arr, res = 0, curr = 0):
            for num in arr:
                curr = max(num, curr + num)
                res = max(res, curr)
            return res
        
        return ((k - 2) * max(sum(arr), 0) + kadane(arr * 2) if k > 1 else kadane(arr)) % M
```


