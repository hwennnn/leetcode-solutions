---
id: most-profit-assigning-work
title: Most Profit Assigning Work
description: Problem Description and Solution for Most Profit Assigning Work
sidebar_label: 826. Most Profit Assigning Work
sidebar_position: 826
---

# [826. Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/)

```py title=most-profit-assigning-work.py
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        A = sorted([(x, y) for x, y in zip(difficulty, profit)])
        difficulty.sort()
        mp = defaultdict(int)
        curr = res = 0
        
        for d, p in A:
            curr = max(curr, p)
            
            mp[d] = max(mp[d], curr)
        
        for ability in worker:
            d = bisect.bisect_right(difficulty, ability) - 1
            
            if ability >= difficulty[d]:
                res += mp[difficulty[d]]
        
        return res
```


