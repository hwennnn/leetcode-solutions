---
id: delete-columns-to-make-sorted
title: Delete Columns to Make Sorted
description: Problem Description and Solution for Delete Columns to Make Sorted
sidebar_label: 944. Delete Columns to Make Sorted
sidebar_position: 944
---

# [944. Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)

```py title=delete-columns-to-make-sorted.py
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        res = 0
        
        for j in range(n):
            for c1, c2 in zip(strs, strs[1:]):
                if c1[j] > c2[j]:
                    res += 1
                    break
        
        return res
```


