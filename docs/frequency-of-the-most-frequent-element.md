---
id: frequency-of-the-most-frequent-element
title: Frequency of the Most Frequent Element
description: Problem Description and Solution for Frequency of the Most Frequent Element
sidebar_label: 1838. Frequency of the Most Frequent Element
sidebar_position: 1838
---

# [1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

```py title=frequency-of-the-most-frequent-element.py
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = s = i = 0
        n = len(nums)
        
        nums.sort()
        
        for j in range(n):
            s += nums[j]
            
            while nums[j] * (j - i + 1) - s > k:
                s -= nums[i]
                i += 1
            
            res = max(res, j - i + 1)
        
        return res
```


