---
id: match-substring-after-replacement
title: Match Substring After Replacement
description: Problem Description and Solution for Match Substring After Replacement
sidebar_label: 2301. Match Substring After Replacement
sidebar_position: 2301
---

# [2301. Match Substring After Replacement](https://leetcode.com/problems/match-substring-after-replacement/)

```py title=match-substring-after-replacement.py
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mp = defaultdict(set)
        n, m = len(s), len(sub)
        
        for a, b in mappings:
            mp[b].add(a)
        
        def go(index, curr):
            if curr == m:
                return True
            
            if index == n:
                return False
            
            if sub[curr] == s[index] or sub[curr] in mp[s[index]]:
                return go(index + 1, curr + 1)
            
            return False
            
        for i, x in enumerate(s):
            if go(i, 0):
                return True
        
        return False
```


