---
id: number-of-matching-subsequences
title: Number of Matching Subsequences
description: Problem Description and Solution for Number of Matching Subsequences
sidebar_label: 792. Number of Matching Subsequences
sidebar_position: 792
---

# [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)

```py title=number-of-matching-subsequences.py
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = collections.defaultdict(collections.deque)
        
        for w in words:
            mp[w[0]].append(w)
        
        res = 0
        
        for c in s:
            n = len(mp[c])
            
            for _ in range(n):
                word = mp[c].popleft()
                if len(word) == 1:
                    res += 1
                else:
                    mp[word[1]].append(word[1:])
        
        return res
```


