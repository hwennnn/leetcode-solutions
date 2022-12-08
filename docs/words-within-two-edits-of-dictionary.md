---
id: words-within-two-edits-of-dictionary
title: Words Within Two Edits of Dictionary
description: Problem Description and Solution for Words Within Two Edits of Dictionary
sidebar_label: 2452. Words Within Two Edits of Dictionary
sidebar_position: 2452
---

# [2452. Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)

```py title=words-within-two-edits-of-dictionary.py
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        
        for query in queries:
            for dictWord in dictionary:
                diff = sum(1 for a, b in zip(query, dictWord) if a != b)

                if diff <= 2:
                    res.append(query)
                    break

        return res
```


