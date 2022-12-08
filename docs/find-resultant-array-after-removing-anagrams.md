---
id: find-resultant-array-after-removing-anagrams
title: Find Resultant Array After Removing Anagrams
description: Problem Description and Solution for Find Resultant Array After Removing Anagrams
sidebar_label: 2273. Find Resultant Array After Removing Anagrams
sidebar_position: 2273
---

# [2273. Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)

```py title=find-resultant-array-after-removing-anagrams.py
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        while len(words) >= 2:
            currN = len(words)
            
            for i in range(1, len(words)):
                if sorted(words[i - 1]) == sorted(words[i]):
                    words.pop(i)
                    break
            
            if currN == len(words):
                break
                
        
        return words
```


