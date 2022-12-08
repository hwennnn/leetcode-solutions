---
id: counting-words-with-a-given-prefix
title: Counting Words With a Given Prefix
description: Problem Description and Solution for Counting Words With a Given Prefix
sidebar_label: 2185. Counting Words With a Given Prefix
sidebar_position: 2185
---

# [2185. Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/)

```py title=counting-words-with-a-given-prefix.py
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        
        for word in words:
            if word.startswith(pref):
                res += 1
            
        return res
```


