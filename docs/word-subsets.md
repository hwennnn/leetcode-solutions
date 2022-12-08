---
id: word-subsets
title: Word Subsets
description: Problem Description and Solution for Word Subsets
sidebar_label: 916. Word Subsets
sidebar_position: 916
---

# [916. Word Subsets](https://leetcode.com/problems/word-subsets/)

```py title=word-subsets.py
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        
        for word in words2:
            cnt = Counter(word)
            
            for x, value in cnt.items():
                counter[x] = max(counter[x], value)
        
        res = []
        
        for word in words1:
            curr = Counter(word)
            
            for x, value in counter.items():
                if curr[x] < value:
                    flag = False
                    break
            else:
                res.append(word)
                
        return res
        
```


