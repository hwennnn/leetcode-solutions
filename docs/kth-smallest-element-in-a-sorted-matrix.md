---
id: kth-smallest-element-in-a-sorted-matrix
title: Kth Smallest Element in a Sorted Matrix
description: Problem Description and Solution for Kth Smallest Element in a Sorted Matrix
sidebar_label: 378. Kth Smallest Element in a Sorted Matrix
sidebar_position: 378
---

# [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

```py title=kth-smallest-element-in-a-sorted-matrix.py
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for mat in matrix:
            for m in mat:
                if len(heap) == k:
                    heappushpop(heap, -m)
                else:
                    heappush(heap, -m)

        return -heap[0]
```


