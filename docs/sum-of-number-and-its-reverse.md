---
id: sum-of-number-and-its-reverse
title: Sum of Number and Its Reverse
description: Problem Description and Solution for Sum of Number and Its Reverse
sidebar_label: 2443. Sum of Number and Its Reverse
sidebar_position: 2443
---

# [2443. Sum of Number and Its Reverse](https://leetcode.com/problems/sum-of-number-and-its-reverse/)

```py title=sum-of-number-and-its-reverse.py
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        N = len(str(num))
        
        for x in range(num, num // 2 - 1, -1):
            if x + int(str(x)[::-1]) == num:
                return True
        
        return False
```


