---
id: minimum-deletions-to-make-character-frequencies-unique
title: Minimum Deletions to Make Character Frequencies Unique
description: Problem Description and Solution for Minimum Deletions to Make Character Frequencies Unique
sidebar_label: 1647. Minimum Deletions to Make Character Frequencies Unique
sidebar_position: 1647
---

# [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

```py title=minimum-deletions-to-make-character-frequencies-unique.py
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        seen = set()
        
        for v in count.values():
            while v > 0 and v in seen:
                res += 1
                v -= 1
            
            if v > 0:
                seen.add(v)
            
        return res
        
```


