---
id: bitwise-and-of-numbers-range
title: Bitwise AND of Numbers Range
description: Problem Description and Solution for Bitwise AND of Numbers Range
sidebar_label: 201. Bitwise AND of Numbers Range
sidebar_position: 201
---

# [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

```py title=bitwise-and-of-numbers-range.py
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        
        return left << i
```


