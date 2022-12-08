---
id: check-if-all-characters-have-equal-number-of-occurrences
title: Check if All Characters Have Equal Number of Occurrences
description: Problem Description and Solution for Check if All Characters Have Equal Number of Occurrences
sidebar_label: 1941. Check if All Characters Have Equal Number of Occurrences
sidebar_position: 1941
---

# [1941. Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/)

```py title=check-if-all-characters-have-equal-number-of-occurrences.py
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = collections.Counter(s)
        values = list(counter.values())
        
        for v in values:
            if v != values[0]: return False
        
        return True
```


