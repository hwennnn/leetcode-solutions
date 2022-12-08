---
id: minimum-bit-flips-to-convert-number
title: Minimum Bit Flips to Convert Number
description: Problem Description and Solution for Minimum Bit Flips to Convert Number
sidebar_label: 2220. Minimum Bit Flips to Convert Number
sidebar_position: 2220
---

# [2220. Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)

```py title=minimum-bit-flips-to-convert-number.py
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = start ^ goal
        count = 0
        
        while a:
            count += a & 1
            a >>= 1
        
        return count
```


