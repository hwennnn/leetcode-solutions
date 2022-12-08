---
id: count-vowels-permutation
title: Count Vowels Permutation
description: Problem Description and Solution for Count Vowels Permutation
sidebar_label: 1220. Count Vowels Permutation
sidebar_position: 1220
---

# [1220. Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/)

```py title=count-vowels-permutation.py
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        
        return (a + e + i + o + u) % (10 ** 9 + 7)
```


