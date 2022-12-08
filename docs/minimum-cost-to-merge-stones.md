---
id: minimum-cost-to-merge-stones
title: Minimum Cost to Merge Stones
description: Problem Description and Solution for Minimum Cost to Merge Stones
sidebar_label: 1000. Minimum Cost to Merge Stones
sidebar_position: 1000
---

# [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

```py title=minimum-cost-to-merge-stones.py
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1): return -1
        prefix = [0] + list(accumulate(stones))
        
        @cache
        def go(i, j):
            if (j - i + 1) < k: return 0
            
            res = min(go(i, mid) + go(mid + 1, j) for mid in range(i, j, k - 1))
            
            if (j - i) % (k - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            
            return res
        
        return go(0, n - 1)
```


