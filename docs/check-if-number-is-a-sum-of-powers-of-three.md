---
id: check-if-number-is-a-sum-of-powers-of-three
title: Check if Number is a Sum of Powers of Three
description: Problem Description and Solution for Check if Number is a Sum of Powers of Three
sidebar_label: 1780. Check if Number is a Sum of Powers of Three
sidebar_position: 1780
---

# [1780. Check if Number is a Sum of Powers of Three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)

```py title=check-if-number-is-a-sum-of-powers-of-three.py
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 2: return False
            
            n //= 3
            
        return n == 1
```


