---
id: last-substring-in-lexicographical-order
title: Last Substring in Lexicographical Order
description: Problem Description and Solution for Last Substring in Lexicographical Order
sidebar_label: 1163. Last Substring in Lexicographical Order
sidebar_position: 1163
---

# [1163. Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/)

```py title=last-substring-in-lexicographical-order.py
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, indexes = 0, list(range(n))
        
        while len(indexes) > 1:
            new = []
            mx = max([s[i + j] for j in indexes if i + j < len(s)])

            for k, j in enumerate(indexes):
                if k - 1 >= 0 and indexes[k - 1] + i == j:
                    continue
                if i + j >= len(s):
                    break
                if s[i + j] == mx:
                    new.append(j)
            i += 1
            indexes = new
            
        return s[indexes[0]:]
```


