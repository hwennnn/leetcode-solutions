---
id: ransom-note
title: Ransom Note
description: Problem Description and Solution for Ransom Note
sidebar_label: 383. Ransom Note
sidebar_position: 383
---

# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

```py title=ransom-note.py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = collections.Counter(ransomNote)
        n = len(mp)
        
        for word in magazine:
            mp[word] -= 1
            if mp[word] == 0:
                n -= 1
            
            if n == 0: return True
        
        return False
```


