---
id: find-common-characters
title: Find Common Characters
description: Problem Description and Solution for Find Common Characters
sidebar_label: 1002. Find Common Characters
sidebar_position: 1002
---

# [1002. Find Common Characters](https://leetcode.com/problems/find-common-characters/)

```py title=find-common-characters.py
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        counter = Counter(words[0])
        
        for i in range(1, n):
            counter &= Counter(words[i])
        
        res = []
        
        for k, v in counter.items():
            res += [k] * v
        
        return res
```


