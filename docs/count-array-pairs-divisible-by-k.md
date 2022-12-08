---
id: count-array-pairs-divisible-by-k
title: Count Array Pairs Divisible by K
description: Problem Description and Solution for Count Array Pairs Divisible by K
sidebar_label: 2183. Count Array Pairs Divisible by K
sidebar_position: 2183
---

# [2183. Count Array Pairs Divisible by K](https://leetcode.com/problems/count-array-pairs-divisible-by-k/)

```py title=count-array-pairs-divisible-by-k.py
class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        divisors = []
        count = Counter()
        
        for x in range(1, k + 1):
            if k % x == 0:
                divisors.append(x)
        
        for x in nums:
            remainder = k // math.gcd(k, x)
            res += count[remainder]
            
            for divisor in divisors:
                if x % divisor == 0:
                    count[divisor] += 1
        
        return res
```


