---
id: kth-largest-element-in-a-stream
title: Kth Largest Element in a Stream
description: Problem Description and Solution for Kth Largest Element in a Stream
sidebar_label: 703. Kth Largest Element in a Stream
sidebar_position: 703
---

# [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

```py title=kth-largest-element-in-a-stream.py
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for x in nums:
            if len(self.heap) == k:
                heapq.heappushpop(self.heap, x)
            else:
                heapq.heappush(self.heap, x)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```


