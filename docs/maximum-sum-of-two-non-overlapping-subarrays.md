---
id: maximum-sum-of-two-non-overlapping-subarrays
title: Maximum Sum of Two Non-Overlapping Subarrays
description: Problem Description and Solution for Maximum Sum of Two Non-Overlapping Subarrays
sidebar_label: 1031. Maximum Sum of Two Non-Overlapping Subarrays
sidebar_position: 1031
---

# [1031. Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/)

```py title=maximum-sum-of-two-non-overlapping-subarrays.py
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] + list(accumulate(nums))
        res = 0
        
        for i in range(firstLen, n + 1):
            first = prefix[i] - prefix[i - firstLen]
            second = 0
            
            for j in range(secondLen, i - firstLen + 1):
                second = max(second, prefix[j] - prefix[j - secondLen])
            
            for j in range(secondLen + i + 1, n + 1):
                second = max(second, prefix[j] - prefix[j - secondLen])

            res = max(res, first + second)
        
        return res

```


