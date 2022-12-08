---
id: sum-of-even-numbers-after-queries
title: Sum of Even Numbers After Queries
description: Problem Description and Solution for Sum of Even Numbers After Queries
sidebar_label: 985. Sum of Even Numbers After Queries
sidebar_position: 985
---

# [985. Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)

```py title=sum-of-even-numbers-after-queries.py
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        total = sum(x for x in nums if x % 2 == 0)
        res = []
        
        for val, index in queries:
            x = nums[index]
            newNum = x + val
            nums[index] = newNum
            
            if x % 2 == 0:
                if newNum % 2 == 0:
                    total += newNum - x
                else:
                    total -= x
            else:
                if newNum % 2 == 0:
                    total += newNum
            
            res.append(total)
        
        return res
```


