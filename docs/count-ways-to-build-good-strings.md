---
id: count-ways-to-build-good-strings
title: Count Ways To Build Good Strings
description: Problem Description and Solution for Count Ways To Build Good Strings
sidebar_label: 2466. Count Ways To Build Good Strings
sidebar_position: 2466
---

# [2466. Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/)

```py title=count-ways-to-build-good-strings.py
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(k):
            if k > high: return 0
            
            res = 0
            
            if low <= k <= high:
                res += 1
            
            return (res + go(k + zero) + go(k + one)) % M
        
        return go(0)
            
            
```


