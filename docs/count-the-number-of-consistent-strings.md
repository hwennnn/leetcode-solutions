---
id: count-the-number-of-consistent-strings
title: Count the Number of Consistent Strings
description: Problem Description and Solution for Count the Number of Consistent Strings
sidebar_label: 1684. Count the Number of Consistent Strings
sidebar_position: 1684
---

# [1684. Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/)

```py title=count-the-number-of-consistent-strings.py
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        res = 0
        for w in words:
            s2 = set(w)
            check = False
            for c in s2:
                if c not in s:
                    check = True
                    break
            
            if not check: res += 1
        
        return res
```


