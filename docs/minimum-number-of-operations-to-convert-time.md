---
id: minimum-number-of-operations-to-convert-time
title: Minimum Number of Operations to Convert Time
description: Problem Description and Solution for Minimum Number of Operations to Convert Time
sidebar_label: 2224. Minimum Number of Operations to Convert Time
sidebar_position: 2224
---

# [2224. Minimum Number of Operations to Convert Time](https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/)

```py title=minimum-number-of-operations-to-convert-time.py
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct: return 0
        
        h1, h2 = int(current[:2]), int(correct[:2])
        m1, m2 = int(current[3:]), int(correct[3:])
        
        res = h2 - h1
        
        if m1 > m2:
            m2 += 60
            res -= 1
        
        while m2 > m1:
            d = m2 - m1

            if d >= 15:
                res += 1
                m2 -= 15
            elif d >= 5:
                res += 1
                m2 -= 5
            else:
                res += 1
                m2 -= 1
            
        
        return res
        
```


