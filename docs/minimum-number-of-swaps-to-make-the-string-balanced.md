---
id: minimum-number-of-swaps-to-make-the-string-balanced
title: Minimum Number of Swaps to Make the String Balanced
description: Problem Description and Solution for Minimum Number of Swaps to Make the String Balanced
sidebar_label: 1963. Minimum Number of Swaps to Make the String Balanced
sidebar_position: 1963
---

# [1963. Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/)

```py title=minimum-number-of-swaps-to-make-the-string-balanced.py
class Solution:
    def minSwaps(self, s: str) -> int:
        count = res = 0
        
        for c in s:
            if c == '[':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                count += 2
                res += 1
        
        return res
```


