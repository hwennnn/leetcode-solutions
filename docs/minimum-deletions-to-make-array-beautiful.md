---
id: minimum-deletions-to-make-array-beautiful
title: Minimum Deletions to Make Array Beautiful
description: Problem Description and Solution for Minimum Deletions to Make Array Beautiful
sidebar_label: 2216. Minimum Deletions to Make Array Beautiful
sidebar_position: 2216
---

# [2216. Minimum Deletions to Make Array Beautiful](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/)

```py title=minimum-deletions-to-make-array-beautiful.py
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        prev = None
        valid = 0
        
        for x in nums:
            if prev is not None:
                if x != prev:
                    prev = None
                    valid += 2
            else:
                prev = x
        
        return n - valid
```


