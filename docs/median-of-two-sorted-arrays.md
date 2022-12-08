---
id: median-of-two-sorted-arrays
title: Median of Two Sorted Arrays
description: Problem Description and Solution for Median of Two Sorted Arrays
sidebar_label: 4. Median of Two Sorted Arrays
sidebar_position: 4
---

# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

```py title=median-of-two-sorted-arrays.py
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n: return self.findMedianSortedArrays(B, A)
        
        half = (m + n + 1) // 2
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = half - i
            
            if i < m and j - 1 >= 0 and B[j - 1] > A[i]:
                left = i + 1
            elif i - 1 >= 0 and j < n and A[i - 1] > B[j]:
                right = i - 1
            else:
                if i == 0:
                    left_max = B[j - 1]
                elif j == 0:
                    left_max = A[i - 1]
                else:
                    left_max = max(A[i - 1], B[j - 1])
                
                if (m + n) & 1:
                    return left_max
                
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                
                return (left_max + right_min) / 2
```


