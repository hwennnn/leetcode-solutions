---
id: find-all-anagrams-in-a-string
title: Find All Anagrams in a String
description: Problem Description and Solution for Find All Anagrams in a String
sidebar_label: 438. Find All Anagrams in a String
sidebar_position: 438
---

# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

```py title=find-all-anagrams-in-a-string.py
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p)
        counter = Counter(p)
        curr = len(counter)
        res = []
        
        for i, x in enumerate(s):
            if x in counter:
                counter[x] -= 1
                if counter[x] == 0:
                    curr -= 1
            
            if curr == 0:
                res.append(i - n2 + 1)
            
            if i - n2 + 1 >= 0 and s[i - n2 + 1] in counter:
                counter[s[i - n2 + 1]] += 1
                if counter[s[i - n2 + 1]] == 1:
                    curr += 1
        
        return res
        
```


