---
id: number-of-ways-to-form-a-target-string-given-a-dictionary
title: Number of Ways to Form a Target String Given a Dictionary
description: Problem Description and Solution for Number of Ways to Form a Target String Given a Dictionary
sidebar_label: 1639. Number of Ways to Form a Target String Given a Dictionary
sidebar_position: 1639
---

# [1639. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)

```py title=number-of-ways-to-form-a-target-string-given-a-dictionary.py
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        count = defaultdict(lambda: defaultdict(int))
        
        for word in words:
            for i, x in enumerate(word):
                count[x][i] += 1
        
        @cache
        def go(i, k):
            if i == n:
                return 1
            
            if k == m:
                return 0
            
            res = go(i, k + 1)
            
            if count[target[i]][k] > 0:
                res += go(i + 1, k + 1) * count[target[i]][k]
                res %= M
            
            return res
        
        return go(0, 0)
        
        
```


