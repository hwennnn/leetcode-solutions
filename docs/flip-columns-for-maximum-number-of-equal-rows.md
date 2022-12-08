---
id: flip-columns-for-maximum-number-of-equal-rows
title: Flip Columns For Maximum Number of Equal Rows
description: Problem Description and Solution for Flip Columns For Maximum Number of Equal Rows
sidebar_label: 1072. Flip Columns For Maximum Number of Equal Rows
sidebar_position: 1072
---

# [1072. Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)

```py title=flip-columns-for-maximum-number-of-equal-rows.py
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mp = collections.defaultdict(int)
        
        for r in matrix:
            A = []
            for c in r:
                A.append(r[0] ^ c)
            
            mp[tuple(A)] += 1
        
        return max(mp.values())
```


