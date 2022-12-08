---
id: count-the-hidden-sequences
title: Count the Hidden Sequences
description: Problem Description and Solution for Count the Hidden Sequences
sidebar_label: 2145. Count the Hidden Sequences
sidebar_position: 2145
---

# [2145. Count the Hidden Sequences](https://leetcode.com/problems/count-the-hidden-sequences/)

```py title=count-the-hidden-sequences.py
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mmax = mmin = s = 0
        
        for x in differences:
            s += x
            
            mmax = max(mmax, s)
            mmin = min(mmin, s)
        
        res = 0
        
        for x in range(lower, upper + 1):
            if x + mmin >= lower and x + mmax <= upper:
                res += 1
        
        return res
```


