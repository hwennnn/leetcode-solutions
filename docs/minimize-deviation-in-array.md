---
id: minimize-deviation-in-array
title: Minimize Deviation in Array
description: Problem Description and Solution for Minimize Deviation in Array
sidebar_label: 1675. Minimize Deviation in Array
sidebar_position: 1675
---

# [1675. Minimize Deviation in Array](https://leetcode.com/problems/minimize-deviation-in-array/)

```py title=minimize-deviation-in-array.py
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        
        for x in nums:
            heapq.heappush(heap, -x if x % 2 == 0 else -x * 2)
        
        mmin = -max(heap)
        res = float('inf')
        
        while len(heap) == len(nums):
            x = -heapq.heappop(heap)
            res = min(res, x - mmin)
            
            if x % 2 == 0:
                mmin = min(mmin, x // 2)
                heapq.heappush(heap, -x // 2)
        
        return res
```


