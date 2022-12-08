---
id: delete-columns-to-make-sorted-iii
title: Delete Columns to Make Sorted III
description: Problem Description and Solution for Delete Columns to Make Sorted III
sidebar_label: 960. Delete Columns to Make Sorted III
sidebar_position: 960
---

# [960. Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)

```py title=delete-columns-to-make-sorted-iii.py
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        dp = [1] * n
        
        for j in range(1, n):
            for i in range(j):
                if all(a[j] >= a[i] for a in A):
                    dp[j] = max(dp[j], dp[i] + 1)
            
        return n - max(dp)
```


