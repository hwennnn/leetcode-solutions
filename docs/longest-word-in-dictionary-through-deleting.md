---
id: longest-word-in-dictionary-through-deleting
title: Longest Word in Dictionary through Deleting
description: Problem Description and Solution for Longest Word in Dictionary through Deleting
sidebar_label: 524. Longest Word in Dictionary through Deleting
sidebar_position: 524
---

# [524. Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)

```py title=longest-word-in-dictionary-through-deleting.py
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: (-len(x), x))
        
        for word in d:
            i = 0
            
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
                
            if i == len(word): return word
        
        return ""
```


