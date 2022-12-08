---
id: destroy-sequential-targets
title: Destroy Sequential Targets
description: Problem Description and Solution for Destroy Sequential Targets
sidebar_label: 2453. Destroy Sequential Targets
sidebar_position: 2453
---

# [2453. Destroy Sequential Targets](https://leetcode.com/problems/destroy-sequential-targets/)

```py title=destroy-sequential-targets.py
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        N = len(nums)
        mod = defaultdict(int)
        
        for x in nums:
            k = x % space
            mod[k] += 1
        
        mmax = max(mod.values())
        res = inf
        for x in nums:
            k = x % space
            if mod[k] == mmax and x < res:
                res = x
        
        return res
```


