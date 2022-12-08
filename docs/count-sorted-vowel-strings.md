---
id: count-sorted-vowel-strings
title: Count Sorted Vowel Strings
description: Problem Description and Solution for Count Sorted Vowel Strings
sidebar_label: 1641. Count Sorted Vowel Strings
sidebar_position: 1641
---

# [1641. Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

```py title=count-sorted-vowel-strings.py
class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        
        for _ in range(n - 1):
            a, e, i, o, u = a + e + i + o + u, e + i + o + u, i + o + u, o + u, u
        
        return a + e + i + o + u
```


