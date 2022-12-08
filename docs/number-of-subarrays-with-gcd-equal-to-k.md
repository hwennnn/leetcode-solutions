---
id: number-of-subarrays-with-gcd-equal-to-k
title: Number of Subarrays With GCD Equal to K
description: Problem Description and Solution for Number of Subarrays With GCD Equal to K
sidebar_label: 2447. Number of Subarrays With GCD Equal to K
sidebar_position: 2447
---

# [2447. Number of Subarrays With GCD Equal to K](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/)

```py title=number-of-subarrays-with-gcd-equal-to-k.py
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            g = 0

            for j in range(i, N):
                g = gcd(g, nums[j])
                
                if g == k:
                    res += 1
        
        return res
        
```


