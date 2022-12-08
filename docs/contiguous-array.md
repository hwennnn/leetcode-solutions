---
id: contiguous-array
title: Contiguous Array
description: Problem Description and Solution for Contiguous Array
sidebar_label: 525. Contiguous Array
sidebar_position: 525
---

# [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

```py title=contiguous-array.py
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = count = 0
        table = {0 : -1}
        
        for i, x in enumerate(nums):
            if x == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i
        
        return res
```


