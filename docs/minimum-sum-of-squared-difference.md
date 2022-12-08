---
id: minimum-sum-of-squared-difference
title: Minimum Sum of Squared Difference
description: Problem Description and Solution for Minimum Sum of Squared Difference
sidebar_label: 2333. Minimum Sum of Squared Difference
sidebar_position: 2333
---

# [2333. Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/)

```py title=minimum-sum-of-squared-difference.py
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [0] * n
        
        for index, (a, b) in enumerate(zip(nums1, nums2)):
            diff[index] = abs(a - b)
        
        mmax = max(diff)
        buckets = [0] * (mmax + 1)
        
        for d in diff:
            buckets[d] += 1
        
        k = k1 + k2
        
        for x in range(mmax, 0, -1):
            cnt = buckets[x]
            
            take = min(k, cnt)
            buckets[x] -= take
            buckets[x - 1] += take
            k -= take

        total = 0
        for x, count in enumerate(buckets):
            total += x * x * count
            
        return total 
                
                
            
            
```


