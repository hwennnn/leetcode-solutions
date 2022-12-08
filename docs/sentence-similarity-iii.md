---
id: sentence-similarity-iii
title: Sentence Similarity III
description: Problem Description and Solution for Sentence Similarity III
sidebar_label: 1813. Sentence Similarity III
sidebar_position: 1813
---

# [1813. Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii/)

```py title=sentence-similarity-iii.py
class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1 = s1.split()
        s2 = s2.split()
        
        def good(a, b):
            a = collections.deque(a)
            b = collections.deque(b)
            
            while len(a) > 0 and len(b) > 0 and a[0] == b[0]:
                a.popleft()
                b.popleft()
            
            while len(a) > 0 and len(b) > 0 and a[-1] == b[-1]:
                a.pop()
                b.pop()
            
            return len(a) == 0
        
        return good(s1, s2) or good(s2, s1)
```


