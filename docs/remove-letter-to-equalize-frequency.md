---
id: remove-letter-to-equalize-frequency
title: Remove Letter To Equalize Frequency
description: Problem Description and Solution for Remove Letter To Equalize Frequency
sidebar_label: 2423. Remove Letter To Equalize Frequency
sidebar_position: 2423
---

# [2423. Remove Letter To Equalize Frequency](https://leetcode.com/problems/remove-letter-to-equalize-frequency/)

```py title=remove-letter-to-equalize-frequency.py
class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)
        
        for i in range(N):
            newWord = word[:i] + word[i + 1:]
            vals = list(Counter(newWord).values())
            
            first = vals[0]
            if all(v == first for v in vals):
                return True
        
        return False
```


