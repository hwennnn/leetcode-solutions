---
id: short-encoding-of-words
title: Short Encoding of Words
description: Problem Description and Solution for Short Encoding of Words
sidebar_label: 820. Short Encoding of Words
sidebar_position: 820
---

# [820. Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/)

```py title=short-encoding-of-words.py
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        
        return sum(len(w) + 1 for w in s)
```


