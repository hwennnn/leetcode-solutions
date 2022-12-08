---
id: odd-string-difference
title: Odd String Difference
description: Problem Description and Solution for Odd String Difference
sidebar_label: 2451. Odd String Difference
sidebar_position: 2451
---

# [2451. Odd String Difference](https://leetcode.com/problems/odd-string-difference/)

```py title=odd-string-difference.py
class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = defaultdict(list)
        
        for word in words:
            d = []
            
            for i in range(1, len(word)):
                d.append(ord(word[i]) - ord(word[i - 1]))
            
            diff[tuple(d)].append(word)
        
        for k, v in diff.items():
            if len(v) == 1:
                return v[0]
```


