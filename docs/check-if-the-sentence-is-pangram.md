---
id: check-if-the-sentence-is-pangram
title: Check if the Sentence Is Pangram
description: Problem Description and Solution for Check if the Sentence Is Pangram
sidebar_label: 1832. Check if the Sentence Is Pangram
sidebar_position: 1832
---

# [1832. Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)

```py title=check-if-the-sentence-is-pangram.py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = 0
        
        for x in sentence:
            k = ord(x) - ord("a")
            
            if res & (1 << k) == 0:
                res ^= (1 << k)
        
        return res == (1 << 26) - 1
```


