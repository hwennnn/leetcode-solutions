---
id: kth-largest-element-in-an-array
title: Kth Largest Element in an Array
description: Problem Description and Solution for Kth Largest Element in an Array
sidebar_label: 215. Kth Largest Element in an Array
sidebar_position: 215
---

# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```py title=kth-largest-element-in-an-array.py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for x in nums:
            if len(heap) == k:
                heappushpop(heap, x)
            else:
                heappush(heap, x)
        
        return heappop(heap)
```


