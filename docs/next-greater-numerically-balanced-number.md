---
id: next-greater-numerically-balanced-number
title: Next Greater Numerically Balanced Number
description: Problem Description and Solution for Next Greater Numerically Balanced Number
sidebar_label: 2048. Next Greater Numerically Balanced Number
sidebar_position: 2048
---

# [2048. Next Greater Numerically Balanced Number](https://leetcode.com/problems/next-greater-numerically-balanced-number/)

```py title=next-greater-numerically-balanced-number.py
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def good(counter):
            for k, v in counter.items():
                if int(k) != v:
                    return False
            
            return True
        
        n += 1
        counter = collections.Counter(str(n))
        
        while not good(counter):
            n += 1
            counter = collections.Counter(str(n))
        
        return n
```


