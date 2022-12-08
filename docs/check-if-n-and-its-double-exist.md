---
id: check-if-n-and-its-double-exist
title: Check If N and Its Double Exist
description: Problem Description and Solution for Check If N and Its Double Exist
sidebar_label: 1346. Check If N and Its Double Exist
sidebar_position: 1346
---

# [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/)

```py title=check-if-n-and-its-double-exist.py
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if arr[i] == 2*arr[j]:
                        return True
        
        return False
```


