---
id: minimum-absolute-sum-difference
title: Minimum Absolute Sum Difference
description: Problem Description and Solution for Minimum Absolute Sum Difference
sidebar_label: 1818. Minimum Absolute Sum Difference
sidebar_position: 1818
---

# [1818. Minimum Absolute Sum Difference](https://leetcode.com/problems/minimum-absolute-sum-difference/)

```py title=minimum-absolute-sum-difference.py
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        M = 10 ** 9 + 7        
        n = len(nums1)
        total = sum(abs(a-b) for a, b in zip(nums1, nums2))
        
        sl = list(sorted(nums1))
        res = float('inf')
        
        for i, (a,b) in enumerate(zip(nums1, nums2)):
            diff = abs(a - b)
            idx = bisect.bisect_left(sl, b)
            
            if idx > 0:
                res = min(res, total - diff + abs(b - sl[idx-1]))    
            
            if idx < n:
                res = min(res, total - diff + abs(b - sl[idx]))
                    
        return res % M
```


