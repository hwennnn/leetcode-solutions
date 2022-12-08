---
id: longest-substring-of-all-vowels-in-order
title: Longest Substring Of All Vowels in Order
description: Problem Description and Solution for Longest Substring Of All Vowels in Order
sidebar_label: 1839. Longest Substring Of All Vowels in Order
sidebar_position: 1839
---

# [1839. Longest Substring Of All Vowels in Order](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/)

```py title=longest-substring-of-all-vowels-in-order.py
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if "a" not in word: return 0
        v = ["a", "e", "i", "o", "u"]

        vi = 0
        n = len(word)
        curr = res = 0
        i = j = word.index("a")
        while j < n and word[j] == "a":
            j += 1
        vi += 1

        while i < n and j < n:
            if word[j] != v[vi]:
                vi = 0
                i = j
                
                while j < n and word[j] != v[vi]:
                    j += 1
                i = j

            if j >= n: return res
            
            while j < n and word[j] == v[vi]:
                j += 1
            
            vi += 1
            if vi == 5: 
                res = max(res, j - i)
                vi = 0
                i = j
            
        return res
```


