---
id: count-prefixes-of-a-given-string
title: Count Prefixes of a Given String
description: Problem Description and Solution for Count Prefixes of a Given String
sidebar_label: 2255. Count Prefixes of a Given String
sidebar_position: 2255
---

# [2255. Count Prefixes of a Given String](https://leetcode.com/problems/count-prefixes-of-a-given-string/)

```py title=count-prefixes-of-a-given-string.py
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        
        for x in words:
            if s.startswith(x):
                res += 1
        
        return res
```


