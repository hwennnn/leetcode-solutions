---
id: sum-of-square-numbers
title: Sum of Square Numbers
description: Problem Description and Solution for Sum of Square Numbers
sidebar_label: 633. Sum of Square Numbers
sidebar_position: 633
---

# [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/)

```py title=sum-of-square-numbers.py
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()

        for i in range(int(math.sqrt(c)) + 1):
            s.add(i * i)
        
        for x in s:
            if c - x in s:
                return True
        
        return False
        
```


