---
id: sorting-the-sentence
title: Sorting the Sentence
description: Problem Description and Solution for Sorting the Sentence
sidebar_label: 1859. Sorting the Sentence
sidebar_position: 1859
---

# [1859. Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)

```py title=sorting-the-sentence.py
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x:x[-1])
        
        return " ".join(c[:-1] for c in s)
```


