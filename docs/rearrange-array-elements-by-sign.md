---
id: rearrange-array-elements-by-sign
title: Rearrange Array Elements by Sign
description: Problem Description and Solution for Rearrange Array Elements by Sign
sidebar_label: 2149. Rearrange Array Elements by Sign
sidebar_position: 2149
---

# [2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

```py title=rearrange-array-elements-by-sign.py
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        
        for x in nums:
            if x < 0:
                neg.append(x)
            else:
                pos.append(x)
        
        res = []
        
        for x, y in zip(pos, neg):
            res.append(x)
            res.append(y)
        
        return res
```


