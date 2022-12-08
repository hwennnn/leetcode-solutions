---
id: verifying-an-alien-dictionary
title: Verifying an Alien Dictionary
description: Problem Description and Solution for Verifying an Alien Dictionary
sidebar_label: 953. Verifying an Alien Dictionary
sidebar_position: 953
---

# [953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)

```py title=verifying-an-alien-dictionary.py
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        O = {x: i for i, x in enumerate(order)}
        
        words = [[O[x] for x in word] for word in words]
        
        return all(x1 <= x2 for x1, x2 in zip(words, words[1:]))
```


