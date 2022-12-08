---
id: build-an-array-with-stack-operations
title: Build an Array With Stack Operations
description: Problem Description and Solution for Build an Array With Stack Operations
sidebar_label: 1441. Build an Array With Stack Operations
sidebar_position: 1441
---

# [1441. Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/)

```py title=build-an-array-with-stack-operations.py
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = [i for i in range(1,n+1)]
        res = []
        j = 0
        for i in range(n):
            if j >= len(target):
                break
            if arr[i] != target[j]:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
                j += 1
        return res
```


