---
id: partition-array-into-two-arrays-to-minimize-sum-difference
title: Partition Array Into Two Arrays to Minimize Sum Difference
description: Problem Description and Solution for Partition Array Into Two Arrays to Minimize Sum Difference
sidebar_label: 2035. Partition Array Into Two Arrays to Minimize Sum Difference
sidebar_position: 2035
---

# [2035. Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/)

```py title=partition-array-into-two-arrays-to-minimize-sum-difference.py
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        def construct(A):
            n = len(A)
            mp = {}
            
            for k in range(1, n + 1):
                sums = []
                for comb in combinations(A, k):
                    sums.append(sum(comb))
                mp[k] = sums
            
            return mp
        
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]
        left_part, right_part = construct(left), construct(right)
        res = abs(sum(left) - sum(right))
        total = sum(nums)
        half = total // 2
        
        for k in range(1, n - 1):
            l, r = left_part[k], right_part[n - k]
            r.sort()
            
            for x in l:
                target = half - x
                index = bisect.bisect_left(r, target)
                
                for p in (index - 1, index):
                    if 0 <= p < len(r):
                        leftSum = x + r[p]
                        rightSum = total - leftSum
                        res = min(res, abs(leftSum - rightSum))
            
        return res
```


