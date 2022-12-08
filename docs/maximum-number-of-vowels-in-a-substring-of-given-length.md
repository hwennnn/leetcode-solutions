---
id: maximum-number-of-vowels-in-a-substring-of-given-length
title: Maximum Number of Vowels in a Substring of Given Length
description: Problem Description and Solution for Maximum Number of Vowels in a Substring of Given Length
sidebar_label: 1456. Maximum Number of Vowels in a Substring of Given Length
sidebar_position: 1456
---

# [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

```py title=maximum-number-of-vowels-in-a-substring-of-given-length.py
class Solution:
    def maxVowels(self, S: str, k: int) -> int:
        d = {"a","e","i","o","u"}
        
        c = res = 0
        
        for i, s in enumerate(S):
            if s in d:
                c += 1
            
            if i >= k and S[i-k] in d:
                c -= 1
            
            res = max(res, c)
        
        return res
```


