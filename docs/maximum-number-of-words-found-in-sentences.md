---
id: maximum-number-of-words-found-in-sentences
title: Maximum Number of Words Found in Sentences
description: Problem Description and Solution for Maximum Number of Words Found in Sentences
sidebar_label: 2114. Maximum Number of Words Found in Sentences
sidebar_position: 2114
---

# [2114. Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)

```py title=maximum-number-of-words-found-in-sentences.py
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        
        for s in sentences:
            res = max(res, len(s.split()))
        
        return res
```


