---
id: 4sum-ii
title: 4Sum II
description: Problem Description and Solution for 4Sum II
sidebar_label: 454. 4Sum II
sidebar_position: 454
---

# [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)

```py title=4sum-ii.py
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        def construct(A, B):
            mp = collections.defaultdict(int)
            
            for a in A:
                for b in B:
                    mp[a + b] += 1
            
            return mp
        
        res = 0
        mp1 = construct(nums1, nums2)
        mp2 = construct(nums3, nums4)
        
        for k, v in mp1.items():
            res += v * mp2[-k]
        
        return res
```


