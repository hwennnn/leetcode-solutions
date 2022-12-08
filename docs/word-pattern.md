---
id: word-pattern
title: Word Pattern
description: Problem Description and Solution for Word Pattern
sidebar_label: 290. Word Pattern
sidebar_position: 290
---

# [290. Word Pattern](https://leetcode.com/problems/word-pattern/)

```py title=word-pattern.py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        def generate(s):
            seen = {}
            res = []
            
            for word in s:
                if word not in seen:
                    seen[word] = len(seen)
                    
                res.append(seen[word])
            
            return "".join(map(str, res))
        
        return generate(pattern) == generate(s.split())
            
```


