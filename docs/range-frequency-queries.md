---
id: range-frequency-queries
title: Range Frequency Queries
description: Problem Description and Solution for Range Frequency Queries
sidebar_label: 2080. Range Frequency Queries
sidebar_position: 2080
---

# [2080. Range Frequency Queries](https://leetcode.com/problems/range-frequency-queries/)

```py title=range-frequency-queries.py
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.mp[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        low = bisect.bisect_left(self.mp[value], left)
        high = bisect.bisect(self.mp[value], right)
        
        return high - low


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```


