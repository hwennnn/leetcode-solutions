---
id: maximum-value-after-insertion
title: Maximum Value after Insertion
description: Problem Description and Solution for Maximum Value after Insertion
sidebar_label: 1881. Maximum Value after Insertion
sidebar_position: 1881
---

# [1881. Maximum Value after Insertion](https://leetcode.com/problems/maximum-value-after-insertion/)

```py title=maximum-value-after-insertion.py
class Solution:
    def maxValue(self, word: str, x: int) -> str:
        
        if word[0] != '-':
            for i,c in enumerate(word):
                if x > int(c):
                    return word[:i] + str(x) + word[i:]
                
            return word + str(x)
        else:
            for i,c in enumerate(word):
                if i != 0 and x < int(c):
                    return word[:i] + str(x) + word[i:]
                
            return word + str(x)
```


