---
id: count-operations-to-obtain-zero
title: Count Operations to Obtain Zero
description: Problem Description and Solution for Count Operations to Obtain Zero
sidebar_label: 2169. Count Operations to Obtain Zero
sidebar_position: 2169
---

# [2169. Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero/)

```py title=count-operations-to-obtain-zero.py
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        
        return count
```


