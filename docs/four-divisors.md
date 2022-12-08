---
id: four-divisors
title: Four Divisors
description: Problem Description and Solution for Four Divisors
sidebar_label: 1390. Four Divisors
sidebar_position: 1390
---

# [1390. Four Divisors](https://leetcode.com/problems/four-divisors/)

```py title=four-divisors.py
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for num in nums:
            s = set()
            for i in range(1, floor(sqrt(num)) + 1):
                
                if num % i == 0:
                    s.add(num//i)
                    s.add(i)
                
                if len(s) > 4:
                    break
            
            if len(s) == 4:
                res += sum(s)
        
        return res
```


