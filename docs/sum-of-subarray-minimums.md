---
id: sum-of-subarray-minimums
title: Sum of Subarray Minimums
description: Problem Description and Solution for Sum of Subarray Minimums
sidebar_label: 907. Sum of Subarray Minimums
sidebar_position: 907
---

# [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

```py title=sum-of-subarray-minimums.py
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        res = 0
        M = 10 ** 9 + 7
        stack = [-1]

        for i, x in enumerate(arr):
            while stack and x < arr[stack[-1]]:
                mid = stack.pop()
                res += (mid - stack[-1]) * (i - mid) * arr[mid]
            stack.append(i)
        
        return res % M

```


