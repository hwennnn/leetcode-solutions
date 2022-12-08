---
id: most-frequent-even-element
title: Most Frequent Even Element
description: Problem Description and Solution for Most Frequent Even Element
sidebar_label: 2404. Most Frequent Even Element
sidebar_position: 2404
---

# [2404. Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/)

```py title=most-frequent-even-element.py
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter()
        have = False
        
        for x in nums:
            if x % 2 == 0:
                counter[x] += 1
                have = True
        
        if not have: return -1
        
        mmax = max(counter.values())
        
        for x in sorted(counter.keys()):
            if counter[x] == mmax:
                return x
        
        return -1
```


