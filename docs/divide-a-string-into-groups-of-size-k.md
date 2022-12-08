---
id: divide-a-string-into-groups-of-size-k
title: Divide a String Into Groups of Size k
description: Problem Description and Solution for Divide a String Into Groups of Size k
sidebar_label: 2138. Divide a String Into Groups of Size k
sidebar_position: 2138
---

# [2138. Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)

```py title=divide-a-string-into-groups-of-size-k.py
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        
        for i in range(0, n, k):
            if i + k <= n:
                res.append(s[i:i + k])
            else:
                c = s[i : n]
                left = k - len(c)
                
                res.append(c + fill * left)
        
        
        return res
```


