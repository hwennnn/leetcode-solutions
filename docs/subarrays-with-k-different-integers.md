---
id: subarrays-with-k-different-integers
title: Subarrays with K Different Integers
description: Problem Description and Solution for Subarrays with K Different Integers
sidebar_label: 992. Subarrays with K Different Integers
sidebar_position: 992
---

# [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

```py title=subarrays-with-k-different-integers.py
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = prefix = res = distinct = 0
        count = Counter()
        
        for right, x in enumerate(nums):
            if count[x] == 0:
                distinct += 1
            
            count[x] += 1
            
            if distinct > k:
                count[nums[left]] -= 1
                left += 1
                prefix = 0
                distinct -= 1
            
            while count[nums[left]] > 1:
                count[nums[left]] -= 1
                prefix += 1
                left += 1
            
            if distinct == k:
                res += prefix + 1
        
        return res
```


