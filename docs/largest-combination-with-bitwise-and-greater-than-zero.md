---
id: largest-combination-with-bitwise-and-greater-than-zero
title: Largest Combination With Bitwise AND Greater Than Zero
description: Problem Description and Solution for Largest Combination With Bitwise AND Greater Than Zero
sidebar_label: 2275. Largest Combination With Bitwise AND Greater Than Zero
sidebar_position: 2275
---

# [2275. Largest Combination With Bitwise AND Greater Than Zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)

```py title=largest-combination-with-bitwise-and-greater-than-zero.py
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        
        for n in range(31, -1, -1):
            mask = 1 << n
            curr = 0

            for x in candidates:
                if mask & x > 0:
                    curr += 1
            
            res = max(res, curr)
            
        return res
```


