---
id: count-number-of-distinct-integers-after-reverse-operations
title: Count Number of Distinct Integers After Reverse Operations
description: Problem Description and Solution for Count Number of Distinct Integers After Reverse Operations
sidebar_label: 2442. Count Number of Distinct Integers After Reverse Operations
sidebar_position: 2442
---

# [2442. Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/)

```py title=count-number-of-distinct-integers-after-reverse-operations.py
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set()
        
        for x in nums:
            res.add(x)
            
            r = int(str(x)[::-1])
            
            res.add(r)
        
        return len(res)
```


