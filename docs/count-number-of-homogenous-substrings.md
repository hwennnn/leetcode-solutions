---
id: count-number-of-homogenous-substrings
title: Count Number of Homogenous Substrings
description: Problem Description and Solution for Count Number of Homogenous Substrings
sidebar_label: 1759. Count Number of Homogenous Substrings
sidebar_position: 1759
---

# [1759. Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/)

```py title=count-number-of-homogenous-substrings.py
class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        res = 0
        
        mp = Counter(s)
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                res += j - i
                j += 1
            
            i = j
        
        return (res + sum(mp.values())) % M
```


