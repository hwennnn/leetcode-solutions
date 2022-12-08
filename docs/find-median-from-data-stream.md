---
id: find-median-from-data-stream
title: Find Median from Data Stream
description: Problem Description and Solution for Find Median from Data Stream
sidebar_label: 295. Find Median from Data Stream
sidebar_position: 295
---

# [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

```py title=find-median-from-data-stream.py
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```


