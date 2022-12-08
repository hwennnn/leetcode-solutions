---
id: smallest-string-with-a-given-numeric-value
title: Smallest String With A Given Numeric Value
description: Problem Description and Solution for Smallest String With A Given Numeric Value
sidebar_label: 1663. Smallest String With A Given Numeric Value
sidebar_position: 1663
---

# [1663. Smallest String With A Given Numeric Value](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/)

```py title=smallest-string-with-a-given-numeric-value.py
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        last = []
        
        while k >= 26 + n:
            last.append("z")
            n -= 1
            k -= 26
            
        first = []
        for i in range(n):
            if i == n - 1:
                first.append(chr(ord("a") + k - 1))
            else:
                first.append("a")
                k -= 1
        
        return "".join(first + last)
```


