---
id: relative-ranks
title: Relative Ranks
description: Problem Description and Solution for Relative Ranks
sidebar_label: 506. Relative Ranks
sidebar_position: 506
---

# [506. Relative Ranks](https://leetcode.com/problems/relative-ranks/)

```py title=relative-ranks.py
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        
        sort = sorted(nums)[::-1]
        
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4,len(nums)+1)]
        
        temp = dict(zip(sort,rank))
        
        return list(map(temp.get,nums))
```


