---
id: sum-of-mutated-array-closest-to-target
title: Sum of Mutated Array Closest to Target
description: Problem Description and Solution for Sum of Mutated Array Closest to Target
sidebar_label: 1300. Sum of Mutated Array Closest to Target
sidebar_position: 1300
---

# [1300. Sum of Mutated Array Closest to Target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/)

```py title=sum-of-mutated-array-closest-to-target.py
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def getSum(k):
            s = 0
            
            for x in arr:
                s += min(x, k)
            
            return s
        
        left, right = 0, max(arr)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            total = getSum(mid)
            
            if total == target:
                return mid
            elif total < target:
                left = mid + 1
            else:
                right = mid - 1
        
        l2 = left - 1
        
        if abs(getSum(left) - target) < abs(getSum(l2) - target):
            return left
        
        return l2
        
```


