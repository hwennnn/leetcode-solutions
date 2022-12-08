---
id: remove-k-digits
title: Remove K Digits
description: Problem Description and Solution for Remove K Digits
sidebar_label: 402. Remove K Digits
sidebar_position: 402
---

# [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

```py title=remove-k-digits.py
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for x in num:
            while k > 0 and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            
            stack.append(x)
            
        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        
        for i in range(len(stack)):
            if stack[i] == '0': continue
            
            return "".join(stack[i:])
        
        return "0"
            
            
```


