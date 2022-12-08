---
id: count-words-obtained-after-adding-a-letter
title: Count Words Obtained After Adding a Letter
description: Problem Description and Solution for Count Words Obtained After Adding a Letter
sidebar_label: 2135. Count Words Obtained After Adding a Letter
sidebar_position: 2135
---

# [2135. Count Words Obtained After Adding a Letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/)

```py title=count-words-obtained-after-adding-a-letter.py
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        targets = Counter()
        
        for words in targetWords:
            mask = 0
            for word in words:
                mask |= (1 << ord(word) - ord('a'))
            
            targets[mask] += 1
        
        res = 0
        
        for words in startWords:
            mask = 0
            for word in words:
                mask |= (1 << ord(word) - ord('a'))
                
            for i in range(26):
                if mask & (1 << i) > 0: continue
                
                newMask = mask | (1 << i)
                
                res += targets[newMask]
                targets[newMask] = 0

        return res
```


