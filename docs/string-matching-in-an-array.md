---
id: string-matching-in-an-array
title: String Matching in an Array
description: Problem Description and Solution for String Matching in an Array
sidebar_label: 1408. String Matching in an Array
sidebar_position: 1408
---

# [1408. String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/)

```py title=string-matching-in-an-array.py
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        
        for i,w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j and w1 in w2:
                    res.add(w1)
        
        return list(res)
```


