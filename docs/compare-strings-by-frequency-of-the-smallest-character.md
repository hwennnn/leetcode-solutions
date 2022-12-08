---
id: compare-strings-by-frequency-of-the-smallest-character
title: Compare Strings by Frequency of the Smallest Character
description: Problem Description and Solution for Compare Strings by Frequency of the Smallest Character
sidebar_label: 1170. Compare Strings by Frequency of the Smallest Character
sidebar_position: 1170
---

# [1170. Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)

```py title=compare-strings-by-frequency-of-the-smallest-character.py
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res, res1, res2 = [], [], []
        
        def f(word):
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1

            for c in count:
                if c != 0: return c
            
            return -1
            
        for word in queries:
            res1.append(f(word))
        
        for word in words:
            res2.append(f(word))
        
        for x in res1:
            count = 0
            for y in res2:
                if y > x:
                    count += 1
            
            res.append(count)
        
        return res
        
        
            
```


