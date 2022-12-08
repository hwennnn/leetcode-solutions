---
id: 132-pattern
title: 132 Pattern
description: Problem Description and Solution for 132 Pattern
sidebar_label: 456. 132 Pattern
sidebar_position: 456
---

# [456. 132 Pattern](https://leetcode.com/problems/132-pattern/)

```py title=132-pattern.py
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, mid = [], float("-inf")
        
        for num in nums[::-1]:
            if num < mid: return True
            else:
                while stack and num > stack[-1]:
                    mid = stack.pop()
            
            stack.append(num)
            
        return False
```


