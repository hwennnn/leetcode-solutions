---
id: replace-non-coprime-numbers-in-array
title: Replace Non-Coprime Numbers in Array
description: Problem Description and Solution for Replace Non-Coprime Numbers in Array
sidebar_label: 2197. Replace Non-Coprime Numbers in Array
sidebar_position: 2197
---

# [2197. Replace Non-Coprime Numbers in Array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)

```py title=replace-non-coprime-numbers-in-array.py
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def non_coprime(x, y):
            return gcd(x, y) > 1
    
        def lcm(x, y):
            lcm = (x*y) // gcd(x,y)
            return lcm
        
        stack = []
        for x in nums:
            stack.append(x)
            
            while len(stack) >= 2 and non_coprime(stack[-1], stack[-2]):
                stack.append(lcm(stack.pop(), stack.pop()))

        return stack
                    
```


