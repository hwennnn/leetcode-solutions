---
id: count-of-smaller-numbers-after-self
title: Count of Smaller Numbers After Self
description: Problem Description and Solution for Count of Smaller Numbers After Self
sidebar_label: 315. Count of Smaller Numbers After Self
sidebar_position: 315
---

# [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

```py title=count-of-smaller-numbers-after-self.py
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = SortedList([nums[-1]])
        
        for i in range(n - 2, -1, -1):
            index = sl.bisect(nums[i] - 1)
            
            res[i] = index
            
            sl.add(nums[i])
        
        return res
```


