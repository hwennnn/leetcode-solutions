---
id: count-integers-with-even-digit-sum
title: Count Integers With Even Digit Sum
description: Problem Description and Solution for Count Integers With Even Digit Sum
sidebar_label: 2180. Count Integers With Even Digit Sum
sidebar_position: 2180
---

# [2180. Count Integers With Even Digit Sum](https://leetcode.com/problems/count-integers-with-even-digit-sum/)

```py title=count-integers-with-even-digit-sum.py
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        
        for x in range(2, num + 1):
            s = sum(int(c) for c in str(x))
            if s % 2 == 0:
                res += 1
        
        return res
```


