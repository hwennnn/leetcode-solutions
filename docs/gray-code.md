---
id: gray-code
title: Gray Code
description: Problem Description and Solution for Gray Code
sidebar_label: 89. Gray Code
sidebar_position: 89
---

# [89. Gray Code](https://leetcode.com/problems/gray-code/)

```py title=gray-code.py
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(n):
            for j in range(len(res) - 1,-1,-1):
                res.append(res[j] | 1 << i)
        
        return res
```


