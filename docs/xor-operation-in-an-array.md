---
id: xor-operation-in-an-array
title: XOR Operation in an Array
description: Problem Description and Solution for XOR Operation in an Array
sidebar_label: 1486. XOR Operation in an Array
sidebar_position: 1486
---

# [1486. XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)

```py title=xor-operation-in-an-array.py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = start
        
        for i in range(1,n):
            ans ^= start+2*i
        
        return ans
```


