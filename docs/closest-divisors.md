---
id: closest-divisors
title: Closest Divisors
description: Problem Description and Solution for Closest Divisors
sidebar_label: 1362. Closest Divisors
sidebar_position: 1362
---

# [1362. Closest Divisors](https://leetcode.com/problems/closest-divisors/)

```py title=closest-divisors.py
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        for i in range(int(math.sqrt(num+2)), 0 , -1):
            if (num + 1) % i == 0:
                return [i, (num+1)//i]
            
            if (num + 2) % i == 0:
                return [i, (num+2)//i]
                
```


