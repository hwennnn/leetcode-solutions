---
id: minimum-time-to-type-word-using-special-typewriter
title: Minimum Time to Type Word Using Special Typewriter
description: Problem Description and Solution for Minimum Time to Type Word Using Special Typewriter
sidebar_label: 1974. Minimum Time to Type Word Using Special Typewriter
sidebar_position: 1974
---

# [1974. Minimum Time to Type Word Using Special Typewriter](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/)

```py title=minimum-time-to-type-word-using-special-typewriter.py
class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        prev = 'a'
        
        for curr in word:
            val = (ord(curr) - ord(prev)) % 26
            prev = curr
            res += min(val, 26 - val)
        
        return res
```


