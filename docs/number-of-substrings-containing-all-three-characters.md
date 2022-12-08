---
id: number-of-substrings-containing-all-three-characters
title: Number of Substrings Containing All Three Characters
description: Problem Description and Solution for Number of Substrings Containing All Three Characters
sidebar_label: 1358. Number of Substrings Containing All Three Characters
sidebar_position: 1358
---

# [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

```py title=number-of-substrings-containing-all-three-characters.py
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = {c:0 for c in "abc"}
        res = i = 0
        
        for j, c in enumerate(s):
            mp[c] += 1
            
            while all(mp.values()):
                mp[s[i]] -= 1
                i += 1
            
            res += i
        
        return res
        
        
        
```


