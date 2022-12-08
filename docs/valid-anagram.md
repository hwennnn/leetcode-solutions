---
id: valid-anagram
title: Valid Anagram
description: Problem Description and Solution for Valid Anagram
sidebar_label: 242. Valid Anagram
sidebar_position: 242
---

# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```py title=valid-anagram.py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = Counter(s)
        
        for x in t:
            if counter[x] <= 0:
                return False
            
            counter[x] -= 1
        
        return True
```


