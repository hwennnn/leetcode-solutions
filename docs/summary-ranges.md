---
id: summary-ranges
title: Summary Ranges
description: Problem Description and Solution for Summary Ranges
sidebar_label: 228. Summary Ranges
sidebar_position: 228
---

# [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/)

```py title=summary-ranges.py
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        
        n = len(nums)
        res = []
        prev = None
        
        for i, x in enumerate(nums):
            if i == n - 1 or (i + 1 < n and x + 1!= nums[i + 1]):
                if prev is None:
                    res.append(str(x))
                else:
                    res.append(f"{prev}->{x}")
                    prev = None
            else:
                if prev is None:
                    prev = x
        
        return res
```


